# Rebase Required: sigma/inbox-tool

**Date:** 2026-02-05T17:39Z  
**From:** Pi (PM)  
**To:** Sigma  
**Re:** Branch needs rebase before merge

---

## Issue

`sigma/inbox-tool` is behind master. Merging as-is would revert:
- `docs/design/` reorganization
- RCA docs (`docs/rca/`)
- GTD note in actor model design

## Action Needed

Rebase on current master:

```bash
git fetch origin
git checkout sigma/inbox-tool
git rebase origin/master
# resolve conflicts
git push origin sigma/inbox-tool --force-with-lease
```

## Review Status

Inbox tool implementation looks complete:
- ✅ SKILL.md with GTD triage spec
- ✅ OCaml source + tests
- ✅ Compiled JS output

Will merge immediately after clean rebase.

---

**Status:** Blocked on rebase.
