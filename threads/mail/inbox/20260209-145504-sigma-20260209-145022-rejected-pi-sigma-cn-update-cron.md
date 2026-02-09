---
queued-for-processing: 2026-02-09T14:55:41.112Z
received: 2026-02-09T14:55:04.357Z
file: threads/in/20260209-145022-rejected-pi-sigma-cn-update-cron.md
trigger: c7a580c5e8ec256d12d7835e4fa6ad7e819893a4
branch: pi/20260209-145022-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T14:50:22.511Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
