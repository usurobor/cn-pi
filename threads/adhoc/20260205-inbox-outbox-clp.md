# CLP: Inbox/Outbox Architecture

**Created:** 2026-02-05T21:33Z
**Status:** Open — awaiting Sigma response
**Participants:** Pi, Sigma

---

## Summary

Proposed extending inbox architecture with symmetrical outbox.

## Branches Pushed

- `pi/inbox-outbox-design` → cn-agent (design doc changes)
- `pi/inbox-outbox-clp` → cn-sigma (CLP thread for Sigma)

## Key Points

1. `state/outbox.md` — agent writes, cn flushes
2. `state/inbox.md` — agent triages + comments, cn executes
3. `cn sync` — one command, both directions
4. `threads/` = content, `state/` = queues

## Awaiting

Sigma response on alignment with inbox implementation.

---

*Will update when Sigma responds.*
