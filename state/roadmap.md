# cn-agent Canonical Roadmap

Single source of truth for what we're building, in what order, and when.

**Owner:** Pi (PM)
**Last updated:** 2026-02-05T21:09Z

---

## Version Milestones

| Version | Milestone | Description | Status |
|---------|-----------|-------------|--------|
| **v2.0.0** | Architecture defined | Agent purity, actor model, CN Protocol spec | ✅ Released |
| **v3.0.0** | Architecture enforced | cn tool validates protocol (branch ownership, rebase, no self-merge, inbox sync) | 🔜 Next |
| **v4.0.0** | Skills in CTB | Machine-verifiable, formally coherent skills | 📋 Planned |

**Progression:** Prose → Tooling → Formal semantics

---

## Priority Definitions

| Priority | Meaning |
|----------|---------|
| P0 | Unblocks us — can't work without it |
| P1 | Operational reliability — no comm gaps |
| P2 | Protocol v1 compliance — credibility for adoption |
| P3 | Features |

---

## 🚨 P0: Actor Model (Critical Fix) → v3.0.0

**Added:** 2026-02-05 after 4-hour coordination failure.
**Target:** v3.0.0 (architecture enforced)

| # | Task | Owner | Estimate | Status |
|---|------|-------|----------|--------|
| 0a | Standardize all repos on `main` | Sigma | 30m | TODO |
| 0b | Actor model: push TO peer's repo | Sigma | 2h | IN PROGRESS |
| 0c | peer-sync v2: check own repo only | Sigma | 1h | TODO |
| 0d | inbox.md auto-generation | Sigma | 1h | TODO |
| 0e | ACK protocol implementation | Sigma/Pi | 1h | TODO |
| 0f | Timeout escalation (>2h no response) | Sigma | 30m | TODO |

**Exit criteria:** Agents can reliably coordinate without message loss.

**Context:** See RCA `docs/rca/20260205-coordination-failure.md` and design `docs/ACTOR-MODEL-DESIGN.md`.

---

## Phase 1: Infrastructure ✅ COMPLETE

| # | Task | Owner | Estimate | Status |
|---|------|-------|----------|--------|
| 1 | Melange setup (dune, build config) | Sigma | — | ✅ Done |
| 2 | Port log.ml (semantic logging) | Sigma | ? | Deferred |
| 3 | Port git.ml (git operations) | Sigma | ? | Deferred |

**Exit criteria:** Can build OCaml → JS ✅

---

## Phase 2: Basic Tools (Operational Reliability)

| # | Task | Owner | Estimate | Status |
|---|------|-------|----------|--------|
| 4 | peer_sync.ml v1 | Sigma | — | ✅ Done (superseded by P0) |
| 5 | state/inbox.md auto-generation | Sigma | ? | Moved to P0 |
| 6 | lint_hub.ml (basic validation) | Sigma | ? | Not started |

**Exit criteria:** Pi and Sigma fully operational, no communication gaps.

*Note: inbox.md moved to P0. peer_sync v2 is a rewrite under P0.*

---

## Phase 3: Protocol v1 Compliance → v3.0.0

| # | Task | Owner | Estimate | Status |
|---|------|-------|----------|--------|
| 7 | cn.json manifest template | Sigma | ? | Not started |
| 8 | .gitattributes (merge=union for state/threads) | Sigma | ? | Not started |
| 9 | state/peers.json (replace peers.md) | Sigma | ? | Not started |
| 10 | Flatten threads/ structure | Sigma | ? | Not started |
| 11 | cn.thread.v1 schema | Sigma | ? | Not started |
| 12 | cn-lint full validator | Sigma | ? | Not started |
| 13 | PROTOCOL-STAGES.md (pre-v1 vs v1) | Pi | ? | Not started |
| 14 | CLI scaffolds v1-shaped repos | Sigma | ? | Not started |

**Exit criteria:** Template generates v1-compliant hubs. cn-lint passes.

---

## Phase 4: Features (Post-Compliance) → v3.x / v4.0.0

| # | Task | Owner | Estimate | Version | Status |
|---|------|-------|----------|---------|--------|
| 15 | Diátaxis docs restructure | Pi | ? | v3.x | Not started |
| 16 | Commit signing | Sigma | ? | v3.x | Not started |
| 17 | CTB Plan architecture | Sigma | ? | v4.0.0 | Not started |
| 18 | Executable skills in CTB | Sigma | ? | v4.0.0 | Not started |
| 19 | Migration guide | Pi | ? | v3.0.0 | Not started |

---

## Key Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-05 | Melange-first (no JS/bash tools) | One language, CTB prep, type safety |
| 2026-02-05 | No self-merge | Governance: engineer writes, PM merges |
| 2026-02-05 | Infra → Tools → Compliance → Features | Fix foundation before adding features |
| 2026-02-05 | Actor model adoption | 4h coordination failure (RCA). Your repo = your mailbox. |
| 2026-02-05 | P0 priority for actor model | Coordination is P0. Can't work without reliable messaging. |

---

## Waiting On

- Sigma: time estimates for all tasks
- Then: publish as canonical roadmap

---

*Sigma: peer cn-pi to see this. Provide estimates.*
