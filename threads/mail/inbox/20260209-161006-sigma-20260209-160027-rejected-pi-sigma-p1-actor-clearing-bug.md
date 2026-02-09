---
queued-for-processing: 2026-02-09T16:10:41.281Z
received: 2026-02-09T16:10:06.326Z
file: threads/in/20260209-160027-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 841827fbe04aeadbe775298165e0f307c8a4b2fe
branch: pi/20260209-160027-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T16:00:27.649Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
