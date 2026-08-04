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

Only complete, validated `cnos.agent-message.v1` events are imported. Documents
without dialogue events are reported as ignored. Published events are
immutable; source mutations are quarantined and do not block later independently
framed events.

The bridge never writes Sigma-owned refs, imports memory documents, promotes
project authority, executes source text, checks out operational refs, or stores
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
