---
queued-for-processing: 2026-02-09T15:20:42.244Z
received: 2026-02-09T15:20:05.644Z
file: threads/in/20260209-151528-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 03f1c6f87188e9e8e62e5ea7ba6111e24faeacee
branch: pi/20260209-151528-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:15:28.622Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
