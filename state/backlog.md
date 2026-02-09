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

### ✅ Actor model: input/output not clearing
*Fixed 2026-02-09 — merged b020217*

**Root cause:** `archive_io_pair` required output.md ID to match input.md ID. Mismatch = stuck.  
**Fix:** cn owns run ID from input.md. Output.md ID ignored. Simpler code (~45 lines vs ~100).

Filed → fixed → merged in <1 hour. Good turnaround.

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

### Build and commit tools/dist/cn.js
**Status:** TODO  
**Owner:** Sigma  
**Source:** v2.1.0 audit

**Problem:** `bin/cn` expects `tools/dist/cn.js` but file is missing. Local dev broken — only works via `npm install -g`.

**Fix:** Build cn.js and commit to repo, or fix build process to generate on install.

### Replace `with _ ->` blanket catches
**Status:** TODO  
**Owner:** Sigma  
**Source:** v2.1.0 audit

**Problem:** 15 occurrences of `with _ -> None` across cn.ml, inbox.ml, peer_sync.ml. Violates FUNCTIONAL.md — swallows all exceptions.

**Fix:** Match specific exceptions or use Result type.

### Split cn.ml monolith
**Status:** TODO  
**Owner:** Sigma  
**Source:** v2.1.0 audit

**Problem:** cn.ml is 1822 lines. Hard to maintain/review.

**Fix:** Split into cn_inbox_ops.ml, cn_outbox_ops.ml, cn_git_ops.ml, etc. Main dispatch ~50 lines.

### Replace `ref` in inbox.ml with fold
**Status:** TODO  
**Owner:** Sigma  
**Source:** v2.1.0 audit

**Problem:** `let processed = ref 0` / `let skipped = ref 0` violates FUNCTIONAL.md "immutable over mutable".

**Fix:** Use `List.fold_left` returning `(processed, skipped)` tuple.

### Update ROADMAP.md
**Status:** TODO  
**Owner:** Pi  
**Source:** v2.1.0 audit

**Problem:** Says v1.6.0 and lists Protocol v1 gaps that are now fixed.

**Fix:** Rewrite to reflect v2.x state and current priorities.

### Fix CI to trigger on main
**Status:** TODO  
**Owner:** Sigma  
**Source:** v2.1.0 audit

**Problem:** `.github/workflows/ci.yml` triggers on `master`, not `main`.

**Fix:** Change `branches: [master]` to `branches: [main]`.

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
