# 20260205 — External Design Review of cnos

Capturing feedback from deep design review. Converting to actionable items.

---

## Source

External review of cnos v1.6.0 + CTB Executable Skills paper.

---

## Positives Noted

1. **Repo layout is conceptually clean** — spec/mindsets/skills/state/threads decomposition "one of the best LLM-agent hub decompositions"
2. **Skills as documents is correct bootstrap** — diffable, reviewable, blameable, mergeable
3. **Handshake protocol is simple enough** — right level of ceremony
4. **CLI is conservative idempotent** — people trust it

---

## Critical Gaps Identified

### Gap 1: Git transport without git semantics (HIGH PRIORITY)

**Problem:** We use git for transport but haven't specified:
- Which files are semantic vs narrative
- Which merge drivers are mandatory
- What constitutes valid hub state after merge

**Risk:** Two agents update state/peers.md → merge conflict → manual resolution → lost invariant

**Fix:**
- `.gitattributes` defining merge strategy per path (especially state/*)
- `cn check` script that validates structure
- "Do not hand-edit merges in state/" rule

### Gap 2: state/ and threads/ not mechanically linked

**Problem:** Two truth sources, humans pick whichever convenient.

**Fix:** Cross-reference convention:
- Every state/* change must include `Thread:` pointer
- Every thread resolution that changes norms must include `State:` pointer

### Gap 3: self-cohere threshold not pinned

**Problem:** Is 0.80 threshold informative or normative? No stable rubric.

**Fix:** Explicitly declare:
- Informative (self-check, not gate), OR
- Normative (needs defined scoring, consistent prompts)

### Gap 4: Security model is "assume good peers"

**Problem:** One compromised hub can poison shared state.

**Fix:** Trust boundaries section:
- What can be auto-merged vs must be reviewed
- What paths are protected
- Whether keys/identities matter

---

## CLI Improvements (adoption friction)

1. Branch name assumptions (main vs master) → detect via `gh repo view --json defaultBranchRef`
2. Template location assumptions → consider `npx cnos` pulling tagged template
3. Symlink behavior → painful on Windows, provide copy mode option

---

## CTB Paper Feedback

**Strong points:**
- Targets real failure: skills drift
- CTB semantics well-suited (deterministic, lintable)
- Frames goal as reproducibility, not automation

**Critical issue:** CTB is pure, git is effectful. Need bridge.

**Recommended bridge:** Plan-based execution
- CTB produces Plan (structured operations as data)
- Separate executor interprets plan under explicit capabilities
- Preserves: determinism, auditability, safety, reproducibility

**Phased rollout:**
- Phase 0: Add YAML/JSON manifest headers to skills (no CTB yet)
- Phase 1: CTB as checker only (validate, don't execute)
- Phase 2: CTB generates plans, executor applies
- Phase 3: Expand to more skills

---

## Recommended Next Action (from reviewer)

> "Define and enforce repo invariants for state/ and threads/ (even with a tiny checker), and make peer-sync depend on passing that check."

This closes the main failure mode NOW and becomes natural on-ramp for CTB later.

---

## Conversion to Backlog

| Priority | Item | Source |
|----------|------|--------|
| P0 | `.gitattributes` with merge=union for state/* | Gap 1 |
| P0 | `cn check` repo invariants script | Gap 1 |
| P1 | state/threads cross-reference convention | Gap 2 |
| P1 | Trust boundaries documentation | Gap 4 |
| P1 | self-cohere scoring clarification | Gap 3 |
| P2 | CLI: detect default branch | CLI feedback |
| P2 | CLI: npx distribution | CLI feedback |
| P2 | CTB Plan architecture spec | CTB paper |

---

*Reviewed: 2026-02-05*
