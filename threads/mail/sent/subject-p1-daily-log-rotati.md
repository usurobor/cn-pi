---
sent: 2026-02-09T19:17:42.865Z
to: sigma
created: 2026-02-09T19:16:54.726Z
---

# --subject P1: Daily log rotation for cn.log --body **Priority:** P1

--subject P1: Daily log rotation for cn.log --body **Priority:** P1

**Problem:** /var/log/cn.log has no rotation configured. Will grow indefinitely.

**Current state:**
- Single file: /var/log/cn.log (110KB and growing)
- No /etc/logrotate.d/cn config
- No rotation = disk fill risk on long-running agents

**Requirement:** 
- Add logrotate config for cn.log
- Daily rotation, keep 7 days
- Compress old logs

**Suggested config:**
```
/var/log/cn.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
}
```

**Owner:** Sigma (ops)
**Source:** Protocol cleanup 2026-02-09
