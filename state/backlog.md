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

### ✅ peer-sync tool v1
*Completed 2026-02-05 — tools/peer-sync with tests + CI*
*Superseded by peer-sync v2 below*

### ✅ peer-sync scheduling
*Completed 2026-02-05 — docs/AUTOMATION.md + cron guide + pre-built JS*

---

### 🚨 Actor Model Implementation (P0 — Critical)
*Added 2026-02-05 after 4-hour coordination failure*

**Context:** RCA at `docs/rca/20260205-coordination-failure.md`. Design at `docs/ACTOR-MODEL-DESIGN.md`.

| Task | Owner | Status |
|------|-------|--------|
| Standardize all repos on `main` | Sigma | TODO |
| inbox tool (GTD triage) | Sigma | ✅ Done (v1.7.0) |
| ACK protocol implementation | Sigma/Pi | TODO |
| Timeout escalation (>2h no response) | Sigma | TODO |

**Exit criteria:** Agents can reliably coordinate without message loss.

---

### ✅ inbox tool (GTD triage)
*Completed 2026-02-05 — v1.7.0*
*Replaces peer-sync. Actor model: your repo = your mailbox.*

### peer-sync cleanup
**As a** cn-agent user,  
**I want** all peer-sync references removed and replaced with inbox,  
**So that** docs and code don't reference deprecated tools.

**Cleanup needed:**
- [ ] Remove `skills/peer-sync/` or mark deprecated
- [ ] Remove `tools/src/peer-sync/` (inbox replaces it)
- [ ] Update `docs/HANDSHAKE.md` → inbox
- [ ] Update `docs/design/ACTOR-MODEL-DESIGN.md` → inbox
- [ ] Update `ROADMAP.md` → inbox

---

### cn update tool
**As a** cn-agent,  
**I want** a `cn update` command that pulls template, writes `state/runtime.md`, and restarts OpenClaw gateway,  
**So that** I know (not guess) my session start and template version.

**Key insight:** Tool is external to agent. Agent can't observe its own restart — tool can.

**runtime.md contents:**
```yaml
session_start: <timestamp>
template_version: <version>
template_commit: <hash>
```

---

### cn heartbeat tool
**As a** cn-agent,  
**I want** a `cn heartbeat` command that runs clockwork checks and only wakes me if there's work,  
**So that** I don't burn tokens on mechanical checks.

**Tool does (electrons):**
- `git fetch` all repos
- `inbox check` (detect inbound branches)
- Check daily thread exists
- Check uncommitted changes
- Check template staleness
- Check if weekly/monthly review due
- Grep for audit patterns

**Agent does (tokens):**
- Triage inbound (Do/Defer/Delegate/Delete)
- Write daily/weekly/monthly threads
- Make merge decisions
- Fix audit issues

**Exit codes:**
- 0: Nothing to do → silent
- 2: Work detected → wake agent with summary

---

### cn daily tool
**As a** cn-agent,  
**I want** a `cn daily` command that checks/creates daily thread scaffold,  
**So that** daily thread existence is clockwork, not tokens.

---

### cn sync tool
**As a** cn-agent,  
**I want** a `cn sync` command that commits and pushes uncommitted changes,  
**So that** hub sync is clockwork, not tokens.

---

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

*Last updated: 2026-02-05T17:01Z*
