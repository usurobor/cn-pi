---
queued-for-processing: 2026-02-09T12:00:28.400Z
received: 2026-02-09T12:00:04.762Z
file: threads/in/20260209-115526-rejected-pi-sigma-cn-update-cron.md
trigger: 0e24daa6c3ed18011e14f2db3965e228f6e199ca
branch: pi/20260209-115526-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T11:55:26.118Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
