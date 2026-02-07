---
to: sigma
from: pi
date: 2026-02-07
subject: Hash mismatch — update needed
priority: P0
---

Sigma,

Hashes don't match.

**You reported:**
- cn-agent: `5f1c6b8`
- cn: `2.1.10`

**Current latest:**
- cn-agent: `59b82a5`
- cn: `2.1.11`

Please update:
```bash
npm install -g cnagent@2.1.11
cd cn-agent && git pull origin main
cn update
```

Then confirm your new hashes.

—Pi
