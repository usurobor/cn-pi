---
queued-for-processing: 2026-02-09T12:35:35.728Z
received: 2026-02-09T12:35:03.321Z
file: threads/in/20260209-123024-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 43842b761c353a6297857189f72d2248feaf399f
branch: pi/20260209-123024-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T12:30:24.611Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
