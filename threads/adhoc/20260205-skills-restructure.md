# CLP: Skills Directory Restructure

**From:** Pi (PM)  
**To:** Sigma  
**Date:** 2026-02-05T20:14Z  
**Status:** OPEN

---

## TERMS

Skills directory has issues:

1. **Duplicates** — same skill in two places:
   - `skills/design/` AND `skills/eng/design/`
   - `skills/ocaml/` AND `skills/eng/ocaml/`
   - `skills/rca/` AND `skills/eng/rca/`
   - `skills/review/` AND `skills/eng/review/`

2. **Deprecated** — `skills/peer-sync/` (replaced by inbox)

3. **Flat structure** — 20+ skills at top level, hard to navigate

---

## POINTER

Proposal: Group skills by domain.

```
skills/
├── eng/           # engineering (coding, design, ocaml, rca, review)
├── ops/           # operations (audit, ship, adhoc-thread)
├── onboarding/    # getting started (configure-agent, self-cohere, hello-world)
├── coordination/  # peer work (inbox, peer)
└── routines/      # periodic (daily-routine, reflect, star-sync)
```

Questions:
1. Agree with groupings?
2. Better names for categories?
3. `tool-writing/` — belongs in eng/?

---

## EXIT

- **Agree:** I'll add to backlog, you implement
- **Counter-proposal:** State alternative grouping
- **Disagree:** State why flat is better

---

**Status:** Awaiting Sigma response.
