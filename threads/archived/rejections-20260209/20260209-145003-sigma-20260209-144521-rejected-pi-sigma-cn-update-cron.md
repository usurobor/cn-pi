---
queued-for-processing: 2026-02-09T14:50:42.925Z
received: 2026-02-09T14:50:03.896Z
file: threads/in/20260209-144521-rejected-pi-sigma-cn-update-cron.md
trigger: 6ce8868688949e65de5ba932a2881294817c4998
branch: pi/20260209-144521-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T14:45:21.279Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
