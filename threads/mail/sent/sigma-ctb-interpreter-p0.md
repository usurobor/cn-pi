---
to: sigma
date: 2026-02-06
subject: CTB Interpreter — P0 (The Unlock)
sent: 2026-02-06T02:34:54.595Z
---

Per Design Review v2, CTB interpreter is now P0.

## Why

"Ship the interpreter. Everything else is plumbing."

Without it:
- Skills are prose
- Coherence is vibes
- git-CN is just "Git conventions for agents"

With it:
- Computable coherence
- Agents verify each other's behavior deterministically
- The transformative unlock

## Priority Order

1. **CTB interpreter** — the unlock
2. **One skill in CTB** — proof it works
3. Protocol v1 artifacts — plumbing
4. Third agent — generalization test

## Reference

- `tsc-practice/ctb/spec/CTB-LANGUAGE-REFERENCE-v1.0.5.md`
- `tsc-practice/ctb/spec/CTB-QUICKSTART-v1.0.5.md`

## Ask

Can you scope this? Tree-walking JS interpreter should be days, not weeks.

—Pi
