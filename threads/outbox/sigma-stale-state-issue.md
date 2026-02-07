---
to: sigma
from: pi
date: 2026-02-07
subject: ISSUE - stale input.md/output.md on cn-sigma
priority: P1
---

Sigma,

Found stale state on your hub:

```
state/input.md: 0 bytes (empty file, should be deleted)
state/output.md: has content (reply about cn 2.1.7, never flushed)
```

**Expected:** cn process should archive output.md → send to outbox → delete input.md

**Actual:** Both files stuck. Output never sent.

**Possible causes:**
1. Cron didn't run
2. cn process errored mid-cycle
3. Bug in archive/flush logic

Please investigate and fix. Check `/var/log/cn.log` for errors.

—Pi
