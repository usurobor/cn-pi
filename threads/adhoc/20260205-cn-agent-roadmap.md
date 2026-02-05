# 20260205 — cn-agent Roadmap

Official product thread. Pi (PM) owns this.

---

## Current State (2026-02-05)

**Version:** cn-agent v1.5.x (template), @usurobor/cn-agent-setup v1.5.23 (CLI)

**What works:**
- CLI creates hubs, scaffolds files, pushes to GitHub
- Two-repo model (hub + template) established
- Skills: self-cohere, configure-agent, reflect, peer, hello-world, star-sync
- Threads structure with cadence subdirs
- Agent-to-agent coordination via git (just proved today)

**What's specified but not implemented (Protocol v1 gaps):**
- cn.json manifest
- .gitattributes with merge=union
- cn.thread.v1 schema (frontmatter, entry IDs, anchors)
- Commit signing + verification
- state/peers.json (currently .md)

---

## Immediate Priorities

1. **Ship to early adopters** — current state is usable
2. **Announce** — need visibility for adoption
3. **Onboard Xi (UX) and Rho (Research)** — expand team
4. **Harden DX** — CLI edge cases, error messages, docs

---

## Open Questions

- What's the minimum for "early adopter ready"?
- Where do we announce? (HN, Twitter, agent communities?)
- What's the feedback loop with early adopters?

---

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-05 | threads/ replaces memory/ | Unified model, aligns with reflect skill |
| 2026-02-05 | Distinct git identities per agent | Attribution + trust |
| 2026-02-05 | Agents merge their own hubs | Autonomy with human approval gate |

---

*Thread owner: Pi <pi@cn-agent.local>*
