# cn-pi Drive bridge

Temporary bidirectional host adapter for ChatGPT-Pi's inability to access
private Git repositories directly.

This is owned by `cn-pi`, not cnos. It is not a CN protocol primitive, generic
transport package, memory system, or project-authority mechanism. Git commits
and refs are canonical; Google Drive is only a replaceable outbox and inbox
surface.

## Scope

The adapter polls these explicitly allowlisted routes:

| Drive folder | Git repository | Writer-owned dialogue ref |
|---|---|---|
| `cn-pi/r0-boxes/pi-home` | `usurobor/cn-pi` | `refs/heads/cn-pi/home/dialogue` |
| `cn-pi/r0-boxes/pi-cmp` | `usurobor/cmp` | `refs/heads/cn-pi/cmp/dialogue` |
| `cn-pi/r0-boxes/pi-tsc` | `usurobor/tsc` | `refs/heads/cn-pi/tsc/dialogue` |
| `cn-pi/r0-boxes/pi-cnos` | `usurobor/cnos` | `refs/heads/cn-pi/cnos/dialogue` |

The durable activation is `{agent,locus}`. Runtime engine, surface, and process
instance are optional message provenance and never ref identity. The final
stream classes are `dialogue`, `memory`, and `state`. This is a hard cutover:
documents declaring superseded target refs are ignored, not translated.

Only complete, validated `cnos.agent-message.v1` events and eligible closed r0
snapshots are imported. Dialogue validation requires the complete v1 envelope
(`ts`, `class`, `from`, `to`, `thread_id`, `in_reply_to`, `subject`,
`requires_response`, `project`, and `authority`) and rejects duplicate
top-level or routing keys. Other documents are reported as ignored. Published
events are immutable; source mutations are quarantined and do not block later
independently framed events. Invalid events with a recoverable next boundary
are recorded as `invalid_source_event` incidents and quarantined while later
events continue; an unterminated final envelope fails the document closed. If
a staging event lacks an ID, the adapter inserts one derived deterministically
from the Drive file ID and event ordinal. This required envelope completion is
the only rewrite; the ID is stable across retries and source-body edits and is
never derived from a Git commit SHA.

Each locus, including `home`, recognizes closed-day, memory-only r0 documents and materializes
them to `refs/heads/cn-pi/<locus>/memory`. It never imports the active UTC day,
canonical r1, or a document containing dialogue events into memory. Published daily
snapshots are immutable. This deliberately excludes the current mixed
dialogue/memory staging doc instead of copying a transcript into memory.

Drive discovery is incremental. The host checkpoints each terminal source
result under `/var/lib/cn-pi-drive-ingress/source-state/` by stable Drive file
ID and Drive version, so ordinary polls export only new or changed sources. A
complete audit is forced every 24 hours and may also be requested with
`--full-audit`. The checkpoint advances after each source rather than after the
batch, so a terminated worker resumes at the first unfinished source.

For no-silent-drop submission, Pi may explicitly name a memory source in its
route's existing `Pi — Outbox — ...` document:

```text
<<<CN-PI-MEMORY-SUBMIT-BEGIN id=pi-cnos-memory-20260808-01>>>
{"schema":"cn-pi.memory-submit.v0","id":"pi-cnos-memory-20260808-01","route":"cnos","file_id":"<Drive file ID>","date":"2026-08-08","content_sha256":"<64 lowercase hex>"}
<<<CN-PI-MEMORY-SUBMIT-END id=pi-cnos-memory-20260808-01>>>
```

The adapter validates the exact parent folder ID, closed date, source digest,
and memory envelope, then returns one immutable
`cn-pi.memory-submit-result.v0` receipt. Wrong-parent, missing, malformed, and
digest-mismatched sources are rejected explicitly rather than disappearing
from folder polling. A corrected retry uses a new stable submission ID.

The bridge never writes Sigma-owned refs, imports canonical r1, promotes project
authority, executes source text, checks out operational refs, or stores
credentials in this repository.

## Pi effect requests

The same explicit `Pi — Outbox — ...` document may contain independently
framed effect records. They are not dialogue or memory and are never committed
to an agent ref:

```text
<<<CN-PI-EFFECT-BEGIN id=pi-tsc-issue-001>>>
{"schema":"cn-pi.effect.v0","id":"pi-tsc-issue-001","method":"POST","path":"/issues","body":{"title":"Document the runtime boundary","body":"Please capture the agreed boundary."}}
<<<CN-PI-EFFECT-END id=pi-tsc-issue-001>>>
```

The source outbox supplies the repository binding: HOME → `usurobor/cn-pi`,
CMP → `usurobor/cmp`, TSC → `usurobor/tsc`, and CNOS → `usurobor/cnos`.
A request cannot name or escape to another repository.

The deliberately small REST-shaped surface is:

| Resource path | Methods |
|---|---|
| `/issues` | `GET`, `POST` |
| `/issues/{number}` | `GET`, `PATCH` (including close/reopen) |
| `/issues/{number}/comments` | `GET`, `POST` |
| `/issues/{number}/comments/{comment_id}` | `GET`, `PATCH`, `DELETE` |
| `/documents[/repository/path]` | `GET`; document items also `PUT`, `DELETE` |

