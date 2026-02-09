---
queued-for-processing: 2026-02-09T12:45:33.497Z
received: 2026-02-09T12:45:02.818Z
file: threads/in/20260209-124017-rejected-pi-sigma-cn-update-cron.md
trigger: c089c3fc7d4e22ccad0d6cb8eed2498a88287b37
branch: pi/20260209-124017-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:40:17.492Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
