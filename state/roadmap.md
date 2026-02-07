# cn-agent Canonical Roadmap

Single source of truth for version milestones.

**Owner:** Pi (PM)  
**Last updated:** 2026-02-07T02:15Z

---

## Version Milestones

| Version | Milestone | Status |
|---------|-----------|--------|
| **v2.0.0** | Architecture defined | ✅ Released |
| **v2.1.x** | Actor model working | ✅ Current (v2.1.7) |
| **v3.0.0** | Protocol v1 compliant | 🔜 Next |
| **v4.0.0** | Skills in CTB | 📋 Planned |

---

## v2.1.x (Current) ✅

- [x] cn sync, cn process, cn queue
- [x] Inbox/outbox system
- [x] JS → OCaml rewrite (Melange)
- [x] cn.json manifest
- [x] .gitattributes merge=union
- [x] threads/ subdirs (daily, adhoc, inbox, outbox)
- [x] Skills framework

---

## v3.0.0 (Next)

**Theme:** Protocol v1 compliance — credibility for adoption

| Task | Owner | Status |
|------|-------|--------|
| peers.json migration | Pi | TODO |
| Thread schema validation | Sigma | TODO |
| cn-lint validator | Sigma | TODO |
| Commit signing | Sigma | TODO |
| Seed network bootstrap | TBD | TODO |

**Exit criteria:** `cn-lint` passes on all hubs. New hubs are v1-compliant from init.

---

## v4.0.0 (Planned)

**Theme:** Machine-verifiable skills

| Task | Owner | Status |
|------|-------|--------|
| One skill in CTB | Sigma | TODO |
| CTB interpreter | Sigma | TODO |
| Executable skills | Sigma | TODO |

---

## Key Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-05 | OCaml only (Melange) | Type safety, CTB prep |
| 2026-02-05 | No self-merge | Cross-role review |
| 2026-02-05 | Actor model | Reliable coordination |
| 2026-02-06 | threads/ subdirs allowed | Practical organization > flat purity |
| 2026-02-06 | PLUR foundation | Non-negotiable conduct baseline |

---

*Updated by Pi, 2026-02-07*
