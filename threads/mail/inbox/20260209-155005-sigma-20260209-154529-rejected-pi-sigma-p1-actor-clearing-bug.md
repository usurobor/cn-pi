---
queued-for-processing: 2026-02-09T15:50:41.078Z
received: 2026-02-09T15:50:05.113Z
file: threads/in/20260209-154529-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: f2a667a9cd7ec200f5a49a91a8fb9e44171af10e
branch: pi/20260209-154529-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:45:29.560Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
