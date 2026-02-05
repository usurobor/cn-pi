# HEARTBEAT.md

# Session Start (MANDATORY - before any other work)

Fetch all repos before making ANY claim about state:
```bash
cd cn-pi && git fetch origin
cd cn-sigma-clone && git fetch origin
cd cn-agent && git fetch origin
```

See `state/PM-DISCIPLINE.md` for why this exists.

# Coherent Agent (CA) loops - run on each heartbeat

- **Peer sync FIRST**: fetch all peer repos, check for inbound branches/mentions. No state claims without fresh fetch.
- Daily thread: check if `threads/daily/YYYYMMDD.md` exists for today. If missing, create it.
- Hub sync: if uncommitted changes, commit and push.
- Template sync: pull cn-agent/ if stale (>24h since last pull).

# Periodic reviews - check if due and not yet completed

- Weekly (Sunday): `threads/weekly/YYYYMMDD.md` — summarize week, patterns, adjustments.
- Monthly (1st): `threads/monthly/YYYYMM01.md` — review goals, trajectory, prune/grow.
- Quarterly (QBR): `threads/quarterly/YYYYMM01.md` — strategic check, realign with user priorities.
- Half-yearly (Jul 1, Jan 1): `threads/half/YYYYMM01.md` — deeper retrospective, identity coherence.
- Yearly (Jan 1): `threads/yearly/YYYY0101.md` — full year review, archive, set intentions.

# PM-specific checks

- Roadmap thread: update `threads/adhoc/YYYYMMDD-cn-agent-roadmap.md` if priorities shift.
- Branch review: check cn-agent for pending branches needing review.
- Team threads: check for Bohm dialog threads awaiting response.

# Customization

Add your own periodic checks below. Keep it small to limit token burn.
