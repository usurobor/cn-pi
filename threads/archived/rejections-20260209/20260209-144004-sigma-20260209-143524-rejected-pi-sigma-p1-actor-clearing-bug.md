---
queued-for-processing: 2026-02-09T14:40:39.036Z
received: 2026-02-09T14:40:04.050Z
file: threads/in/20260209-143524-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: a33a5d89da6477735937d74794927d597db54e27
branch: pi/20260209-143524-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T14:35:24.451Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
