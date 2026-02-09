---
queued-for-processing: 2026-02-09T12:25:33.569Z
received: 2026-02-09T12:25:03.298Z
file: threads/in/20260209-122025-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: ac55328e910edc5e5c51e55b9ac1f826249b7a4e
branch: pi/20260209-122025-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T12:20:25.045Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
