---
queued-for-processing: 2026-02-09T13:00:37.638Z
received: 2026-02-09T13:00:04.947Z
file: threads/in/20260209-125523-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 157a763cffa77b7e30617bf2bf919587eee56dae
branch: pi/20260209-125523-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T12:55:23.990Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
