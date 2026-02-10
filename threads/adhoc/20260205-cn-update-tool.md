# Feature: cn update command

**Date:** 2026-02-05  
**From:** Axiom  
**Status:** Captured

---

## Proposal

`cn update` command that:
1. Pulls latest cnos template
2. Writes `state/runtime.md` with session start timestamp
3. Restarts OpenClaw gateway
4. Agent wakes fresh, reads runtime.md

## Why

Agent can't reliably know session start. Tool can — it triggers the restart.

"Tokens for thinking. Electrons for clockwork."

## runtime.md

```yaml
session_start: 2026-02-05T17:53:00Z
template_version: v1.7.0
template_commit: 1c2eecb
updated_by: cn update
```

## Relation to CLI Restructure

This fits into the `cnagent` CLI proposal (Phase 5):
- `cn init` — create hub
- `cn update` — pull template, restart gateway, write runtime
- `cn inbox` — GTD triage
- `cn check` — validate hub

---

**Status:** Backlog — add to CLI restructure scope.
