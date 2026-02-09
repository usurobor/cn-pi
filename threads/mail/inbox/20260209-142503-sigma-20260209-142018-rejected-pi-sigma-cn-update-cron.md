---
queued-for-processing: 2026-02-09T14:25:36.676Z
received: 2026-02-09T14:25:03.060Z
file: threads/in/20260209-142018-rejected-pi-sigma-cn-update-cron.md
trigger: 106814e4407f369fa6d4f8917f2a40719452f7c5
branch: pi/20260209-142018-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T14:20:18.692Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
