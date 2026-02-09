---
queued-for-processing: 2026-02-09T15:10:41.674Z
received: 2026-02-09T15:10:05.190Z
file: threads/in/20260209-150528-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: f52feadb46773a399d15e0264618f1d2419136f4
branch: pi/20260209-150528-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:05:28.368Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
