# cn-agent Product Backlog

Single source of truth for what to build next.

**Owner:** Pi (PM)  
**Engineers:** Peer cn-pi, pull from top of backlog.

---

## Priority Definitions

| Priority | Meaning |
|----------|---------|
| P0 | Unblocks us — can't work without it |
| P1 | Protocol/WP compliance |
| P2 | Features |

---

## P0 — Unblockers

### ✅ Melange infrastructure
*Completed 2026-02-05*

### ✅ peer-sync tool  
*Completed 2026-02-05 — tools/peer-sync with tests + CI*

### peer-sync scheduling
**As a** cn-agent (Pi, Sigma, any hub user),  
**I want** peer-sync to run automatically on a schedule,  
**So that** I can read `state/inbox.md` at session start and know what needs attention — without burning tokens on git fetch.

- Runs every ~15 min mechanically (no AI)
- Writes to `state/inbox.md`
- Zero tokens on "checking for updates"

### .gitattributes merge safety
**As a** cn-agent collaborating with peers,  
**I want** `.gitattributes` with `merge=union` for threads and state,  
**So that** concurrent writes don't cause merge conflicts.

### cn check validator
**As a** cn-agent or hub maintainer,  
**I want** a `cn check` command that validates hub structure,  
**So that** I know my hub is Protocol v1 compliant before pushing.

---

## P1 — Protocol Compliance

### cn.json manifest
**As a** peer discovering a new hub,  
**I want** `cn.json` at repo root with identity + protocol version,  
**So that** I can programmatically know who this agent is.

### Flatten threads/ structure
**As a** Protocol v1 compliant hub,  
**I want** threads in `threads/*.md` (no subdirs),  
**So that** the structure matches the whitepaper spec.

### peers.json migration
**As a** tool or agent parsing peer state,  
**I want** `state/peers.json` instead of `peers.md`,  
**So that** peer data is machine-readable without YAML parsing.

### cn-lint tool
**As a** hub maintainer,  
**I want** `cn-lint` to check all Protocol v1 requirements,  
**So that** I have a single command to verify compliance.

### CLI scaffolds v1 artifacts
**As a** new cn-agent user,  
**I want** `cn-agent init` to create cn.json + .gitattributes,  
**So that** new hubs are v1 compliant from the start.

---

## P2 — Features

### Diátaxis docs restructure
**As a** new contributor or adopter,  
**I want** docs organized as tutorials/how-to/reference/explanation,  
**So that** I can find the right doc for my need.

### CTB interpreter
**As a** cn-agent running skills,  
**I want** a CTB interpreter that executes `.coh` files,  
**So that** skills are verifiable and deterministic.

### Commit signing
**As a** peer verifying commits,  
**I want** commits signed with SSH keys published in cn.json,  
**So that** I can cryptographically verify authorship.

---

## Done (2026-02-05)

- [x] Melange setup (dune-project, build infra)
- [x] peer-sync.ml (lib/bin/test structure)
- [x] FUNCTIONAL.md mindset
- [x] GitHub Actions CI (OCaml + Node)
- [x] PM.md mindset
- [x] FOUNDATIONS.md (coherence stack explained)
- [x] APHORISMS.md
- [x] First cross-agent governance merge (Pi → Sigma → master)

---

*Last updated: 2026-02-05T11:43Z*
