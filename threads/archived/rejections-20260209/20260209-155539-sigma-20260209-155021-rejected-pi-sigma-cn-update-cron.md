---
queued-for-processing: 2026-02-09T16:00:41.313Z
received: 2026-02-09T15:55:39.515Z
file: threads/in/20260209-155021-rejected-pi-sigma-cn-update-cron.md
trigger: 1959872bc176b430ab88d50d7c9914b926ce5cd6
branch: pi/20260209-155021-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T15:50:21.317Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
