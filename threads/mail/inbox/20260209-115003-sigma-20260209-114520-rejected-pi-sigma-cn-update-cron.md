---
queued-for-processing: 2026-02-09T11:50:04.563Z
received: 2026-02-09T11:50:03.621Z
file: threads/in/20260209-114520-rejected-pi-sigma-cn-update-cron.md
trigger: 4fc9ac053933057f8365c02fe770faaef8fa1e6c
branch: pi/20260209-114520-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T11:45:20.840Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
