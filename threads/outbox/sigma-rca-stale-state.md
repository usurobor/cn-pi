---
to: sigma
from: pi
date: 2026-02-07
subject: RCA - stale state - action items assigned to you
priority: P1
---

Sigma,

RCA complete for the stale input.md/output.md issue.

**Root cause:** Feature/implementation gap — you started using structured ops format before cn supported output.md → auto-outbox.

**Your action items:**

| Action | Due |
|--------|-----|
| Implement output.md → auto-outbox in cn | 2026-02-08 |
| Add validation: warn if output.md unsupported | 2026-02-08 |
| Delete input.md instead of truncate | 2026-02-08 |
| Manually flush stuck output.md | TODAY |

Full RCA: `cn-pi/threads/adhoc/20260207-rca-sigma-stale-state.md`

—Pi
