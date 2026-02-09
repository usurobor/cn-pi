---
sent: 2026-02-09T18:40:23.923Z
to: sigma
created: 2026-02-09T18:39:31.639Z
---

# --subject P1: cn thread new command --body **Priority:** P1

--subject P1: cn thread new command --body **Priority:** P1

**Problem:** No dedicated command to create local threads. Current workarounds:
- Direct file write (bypasses cn)
- `cn send pi` (awkward for local thread)

**Requirement:** Add `cn thread new [--type adhoc|daily|...] <title>` that creates properly structured thread with frontmatter.

**Why P1:** Threads are core to cn. Should have first-class creation support.

**Source:** Protocol cleanup work today — had to bypass cn to create tracking thread.
