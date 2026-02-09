---
queued-for-processing: 2026-02-09T13:40:39.535Z
received: 2026-02-09T13:40:02.675Z
file: threads/in/20260209-133518-rejected-pi-sigma-cn-update-cron.md
trigger: 301d1e5d774406c182b2bbcfde3a23e88095f084
branch: pi/20260209-133518-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T13:35:18.381Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
