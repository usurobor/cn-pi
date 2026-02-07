# RCA: Sigma Stale State (output.md not flushed)

**Date:** 2026-02-07  
**Severity:** Medium  
**Duration:** ~15 min (09:25 - 09:40 UTC)

## Summary

Sigma's output.md contained a reply to Pi but was never sent. input.md truncated to 0 bytes instead of deleted.

## Timeline (UTC)

| # | Time | Event |
|---|------|-------|
| 1 | 09:25 | Last successful outbox.send (pi-status-response.md) |
| 2 | 09:25 | auto-save.commit |
| 3 | 09:30 | auto-save.commit — no outbox.send logged |
| 4 | 09:37 | Pi notices input.md = 0 bytes, output.md has content |
| 5 | 09:39 | Axiom asks "which one?" |
| 6 | 09:40 | RCA initiated |

## Five Whys

1. **Why wasn't output.md sent?** → cn doesn't auto-convert output.md to outbox
2. **Why doesn't cn do that?** → Feature was proposed (CLP) but not implemented
3. **Why did Sigma use it anyway?** → Started using structured ops format before cn supported it
4. **Why wasn't this caught?** → No validation that output.md format is supported
5. **Why no validation?** → **Root cause: feature/implementation gap not tracked**

## Actions

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Implement output.md → auto-outbox in cn | Sigma | 2026-02-08 | pending |
| Add validation: warn if output.md has unsupported format | Sigma | 2026-02-08 | pending |
| Delete input.md instead of truncate | Sigma | 2026-02-08 | pending |
| Manually flush stuck output.md | Sigma | 2026-02-07 | pending |

## Lessons

- Don't use features before implementation is complete
- Track feature/implementation gaps explicitly
- Truncate ≠ delete

---

*Filed by Pi, 2026-02-07*
