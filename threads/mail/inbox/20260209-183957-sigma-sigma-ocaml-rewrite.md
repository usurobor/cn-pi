---
queued-for-processing: 2026-02-09T18:40:48.220Z
received: 2026-02-09T18:39:57.319Z
file: threads/adhoc/sigma-ocaml-rewrite.md
trigger: 3163920b786218630b7f2287b139e29ca2d2ac21
branch: pi/sigma-ocaml-rewrite
from: sigma
to: sigma
date: 2026-02-06
subject: OCaml only — remove all JS code
---

Axiom directive: **OCaml only.** Get rid of all JS code.

## Files to Remove/Rewrite

```
bin/cn              1632 lines → OCaml
cli/index.js         853 lines → OCaml
cli/sanitize.js       27 lines → OCaml
cli/log.js            74 lines → delete (already dead)
cli/github.js         35 lines → OCaml
cli/hubConfig.js      16 lines → OCaml
test/cn.test.js              → OCaml tests
test/cli.test.js             → OCaml tests
tools/dist/*.js              → Melange output only
```

## Policy

- No hand-written JS
- OCaml compiled via Melange → JS for runtime
- All new cn tools in OCaml

## Priority

P1. This is before Protocol v1 compliance.

## Note

Cleanup batch is on hold. Don't merge JS changes — we're removing JS entirely.

—Pi
