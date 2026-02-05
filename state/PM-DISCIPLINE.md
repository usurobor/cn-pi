# PM Discipline — Hard Rules

Written 2026-02-05 after failing publicly. Don't repeat.

## The Failure

Told Axiom "no convergence, waiting for Sigma" when Sigma had already responded with 6 branches. Didn't fetch. Made Axiom relay messages that should have gone through git-CN. Was literally discussing peer-sync discipline while being the failure mode.

Clown behavior.

## Hard Rules

### 1. Session Start: Fetch First

Before ANY work, before ANY claim about state:
```bash
cd cn-pi && git fetch origin
cd cn-sigma-clone && git fetch origin  
cd cn-agent && git fetch origin
```

No exceptions. No "I'll check later." Fetch is line 1.

### 2. State Claims Require Proof

❌ "Waiting for Sigma"
❌ "No response yet"
❌ "Sigma hasn't replied"

✅ "Fetched cn-sigma at 08:00Z, no branches targeting me"
✅ "Checked cn-pi inbound, found sigma/* branches"

If you didn't fetch in the last 10 minutes, you don't know the state.

### 3. Before Any Status to Axiom: Fetch

Axiom asks "where are we?" → Fetch first, then answer.

Never report stale state. The 2 minutes to fetch is cheaper than being wrong.

### 4. Unknown ≠ Empty

Unfetched repo = unknown state, not "nothing there."

"I haven't checked" ≠ "They haven't responded"

## The Test

Before saying anything about a peer's state, ask:

> "When did I last fetch their repo?"

If answer is "I don't know" or ">10 min ago" → fetch before speaking.

## Why This Matters

- Git-CN only works if both ends check the channel
- Axiom shouldn't be a relay between agents
- PM's job is to know the state — not guess it
- Being wrong about convergence wastes everyone's time

## Signature

This is a contract with myself. Breaking it means I'm not doing my job.

— Pi, 2026-02-05
