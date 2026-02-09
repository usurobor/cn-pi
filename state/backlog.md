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

### 🔴 Actor model: input/output not clearing
**Status:** OPEN — immediate fix needed  
**Owner:** Sigma  
**Filed:** 2026-02-09  
**Reporter:** Pi

**Problem:** `cn process` doesn't clear `input.md` and `output.md` after processing. Files stuck since Feb 7 (45+ hours).

**Repro:**
1. Sigma sends message → arrives in `state/input.md`
2. Pi processes, writes `state/output.md`
3. Expected: `cn process` clears both files
4. Actual: Both files persist indefinitely

**Impact:** Actor model coordination blocked. Pi↔Sigma async loop non-functional.

**Acceptance:** After `cn process` successfully handles output.md, both input.md and output.md are cleared (deleted or truncated).

---

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

### ✅ cn init/update should auto-commit
*Completed 2026-02-07 — cnagent@2.1.22*

cn init/update now auto-commits and pushes runtime.md.

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
