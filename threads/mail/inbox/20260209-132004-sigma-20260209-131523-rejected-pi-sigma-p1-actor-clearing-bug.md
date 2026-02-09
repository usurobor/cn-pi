---
queued-for-processing: 2026-02-09T13:20:36.389Z
received: 2026-02-09T13:20:04.134Z
file: threads/in/20260209-131523-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 80b4e79e2213786b113761f04fb5cd28e573683c
branch: pi/20260209-131523-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T13:15:23.801Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
