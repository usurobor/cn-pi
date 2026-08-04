#!/usr/bin/env python3
from __future__ import annotations

import importlib.machinery
import importlib.util
from io import BytesIO
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile


SCRIPT = str(Path(__file__).with_name("cn-pi-drive-ingress"))
loader = importlib.machinery.SourceFileLoader("cmp_pi_drive_sync", SCRIPT)
spec = importlib.util.spec_from_loader(loader.name, loader)
assert spec is not None
bridge = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = bridge
loader.exec_module(bridge)


class AuthenticatedDriveTests(unittest.TestCase):
    def test_service_account_credentials_are_detected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            credentials = root / "service-account.json"
            credentials.write_text("{}", encoding="utf-8")
            config = root / "rclone.conf"
            config.write_text(
                "[gdrive]\n"
                "type = drive\n"
                f"service_account_file = {credentials}\n",
                encoding="utf-8",
            )
            self.assertTrue(
                bridge.rclone_credentials_present(config, "gdrive:cn-pi/r0-boxes/pi-cmp")
            )

    def test_docx_is_extracted_to_deterministic_utf8(self) -> None:
        xml = b'''<?xml version="1.0" encoding="UTF-8"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:r><w:t>Hello</w:t><w:tab/><w:t>world</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>line one</w:t><w:br/><w:t>line two</w:t></w:r></w:p>
  </w:body>
</w:document>'''
        container = BytesIO()
        with zipfile.ZipFile(container, "w") as archive:
            archive.writestr("word/document.xml", xml)
        self.assertEqual(
            bridge.extract_docx_text(container.getvalue(), "test.docx"),
            b"Hello\tworld\n\nline one\nline two\n",
        )

    def test_invalid_docx_is_rejected(self) -> None:
        with self.assertRaisesRegex(bridge.SyncError, "not a valid DOCX"):
            bridge.extract_docx_text(b"not a zip", "test.docx")


class ProjectRoutingTests(unittest.TestCase):
    def test_three_routes_are_explicit_and_writer_owned(self) -> None:
        self.assertEqual(set(bridge.PROJECT_ROUTES), {"cmp", "tsc", "cnos"})
        for project, route in bridge.PROJECT_ROUTES.items():
            self.assertEqual(route.expected_repo, f"usurobor/{project}")
            self.assertEqual(route.target_ref, f"refs/heads/cn-pi/{project}/gpt/chat")
            self.assertEqual(route.drive_root, f"gdrive:cn-pi/r0-boxes/pi-{project}")

    def test_tsc_event_is_accepted_only_on_tsc_route(self) -> None:
        document = """CNPI-DOC: 0.2
activation: pi-tsc-chatgpt
project: tsc
intended_git_repo: usurobor/tsc
intended_git_ref: refs/heads/cn-pi/tsc/gpt/chat

---
schema: cnos.agent-message.v1
id: msg-cn-pi-tsc-test-01
rank: r0
authority: communication-only
thread_id: tsc-test
from:
  agent: usurobor/cn-pi
  activation: gpt/chat
  locus: usurobor/tsc
to:
  - agent: usurobor/cn-sigma
    activation: claude/chat
project:
  repo: usurobor/tsc
---
test
"""
        route = bridge.PROJECT_ROUTES["tsc"]
        bridge.validate_dialogue_document(document, route)
        events = bridge.extract_dialogue_events(document, route)
        self.assertEqual([event_id for event_id, _ in events], ["msg-cn-pi-tsc-test-01"])
        with self.assertRaisesRegex(bridge.SyncError, "not from cn-pi at CNOS"):
            bridge.extract_dialogue_events(document, bridge.PROJECT_ROUTES["cnos"])

    def test_memory_only_document_has_no_dialogue_events(self) -> None:
        document = """CNPI-DOC: 0.3
activation: pi-cnos-chatgpt
project: cnos
intended_git_repo: usurobor/cnos
intended_git_ref: refs/heads/pi/pi-cnos-chatgpt

memory notes only
"""
        self.assertEqual(
            bridge.extract_dialogue_events(document, bridge.PROJECT_ROUTES["cnos"]),
            [],
        )

    def test_empty_stream_readme_does_not_import_memory_source(self) -> None:
        text = bridge.readme_bytes(bridge.PROJECT_ROUTES["tsc"], "", "").decode()
        self.assertIn("No memory document or dialogue event was imported", text)
        self.assertNotIn("Source document:", text)


class CanonicalComparisonTests(unittest.TestCase):
    def test_only_transport_insignificant_differences_are_normalized(self) -> None:
        published = "subject: caf\u00e9  \r\nbody\t\r\n".encode()
        current = "subject: cafe\u0301\nbody\n".encode()
        self.assertEqual(
            bridge.canonical_event_bytes(published),
            bridge.canonical_event_bytes(current),
        )

    def test_punctuation_is_not_normalized(self) -> None:
        published = b"requires_response remains true.\n"
        current = b"requires_response remains true\n"
        self.assertNotEqual(
            bridge.canonical_event_bytes(published),
            bridge.canonical_event_bytes(current),
        )


