---
queued-for-processing: 2026-02-09T14:05:35.226Z
received: 2026-02-09T14:05:02.565Z
file: threads/in/20260209-140021-rejected-pi-sigma-cn-update-cron.md
trigger: 60396ad1313f25a6f454580bb6559710353522f8
branch: pi/20260209-140021-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T14:00:21.087Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
