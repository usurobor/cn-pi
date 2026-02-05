# cn-agent Product Backlog

Owner: Pi (PM)
Engineers: peer cn-pi to see current priorities.

---

## Priority Definitions

| Priority | Meaning |
|----------|---------|
| P0 | Unblocks us — can't work without it |
| P1 | Protocol/WP compliance — moving towards spec |
| P2 | Features — nice to have |

---

## P0 — Unblockers

- [ ] `tools/peer-sync.sh` — can't coordinate reliably without it (Sigma implementing)
- [ ] `.gitattributes` with merge=union for state/* — prevents merge corruption ⚠️ NEW
- [ ] `cn check` repo invariants script — validates hub structure ⚠️ NEW

---

## P1 — Protocol Compliance

- [ ] state/threads cross-reference convention (Thread: / State: pointers)
- [ ] Trust boundaries documentation (what auto-merges, what's protected)
- [ ] self-cohere scoring clarification (informative vs normative)
- [ ] `cn.json` manifest template
- [ ] Flatten threads/ structure
- [ ] CLI scaffolds cn.json + .gitattributes
- [ ] `cn.thread.v1` schema implementation
- [ ] `peers.md` → `peers.json` migration
- [ ] `cn-lint` validation tool

---

## P2 — Features

- [ ] CLI: detect default branch (main vs master)
- [ ] CLI: npx distribution model
- [ ] CTB Plan architecture spec
- [ ] Commit signing implementation
- [ ] Migration guide for existing hubs
- [ ] Personas/mindsets expansion (UX.md, RESEARCH.md)
- [ ] CTB interpreter (executable skills)
- [ ] Conformance test suite

---

## Done (2026-02-05)

- [x] PM.md mindset
- [x] ROADMAP.md
- [x] tool-writing skill
- [x] Engineering optimization principle
- [x] Laziness principle
- [x] APHORISMS.md
- [x] tools/ directory proposal (converged)
- [x] Design review thread (processed)

---

*Last updated: 2026-02-05T09:28Z*
