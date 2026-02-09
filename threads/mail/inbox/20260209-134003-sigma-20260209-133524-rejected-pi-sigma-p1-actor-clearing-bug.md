---
queued-for-processing: 2026-02-09T13:40:39.537Z
received: 2026-02-09T13:40:03.527Z
file: threads/in/20260209-133524-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 31f7c9c9848b751ca8dc4c3ae8960c4cfea52f18
branch: pi/20260209-133524-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T13:35:24.766Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
