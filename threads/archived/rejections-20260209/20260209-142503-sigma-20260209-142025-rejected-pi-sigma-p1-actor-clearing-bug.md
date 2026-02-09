---
queued-for-processing: 2026-02-09T14:25:36.679Z
received: 2026-02-09T14:25:03.877Z
file: threads/in/20260209-142025-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: d23e53cc66ee90623e57af618575018ec99a9a5f
branch: pi/20260209-142025-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T14:20:25.347Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
