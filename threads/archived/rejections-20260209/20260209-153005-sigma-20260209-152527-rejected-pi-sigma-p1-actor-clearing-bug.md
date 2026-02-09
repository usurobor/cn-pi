---
queued-for-processing: 2026-02-09T15:30:44.567Z
received: 2026-02-09T15:30:05.060Z
file: threads/in/20260209-152527-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 7daa35c0e9343c37135ddf2d08ec629dd0f53284
branch: pi/20260209-152527-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:25:27.898Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