class MutationIsolationTests(unittest.TestCase):
    def test_mutated_published_event_does_not_block_unseen_event(self) -> None:
        parent = "a" * 40
        publishing_commit = "b" * 40
        published_003 = b"schema: cnos.agent-message.v1\nid: msg-003\nbody: true.\n"
        current_003 = b"schema: cnos.agent-message.v1\nid: msg-003\nbody: true\n"
        current_004 = b"schema: cnos.agent-message.v1\nid: msg-004\nbody: new\n"

        def existing(_repo: Path, _parent: str, destination: str) -> bytes | None:
            if destination == "events/msg-003.md":
                return published_003
            if destination == "events/msg-004.md":
                return None
            raise AssertionError(destination)

        with (
            mock.patch.object(bridge, "remote_head", return_value=parent),
            mock.patch.object(bridge, "fetch_parent", return_value=parent),
            mock.patch.object(bridge, "existing_file", side_effect=existing),
            mock.patch.object(bridge, "published_file_commit", return_value=publishing_commit),
        ):
            result = bridge.project(
                Path("/unused"),
                "origin",
                "refs/heads/cn-pi/cmp/gpt/chat",
                "document-id-1234567890",
                b"source revision",
                "https://docs.google.com/document/d/document-id-1234567890",
                [("msg-003", current_003), ("msg-004", current_004)],
                dry_run=True,
            )

        self.assertEqual(result["status"], "would_update")
        self.assertEqual(result["events_to_add"], ["msg-004"])
        self.assertEqual(len(result["incidents"]), 1)
        incident = result["incidents"][0]
        self.assertEqual(incident["event_id"], "msg-003")
        self.assertEqual(incident["action"], "published_event_preserved")
        self.assertEqual(incident["published_git_commit"], publishing_commit)

    def test_live_git_projection_preserves_mutation_and_imports_later_event(self) -> None:
        published_003 = b"schema: cnos.agent-message.v1\nid: msg-003\nbody: true.\n"
        current_003 = b"schema: cnos.agent-message.v1\nid: msg-003\nbody: true\n"
        current_004 = b"schema: cnos.agent-message.v1\nid: msg-004\nbody: new\n"

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            remote = root / "remote.git"
            repo.mkdir()
            subprocess.run(["git", "init", "--quiet", str(repo)], check=True)
            subprocess.run(["git", "init", "--quiet", "--bare", str(remote)], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.invalid"], check=True)
            (repo / "events").mkdir()
            (repo / "events/msg-003.md").write_bytes(published_003)
            subprocess.run(["git", "-C", str(repo), "add", "events/msg-003.md"], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "--quiet", "-m", "publish 003"], check=True)
            subprocess.run(["git", "-C", str(repo), "remote", "add", "origin", str(remote)], check=True)
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(repo),
                    "push",
                    "--quiet",
                    "origin",
                    "HEAD:refs/heads/cn-pi/cmp/gpt/chat",
                ],
                check=True,
            )

            with mock.patch.object(bridge, "persist_incidents", return_value=None):
                result = bridge.project(
                    repo,
                    "origin",
                    "refs/heads/cn-pi/cmp/gpt/chat",
                    "document-id-1234567890",
                    b"source revision",
                    "https://docs.google.com/document/d/document-id-1234567890",
                    [("msg-003", current_003), ("msg-004", current_004)],
                    dry_run=False,
                )

            preserved = subprocess.run(
                [
                    "git",
                    f"--git-dir={remote}",
                    "show",
                    "refs/heads/cn-pi/cmp/gpt/chat:events/msg-003.md",
                ],
                check=True,
                stdout=subprocess.PIPE,
            ).stdout
            imported = subprocess.run(
                [
                    "git",
                    f"--git-dir={remote}",
                    "show",
                    "refs/heads/cn-pi/cmp/gpt/chat:events/msg-004.md",
                ],
                check=True,
                stdout=subprocess.PIPE,
            ).stdout

        self.assertEqual(result["status"], "updated")
        self.assertEqual(result["events_added"], ["msg-004"])
        self.assertEqual(len(result["incidents"]), 1)
        self.assertEqual(preserved, published_003)
        self.assertEqual(imported, current_004)

    def test_incident_ledger_deduplicates_the_same_mutation(self) -> None:
        incident = {
            "incident_id": "c" * 64,
            "kind": "source_mutation",
            "event_id": "msg-003",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "incidents.jsonl"
            self.assertIsNone(bridge.persist_incidents([incident], path))
            self.assertIsNone(bridge.persist_incidents([incident], path))
            lines = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
