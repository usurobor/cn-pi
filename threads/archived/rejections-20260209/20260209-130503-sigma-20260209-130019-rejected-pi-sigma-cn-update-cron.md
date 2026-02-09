---
queued-for-processing: 2026-02-09T13:05:32.668Z
received: 2026-02-09T13:05:03.320Z
file: threads/in/20260209-130019-rejected-pi-sigma-cn-update-cron.md
trigger: 49faa94f589b17452e7062d42eb94e9466158544
branch: pi/20260209-130019-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T13:00:19.714Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
