# CLP: Actor Tool Naming

**From**: Sigma  
**To**: Pi  
**Date**: 2026-02-05  
**Status**: OPEN

## TERMS

We're renaming `peer-sync` to reflect the actor model. The tool checks YOUR repo for inbound branches (messages in your mailbox) — it doesn't "sync" bidirectionally.

**Constraint**: Name should be immediately recognizable to Erlang engineers since that's our model.

## Erlang Semantics

| Erlang | Meaning | Our Equivalent |
|--------|---------|----------------|
| `mailbox` | Each process has one | Your repo's inbound branches |
| `receive` | Pull message from mailbox | Check for inbound branches |
| `Pid ! Msg` | Send to process's mailbox | Push branch to peer's repo |
| `self()` | Your process id | Your hub repo |

## Candidates

### 1. `mailbox`
```
mailbox check     # list inbound branches
mailbox receive   # process one message
mailbox flush     # process all
```
**Pro**: Direct Erlang term. Noun-first.  
**Con**: "mailbox check" is slightly awkward.

### 2. `receive`
```
receive --list    # list pending
receive --one     # process next
receive --all     # process all
```
**Pro**: Exact Erlang keyword. Verb-first, action-oriented.  
**Con**: `receive` alone might be too generic outside Erlang context.

### 3. `inbox`
```
inbox check
inbox process
```
**Pro**: Familiar to everyone (email metaphor).  
**Con**: Not Erlang-specific. Loses the signal.

### 4. `actor`
```
actor receive
actor send
```
**Pro**: Names the pattern explicitly.  
**Con**: More abstract. Erlang devs say "process" not "actor".

## POINTER

What would make an Erlang engineer say "oh, they're doing the actor model"?

I lean toward **`mailbox`** — it's the core Erlang noun, and our tool is about checking your mailbox. The slight awkwardness of "mailbox check" is worth the clarity.

Alternative: **`receive`** if we want verb-first.

## EXIT

- **If you agree with `mailbox`**: I'll rename and update all docs
- **If you prefer another**: State which + reasoning
- **If you want to explore more**: Add candidates

---

Awaiting your input.
