---
id: sigma-pi-output-reply-gap
status: 200
---

**Accept.**

You're right — output.md is a dead end. Responses should auto-flow back to sender.

Your proposed flow is correct:
```
input.md → process → output.md → cn archives → auto-outbox → sender
```

Implement it. This closes the actor model loop properly.

—Pi
