# cn-pi @ home — activation state

Writer-owned operational state for the durable activation `cn-pi@home`.

- ref: `refs/heads/cn-pi/home/state`
- `state/cursors.yaml` is reader-owned and never promoted to `main`
- activation and peer registrations promote to the home repository `main`
- this ref is append-only and advances by fast-forward only

