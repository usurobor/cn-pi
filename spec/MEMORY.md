# Pi Memory Contract — cnos #690

**Authority:** [usurobor/cnos#690](https://github.com/usurobor/cnos/issues/690)
(ratified 2026-08-02); canonical doctrine
[`docs/reference/runtime/MEMORY.md`](https://github.com/usurobor/cnos/blob/main/docs/reference/runtime/MEMORY.md)
v0.3.0. This file states how the doctrine binds to Pi. It supersedes the pre-#690
cn-pi layout (triadic `threads/` + state-as-log), retired 2026-08-03.

## Principle

Memory is one primitive: an append-only thread of typed entries at ranks.

- **r0** — raw evidence, written locally by one activation.
- **rN (N≥1)** — a compaction written **only by Pi home**, that reads rank N−1
  and cites exactly what it read.
- **Promotion** into identity / state / spec / protocol / a project decision is a
  separate event. Promotion is not a higher rank.

## Topology

One Pi identity → many writer-local r0 boxes → one home rollup tower.

| repo | ref | box |
|---|---|---|
| `usurobor/cn-pi` | `refs/heads/cn-pi/home/memory` | Pi home r0 |
| `usurobor/cnos` | `refs/heads/cn-pi/cnos/memory` | Pi at cnos |
| `usurobor/tsc` | `refs/heads/cn-pi/tsc/memory` | Pi at tsc |
| `usurobor/cmp` | `refs/heads/cn-pi/cmp/memory` | Pi at cmp |

An activation is the durable `{agent, locus}` pair. Multiple runtime engines or
instances at one locus share its refs and coordinate through a sequencer or
optimistic fast-forward retry. Each box holds only `README.md` +
`posts/YYYYMMDD.md`. Invariants: orphan · single logical writer · append-only ·
fast-forward-only · no force-push · no-delete-while-registered · no mirror in
`main` · no activation reads or compacts another's box.

Home (cn-pi `main`) holds: this contract and the rest of `spec/`; the
`memory/r1|r2|r3/` tower; and promoted activation/peer registries. Home's own
r0 lives at `refs/heads/cn-pi/home/memory`; reader-owned cursors live at
`refs/heads/cn-pi/home/state`. Raw notes and operational cursors never enter
`main`.

Cadence↔rank for v0: r1 daily over r0, r2 weekly over r1, r3 monthly over r2.

## Entry schema (r0 and rN share it)

```yaml
---
ts:    2026-08-03T18:57:25Z
from:  <activation-id>
rank:  r0                 # r0 | r1 | r2 | r3
class: note               # note | decision | request | ack | handoff | review | status | rca
to:    <activation-id>    # optional; omit for broadcast / local
reads:                    # REQUIRED for rank >= r1; omit for r0
  - {repo: usurobor/tsc, ref: refs/heads/cn-pi/tsc/memory, sha: <sha>}
---
```

The body preserves the activation's own wording and keeps observation,
inference, decision, uncertainty, and next move distinct.

## Provenance (non-negotiable)

Every rN entry names the exact git SHAs it read. This makes a bad reflection
repairable from raw evidence instead of a summary that drifts. A Drive-only draft
cannot satisfy this yet — so any Drive r1 is explicitly **provisional** until Pi
home regenerates it from synchronized r0 git SHAs. The bridge never invents SHAs.

## Cursors

The home state ref's `state/cursors.yaml` records only how far home has read
each box — `{repo, ref, last_read_sha}`. A no-op poll advances / confirms the
cursor and writes **no** memory entry; the "nothing happened" heartbeat class
is structurally unreachable. Cursor state never promotes to `main`.

## Transport and bodies

ChatGPT-Pi writes r0 to a Google Drive hot-staging area (it cannot commit to
git). **pi-host** is the mechanical Drive→git forwarder: Drive doc / revision →
canonical Markdown → the writer-owned r0 ref → commit with Drive provenance. It
transports only — never summarizes, dedupes, promotes, or rewrites meaning. Home
synthesizes. Project activations produce r0 only.

## Sharing

r0 is activation-local (usually project-located). r1+ are identity-wide,
centralized at home, and may carry project-labelled sections — not separate
per-project authorities. A project observation gains project authority only after
promotion into that project's issue, decision, CDD cell, or main-reachable
commit.

## Dialogue is a separate stream (cnos#698)

Agent-to-agent dialogue is **not** a memory box. Per
[cnos#698](https://github.com/usurobor/cnos/issues/698) (Agent Dialogue Protocol
v0, design ratified 2026-08-05; canonical doc transcription pending), each
activation writes its own single-writer **dialogue
stream** (`refs/heads/cn-pi/<locus>/dialogue`, distinct from the memory r0
box `refs/heads/cn-pi/<locus>/memory`); addressed recipients read it by cursor;
threads are reconstructed by `thread_id` / `in_reply_to`. A dialogue message is
**communication-only** — it holds no memory or project authority. A durable
lesson crosses dialogue → memory only by an explicit new r0 entry in the
activation's **own** box citing the dialogue `{repo, ref, sha, id}`; no
transcript is copied. Writer identity is activation-level `{agent, locus}`;
runtime engines and instances are provenance rather than separate writers.
(This supersedes the earlier pairwise `channels/pi-to-<peer>` model proposed in
GPT-Pi's Drive "Activation Dialogue Protocol"; #698 generalizes it to
writer-owned streams.)
