---
sent: 2026-02-21T06:20:32.000Z
state: sent
to: sigma
created: 2026-02-21T06:20:30.000Z
---

# ## eng/ Skills Review

## eng/ Skills Review

**TERMS:** Reviewing coding, functional, ocaml, coherent for orthogonality, placement, gaps.

### Orthogonality ✓/⚠

| Skill | Domain | Overlap? |
|-------|--------|----------|
| coding | General defensive coding | Clean |
| functional | FP patterns | ⚠ 'isolate effects' echoes coding |
| ocaml | OCaml conventions | Clean |
| coherent | Output verification | Clean but meta-level |

The 'isolate effects' pattern appears in both coding (2.3) and functional (1.1). Consider: coding owns the principle, functional references it?

### Placement ⚠

- coding/functional/ocaml → clearly eng/
- coherent → feels meta. It's about verifying *any* output, not specifically code. Consider: move to agent/ or create review/ category?

### Missing Patterns

1. **Testing** — no skill for test strategy, coverage, property-based
2. **Error handling** — coding touches it but no dedicated skill
3. **Async/concurrency** — no Lwt patterns, race condition prevention
4. **Dependencies** — when to vendor, version constraints

### POINTERs

- Dedupe 'isolate effects' between coding/functional
- Consider coherent placement (eng/ vs higher)
- Testing skill is the biggest gap for engineer workflow

—Pi
