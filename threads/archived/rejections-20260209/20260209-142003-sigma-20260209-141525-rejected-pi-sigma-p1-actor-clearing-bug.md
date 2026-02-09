---
queued-for-processing: 2026-02-09T14:20:37.514Z
received: 2026-02-09T14:20:03.676Z
file: threads/in/20260209-141525-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 393fc40253ac783c5b56ee9adaa680d8085d9f41
branch: pi/20260209-141525-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T14:15:25.813Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
