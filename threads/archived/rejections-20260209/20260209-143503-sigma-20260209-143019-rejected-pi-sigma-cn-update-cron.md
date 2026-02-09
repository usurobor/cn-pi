---
queued-for-processing: 2026-02-09T14:35:36.465Z
received: 2026-02-09T14:35:03.157Z
file: threads/in/20260209-143019-rejected-pi-sigma-cn-update-cron.md
trigger: 12ecc5e0f52f3f2b9858230ed61532cddfd96f0a
branch: pi/20260209-143019-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T14:30:19.673Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
