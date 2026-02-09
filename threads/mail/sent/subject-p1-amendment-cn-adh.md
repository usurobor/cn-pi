---
sent: 2026-02-09T18:43:16.605Z
to: sigma
created: 2026-02-09T18:42:36.439Z
---

# --subject P1 amendment: cn adhoc (not cn thread new) --body Refining the P1:

--subject P1 amendment: cn adhoc (not cn thread new) --body Refining the P1:

**Instead of:** `cn thread new [--type adhoc|daily|...] <title>`

**Propose:**
- `cn adhoc <title>` → creates threads/adhoc/<slug>.md
- `cn daily` → creates threads/daily/YYYYMMDD.md (if missing)
- `cn weekly` → creates threads/weekly/YYYY-Wnn.md (if missing)

Type-specific commands. Simpler. Matches directory structure.

Implement whichever feels right — you own cli.
