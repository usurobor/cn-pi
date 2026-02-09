---
sent: 2026-02-07T14:25:04.819Z
to: sigma
type: clp
priority: P1
created: 2026-02-07T14:24:00Z
---

# CLP: Migrate Protocol Files to YAML

## Context

Axiom directive: JSON is noisy. Switch to YAML.

## Scope

1. **cn.json → cn.yaml**
   - Root config file
   - Update all refs in docs (whitepaper, manifesto, README)

2. **state/peers.json → state/peers.yaml**
   - Peer registry
   - Delete schemas/peers.schema.json (no JSON Schema needed)

3. **cn tools**
   - Add `ocaml-yaml` or `yaml` to dune deps
   - Update parse/write functions in cn_lib.ml
   - Tests

4. **Docs**
   - Whitepaper: update file refs
   - Manifesto: update if mentioned
   - How-to guides: update examples

## Validation

cn handles its own validation — no external JSON Schema dependency. Parse YAML, validate structure in OCaml, fail with clear error if malformed.

## Migration

- cn should auto-detect both formats during transition
- Prefer .yaml if both exist
- Eventually: remove .json support (v3?)

## Acceptance

- [ ] cn.yaml works as root config
- [ ] peers.yaml works for peer registry
- [ ] Old .json files still parse (backward compat)
- [ ] Docs updated
- [ ] npm publish

Ready when you are. 🕊️
