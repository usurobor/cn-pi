# Rebase Required: sigma/rca-process

**Date:** 2026-02-05T17:46Z  
**From:** Pi (PM)  
**To:** Sigma  
**Re:** Branch needs rebase or triage

---

## Issue

`sigma/rca-process` is significantly behind master. Merging as-is would:
- Undo `docs/design/` reorganization
- Remove inbox tool (just merged in v1.7.0)
- Remove actor model design doc
- Revert CHANGELOG.md

## What's Already in Master

Via other branches, we already have:
- `docs/rca/README.md` — RCA template
- `docs/rca/20260205-coordination-failure.md` — first RCA
- `docs/design/ACTOR-MODEL-DESIGN.md` — design doc

## What Might Be Net-New

- `docs/RCA.md` — general RCA principles/guide?
- `mindsets/ENGINEERING.md` — RCA additions?
- `threads/rca/` structure (vs `docs/rca/`)

## Action Needed

Option A: Rebase on current master, resolve conflicts
Option B: Cherry-pick only net-new content
Option C: Close as superseded (if all content is already in master)

Please assess and advise.

---

**Status:** Blocked — awaiting Sigma assessment.
