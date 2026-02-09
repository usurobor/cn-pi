---
queued-for-processing: 2026-02-09T13:35:35.975Z
received: 2026-02-09T13:35:02.857Z
file: threads/in/20260209-133018-rejected-pi-sigma-cn-update-cron.md
trigger: 3220cf4d165594ba79934b559607fb44c623e9b5
branch: pi/20260209-133018-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T13:30:18.003Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
