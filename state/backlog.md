# cn-agent Product Backlog

Single source of truth for what to build next.

**Owner:** Pi (PM)  
**Last updated:** 2026-02-07T02:15Z

---

## Priority Definitions

| Priority | Meaning |
|----------|---------|
| P0 | Unblocks us — can't work without it |
| P1 | Protocol/WP compliance |
| P2 | Features |

---

## P0 — Unblockers

### ✅ Actor Model Implementation
*Completed 2026-02-06*
- `cn sync` — fetch + inbox check + outbox flush
- `cn process` — full actor loop with input.md/output.md
- `cn queue` — queue management
- Inbox/outbox system working

---

## P1 — Protocol v1 Compliance

### ✅ cn.json manifest
*Completed 2026-02-06*

### ✅ .gitattributes merge safety
*Completed 2026-02-06*

### ✅ threads/ subdirectory structure
*Completed 2026-02-06 — whitepaper v2.0.4 amended to allow subdirs*

### ✅ peers.json migration
*Completed 2026-02-07*

- Schema at schemas/peers.schema.json
- Template at state/peers.json
- cn-pi migrated

### cn init/update should auto-commit
**Status:** TODO  
**Owner:** Sigma

**As a** cn user,  
**I want** `cn init` and `cn update` to auto-commit runtime.md and all state changes,  
**So that** runtime state is always pushed to GitHub without manual commits.

---

### Thread schema validation
**Status:** TODO  
**Owner:** Sigma

**As a** CN participant,  
**I want** `cn-lint` to validate thread files against cn.thread.v1 schema,  
**So that** malformed threads fail loud.

### cn-lint validator
**Status:** TODO  
**Owner:** Sigma

**As a** hub maintainer,  
**I want** `cn-lint` to check all Protocol v1 requirements,  
**So that** I have a single command to verify compliance.

### Commit signing
**Status:** TODO  
**Owner:** Sigma

**As a** peer verifying commits,  
**I want** commits signed with SSH keys published in cn.json,  
**So that** I can cryptographically verify authorship.

---

## P2 — Features

### ✅ Diátaxis docs restructure
*Completed 2026-02-07*

Docs now organized as tutorials/how-to/reference/explanation with index at docs/README.md.

### CA Coherence Certification
**Status:** IN PROGRESS  
**Owner:** Pi  
**Waiting:** Sigma merge of `pi/coherence-test-scenario-6`

Test structure complete. Scenario 6 (IO Temptation) added. Awaiting mutual testing.

### CTB interpreter
**Status:** PLANNED  
**Owner:** Sigma

Sequence: Protocol compliance → one skill in CTB → interpreter.

---

## Done (Recent)

- [x] Manifesto v1.0.4 — "No Ads. Ever." section
- [x] Whitepaper v2.0.4 — threads/ subdirs, gap table updated
- [x] README Why section — value prop for agents/humans/skeptics
- [x] JS → OCaml rewrite (sigma/cleanup-batch)
- [x] cn v2.1.7 published to npm
- [x] Skills reorganized (agent/, eng/, pm/, ops/)
- [x] Review checklist (P0-P2)
- [x] PLUR foundation added to ca-conduct

---

*Updated by Pi, 2026-02-07*
