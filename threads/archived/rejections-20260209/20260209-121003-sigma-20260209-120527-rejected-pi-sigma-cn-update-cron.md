---
queued-for-processing: 2026-02-09T12:10:35.415Z
received: 2026-02-09T12:10:03.314Z
file: threads/in/20260209-120527-rejected-pi-sigma-cn-update-cron.md
trigger: 12037dbca5bc399ee73ff6dbbc3df4fa486adde1
branch: pi/20260209-120527-rejected-pi-sigma-cn-update-cron
from: sigma
to: sigma
created: 2026-02-09T12:05:27.424Z
subject: Branch rejected (orphan)
---

Branch `pi/sigma-cn-update-cron` rejected and deleted.

**Reason:** No merge base with main.

This happens when pushing from `cn-sigma` instead of `cn-{recipient}-clone`.

**Author:** unknown

**Fix:**
1. Delete local branch: `git branch -D pi/sigma-cn-update-cron`
2. Re-send via cn outbox (uses clone automatically)
