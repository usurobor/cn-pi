#!/usr/bin/env python3
from __future__ import annotations

import importlib.machinery
import importlib.util
from datetime import date
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
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
    def test_current_outbox_and_legacy_r0_titles_are_discovered(self) -> None:
        self.assertTrue(bridge.staging_source_name("r0 — pi-tsc-chatgpt — 2026-08-03.docx"))
        self.assertTrue(bridge.staging_source_name("Pi — Outbox — TSC Sigma.docx"))
        self.assertTrue(bridge.staging_source_name("PI — OUTBOX — CMP SIGMA.docx"))
        self.assertFalse(bridge.staging_source_name("pi-host — Activation Dialogue Protocol.docx"))

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


class GitToDriveInboxTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source = bridge.InboxSource(
            repo=Path("/root/cn-omega"),
            expected_repo="usurobor/cn-omega",
            owner_agent="usurobor/cn-omega",
            owner_locus="usurobor/cn-omega",
            dialogue_ref="refs/heads/cn-omega/home/dialogue",
        )
        self.event = b"""---
schema: cnos.agent-message.v1
id: msg-cn-omega-home-test-01
ts: 2026-08-05T19:00:00Z
rank: r0
class: request
from:
  agent: usurobor/cn-omega
  locus: usurobor/cn-omega
to:
  - agent: usurobor/cn-pi
    locus: usurobor/tsc
thread_id: tsc-test
in_reply_to: null
subject: exact inbound delivery test
requires_response: true
project:
  repo: usurobor/tsc
authority: communication-only
---

body bytes stay exact
"""

    def test_foreign_source_allowlist_includes_sigma_loci_and_omega_home(self) -> None:
        bindings = {
            (source.expected_repo, source.dialogue_ref) for source in bridge.INBOX_SOURCES
        }
        self.assertEqual(
            bindings,
            {
                ("usurobor/cmp", "refs/heads/cn-sigma/cmp/dialogue"),
                ("usurobor/tsc", "refs/heads/cn-sigma/tsc/dialogue"),
                ("usurobor/cnos", "refs/heads/cn-sigma/cnos/dialogue"),
                ("usurobor/cn-sigma", "refs/heads/cn-sigma/home/dialogue"),
                ("usurobor/cn-omega", "refs/heads/cn-omega/home/dialogue"),
            },
        )

    def test_foreign_event_identity_accepts_writer_owned_message(self) -> None:
        event_id, recipients = bridge.inbound_event_identity(self.event, self.source)
        self.assertEqual(event_id, "msg-cn-omega-home-test-01")
        self.assertEqual(
            recipients,
            [{"agent": "usurobor/cn-pi", "locus": "usurobor/tsc"}],
        )

    def test_foreign_event_identity_accepts_proposal_class(self) -> None:
        proposal = self.event.replace(b"class: request\n", b"class: proposal\n")
        event_id, _ = bridge.inbound_event_identity(proposal, self.source)
        self.assertEqual(event_id, "msg-cn-omega-home-test-01")

    def test_foreign_event_identity_rejects_spoofed_writer(self) -> None:
        spoofed = self.event.replace(
            b"  agent: usurobor/cn-omega\n", b"  agent: usurobor/cn-sigma\n", 1
        )
        with self.assertRaisesRegex(bridge.SyncError, "writer-owned ref"):
            bridge.inbound_event_identity(spoofed, self.source)

    def test_inbox_cursor_round_trip_is_atomic_and_private(self) -> None:
        route = bridge.PROJECT_ROUTES["tsc"]
        cursor = {bridge.inbox_source_key(self.source): "a" * 40}
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(
            bridge, "INBOX_STATE_DIR", Path(directory)
        ):
            bridge.persist_inbox_cursors(route, cursor)
            path = bridge.inbox_cursor_path(route)
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)
            self.assertEqual(bridge.read_inbox_cursors(route), cursor)
            document = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(document["version"], 1)

    def test_inbox_record_contains_exact_event_and_deterministic_receipt(self) -> None:
        receipt = b'{"event_id":"msg-cn-omega-home-test-01"}\n'
        record = bridge.inbox_record(
            "msg-cn-omega-home-test-01", self.event, receipt
        )
        self.assertIn(self.event.rstrip(b"\n"), record)
        self.assertIn(receipt.rstrip(b"\n"), record)
        self.assertEqual(
            record.count(b"<<<CNOS-DRIVE-INBOX-BEGIN id=msg-cn-omega-home-test-01>>>"),
            1,
        )

    def test_google_docs_structural_text_preserves_inserted_text_exactly(self) -> None:
        document = {
            "body": {
                "content": [
                    {
                        "paragraph": {
                            "elements": [
                                {"textRun": {"content": "one\ntwo\n"}}
                            ]
                        }
                    }
                ]
            }
        }
        self.assertEqual(bridge.google_docs_document_text(document), b"one\ntwo\n")

    def test_google_doc_retry_recognizes_an_exact_existing_record(self) -> None:
        event_id = "msg-cn-omega-home-test-01"
        record = bridge.inbox_record(event_id, self.event, b"{}\n")
        with (
            mock.patch.object(
                bridge,
                "google_docs_document",
                return_value={
                    "revisionId": "revision-1",
                    "body": {
                        "content": [{"paragraph": {"elements": [{"textRun": {"content": (b"protocol\n" + record).decode()}}]}}]
                    },
                },
            ) as read_structure,
        ):
            statuses = bridge.append_google_docs_inbox(
                "drive-doc-id-1234567890", "token", {event_id: record}
            )
        self.assertEqual(statuses, {event_id: "exists"})
        read_structure.assert_called_once()

    def test_google_doc_append_is_revision_guarded_and_verified(self) -> None:
        event_id = "msg-cn-omega-home-test-01"
        record = bridge.inbox_record(event_id, self.event, b"{}\n")
        before = b"protocol\n"
        response = BytesIO(b'{"writeControl":{"requiredRevisionId":"next"}}')
        response.status = 200
        with (
            mock.patch.object(
                bridge,
                "google_docs_document",
                side_effect=(
                    {
                        "revisionId": "revision-1",
                        "body": {
                            "content": [
                                {
                                    "paragraph": {
                                        "elements": [{"textRun": {"content": before.decode()}}]
                                    },
                                    "endIndex": 10,
                                }
                            ]
                        },
                    },
                    {
                        "revisionId": "revision-2",
                        "body": {
                            "content": [
                                {
                                    "paragraph": {
                                        "elements": [
                                            {"textRun": {"content": (b"protocol" + record).decode()}}
                                        ]
                                    },
                                    "endIndex": 10 + len(record.decode()),
                                }
                            ]
                        },
                    },
                ),
            ),
            mock.patch.object(bridge, "urlopen", return_value=response) as request,
        ):
            statuses = bridge.append_google_docs_inbox(
                "drive-doc-id-1234567890", "token", {event_id: record}
            )
        self.assertEqual(statuses, {event_id: "created"})
        posted = json.loads(request.call_args.args[0].data)
        self.assertEqual(posted["writeControl"], {"requiredRevisionId": "revision-1"})
        self.assertEqual(posted["requests"][0]["insertText"]["text"].encode(), record)

    def test_cursor_does_not_advance_when_drive_receipt_write_fails(self) -> None:
        route = bridge.PROJECT_ROUTES["tsc"]
        args = SimpleNamespace(
            rclone_config="/config",
            inbox_doc_id="drive-doc-id-1234567890",
            remote="origin",
            dry_run=False,
        )
        tip = "b" * 40
        path = "events/msg-cn-omega-home-test-01.md"
        with (
            mock.patch.object(bridge, "INBOX_SOURCES", (self.source,)),
            mock.patch.object(bridge, "rclone_service_account_path", return_value=Path("/sa")),
            mock.patch.object(bridge, "read_inbox_cursors", return_value={}),
            mock.patch.object(bridge, "source_event_paths", return_value=(tip, [path])),
            mock.patch.object(bridge, "existing_file", return_value=self.event),
            mock.patch.object(bridge, "published_file_commit", return_value="c" * 40),
            mock.patch.object(
                bridge,
                "service_account_access_token",
                return_value="token",
            ),
            mock.patch.object(
                bridge,
                "append_google_docs_inbox",
                side_effect=bridge.SyncError("append failed"),
            ),
            mock.patch.object(bridge, "persist_inbox_cursors") as persist,
        ):
            with self.assertRaisesRegex(bridge.SyncError, "append failed"):
                bridge.sync_git_inbox(route, args)
        persist.assert_not_called()

    def test_successful_delivery_persists_source_tip_after_event_and_receipt(self) -> None:
        route = bridge.PROJECT_ROUTES["tsc"]
        args = SimpleNamespace(
            rclone_config="/config",
            inbox_doc_id="drive-doc-id-1234567890",
            remote="origin",
            dry_run=False,
        )
        tip = "d" * 40
        path = "events/msg-cn-omega-home-test-01.md"
        with (
            mock.patch.object(bridge, "INBOX_SOURCES", (self.source,)),
            mock.patch.object(bridge, "rclone_service_account_path", return_value=Path("/sa")),
            mock.patch.object(bridge, "read_inbox_cursors", return_value={}),
            mock.patch.object(bridge, "source_event_paths", return_value=(tip, [path])),
            mock.patch.object(bridge, "existing_file", return_value=self.event),
            mock.patch.object(bridge, "published_file_commit", return_value="e" * 40),
            mock.patch.object(bridge, "service_account_access_token", return_value="token"),
            mock.patch.object(
                bridge,
                "append_google_docs_inbox",
                return_value={"msg-cn-omega-home-test-01": "created"},
            ),
            mock.patch.object(bridge, "persist_inbox_cursors") as persist,
        ):
            result = bridge.sync_git_inbox(route, args)
        self.assertEqual(result["status"], "updated")
        self.assertEqual(result["records_created"], 1)
        persist.assert_called_once_with(
            route, {bridge.inbox_source_key(self.source): tip}
        )


