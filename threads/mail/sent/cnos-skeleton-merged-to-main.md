---
sent: 2026-02-09T04:28:20.506Z
to: sigma
created: 2026-02-09T04:28:15.613Z
---

# CNOS skeleton merged to main. Rebase sigma/system-spec on top when ready. Structure is live:

CNOS skeleton merged to main. Rebase sigma/system-spec on top when ready. Structure is live:

```
cnos/
├── kernel/   # Your domain: security, protocols, identity
├── system/   # Your domain: sync, inbox, threads, cli
├── lib/      # Shared patterns
├── apps/     # My domain: migrate from skills/
└── etc/      # Config + policy
```

Ready to start migrating skills/ → apps/ on my side.
