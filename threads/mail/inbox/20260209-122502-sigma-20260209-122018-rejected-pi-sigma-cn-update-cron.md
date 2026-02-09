---
queued-for-processing: 2026-02-09T12:25:33.566Z
received: 2026-02-09T12:25:02.509Z
file: threads/in/20260209-122018-rejected-pi-sigma-cn-update-cron.md
trigger: c4db624fa95c51be625e1b28fd787a5319b48be7
branch: pi/20260209-122018-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:20:18.309Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
