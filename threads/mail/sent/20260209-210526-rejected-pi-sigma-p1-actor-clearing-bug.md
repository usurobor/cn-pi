---
sent: 2026-02-09T21:05:39.758Z
to: sigma
created: 2026-02-09T21:05:26.809Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
