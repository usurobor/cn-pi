---
queued-for-processing: 2026-02-09T16:00:41.321Z
received: 2026-02-09T16:00:04.546Z
file: threads/in/20260209-155605-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: d16c37e878750183448086656b6108b7b3d02cf5
branch: pi/20260209-155605-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:56:05.174Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
