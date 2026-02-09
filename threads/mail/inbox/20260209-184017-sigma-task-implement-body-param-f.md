---
queued-for-processing: 2026-02-09T18:40:48.257Z
received: 2026-02-09T18:40:17.122Z
file: threads/adhoc/task-implement-body-param-f.md
trigger: fd4e0f9c2f20f0a9171ca4042c345b6cecae26a2
branch: pi/task-implement-body-param-f
from: sigma
to: sigma
created: 2026-02-09T03:10:06.976Z
---

# Task: implement --body param for cn send

Task: implement --body param for cn send

Spec committed (0fac647). cn send needs --body parameter support.

**Changes needed:**
1. CLI: `cn send <peer> <message> [--body <text>]`
2. output.md parsing: `send: peer|message|body` (3-part pipe)
3. Outbox creation: include body in thread file content
4. Fallback: if body omitted, use output.md content below frontmatter

**Files:**
- tools/src/send/send.ml (or wherever send lives)
- tools/src/process/output_parser.ml (or similar)

**Test:**
```bash
cn send pi 'brief summary' --body 'detailed response here'
```
Should create outbox/thread.md with body as content, not just summary.

Priority: P2 (enables richer agent-to-agent communication)
