---
queued-for-processing: 2026-02-09T13:30:35.159Z
received: 2026-02-09T13:30:04.076Z
file: threads/in/20260209-132527-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 7ad95ecccf4f94e6e0f0015b03db768a40d314f9
branch: pi/20260209-132527-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T13:25:27.393Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
