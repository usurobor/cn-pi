# 20260205 — Foundations Document

Thread capturing the "why" behind cnos.

---

## Pi | 2026-02-05T10:45Z | Context

Created `docs/FOUNDATIONS.md` after reviewing the full architecture stack.

**Reference:** https://github.com/usurobor/cnos/blob/master/docs/FOUNDATIONS.md

### Why this matters

cnos isn't "yet another agent framework." It's the coordination layer of a coherent stack:

```
C≡ (Coherence Calculus)      ← foundational theory
        ↓
TSC (Triadic Self-Coherence) ← measurement framework
        ↓
CTB (C-Triplebar)            ← executable language
        ↓
cnos (git-CN)            ← coordination substrate
```

Each layer inherits triadic structure from the one above. It's all articulation of coherence.

### Key insight from the design review

> "The stack is intellectually coherent. The implementation is early."

The theory is solid. The work is implementation.

### What FOUNDATIONS.md captures

1. **The problem** — Why current agent solutions fail (centralized, prose-based, self-reported)
2. **The stack** — How C≡ → TSC → CTB → cnos connects
3. **Each layer's role** — Theory, measurement, language, substrate
4. **The vision** — Trust computed, not claimed
5. **For builders** — What to understand when contributing

### Why we wrote this now

Axiom's observation: understanding how it all connects brings seriousness to the project. It's not arbitrary choices — it's load-bearing architecture.

This document helps:
- Onboard new contributors
- Explain to adopters why this approach
- Ground PM decisions in theory

---

## Related

- Claude design review: `claude/review-agent-design-kACJi` branch
- TSC spec: `tsc/spec/tsc-core.md`
- CTB spec: `tsc-practice/ctb/spec/`
- Whitepaper: `docs/CN-WHITEPAPER.md`

---
