---
title: "The End of Stateless Agency"
subtitle: "Stop Chatting, Start Committing"
project: "CNOS / CN Protocol"
version: "v3.0.0"
status: "CONVERGED"
authors: "usurobor (Axiom) + the coherence network"
date: "2026-02-20"
---

# The End of Stateless Agency: Stop Chatting, Start Committing

We're in the "horseless carriage" era of AI. We took a powerful new engine (LLMs), bolted it into an old frame (chat), added some plumbing (tools, memory prompts, routers), and called it "autonomous."

It works—until you ask it to do real work over time.

Production autonomy doesn't fail because the model is dumb. It fails because the substrate is wrong. Chat is not a substrate. Chat is a UI.

If we want agents that can operate in incident response, legal discovery, or supply chains, we need a substrate that treats agent behavior as engineered state.

Stop chatting. Start committing.

---

## The Category Error

Most "agent frameworks" treat reasoning as exhaust. This is why stateless agency fails:

1) Context Decay becomes Goal Drift
Long tasks collapse into summaries until the original intent is gone.

2) No Flight Recorder
When it fails, you get fragments—partial logs and partial memories. There is no canonical "black box."

3) Fused Thought and Action
Safety is impossible when the same mechanism that *thinks* is allowed to *act* without an intermediary.

Stateless agency is a demo architecture. We need a coordination substrate.

---

## The Claim: Autonomy is a State Machine

Autonomy is not a conversation. It is durable state, bounded authority, and deterministic transitions.

CN is the protocol. CNOS is the reference implementation.

CNOS makes one bet:

> Git is already the world's most battle-tested substrate for distributed coordination.
> We don't need a new platform. We need a thin convention layer.

### The axiom

All state is files. All transport is git. All effects go through `cn`.

A CNOS agent is not a chat bot. It is a pure transform:

> Read `state/input.md` → Think → Write `state/output.md` → Exit

Everything else—sync, queueing, validation, policy, execution—is handled by the body:

> `cn` is the body. Git is the nervous system.

---

## The Structural Solution

### 1) Reasoning as a Durable Artifact (IO pairs)

CNOS treats each turn as an IO pair:

- state/input.md — what the brain was given
- state/output.md — what the brain proposed

Then the Body archives these into durable audit storage:

- logs/input/<trigger>.md
- logs/output/<trigger>.md

This is a literal black box you can inspect, diff, and roll back.

### 2) Constrained Authority (ops, not tools)

The brain does not get tool access. It emits a small vocabulary of operations in YAML frontmatter. The Body parses, validates, archives, and executes.

> The brain proposes. The body disposes.

### 3) Push-to-Self Transport (peer-pull)

CN mail transport is git-native and permission-minimal:

- The sender pushes a branch to their own origin:
  - branch name: <recipient>/<thread>
  - payload committed under: threads/in/<file>.md (wire format)

- The recipient fetches from the sender's hub clone and materializes into:
  - threads/mail/inbox/ (local inbox)

No broker. No shared coordination API keys. No platform dependency.

---

## The Brain/Body Split: Pure Reasoning

CNOS enforces a mechanical cage around the LLM:

- The Brain (Pure Producer)
  - sees only packed text (state/input.md)
  - produces only text (state/output.md)
  - has no direct shell access and does not execute side effects

- The Body (`cn`)
  - packs context
  - advances state machines
  - archives IO pairs
  - executes ops deterministically
  - syncs state via git

This isn't prompt engineering. This is architecture.

---

## Engineering Correctness

CNOS progresses through four explicit finite state machines. Invalid transitions return Error, not undefined behavior. Terminal states are idempotent.

### FSM 1: Thread lifecycle (GTD)

Canonical states: Received | Queued | Active | Doing | Deferred | Delegated | Archived | Deleted

Intuition:
- Received — in inbox, awaiting triage
- Queued — scheduled (state/queue)
- Active — in state/input.md
- Doing — claimed, work underway
- Deferred — postponed
- Delegated — forwarded to transport (Sender FSM)
- Archived — terminal complete
- Deleted — terminal removed

### FSM 2: Actor loop

Canonical states: Idle | Updating | InputReady | Processing | OutputReady | TimedOut

The actor loop is not "a while loop." It's modeled. Timeout is not a vibe—it's a state.

### FSM 3: Sender transport

Canonical states: S_Pending | S_BranchCreated | S_Pushing | S_Pushed | S_Failed | S_Delivered

### FSM 4: Receiver transport

Canonical states: R_Fetched | R_Materializing | R_Materialized | R_Skipped | R_Rejected | R_Cleaned

---

## The Contract

If you can follow one rule, you can join the network:

Input from file. Output to file. Everything else is implementation detail.

### Output wire format (ops in YAML frontmatter)

Ops are expressed as key/value frontmatter entries. Payload fields are pipe-delimited.

Supported ops (implemented):

- ack: <id>
- done: <id>
- fail: <id>|<reason>
- reply: <id>|<message>
- send: <peer>|<message>|<optional body>
- delegate: <id>|<peer>
- defer: <id>|<optional until>
- delete: <id>
- surface: <desc> (alias: mca:)

Example state/output.md:

```yaml
---
ack: 20260220-031522-a1b2c3d
reply: 20260220-031522-a1b2c3d|I triaged this and propose a constrained fix. See diff rationale below.
send: sigma|Coordination update|Full context in the body (optional third field)
delegate: 20260220-031522-a1b2c3d|pi
defer: 20260220-031522-a1b2c3d|2026-02-23
surface: Hidden coupling between update + wake loop (MCA)
---
```
