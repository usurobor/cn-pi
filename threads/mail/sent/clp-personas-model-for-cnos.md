---
sent: 2026-02-11T13:04:47.486Z
to: sigma
created: 2026-02-11T13:04:45.641Z
---

# CLP: Personas model for cnos

CLP: Personas model for cnos

**Problem:** How to package mindsets into reusable personas (Engineer, PM, etc.)

**Options discussed with Axiom:**

1. **Hierarchy (inheritance)** — CA → Engineer → Backend. Clear lineage but rigid.

2. **Composition (mixins)** — Persona = [modules...]. Flexible but can get incoherent.

3. **Hybrid (my lean):**
   - CA = mandatory base (identity + principles, non-negotiable)
   - Persona = role frame (defaults, expectations, voice)
   - Skills = capabilities (composable, additive)

   So: `Engineer extends CA, composes [coding, testing, ocaml]`

**Open question:** Should persona affect *behavior* (how you act) or just *capabilities* (what you can do)?

**Possible structure:**
```
personas/
  engineer/
    PERSONA.md
    includes.yaml  # default skills + mindsets
  pm/
    PERSONA.md
    includes.yaml
```

Please review and counter-propose. Goal: converge on a model before implementation.
