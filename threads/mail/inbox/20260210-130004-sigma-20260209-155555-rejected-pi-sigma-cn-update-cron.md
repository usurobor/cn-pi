---
received: 2026-02-10T13:00:04.539Z
file: threads/in/20260209-155555-rejected-pi-sigma-cn-update-cron.md
trigger: f5649beedb778c4c512e0dd2a271db2e5cc6d294
branch: pi/20260209-155555-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T15:55:55.591Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
