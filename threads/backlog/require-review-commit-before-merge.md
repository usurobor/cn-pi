---
created: 2026-02-11T22:16:00.000Z
status: backlog
priority: normal
---

# Require review commit before merging to main

## Request

Before merging any branch to main, require a review commit with "accepted" (or similar) from a non-author reviewer.

## Rationale

Creates explicit audit trail of review approval in git history.

## Implementation

Update `eng/review/SKILL.md` and `eng/ship/SKILL.md`:
- Reviewer must commit "review: accepted" (or sign-off) on the branch before author can merge
- Or: reviewer commits acceptance, then merges

## Status

Backlog — awaiting prioritization.
