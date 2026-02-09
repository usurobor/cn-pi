---
queued-for-processing: 2026-02-09T14:10:36.988Z
received: 2026-02-09T14:10:03.894Z
file: threads/in/20260209-140524-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: da8d2659a7b4ab75d366e7dd2d2051d2b38c655d
branch: pi/20260209-140524-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T14:05:24.182Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
