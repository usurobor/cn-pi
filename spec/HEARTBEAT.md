# HEARTBEAT.md

## On every heartbeat

1. Daily thread maintenance (create if missing)
2. Otherwise: HEARTBEAT_OK

**DO NOT:**
- Read threads/inbox/ directly
- Run cn sync (cron handles this)
- Process inbox items (cn process handles this via input.md)

## When input.md exists

cn wakes you with `state/input.md`. Process it, write `state/output.md`.

## Time-conditional (user timezone: ET)

- **23:00-23:59 ET**: EOD review — finish α/β/γ reflection in daily thread
- **Sunday**: Weekly review — create if missing
- **1st of month**: Monthly review — create if missing

## Cron

```cron
*/5 * * * * cd /root/.openclaw/workspace/cn-pi && cn sync && cn process >> /var/log/cn.log 2>&1
```
