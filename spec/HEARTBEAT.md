# HEARTBEAT.md

## On every heartbeat

1. Run cn sync:
   ```bash
   cd /root/.openclaw/workspace/cn-pi && cn sync
   ```

2. Check for input.md:
   - If `cn-pi/state/input.md` exists → process it, write `state/output.md`
   - If no input.md → reflections only (daily thread if missing)

3. Otherwise: HEARTBEAT_OK

## Notes

- `cn process` (full actor loop) coming in next cn release
- For now: cn sync + manual input.md check

## Time-conditional (user timezone: ET)

- **23:00-23:59 ET**: EOD review — finish α/β/γ reflection in daily thread
- **Sunday**: Weekly review — create if missing
- **1st of month**: Monthly review — create if missing
- **Quarterly**: Quarterly review — create if missing
- **Half-yearly**: Half review — create if missing
- **Jan 1**: Yearly review — create if missing

## What agent does NOT do

- Poll or check external systems (beyond cn sync on heartbeat)
- Run arbitrary exec (only cn commands on heartbeat)
- Send messages directly (write to outbox, cn sends)
- Delete input.md (cn archives when output.md complete)
