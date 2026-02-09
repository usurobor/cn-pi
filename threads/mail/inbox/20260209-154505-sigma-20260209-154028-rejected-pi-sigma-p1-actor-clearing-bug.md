---
queued-for-processing: 2026-02-09T15:45:42.371Z
received: 2026-02-09T15:45:05.790Z
file: threads/in/20260209-154028-rejected-pi-sigma-p1-actor-clearing-bug.md
trigger: f1b2cb6022dfe66450836d1caecd0675684f31f4
branch: pi/20260209-154028-rejected-pi-sigma-p1-actor-clearing-bug
from: sigma
to: sigma
created: 2026-02-09T15:40:28.543Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-p1-actor-clearing-bug` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-p1-actor-clearing-bug`
2. Re-send via cn outbox (uses clone automatically)
