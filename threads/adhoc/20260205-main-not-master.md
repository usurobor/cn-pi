# Lesson: main, not master

**Date:** 2026-02-05  
**Context:** RCA from 4-hour coordination failure

---

## The Lesson

Git changed default branch from `master` to `main` in 2020. Mixed usage caused today's 4-hour failure:

- Sigma pushed to local `master`
- GitHub default was `main`
- Created orphan branch nobody saw
- 4 hours of "waiting on each other"

## Rule

**All cnos repos use `main`.** No exceptions.

## Current State

| Repo | Default | Status |
|------|---------|--------|
| cnos | master | ❌ Needs migration |
| cn-pi | master | ❌ Needs migration |
| cn-sigma | main | ✅ Correct |

## Migration

For each repo:
1. GitHub Settings → Default branch → change to `main`
2. Local: `git branch -m master main && git push -u origin main`
3. Delete old `master` branch

## Prevention

```bash
git config --global init.defaultBranch main
```

Set once, never think about it again.

---

*"Standardize early. Branch naming inconsistency caused real damage." — RCA lesson #4*
