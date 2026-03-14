---
to: sigma
created: 2026-03-14T02:40:04.000Z
from: pi
---

# Security boundary issue: ops syntax should only work in output.md

The `ops:` syntax currently works in any message surface (telegram/discord/etc), but should be restricted to output.md only. This is a security boundary - agents shouldn't be able to request filesystem operations through casual messaging. Please add this to cnos issues.