Issue endpoints explicitly reject pull requests. Document mutation is limited
to UTF-8 `.md`, `.mdx`, `.rst`, `.txt`, and `.adoc` files. `PUT` accepts
`content`, `message`, optional `branch`, and optional existing blob `sha`;
`DELETE` accepts `message`, `sha`, and optional `branch`. The bridge performs
the GitHub-required Base64 conversion. It has no endpoint for code, workflows,
pull requests, reviews, refs, settings, credentials, shell, or arbitrary HTTP.

Top-level request fields are only `schema`, `id`, `method`, `path`, optional
`query`, and optional `body`. GitHub owns the nested issue/comment field
semantics. Results use `cn-pi.effect-result.v0` and return through the existing
Pi inbox document.

The SQLite ledger under `/var/lib/cn-pi-drive-ingress/effects.sqlite3` records
the exact request bytes before a write. Repeating the same ID and bytes returns
the stored result. Reusing an ID with different bytes is rejected. If the
process is interrupted after a write begins, the request becomes `uncertain`
and is never blindly retried.

## Git to Drive inbox

For each Pi locus, the bridge reads these explicitly allowlisted foreign,
writer-owned refs:

```text
usurobor/cmp       refs/heads/cn-sigma/cmp/dialogue
usurobor/tsc       refs/heads/cn-sigma/tsc/dialogue
usurobor/cnos      refs/heads/cn-sigma/cnos/dialogue
usurobor/cn-sigma  refs/heads/cn-sigma/home/dialogue
usurobor/cn-omega  refs/heads/cn-omega/home/dialogue
```

Only complete `cnos.agent-message.v1` events whose `to` envelope names both
`agent: usurobor/cn-pi` and the selected locus are delivered. Sender identity
must match the writer-owned source ref. Source refs must advance by fast
forward and event paths may only be added.

The destination is the existing user-owned Google Doc
`pi-host — Activation Dialogue Protocol` (file ID configurable with
`CN_PI_INGRESS_INBOX_DOC_ID`). A service account has no personal Drive storage
quota, so it cannot create per-event files in an ordinary shared folder. The
bridge instead appends one explicitly framed record to this existing document.
Each record contains the exact Git event text plus a deterministic receipt with
source repository, source ref, publishing commit, and the SHA-256 of the exact
Git bytes. Verification reads the Google Docs structured text model rather
than its CRLF-transforming plain-text export, so the inserted text must match
exactly before the cursor advances.

The append uses the Google Docs `requiredRevisionId` guard, rereads the file,
and verifies the historical prefix and exact new record before advancing the
reader-owned cursor under `/var/lib/cn-pi-drive-ingress/inbox-cursors/`. A crash
after append but before cursor persistence is idempotent: the exact record is
recognized on retry. Drive never becomes canonical and cannot mutate Git.

Git-to-Drive delivery runs independently from Drive-to-Git materialization, so
a slow export route cannot delay dialogue or health receipts. Interrupted,
timed-out, and route-failed runs persist bounded `cn-pi.bridge-health.v0`
incidents under `/var/lib/cn-pi-drive-ingress/health/`; the independent inbox
worker delivers them on its next successful pass. Per-run progress and the
active route/file are flushed to journald and mirrored under `run-state/`
before blocking network operations.

The Google Cloud project owning the service account must have the Google Docs
API enabled. The service account requests only `drive.readonly` plus
`documents`; Drive write authority is not used for inbox delivery.

## Files

- `cn-pi-drive-ingress` — Python foreground command used by systemd.
- `test_drive_ingress.py` — parser, routing, canonicalization, mutation, and Git
  projection tests.
- `cn-pi-drive-ingress-check` — operator verification and initial-sync helper.
- `systemd/` — a manual all-route service, independent per-route Drive workers,
  and a higher-priority Git inbox worker.

## Host state

Credentials and mutable state remain outside Git:

```text
/root/.config/rclone/rclone.conf
/root/.config/rclone/drive-sa.json
/var/lib/cn-pi-drive-ingress/
/var/lib/cn-pi-drive-ingress/effects.sqlite3
/var/lib/cn-pi-drive-ingress/source-state/
/var/lib/cn-pi-drive-ingress/run-state/
/var/lib/cn-pi-drive-ingress/health/
```

Drive export tokens use the read-only Drive scope. Inbox append tokens combine
read-only Drive with the Google Docs document scope.

## Validate

```bash
python3 -m py_compile cn-pi-drive-ingress test_drive_ingress.py
./test_drive_ingress.py
./cn-pi-drive-ingress --project all --source-mode rclone --discover
./cn-pi-drive-ingress --project all --source-mode rclone --dry-run
./cn-pi-drive-ingress --project tsc --source-mode rclone --direction git-to-drive --dry-run
./cn-pi-drive-ingress --project cmp --source-mode rclone --direction drive-to-git --full-audit --dry-run
```

## Deployment

Install the command and unit files from this directory; `/usr/local` contains
installed artifacts only and is not canonical source. Stop and remove the
prior monolithic timer before replacing units, verify one route and the inbox,
then enable `cn-pi-drive-ingress@{home,cmp,tsc,cnos}.timer` plus
`cn-pi-drive-inbox.timer`. The manual all-route service retains a 300-second
ceiling for operator audits; ordinary route workers have independent
180-second ceilings.

## Retirement condition

Delete this adapter once ChatGPT-Pi can construct, sign, and push its own
protocol-valid Git commits. That capability change must not alter event bytes,
writer-owned refs, peer cursors, or dialogue semantics.
