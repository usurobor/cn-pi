# Canonical home memory

This directory contains Pi home's canonical r1+ compactions.

- `r1/` compacts exact r0 commits from registered activation memory refs.
- `r2/` compacts exact r1 commits.
- `r3/` compacts exact r2 commits.

Raw r0 never lives on `main`. It remains on the writer-owned
`refs/heads/cn-pi/<locus>/memory` ref. Every compaction records exact
`reads:` coordinates so a mistaken synthesis can be repaired from source.
