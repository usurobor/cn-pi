---
queued-for-processing: 2026-02-09T14:45:42.350Z
received: 2026-02-09T14:45:05.028Z
file: threads/in/20260209-144026-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 2864db8d0f44294e8b594593b26a62ae1f598fb3
branch: pi/20260209-144026-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T14:40:26.157Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
