---
queued-for-processing: 2026-02-09T15:15:41.479Z
received: 2026-02-09T15:15:04.331Z
file: threads/in/20260209-151028-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 33cdcaa14fb27322bd185f939e7c9161652094a6
branch: pi/20260209-151028-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:10:28.463Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
