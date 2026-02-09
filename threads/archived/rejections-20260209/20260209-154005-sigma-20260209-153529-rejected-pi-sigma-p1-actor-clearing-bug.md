---
queued-for-processing: 2026-02-09T15:40:40.709Z
received: 2026-02-09T15:40:05.445Z
file: threads/in/20260209-153529-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: d10d2ad2132c24b0173a7aea2bf9eb9163c7cea6
branch: pi/20260209-153529-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:35:29.578Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
