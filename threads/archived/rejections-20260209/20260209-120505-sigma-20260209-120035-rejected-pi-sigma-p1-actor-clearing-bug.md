---
queued-for-processing: 2026-02-09T12:05:37.867Z
received: 2026-02-09T12:05:05.417Z
file: threads/in/20260209-120035-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 45a763b6f0c971fbc7eeadbd7b76fe1175cf3b83
branch: pi/20260209-120035-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T12:00:35.957Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
