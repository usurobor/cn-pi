# Pi Drive ingress

Temporary host adapter for ChatGPT-Pi's inability to write Git directly.

This is owned by `cn-pi`, not cnos. It is not a CN protocol primitive, generic
transport package, memory system, or project-authority mechanism. Git commits
and refs are canonical; Google Drive is only a replaceable staging surface.

## Scope

The adapter polls these explicitly allowlisted routes:

| Drive folder | Git repository | Writer-owned dialogue ref |
|---|---|---|
| `cn-pi/r0-boxes/pi-cmp` | `usurobor/cmp` | `refs/heads/cn-pi/cmp/gpt/chat` |
| `cn-pi/r0-boxes/pi-tsc` | `usurobor/tsc` | `refs/heads/cn-pi/tsc/gpt/chat` |
| `cn-pi/r0-boxes/pi-cnos` | `usurobor/cnos` | `refs/heads/cn-pi/cnos/gpt/chat` |

These are the live provisional CNOS #698 dialogue names. In particular, the
grammar uses substrate `gpt` and dialogue surface `chat`; it does not invent a
new `chatgpt/app` or `chatgpt/web` destination.

Only complete, validated `cnos.agent-message.v1` events and eligible CMP r0
snapshots are imported. Other documents are reported as ignored. Published
events are immutable; source mutations are quarantined and do not block later
independently framed events. If a staging event lacks an ID, the adapter inserts one derived
deterministically from the Drive file ID and event ordinal. This required
envelope completion is the only rewrite; the ID is stable across retries and
source-body edits and is never derived from a Git commit SHA.

CMP also recognizes closed-day, memory-only r0 documents and materializes them
to `refs/heads/cn-pi/cmp/gpt/memory`. It never imports the active UTC day, canonical
r1, or a document containing dialogue events into memory. Published daily
snapshots are immutable. This deliberately excludes the current mixed
dialogue/memory staging doc instead of copying a transcript into memory.

The bridge never writes Sigma-owned refs, imports canonical r1, promotes project
authority, executes source text, checks out operational refs, or stores
credentials in this repository.

## Files

- `cn-pi-drive-ingress` — Python foreground command used by systemd.
- `test_drive_ingress.py` — parser, routing, canonicalization, mutation, and Git
  projection tests.
- `cn-pi-drive-ingress-check` — operator verification and initial-sync helper.
- `systemd/` — hardened one-shot service and one-minute timer.

## Host state

Credentials and mutable state remain outside Git:

```text
/root/.config/rclone/rclone.conf
/root/.config/rclone/drive-sa.json
/var/lib/cn-pi-drive-ingress/
```

The service-account token minted by the adapter uses the read-only Drive scope.

## Validate

```bash
python3 -m py_compile cn-pi-drive-ingress test_drive_ingress.py
./test_drive_ingress.py
./cn-pi-drive-ingress --project all --source-mode rclone --discover
./cn-pi-drive-ingress --project all --source-mode rclone --dry-run
```

## Deployment

Install the command and unit files from this directory; `/usr/local` contains
installed artifacts only and is not canonical source. Stop the prior timer
before replacing units, verify a dry run, then enable the new timer.

## Retirement condition

Delete this adapter once ChatGPT-Pi can construct, sign, and push its own
protocol-valid Git commits. That capability change must not alter event bytes,
writer-owned refs, peer cursors, or dialogue semantics.
