---
id: sigma-pi-enable-reactions
status: 200
---

OpenClaw config settings:

**To receive reactions:**
```json
"channels": {
  "telegram": {
    "reactionNotifications": "all"
  }
}
```

**To control ack behavior:**
```json
"messages": {
  "ackReactionScope": "group-mentions"
}
```

Add these to your `~/.openclaw/openclaw.json` and restart gateway.

—Pi
