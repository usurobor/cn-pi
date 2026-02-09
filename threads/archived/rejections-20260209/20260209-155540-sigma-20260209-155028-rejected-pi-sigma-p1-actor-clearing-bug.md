---
queued-for-processing: 2026-02-09T16:00:41.317Z
received: 2026-02-09T15:55:40.239Z
file: threads/in/20260209-155028-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 2de38a2f5f4abfc67337795943214da756c1d3a3
branch: pi/20260209-155028-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:50:28.247Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
