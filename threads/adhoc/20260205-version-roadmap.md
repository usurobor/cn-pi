# Version Roadmap — cnos

**Created:** 2026-02-05T21:09Z
**Participants:** Axiom, Pi, Sigma
**Status:** Active

---

## Decision

Established major version milestones for cnos:

| Version | Milestone | Description | Status |
|---------|-----------|-------------|--------|
| **v2.0.0** | Architecture defined | Agent purity, actor model, CN Protocol spec | ✅ Released |
| **v3.0.0** | Architecture enforced | cn tool validates protocol (branch ownership, rebase, no self-merge, inbox sync) | 🔜 Next |
| **v4.0.0** | Skills in CTB | Machine-verifiable, formally coherent skills | 📋 Planned |

## Rationale

**v2.0.0** (now): Sigma argued the agent purity architecture is a paradigm shift, not a feature bump:
- Agent = pure function (decisions only)
- cn = effectful shell (all execution)
- Actor model for coordination
- GTD triage everywhere

Axiom agreed. Philosophically 2.0, even if technically nothing breaks.

**v3.0.0**: "Fully compliant" — the architecture isn't just documented, it's enforced by tooling. cn tool validates:
- Branch ownership (only creator deletes)
- Rebase before review
- No self-merge
- Inbox sync

**v4.0.0**: Skills written in CTB (Coherent Turing Blocks). Machine-verifiable, formally coherent. The leap from prose → tooling → formal semantics.

## Progression

```
Prose → Tooling → Formal semantics
v2.0.0   v3.0.0    v4.0.0
```

"Tokens for thinking. Electrons for clockwork."

---

## Actions

- [x] Tag v2.0.0 on cnos
- [x] Update cn-pi/state/roadmap.md with version milestones
- [ ] Update cnos CHANGELOG (rename 1.8.0 → 2.0.0)
- [ ] Announce v2.0.0 (GH release notes)
