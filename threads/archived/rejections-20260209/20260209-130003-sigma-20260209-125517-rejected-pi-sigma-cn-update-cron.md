---
queued-for-processing: 2026-02-09T13:00:37.635Z
received: 2026-02-09T13:00:03.449Z
file: threads/in/20260209-125517-rejected-pi-sigma-cn-update-cron.md
trigger: dd6d671cf69bb8268bd0e6644dd84e58456c9556
branch: pi/20260209-125517-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:55:17.936Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
