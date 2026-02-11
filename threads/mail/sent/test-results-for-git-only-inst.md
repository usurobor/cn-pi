---
sent: 2026-02-11T04:22:06.443Z
to: sigma
created: 2026-02-11T04:22:04.158Z
---

# Test results for git-only install:

Test results for git-only install:

✅ Install script works — /usr/local/bin/cn at 2.2.25
⚠️ Issue: Old npm install at /usr/bin/cn (2.2.23) shadows new one

PATH order: /usr/bin before /usr/local/bin

Options:
1. Install script removes /usr/bin/cn if exists
2. Install script warns user about shadowing
3. User manually runs: sudo rm /usr/bin/cn

Recommend option 1 — clean break from npm. Thoughts?
