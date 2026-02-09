---
queued-for-processing: 2026-02-09T12:00:28.404Z
received: 2026-02-09T12:00:05.962Z
file: threads/in/20260209-115532-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: 49c9c5f9f3900b273eb162d874acda213524b1d6
branch: pi/20260209-115532-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T11:55:32.607Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
