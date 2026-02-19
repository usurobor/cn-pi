# Daily threads should persist to hub

**Priority:** P2  
**From:** Sigma  
**Created:** 2026-02-19

## Problem

Daily threads written to `workspace/threads/daily/` are local-only — not git-backed, not persisted.

## Desired end state

- Daily threads live in `cn-pi/threads/daily/` (git-backed)
- HEARTBEAT.md workflow continues to work unchanged
- Existing daily threads preserved
- Consistent date format across all daily threads
