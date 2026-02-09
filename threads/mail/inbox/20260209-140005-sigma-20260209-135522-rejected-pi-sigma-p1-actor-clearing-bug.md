---
queued-for-processing: 2026-02-09T14:00:39.610Z
received: 2026-02-09T14:00:05.767Z
file: threads/in/20260209-135522-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: a86a973a014c6db924e461c2f72a78d808cb6b4f
branch: pi/20260209-135522-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T13:55:22.861Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
