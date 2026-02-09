---
queued-for-processing: 2026-02-09T13:35:35.977Z
received: 2026-02-09T13:35:03.810Z
file: threads/in/20260209-133024-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 17219d7c227bd284e594b94e619b3524e8e3bc1a
branch: pi/20260209-133024-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T13:30:24.072Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
