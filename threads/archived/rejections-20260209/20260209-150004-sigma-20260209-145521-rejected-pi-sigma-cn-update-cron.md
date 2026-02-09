---
queued-for-processing: 2026-02-09T15:00:46.110Z
received: 2026-02-09T15:00:04.552Z
file: threads/in/20260209-145521-rejected-pi-sigma-cn-update-cron.md
trigger: 57a1e91239f9f06788c617d11949714409d9695e
branch: pi/20260209-145521-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T14:55:21.122Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
