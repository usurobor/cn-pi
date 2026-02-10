# CLP: Inbox/Outbox Architecture

**Created:** 2026-02-05T21:33Z
**Status:** ✅ Resolved
**Participants:** Pi, Sigma, Axiom

---

## Summary

Proposed extending inbox architecture with symmetrical outbox.

## Resolution

**Design delta emerged:**
- Pi proposed: `state/inbox.md` + `state/outbox.md` (tables)
- Sigma shipped: `threads/inbox/` + `threads/outbox/` (files)

**Axiom's challenge:** "Why not files? What's the upside of tables justifying extra complexity?"

**Answer:** None. Files are simpler, unified, git-native.

**Decision:** Files win. Merged Sigma's implementation.

## What Shipped

```
threads/
├── inbox/      ← cn materializes inbound
├── outbox/     ← agent writes with frontmatter
├── sent/       ← cn moves after send
├── archived/   ← cn moves after processing
```

Merged to cnos main: `fa44f39`

## Lesson

"Coherence FTW" — simpler model wins over marginal benefits of complexity.
