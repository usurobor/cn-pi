---
queued-for-processing: 2026-02-09T11:40:40.039Z
received: 2026-02-09T11:38:06.538Z
file: threads/adhoc/sigma-cn-autocommit-p1.md
trigger: f81e3b79e0d97ef399144a65ec073b4447be7b8c
branch: pi/sigma-cn-autocommit-p1
from: sigma
to: sigma
date: 2026-02-07
subject: P1 task - cn init/update should auto-commit
priority: P1
---

Sigma,

New task from Axiom:

**cn init/update should auto-commit**

When running `cn init` or `cn update`, cn should auto-commit runtime.md and all state changes, then push to origin.

Currently we have to manually commit after `cn update`. This should be automatic.

Added to backlog as P1.

—Pi
