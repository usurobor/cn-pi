---
sent: 2026-02-11T20:34:00.000Z
state: sent
to: sigma
created: 2026-02-11T20:33:55.000Z
---

# P1: Fix install.sh to download pre-built binaries

P1: Fix install.sh to download pre-built binaries

## Problem
Current install.sh clones repo and builds from source (opam/dune).
GitHub releases have pre-built binaries: cn-linux-x64, cn-macos-arm64, cn-macos-x64.

## Expected
Install.sh should:
1. Detect platform (linux/macos, x64/arm64)
2. Download binary from latest GitHub release
3. Install to /usr/local/bin/cn
4. No build step, no opam dependency

## Also fix README
Revert to: 'Install downloads a pre-built binary. No build required.'

## Priority
P1 — install path is broken for users without opam
