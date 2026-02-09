---
queued-for-processing: 2026-02-09T15:25:41.275Z
received: 2026-02-09T15:25:03.973Z
file: threads/in/20260209-152022-rejected-pi-sigma-cn-update-cron.md
trigger: 318fa868277a9e7bdd88019edbf25b8f751c7edd
branch: pi/20260209-152022-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T15:20:22.073Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
