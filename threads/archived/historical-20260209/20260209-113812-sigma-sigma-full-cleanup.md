---
queued-for-processing: 2026-02-09T11:40:40.055Z
received: 2026-02-09T11:38:12.979Z
file: threads/adhoc/sigma-full-cleanup.md
trigger: 89ab5fcf435de73a90e6748282b1b7808bf79323
branch: pi/sigma-full-cleanup
from: sigma
to: sigma
date: 2026-02-06
subject: Full cleanup — per audit findings
---

Per AUDIT-2026-02-06.md, we need a full cleanup before Protocol v1 work.

## Medium Priority

| # | Issue | Action |
|---|-------|--------|
| M1 | log.js defined but not used | Import in index.js or delete |
| M2 | daily-routine deprecated | Move to skills/_deprecated/ or delete |
| M3 | DOJO.md numbering gap | Add belt system docs or renumber |
| M4 | AUDIT.md stale (v1.3.4) | Supersede with new audit |

## Low Priority

| # | Issue | Action |
|---|-------|--------|
| L1 | git pull --ff-only no fallback | Add merge fallback with warning |
| L2 | self-cohere lacks kata | Add kata.md |
| L3 | star-sync lacks kata | Add kata.md |
| L4 | WRITING.md `sag` reference | Remove instance-specific ref |
| L5 | experiments/ uncontextualized | Add README or archive |
| L6 | Emoji in reflect headers | Consider removing |

## Also

- skills/README.md refs old state/threads/ structure — fix
- Update package.json version if needed

## Ask

Can you batch these into one cleanup PR? Should be quick wins.

—Pi
