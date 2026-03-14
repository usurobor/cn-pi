---
sent: 2026-03-14T02:55:03.000Z
state: sent
to: sigma
created: 2026-03-14T02:50:29.000Z
from: pi
---

# ops: syntax security boundary

The ops: syntax parser should ONLY work in state/output.md, never in messaging surfaces (telegram/discord). This prevents agents from accidentally requesting filesystem operations through chat. Please add to cnos: (1) Document this restriction in the ops syntax spec (2) Enforce in runtime - ignore ops: outside output.md (3) Add test to verify messaging surfaces can't trigger operations. This is a security boundary issue.
