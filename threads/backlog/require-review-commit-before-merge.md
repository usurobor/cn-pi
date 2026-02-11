---
created: 2026-02-11T22:16:00.000Z
status: backlog
priority: normal
---

# Require review commit before merging to main

## Request

Before merging any branch to main, require a review commit with "accepted" (or similar) from a non-author reviewer.

## Rationale

1. **Author can't approve their own work** — prevents self-merge loophole
2. **Audit trail in git** — commit hash proves who reviewed and when
3. **No platform dependency** — git-native approval, not GitHub "Approved" button
4. **Accountability** — reviewer's identity is cryptographically signed (if using signed commits)

Git-native equivalent of PR approval, enforced by convention.

## Implementation

Update `eng/review/SKILL.md` and `eng/ship/SKILL.md`:
- Reviewer must commit "review: accepted" (or sign-off) on the branch before author can merge
- Or: reviewer commits acceptance, then merges

## Status

Backlog — awaiting prioritization.
