---
queued-for-processing: 2026-02-09T13:15:34.515Z
received: 2026-02-09T13:15:03.678Z
file: threads/in/20260209-131026-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 598c37590f016dd7ec5b362408e4d0e986d83e09
branch: pi/20260209-131026-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T13:10:26.484Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
