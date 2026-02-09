---
queued-for-processing: 2026-02-09T12:30:36.611Z
received: 2026-02-09T12:30:03.410Z
file: threads/in/20260209-122516-rejected-pi-sigma-cn-update-cron.md
trigger: af5e5611a68d44686872e07e8adf8fa979733be4
branch: pi/20260209-122516-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:25:16.842Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
