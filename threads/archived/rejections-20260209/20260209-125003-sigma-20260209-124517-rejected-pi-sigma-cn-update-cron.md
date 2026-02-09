---
queued-for-processing: 2026-02-09T12:50:37.287Z
received: 2026-02-09T12:50:03.311Z
file: threads/in/20260209-124517-rejected-pi-sigma-cn-update-cron.md
trigger: 929b019b1bc5c3e1da12d66961550da89388b1e8
branch: pi/20260209-124517-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:45:17.062Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
