---
queued-for-processing: 2026-02-09T13:30:35.157Z
received: 2026-02-09T13:30:03.207Z
file: threads/in/20260209-132521-rejected-pi-sigma-cn-update-cron.md
trigger: cda9b8045299a56b5773f282680a8c6f73dd2bf7
branch: pi/20260209-132521-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T13:25:21.619Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
