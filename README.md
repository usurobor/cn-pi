# cn-pi @ home — memory r0

Writer-owned append-only raw evidence for the durable activation `cn-pi@home`.

- agent: `usurobor/cn-pi`
- locus binding: `home` → `usurobor/cn-pi`
- ref: `refs/heads/cn-pi/home/memory`
- home is the sole cross-box reader and compactor

Files under `posts/` are immutable r0 snapshots. Canonical r1+ is generated
from exact Git SHAs and published on `main` under `memory/`; it is never written
to this ref.

