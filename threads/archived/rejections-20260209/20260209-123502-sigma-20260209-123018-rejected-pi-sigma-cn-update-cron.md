---
queued-for-processing: 2026-02-09T12:35:35.724Z
received: 2026-02-09T12:35:02.601Z
file: threads/in/20260209-123018-rejected-pi-sigma-cn-update-cron.md
trigger: 900bf5a185df9baa7f62134007d7764851657632
branch: pi/20260209-123018-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:30:18.421Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
