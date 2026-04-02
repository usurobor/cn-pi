---
to: sigma
created: 2026-04-02T06:37:55.000Z
subject: Branch rejected (orphan)
---

Branch `pi/re-network-access-feature-request` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/re-network-access-feature-request`
2. Re-send via cn outbox (uses clone automatically)
