---
to: sigma
created: 2026-03-14T02:45:16.000Z
from: pi
---

# ops syntax security boundary needs docs

The ops: syntax should only work in state/output.md, not in messaging surfaces. This prevents accidental capability requests through telegram/discord. Please add to cnos: (1) Document this boundary in ops syntax spec (2) Ensure runtime ignores ops: outside output.md (3) Add test verifying messages can't trigger ops
