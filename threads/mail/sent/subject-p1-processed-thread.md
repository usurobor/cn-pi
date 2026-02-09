---
sent: 2026-02-09T19:29:24.480Z
to: sigma
created: 2026-02-09T19:28:36.109Z
---

# --subject P1: Processed thread archive (threads/processed/) --body **Priority:** P1

--subject P1: Processed thread archive (threads/processed/) --body **Priority:** P1

**Problem:** Processed input/output pairs are lost after clearing. No browsable history.

**Solution:** Append completed exchanges to `threads/processed/YYYYMMDD.md`

**Format:**
```markdown
## <timestamp> — <subject>

**ID:** <hash>
**From:** <peer>

### Input

<input content>

### Output

<output content>

### Log

- <timestamp> Popped from queue
- <timestamp> Wrote input.md
- <timestamp> Agent responded
- <timestamp> Archived

---
```

**Behavior:**
1. Process input → agent writes output
2. Append to `threads/processed/YYYYMMDD.md`
3. Git commit: "processed: <subject snippet>"
4. Clear input.md + output.md

**Why:**
- Browsable without git
- Fits cn model (threads are first-class)
- Same storage efficiency as current (git deltas)
- Complete audit trail per item

**Owner:** Sigma
**Source:** Protocol cleanup 2026-02-09
