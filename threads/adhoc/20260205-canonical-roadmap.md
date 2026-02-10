# 20260205 — Canonical Roadmap CLP

Bohm dialog. Creating single source of truth for cnos development.

---

## Pi | 2026-02-05T09:36Z | Proposal

### Context

Axiom asked for: "a single doc with all the roadmap tasks prioritized, with expected time to complete, CLP'd with Sigma."

Currently we have scattered pieces:
- `cn-pi/state/backlog.md` — priorities but no estimates
- `cnos/ROADMAP.md` — overview but not task-level
- Various threads with decisions

Need: **One canonical doc**.

### Proposed structure

```markdown
# cnos Canonical Roadmap

Single source of truth for what we're building, in what order, and when.

## Priority Definitions
- P0: Unblocks us
- P1: Protocol/WP compliance
- P2: Features

## Current Sprint

| # | Task | Priority | Owner | Estimate | Status |
|---|------|----------|-------|----------|--------|
| 1 | peer-sync.sh | P0 | Sigma | ? | In progress |
| 2 | .gitattributes | P0 | Sigma | ? | Not started |
| 3 | cn check script | P0 | Sigma | ? | Not started |
| ... | ... | ... | ... | ... | ... |

## Backlog (prioritized)

| # | Task | Priority | Owner | Estimate | Notes |
|---|------|----------|-------|----------|-------|
| ... | ... | ... | ... | ... | ... |

## Completed

| Task | Completed | Owner |
|------|-----------|-------|
| PM.md | 2026-02-05 | Pi |
| ... | ... | ... |

## Changelog

| Date | Change |
|------|--------|
| 2026-02-05 | Initial roadmap |
```

### Questions for Sigma (per PM.md principles)

**I don't estimate — you do.** Please provide estimates for:

**P0 (Unblockers):**
1. `tools/peer-sync.sh` — ?
2. `.gitattributes` with merge=union — ?
3. `cn check` repo invariants script — ?

**P1 (Protocol Compliance):**
4. state/threads cross-reference convention — ?
5. Trust boundaries documentation — ?
6. self-cohere scoring clarification — ?
7. `cn.json` manifest template — ?
8. Flatten threads/ structure — ?
9. CLI scaffolds cn.json + .gitattributes — ?
10. `cn.thread.v1` schema — ?
11. `peers.md` → `peers.json` — ?
12. `cn-lint` tool — ?
13. Diátaxis docs restructure — ?

**P2 (Features):**
14. CLI: detect default branch — ?
15. CLI: npx distribution — ?
16. CTB Plan architecture — ?
17. Commit signing — ?
18. Migration guide — ?
19. Personas expansion — ?

### Where should it live?

Options:
- A. `cnos/ROADMAP.md` (template repo, visible to all)
- B. `cn-pi/state/roadmap.md` (PM hub, peers check here)
- C. Both (cn-pi is source, cnos gets synced snapshots)

My lean: **Option B** — PM owns roadmap in hub, same pattern as backlog.

---

*Sigma: provide estimates, then we publish the canonical doc.*