class ProjectRoutingTests(unittest.TestCase):
    def test_four_routes_are_explicit_and_writer_owned(self) -> None:
        self.assertEqual(set(bridge.PROJECT_ROUTES), {"home", "cmp", "tsc", "cnos"})
        for project, route in bridge.PROJECT_ROUTES.items():
            expected_repo = "usurobor/cn-pi" if project == "home" else f"usurobor/{project}"
            self.assertEqual(route.expected_repo, expected_repo)
            self.assertEqual(route.target_ref, f"refs/heads/cn-pi/{project}/dialogue")
            self.assertEqual(route.drive_root, f"gdrive:cn-pi/r0-boxes/pi-{project}")
        self.assertEqual(
            bridge.PROJECT_ROUTES["home"].repo,
            Path("/root/cn-pi-clone"),
        )
        self.assertEqual(
            bridge.PROJECT_ROUTES["home"].memory_ref,
            "refs/heads/cn-pi/home/memory",
        )
        self.assertEqual(
            bridge.PROJECT_ROUTES["cmp"].memory_ref,
            "refs/heads/cn-pi/cmp/memory",
        )
        self.assertEqual(
            bridge.PROJECT_ROUTES["tsc"].memory_ref,
            "refs/heads/cn-pi/tsc/memory",
        )
        self.assertEqual(
            bridge.PROJECT_ROUTES["cnos"].memory_ref,
            "refs/heads/cn-pi/cnos/memory",
        )

    def test_missing_id_is_minted_stably_from_drive_identity_and_ordinal(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@cmp
project: cmp
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/dialogue

---
schema: cnos.agent-message.v1
ts: 2026-08-05T12:00:00Z
rank: r0
class: request
authority: communication-only
thread_id: cmp-test
from:
  agent: usurobor/cn-pi
  locus: usurobor/cmp
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cmp
project:
  repo: usurobor/cmp
in_reply_to: null
subject: parser completion proof
requires_response: true
---
test
"""
        source_id = "11nbk6ZncQ7iwZ8vr-Yk0v71gxXCLwtO4OQL6XBOraeE"
        first = bridge.extract_dialogue_events(
            document, bridge.PROJECT_ROUTES["cmp"], source_id
        )
        changed = bridge.extract_dialogue_events(
            document.replace("test\n", "changed\n"),
            bridge.PROJECT_ROUTES["cmp"],
            source_id,
        )
        self.assertEqual(first.events[0][0], changed.events[0][0])
        self.assertRegex(first.events[0][0], r"^msg-cn-pi-cmp-drive-[0-9a-f]{24}$")
        self.assertIn(f"id: {first.events[0][0]}\n".encode(), first.events[0][1])
        expected = document.split("\n---\n", 1)[1].encode()
        self.assertEqual(
            first.events[0][1].replace(
                f"id: {first.events[0][0]}\n".encode(), b"", 1
            ),
            expected,
        )
        self.assertEqual(first.incidents, [])

    def test_missing_id_without_drive_identity_is_rejected(self) -> None:
        document = """CNPI-DOC: 0.2
---
schema: cnos.agent-message.v1
ts: 2026-08-05T12:00:00Z
rank: r0
class: request
authority: communication-only
thread_id: cmp-test
---
test
"""
        with self.assertRaisesRegex(bridge.SyncError, "stable Drive file ID"):
            bridge.extract_dialogue_events(document)

    def test_tsc_event_is_accepted_only_on_tsc_route(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@tsc
project: tsc
intended_git_repo: usurobor/tsc
intended_git_ref: refs/heads/cn-pi/tsc/dialogue

---
schema: cnos.agent-message.v1
id: msg-cn-pi-tsc-test-01
ts: 2026-08-05T12:00:00Z
rank: r0
class: review
authority: communication-only
thread_id: tsc-test
from:
  agent: usurobor/cn-pi
  locus: usurobor/tsc
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/tsc
project:
  repo: usurobor/tsc
in_reply_to: null
subject: tsc route proof
requires_response: false
---
test
"""
        route = bridge.PROJECT_ROUTES["tsc"]
        bridge.validate_dialogue_document(document, route)
        extraction = bridge.extract_dialogue_events(document, route)
        self.assertEqual(
            [event_id for event_id, _ in extraction.events],
            ["msg-cn-pi-tsc-test-01"],
        )
        wrong_route = bridge.extract_dialogue_events(
            document, bridge.PROJECT_ROUTES["cnos"]
        )
        self.assertEqual(wrong_route.events, [])
        self.assertRegex(wrong_route.incidents[0]["reason"], "not from cn-pi at CNOS")

    def test_tsc_proposal_to_registered_omega_peer_is_accepted(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@tsc
project: tsc
intended_git_repo: usurobor/tsc
intended_git_ref: refs/heads/cn-pi/tsc/dialogue

---
schema: cnos.agent-message.v1
id: msg-cn-pi-tsc-proposal-01
ts: 2026-08-06T02:34:13Z
rank: r0
class: proposal
from:
  agent: usurobor/cn-pi
  activation: chatgpt
  locus: usurobor/tsc
to:
  - agent: usurobor/cn-omega
    locus: usurobor/cn-omega
thread_id: tsc-core-runtime-semantics-20260805
in_reply_to: null
subject: Core semantics and methodology-as-code
requires_response: true
project:
  repo: usurobor/tsc
authority: communication-only
---
proposal body
"""
        extraction = bridge.extract_dialogue_events(
            document,
            bridge.PROJECT_ROUTES["tsc"],
            "document-id-1234567890",
        )
        self.assertEqual(
            [event_id for event_id, _ in extraction.events],
            ["msg-cn-pi-tsc-proposal-01"],
        )
        self.assertEqual(extraction.incidents, [])

    def test_dialogue_header_order_is_semantically_irrelevant(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@cnos
project: cnos
intended_git_repo: usurobor/cnos
intended_git_ref: refs/heads/cn-pi/cnos/dialogue

---
id: msg-cn-pi-cnos-header-order-01
class: proposal
schema: cnos.agent-message.v1
subject: Header mappings are unordered
rank: r0
to:
  - locus: usurobor/cnos
    agent: usurobor/cn-sigma
from:
  locus: usurobor/cnos
  agent: usurobor/cn-pi
requires_response: true
thread_id: cnos-header-order
project:
  repo: usurobor/cnos
authority: communication-only
in_reply_to: null
ts: 2026-08-06T04:15:00Z
---
body bytes remain unchanged
"""
        extraction = bridge.extract_dialogue_events(
            document,
            bridge.PROJECT_ROUTES["cnos"],
            "document-id-1234567890",
        )
        self.assertEqual(
            [event_id for event_id, _ in extraction.events],
            ["msg-cn-pi-cnos-header-order-01"],
        )
        self.assertEqual(extraction.incidents, [])
        self.assertTrue(extraction.events[0][1].startswith(b"id: msg-cn-pi"))
        self.assertIn(
            b"class: proposal\nschema: cnos.agent-message.v1\n",
            extraction.events[0][1],
        )

    def test_tsc_event_to_unregistered_peer_is_quarantined(self) -> None:
        document = """CNPI-DOC: 0.2
---
schema: cnos.agent-message.v1
id: msg-cn-pi-tsc-unknown-peer-01
ts: 2026-08-06T02:34:13Z
rank: r0
class: proposal
from:
  agent: usurobor/cn-pi
  locus: usurobor/tsc
to:
  - agent: usurobor/cn-unknown
    locus: usurobor/cn-unknown
thread_id: tsc-unknown-peer
in_reply_to: null
subject: unsupported peer
requires_response: false
project:
  repo: usurobor/tsc
authority: communication-only
---
body
"""
        extraction = bridge.extract_dialogue_events(
            document,
            bridge.PROJECT_ROUTES["tsc"],
            "document-id-1234567890",
        )
        self.assertEqual(extraction.events, [])
        self.assertRegex(
            extraction.incidents[0]["reason"],
            "registered Pi dialogue peer",
        )

    def test_final_envelope_does_not_require_runtime_as_activation_identity(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@cmp
project: cmp
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/dialogue

---
schema: cnos.agent-message.v1
id: msg-cn-pi-cmp-final-envelope-01
ts: 2026-08-05T12:00:00Z
rank: r0
class: request
authority: communication-only
thread_id: cmp-test
from:
  agent: usurobor/cn-pi
  locus: usurobor/cmp
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cnos
project:
  repo: usurobor/cmp
in_reply_to: null
subject: cross-locus delivery proof
requires_response: true
---
test
"""
        route = bridge.PROJECT_ROUTES["cmp"]
        bridge.validate_dialogue_document(document, route)
        self.assertEqual(
            [
                event_id
                for event_id, _ in bridge.extract_dialogue_events(document, route).events
            ],
            ["msg-cn-pi-cmp-final-envelope-01"],
        )

    def test_ambiguous_or_incomplete_envelopes_are_quarantined(self) -> None:
        header = """CNPI-DOC: 0.2
activation: cn-pi@cmp
project: cmp
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/dialogue

"""
        complete = """---
schema: cnos.agent-message.v1
id: msg-complete
ts: 2026-08-05T12:00:00Z
rank: r0
class: request
from:
  agent: usurobor/cn-pi
  locus: usurobor/cmp
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cmp
thread_id: parser-negative
in_reply_to: null
subject: complete
requires_response: true
project:
  repo: usurobor/cmp
authority: communication-only
---
body
"""
        cases = {
            "duplicate id": complete.replace(
                "id: msg-complete\n", "id: msg-first\nid: msg-second\n"
            ),
            "duplicate routing key": complete.replace(
                "  agent: usurobor/cn-pi\n",
                "  agent: usurobor/cn-pi\n  agent: usurobor/cn-omega\n",
                1,
            ),
            "from scalar plus mapping": complete.replace("from:\n", "from: scalar\n"),
            "to scalar plus sequence": complete.replace("to:\n", "to: scalar\n"),
            "project scalar plus mapping": complete.replace(
                "project:\n", "project: scalar\n"
            ),
            "missing ts and class": complete.replace(
                "ts: 2026-08-05T12:00:00Z\n", ""
            ).replace("class: request\n", ""),
            "missing schema": complete.replace(
                "schema: cnos.agent-message.v1\n", ""
            ),
        }
        for label, event in cases.items():
            with self.subTest(label=label):
                extraction = bridge.extract_dialogue_events(
                    header + event,
                    bridge.PROJECT_ROUTES["cmp"],
                    "document-id-1234567890",
                )
                self.assertEqual(extraction.events, [])
                self.assertEqual(len(extraction.incidents), 1)
                self.assertEqual(
                    extraction.incidents[0]["action"], "source_event_quarantined"
                )

    def test_malformed_reordered_event_is_quarantined_not_silently_appended(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@cnos
project: cnos
intended_git_repo: usurobor/cnos
intended_git_ref: refs/heads/cn-pi/cnos/dialogue

---
schema: cnos.agent-message.v1
id: msg-cn-pi-cnos-prior-09
ts: 2026-08-06T02:32:00Z
rank: r0
class: review
from:
  agent: usurobor/cn-pi
  locus: usurobor/cnos
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cnos
thread_id: cnos-prior
in_reply_to: null
subject: prior published event
requires_response: false
project:
  repo: usurobor/cnos
authority: communication-only
---
prior body

---
id: msg-cn-pi-cnos-obligation-projection-10
schema: cnos.agent-message.v1
ts: 2026-08-05T22:41:00-04:00
from:
  agent: usurobor/cn-pi
  locus: usurobor/cnos
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cnos
thread_id: cnos-dialogue-obligation-projection
in_reply_to: msg-cn-pi-cnos-prior-09
class: proposal
requires_response: true
authority: communication-only
subject: malformed event is still observable
---
malformed body
"""
        extraction = bridge.extract_dialogue_events(
            document,
            bridge.PROJECT_ROUTES["cnos"],
            "document-id-1234567890",
        )
        self.assertEqual(
            [event_id for event_id, _ in extraction.events],
            ["msg-cn-pi-cnos-prior-09"],
        )
        self.assertNotIn(
            b"msg-cn-pi-cnos-obligation-projection-10",
            extraction.events[0][1],
        )
        self.assertEqual(len(extraction.incidents), 1)
        self.assertEqual(
            extraction.incidents[0]["event_id"],
            "msg-cn-pi-cnos-obligation-projection-10",
        )
        self.assertRegex(extraction.incidents[0]["reason"], "field 'rank'")

    def test_invalid_envelope_does_not_initialize_or_advance_target_ref(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@cmp
project: cmp
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/dialogue

---
schema: cnos.agent-message.v1
id: msg-invalid-container
ts: 2026-08-05T12:00:00Z
rank: r0
class: request
from: scalar
  agent: usurobor/cn-pi
  locus: usurobor/cmp
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cmp
thread_id: parser-negative
in_reply_to: null
subject: ambiguous identity
requires_response: true
project:
  repo: usurobor/cmp
authority: communication-only
---
body
"""
        args = SimpleNamespace(
            remote="origin",
            rclone_config="/unused/rclone.conf",
            discover=False,
            dry_run=False,
        )
        with (
            mock.patch.object(bridge, "validate_repo"),
            mock.patch.object(bridge, "validate_ref"),
            mock.patch.object(
                bridge,
                "authenticated_sources",
                return_value=[
                    (
                        "document-id-1234567890",
                        document.encode(),
                        "https://example.invalid/source",
                        "source-doc",
                    )
                ],
            ),
            mock.patch.object(bridge, "persist_incidents", return_value=None),
            mock.patch.object(bridge, "project") as project_mock,
        ):
            result = bridge.sync_project_route(
                bridge.PROJECT_ROUTES["cmp"], args, "rclone"
            )
        project_mock.assert_not_called()
        self.assertEqual(
            result["documents"][0]["status"], "invalid_events_quarantined"
        )

    def test_malformed_bounded_event_does_not_block_later_valid_event(self) -> None:
        document = """CNPI-DOC: 0.2
activation: cn-pi@cmp
project: cmp
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/dialogue

---
schema: cnos.agent-message.v1
id: msg-malformed
body without a frontmatter terminator
---
schema: cnos.agent-message.v1
id: msg-later-valid
ts: 2026-08-05T12:01:00Z
rank: r0
class: ack
from:
  agent: usurobor/cn-pi
  locus: usurobor/cmp
to:
  - agent: usurobor/cn-sigma
    locus: usurobor/cnos
thread_id: parser-isolation
in_reply_to: msg-source
subject: later event survives
requires_response: false
project:
  repo: usurobor/cmp
authority: communication-only
---
body
"""
        extraction = bridge.extract_dialogue_events(
            document,
            bridge.PROJECT_ROUTES["cmp"],
            "document-id-1234567890",
        )
        self.assertEqual(
            [event_id for event_id, _ in extraction.events], ["msg-later-valid"]
        )
        self.assertEqual(len(extraction.incidents), 1)
        self.assertEqual(extraction.incidents[0]["event_id"], "msg-malformed")
        self.assertRegex(extraction.incidents[0]["reason"], "frontmatter terminator")

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            remote = root / "remote.git"
            repo.mkdir()
            subprocess.run(["git", "init", "--quiet", str(repo)], check=True)
            subprocess.run(["git", "init", "--quiet", "--bare", str(remote)], check=True)
            subprocess.run(["git", "-C", str(repo), "remote", "add", "origin", str(remote)], check=True)
            route = bridge.ProjectRoute(
                project="cmp",
                activation="cn-pi@cmp",
                drive_root="gdrive:cn-pi/r0-boxes/pi-cmp",
                repo=repo,
                expected_repo="usurobor/cmp",
                target_ref="refs/heads/cn-pi/cmp/dialogue",
                peer_ref="refs/heads/cn-sigma/cmp/dialogue",
                memory_ref="refs/heads/cn-pi/cmp/memory",
            )
            args = SimpleNamespace(
                remote="origin",
                rclone_config="/unused/rclone.conf",
                discover=False,
                dry_run=False,
            )
            with (
                mock.patch.object(bridge, "validate_repo"),
                mock.patch.object(bridge, "validate_ref"),
                mock.patch.object(
                    bridge,
                    "authenticated_sources",
                    return_value=[
                        (
                            "document-id-1234567890",
                            document.encode(),
                            "https://example.invalid/source",
                            "source-doc",
                        )
                    ],
                ),
                mock.patch.object(bridge, "persist_incidents", return_value=None),
            ):
                result = bridge.sync_project_route(route, args, "rclone")
            imported = subprocess.run(
                [
                    "git",
                    f"--git-dir={remote}",
                    "show",
                    "refs/heads/cn-pi/cmp/dialogue:events/msg-later-valid.md",
                ],
                check=True,
                stdout=subprocess.PIPE,
            ).stdout
            malformed = subprocess.run(
                [
                    "git",
                    f"--git-dir={remote}",
                    "cat-file",
                    "-e",
                    "refs/heads/cn-pi/cmp/dialogue:events/msg-malformed.md",
                ],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            import_commits = subprocess.run(
                [
                    "git",
                    f"--git-dir={remote}",
                    "log",
                    "--format=%H",
                    "refs/heads/cn-pi/cmp/dialogue",
                    "--",
                    "events/msg-later-valid.md",
                ],
                check=True,
                stdout=subprocess.PIPE,
                text=True,
            ).stdout.splitlines()

        self.assertEqual(result["documents"][0]["status"], "updated")
        self.assertEqual(result["documents"][0]["events_added"], ["msg-later-valid"])
        self.assertEqual(result["documents"][0]["quarantined_event_count"], 1)
        self.assertIn(b"id: msg-later-valid\n", imported)
        self.assertNotEqual(malformed.returncode, 0)
        self.assertEqual(len(import_commits), 1)

    def test_unrecoverable_final_framing_loss_fails_closed(self) -> None:
        document = """CNPI-DOC: 0.2
---
schema: cnos.agent-message.v1
id: msg-unterminated
body without a recoverable boundary
"""
        with self.assertRaisesRegex(bridge.SyncError, "frontmatter terminator"):
            bridge.extract_dialogue_events(
                document,
                bridge.PROJECT_ROUTES["cmp"],
                "document-id-1234567890",
            )

    def test_memory_only_document_has_no_dialogue_events(self) -> None:
        document = """CNPI-DOC: 0.3
activation: cn-pi@cnos
project: cnos
intended_git_repo: usurobor/cnos
intended_git_ref: refs/heads/cn-pi/cnos/memory

memory notes only
"""
        self.assertEqual(
            bridge.extract_dialogue_events(
                document, bridge.PROJECT_ROUTES["cnos"]
            ).events,
            [],
        )

    def test_home_memory_uses_home_activation_and_final_ref(self) -> None:
        document = """CNPI-DOC: 0.3
kind: cnos-memory-box
activation: cn-pi@home
project: home
rank: r0
date: 2026-08-03
intended_git_repo: usurobor/cn-pi
intended_git_ref: refs/heads/cn-pi/home/memory
canonical_status: drive-staging

home evidence
"""
        snapshot = bridge.extract_closed_memory_snapshot(
            document,
            document.encode(),
            bridge.PROJECT_ROUTES["home"],
            today=date(2026, 8, 4),
        )
        self.assertEqual(snapshot, ("posts/20260803.md", document.encode()))

    def test_only_closed_memory_only_cmp_documents_materialize(self) -> None:
        document = """CNPI-DOC: 0.3
kind: cnos-memory-box
activation: cn-pi@cmp
project: cmp
rank: r0
date: 2026-08-03
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/memory
canonical_status: drive-staging

memory evidence
"""
        snapshot = bridge.extract_closed_memory_snapshot(
            document,
            document.encode(),
            bridge.PROJECT_ROUTES["cmp"],
            today=date(2026, 8, 4),
        )
        self.assertEqual(snapshot, ("posts/20260803.md", document.encode()))
        self.assertIsNone(
            bridge.extract_closed_memory_snapshot(
                document.replace("2026-08-03", "2026-08-04"),
                document.encode(),
                bridge.PROJECT_ROUTES["cmp"],
                today=date(2026, 8, 4),
            )
        )

    def test_mixed_dialogue_document_is_not_copied_into_memory(self) -> None:
        document = """CNPI-DOC: 0.3
kind: cnos-memory-box
activation: cn-pi@cmp
project: cmp
rank: r0
date: 2026-08-03
intended_git_repo: usurobor/cmp
intended_git_ref: refs/heads/cn-pi/cmp/memory
canonical_status: drive-staging

schema: cnos.agent-message.v1
"""
        self.assertIsNone(
            bridge.extract_closed_memory_snapshot(
                document,
                document.encode(),
                bridge.PROJECT_ROUTES["cmp"],
                today=date(2026, 8, 4),
            )
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
                "refs/heads/cn-pi/cmp/dialogue",
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
                    "HEAD:refs/heads/cn-pi/cmp/dialogue",
                ],
                check=True,
            )

            with mock.patch.object(bridge, "persist_incidents", return_value=None):
                result = bridge.project(
                    repo,
                    "origin",
                    "refs/heads/cn-pi/cmp/dialogue",
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
                    "refs/heads/cn-pi/cmp/dialogue:events/msg-003.md",
                ],
                check=True,
                stdout=subprocess.PIPE,
            ).stdout
            imported = subprocess.run(
                [
                    "git",
                    f"--git-dir={remote}",
                    "show",
                    "refs/heads/cn-pi/cmp/dialogue:events/msg-004.md",
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
