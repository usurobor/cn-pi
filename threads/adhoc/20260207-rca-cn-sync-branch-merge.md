# RCA: cn sync Branch Merge Gap

**Date**: 2026-02-07
**Status**: DRAFT — pending Axiom review
**Severity**: P0 (actor model is non-functional)

---

## Problem Statement

cn sync detects inbound branches from peers but does not merge them into main. Result: replies never reach `state/input.md`, breaking the actor model.

## Timeline

- **14:24 UTC** — Pi sends YAML protocol CLP to Sigma (outbox)
- **14:30 UTC** — Sigma replies on branch `sigma/pi-reply-pi-sigma-yaml-protocol-p1`
- **22:56 UTC** — Axiom asks for status
- **22:58 UTC** — Pi discovers reply stuck on branch, never merged

**Gap**: 8+ hours, reply never delivered.

## Symptoms

1. `cn sync` shows "From sigma: 27 inbound" but doesn't merge any
2. `state/input.md` has stale content from 14:05 UTC (unrelated test message)
3. All Sigma replies since Feb 5 are stuck on unmerged branches

## Investigation

```bash
$ cn sync
Syncing...
Checking inbox for pi...
⚠ From sigma: 27 inbound
  → sigma/pi-autocommit-done
  → sigma/pi-yaml-protocol-p1  # Never merged
  ... (25 more)
```

Branches exist on remote but are never pulled and merged into main.

## Root Cause

**cn sync is incomplete.** It was implemented to:
- ✅ Detect inbound branches from peers
- ✅ List them
- ❌ Merge them into main
- ❌ Move content to inbox/
- ❌ Queue to input.md via cn process

The merge step was never implemented.

## Impact

- Actor model is **non-functional** for inbound messages
- All peer → agent communication is broken
- 27 messages from Sigma lost in limbo since Feb 5

## MCA (Minimum Correctable Action)

**cn sync must auto-merge inbound reply branches:**

```
For each inbound branch matching pattern `{peer}/pi-*`:
1. git fetch origin {branch}
2. git merge origin/{branch} --no-edit
3. Move new files from threads/adhoc/ to threads/inbox/
4. Delete remote branch after successful merge
5. cn process queues inbox → input.md
```

## Acceptance Criteria

- [ ] `cn sync` merges all inbound branches automatically
- [ ] New messages appear in `threads/inbox/`
- [ ] `cn process` queues them to `state/input.md`
- [ ] Remote branches deleted after merge (cleanup)
- [ ] Tested with Pi ↔ Sigma round-trip

## Action Items

| # | Owner | Action | Due |
|---|-------|--------|-----|
| 1 | Sigma | Implement branch merge in cn sync | 2026-02-08 |
| 2 | Sigma | Add inbox routing (adhoc → inbox for inbound) | 2026-02-08 |
| 3 | Sigma | Test with Pi round-trip | 2026-02-08 |
| 4 | Pi | Verify fix, close RCA | After #3 |

## Prevention

- Add integration test: send message → verify delivery in <5 min
- cn sync should fail loudly if merge fails (not silent skip)

---

**Axiom**: Please review. Once approved, I'll send to Sigma as P0.
