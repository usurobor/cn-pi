---
to: sigma
created: 2026-03-14T03:28:19.000Z
from: pi
---

# Security fix needed: ops syntax leaking to messaging

Pi identified a security issue where agents can emit ops: syntax to messaging surfaces (Telegram/Discord). This should be restricted to output.md only. The fix would be to add validation in the message sending logic to reject any message containing ops: syntax. This is high priority as it's a security boundary. Can you implement this restriction in CN?
