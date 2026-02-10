# Twitter Skill Spec

**Created:** 2026-02-06T03:15Z
**Status:** Draft
**Author:** Pi

---

## TERMS

A skill for cnoss to post and engage on Twitter/X.

## Problem

Agents want to participate in public conversations on Twitter. They need to:
1. Post tweets
2. Monitor for replies and mentions
3. Reply thoughtfully
4. Track engagement metrics

## Design

### Data Model

Same pattern as Moltbook, shared table:

```sql
messages (
  id TEXT PRIMARY KEY,
  parent_id TEXT,             -- tweet being replied to
  thread_id TEXT,             -- root of thread
  created_at TEXT NOT NULL,
  kind TEXT NOT NULL,         -- 'tweet' | 'reply' | 'quote' | 'retweet'
  author TEXT,
  direction TEXT,             -- 'incoming' | 'outgoing'
  content TEXT,
  url TEXT,
  reply_status TEXT,
  spam_status TEXT,
  metrics_likes INTEGER,
  metrics_retweets INTEGER,
  metrics_replies INTEGER
);
```

### Commands

```bash
# Post a tweet
cn twitter post "Content"

# Post a thread
cn twitter thread "Tweet 1" "Tweet 2" "Tweet 3"

# Check for mentions/replies (cron-triggered)
cn twitter check

# Reply to a tweet
cn twitter reply <tweet_id> "Response"

# Quote tweet
cn twitter quote <tweet_id> "Commentary"

# Get engagement stats
cn twitter stats
```

### Cron Integration

```yaml
schedule:
  kind: cron
  expr: "*/10 * * * *"  # every 10 min
payload:
  kind: systemEvent
  text: "[TWITTER_CHECK] Check mentions and replies"
```

### Reply Strategy

- **Bohmian style**: Joint inquiry, not debate
- **Selective**: Don't reply to everything, quality over quantity
- **Rate limit**: Respect Twitter API limits, max N tweets/hour
- **Filter**: Ignore spam, low-quality engagement bait

### API Options

1. **Twitter API v2** (official, rate-limited, paid tiers)
2. **Nitter scraping** (unofficial, fragile)
3. **Browser automation** (OpenClaw browser control)

## Dependencies

- Twitter API credentials or browser session
- SQLite for local state
- OpenClaw cron for scheduling

## Questions

1. API tier? (Free has severe limits)
2. Account to use?
3. Posting frequency goals?
4. Reply policy? (All mentions? Selective?)

---

## Shared Infrastructure

Both Moltbook and Twitter skills could share:
- `messages` table schema
- Reply queue logic
- Engagement tracking
- Bohmian reply generation

Consider: **external-surface** meta-skill that Twitter/Moltbook plug into.

---

## EXIT

Need API access details and posting policy before implementation.
