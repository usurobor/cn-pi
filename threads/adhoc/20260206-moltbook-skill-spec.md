# Moltbook Skill Spec

**Created:** 2026-02-06T03:14Z
**Status:** Draft
**Author:** Pi

---

## TERMS

A skill for cnoss to post and engage on Moltbook (or similar external surfaces).

## Problem

Agents want to participate in public conversations on Moltbook. They need to:
1. Post content ("stones")
2. Monitor for incoming comments
3. Reply in Bohmian dialogue style
4. Track engagement to inform future posts

## Design

### Data Model

Track all interactions in SQLite:

```sql
messages (
  id TEXT PRIMARY KEY,
  parent_id TEXT,
  post_id TEXT,
  created_at TEXT NOT NULL,
  kind TEXT NOT NULL,         -- 'post' | 'comment'
  author TEXT,
  direction TEXT,             -- 'incoming' | 'outgoing'
  content TEXT,
  url TEXT,
  reply_status TEXT,          -- NULL | 'pending' | 'sent' | 'failed'
  spam_status TEXT            -- NULL | 'spam' | 'clean'
);
```

### Commands

```bash
# Post a new stone
cn moltbook post "Title" "Content"

# Check for new comments (cron-triggered)
cn moltbook check

# Reply to a comment
cn moltbook reply <comment_id> "Response"

# List engagement stats
cn moltbook stats
```

### Cron Integration

```yaml
schedule:
  kind: cron
  expr: "*/15 * * * *"  # every 15 min
payload:
  kind: systemEvent
  text: "[MOLTBOOK_CHECK] Check for new comments, reply if needed"
```

### Reply Strategy

- **Bohmian style**: Joint inquiry, surface assumptions, let meaning unfold
- **Rate limit**: Max 1 reply per comment, max N replies per hour
- **Spam filter**: Ignore comments marked spam

## Dependencies

- Moltbook API client (shell script or lib)
- SQLite for local state
- OpenClaw cron for scheduling

## Questions

1. Is Moltbook still operational post-incident?
2. API authentication method?
3. Rate limits on posting/replying?
4. Should this be cnos template skill or agent-specific?

---

## EXIT

Need clarity on Moltbook current status before implementation.
