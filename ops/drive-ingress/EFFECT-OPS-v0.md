# Pi Drive effect operations v0

**Version:** 0.1.0

**Status:** experimental bridge design; implementation pending

**Owner:** `usurobor/cn-pi`

**Owns:** the temporary Drive-staged, policy-bounded effect contract executed by the cn-pi host bridge

**Does-not-own:** dialogue, memory, direct agent credentials, project authority, or a canonical CNOS runtime protocol

## Authority, status, and experiment boundary

This document specifies a small bridge experiment. Pi emits data; the host bridge admits and executes only operator-authorized operations. Request fields ask for authority. They never grant it.

On cn-pi `main` at `6baa504bc18105f644f522d7a4393ea3449c493f`, `ops/drive-ingress/` is a proposed/new executable source path. The live `/usr/local/libexec/cn-pi-drive-ingress` is installed, unversioned host state. It is byte-identical to experimental branch `origin/agent/pi-drive-ingress` at `49846607f`, but neither that branch nor effect execution is canonical on `main`.

The selected boundary is the smallest one that addresses a current failure: Pi cannot write private repositories, while granting it credentials would bypass operator policy. Dialogue-as-commands would mix communication with authority; direct credentials would widen authority; a CNOS scheduler/provider host has no present consumer. The selected adapter keeps credentials and policy on the host and emits evidence for later design.

The only authority after review is this design. Implementation, Drive provisioning, deployment, and CNOS promotion require separate operator decisions.

## Current bridge and Drive topology

The installed Python bridge polls four Drive roots and materializes dialogue/memory to writer-owned Git refs. It already has stable-ID, quarantine, immutable-publication, cursor, revision-guarded append, and retry precedents. Its experimental branch contains 38 unit-test methods. It does not execute effect requests today.

Current r0 roots remain unchanged:

```text
cn-pi/r0-boxes/pi-home
cn-pi/r0-boxes/pi-cmp
cn-pi/r0-boxes/pi-tsc
cn-pi/r0-boxes/pi-cnos
```

Dialogue, memory, activation refs, and their cursors are not effect intake. Effect state is a fourth, separate plane. Google Drive is staging and projection; the local ledger is execution authority; GitHub and bridge-local state are effect backends.

The bridge's service account can read Drive and append to a shared user-owned Google Doc, but it has no personal Drive quota for per-operation files. V0 therefore uses paired, pre-created Docs rather than one Drive object per request.

## Governing sentence and invariants

> For one authenticated Drive route, persist one framed request, admit one policy-allowed operation, reconcile it against the real backend, and publish one truthful receipt without ever inferring success or repeating an uncertain effect.

- One framed record contains one operation and one issuer-scoped logical `id`.
- The stable `id` is not a digest or a Drive, Git, GitHub, ledger, marker, or projection identity.
- Operator route configuration and policy are the only grants; request assertions can only narrow them.
- Exact Doc identity and effective permissions are checked before semantic admission.
- Durable local state precedes every external mutation.
- Every discovered candidate receives a durable disposition; uncertainty remains visible.
- Terminal replay and receipt retry never re-execute an effect.
- Backend guarantees remain backend-specific. In particular, GitHub issue updates are not atomic compare-and-swap.

## Drive outbox and receipt layout

The operator pre-creates eight user-owned Google Docs:

```text
cn-pi/effect-ops/v0/outbox/Pi — Effect Outbox — {HOME|CMP|TSC|CNOS}
cn-pi/effect-ops/v0/receipts/Pi — Effect Receipts — {HOME|CMP|TSC|CNOS}
```

Folder and title organize; they do not authenticate. For each locus, host configuration pins:

```text
outbox_doc_id + owner + allowed_principal_roles + permission_fingerprint
  -> issuer agent/locus + target repository/profile
  -> receipt_doc_id + receipt_allowed_principal_roles + receipt_permission_fingerprint
```

The outbox has the operator/Pi principal as owner-writer, the bridge service account as reader, and no other writer unless explicitly allowlisted. The receipt Doc has its configured operator owner, the bridge service account as writer, Pi as reader, and only explicitly allowlisted additional writers. Credentials remain host-only.

Admission reads file metadata and every page of `permissions.list`. It normalizes each effective permission to `{permission_id,type,principal,role,inherited,deleted,pending_owner}`, sorts the array, and hashes its compact key-sorted JSON. The resulting fingerprint and effective owner/writer roles must exactly equal configuration for both Docs. The route is rechecked immediately before execution and after restart. Any missing page/field, unexpected group/domain/anyone grant, unavailable permission metadata, changed role, or fingerprint drift creates a durable local `trust_incident` and causes zero external calls. Its Drive projection remains pending until the receipt route is trusted. If an implementation cannot verify the exact effective writer boundary, it must add another authenticated write boundary; it must not weaken this check. Unsigned framing is permitted only inside this exact ACL-bound v0 route.

Pi appends complete records. The bridge reads the Docs structured-text model and records Doc ID, revision ID, and ordinal. A request starts with the exact line `<<<CN-PI-EFFECT-REQUEST-BEGIN id=<id>>>` and ends with `<<<CN-PI-EFFECT-REQUEST-END id=<same-id>>>`. Frames require matching IDs, no nesting, and exactly one intervening JSON object.

Scanning resumes at the next valid begin marker after a malformed bounded record. An unterminated record is incomplete, never executed, and remains observable. Unexpected objects under `effect-ops/v0/` also produce incidents.

## One-operation request contract

Schema name: `cn-pi.effect-request.v0`. Unknown fields are denied. Required fields are `schema`, `id`, `issuer`, `target`, `resource`, `method`, `precondition`, and `digest`, plus exactly one of `query` or `representation` when the matrix requires it.

| Field | Contract |
|---|---|
| `id` | `1..128` characters from `[A-Za-z0-9._-]`; stable logical request and operation ID, scoped by issuer |
| `issuer` | exact `{agent,locus}` assertion matching the route |
| `target` | exact `{repository,profile}` assertion matching the route |
| `resource` | `{kind}` for a collection; item adds `number`, `issue_number`+`comment_id`, `path`, or `key` |
| `method` | one of `GET|POST|PUT|PATCH|DELETE` |
| `query` | read filters only; required for collection `GET`, optional for item `GET` |
| `representation` | mutation body; required for `POST|PUT|PATCH`, absent from reads and `DELETE` |
| `precondition` | one backend-specific shape from section 7; reads use `{"kind":"none"}` |
| `digest` | `sha256:` plus lowercase SHA-256 of the request canonical bytes with `digest` omitted |

Canonicalization is a bridge-local procedure, not a generic CNOS subsystem: parse strict UTF-8 as exactly one JSON object; reject duplicate keys, floats/exponents, non-finite numbers, unknown fields, BOMs, and integers outside signed 64-bit range; remove the top-level digest field; recursively sort object keys by Unicode code point; preserve array order; emit UTF-8 JSON with no insignificant whitespace or final newline; SHA-256 those bytes. Receipt digests use the same procedure with their top-level `digest` omitted. No Unicode normalization or adapter inference occurs.

Complete synthetic request fixture:

```text
<<<CN-PI-EFFECT-REQUEST-BEGIN id=req-cn-pi-tsc-20260807-0001>>>
{"schema":"cn-pi.effect-request.v0","id":"req-cn-pi-tsc-20260807-0001","issuer":{"agent":"usurobor/cn-pi","locus":"usurobor/tsc"},"target":{"repository":"usurobor/tsc","profile":"issues-and-docs-v0"},"resource":{"kind":"issue"},"method":"POST","representation":{"title":"Define customer-case realization proof","body":"Capture the bounded customer-case realization and its proof plan.","labels":["documentation"]},"precondition":{"kind":"marker_absent"},"digest":"sha256:b245954dcd2e1cb10d6c83319b1ef1b0eca73fe0370486b149eac057f306a467"}
<<<CN-PI-EFFECT-REQUEST-END id=req-cn-pi-tsc-20260807-0001>>>
```

The canonical bytes begin `{"id":...` because keys are sorted. Independent recomputation yields `sha256:b245954dcd2e1cb10d6c83319b1ef1b0eca73fe0370486b149eac057f306a467`.

## Resource, method, and policy matrix

This matrix is closed. The 14 listed resource-shape/method pairs are the entire vocabulary; every other pair is denied.

| # | Resource shape | Method | Input and meaning |
|---:|---|---|---|
| 1 | issue collection `{kind}` | `GET` | `query`; list issues |
| 2 | issue item `{kind,number}` | `GET` | optional `query`; retrieve issue |
| 3 | issue collection `{kind}` | `POST` | `representation`; create issue |
| 4 | issue item `{kind,number}` | `PATCH` | `representation`; update, close, or reopen |
| 5 | comment collection `{kind,issue_number}` | `GET` | `query`; list comments |
| 6 | comment item `{kind,issue_number,comment_id}` | `GET` | optional `query`; retrieve comment |
| 7 | comment collection `{kind,issue_number}` | `POST` | `representation`; create comment |
| 8 | document collection `{kind}` | `GET` | `query`; list allowed non-code documents |
| 9 | document item `{kind,path}` | `GET` | optional `query`; retrieve document |
| 10 | document item `{kind,path}` | `PUT` | `representation`; create or replace document |
| 11 | document item `{kind,path}` | `DELETE` | delete document |
| 12 | state collection `{kind}` | `GET` | `query`; list Pi activation state keys |
| 13 | state item `{kind,key}` | `GET` | optional `query`; retrieve state |
| 14 | state item `{kind,key}` | `PUT` | `representation`; create or replace state |

The route fixes the repository and profile. Policy then intersects exact resource/method pairs with repository attachment, issue fields/labels, maximum body and result sizes, document path prefixes and media types, state key prefixes, pagination, and per-route rate/budget limits. Home may target only `usurobor/cn-pi`; an attached route targets only its bound repository. State stays under the bound Pi-owned locus namespace.

Document policy is positive: a path and media type must both be listed as non-code. Extension alone never grants. Code, workflows, build/config files, symlinks, binary media, policy files, raw HTTP/Git/shell, credentials, repository settings, and unattached repositories are denied. Issue deletion and comment update/delete do not exist. Policy cannot be mutated by this protocol.

## Backend preconditions and reconciliation

| Operation | Required precondition and execution truth |
|---|---|
| any `GET` | `none`; read exact backend state, paginate within policy, and receipt the observed version/digest |
| issue `POST` / comment `POST` | `marker_absent`; derive a stable hidden marker from `agent NUL locus NUL id NUL request_digest`, query it before first attempt and every retry, create once, then exact-read the returned item |
| issue `PATCH` | `observed_issue` with `updated_at` and representation digest; immediate preflight equality, PATCH, exact post-read; the interval between preflight and mutation is non-atomic and profiles may deny updates that need stronger exclusion |
| document `PUT` existing | `document_match` with blob/content SHA, ref, and observed head SHA; preflight all evidence, send the backend-required blob SHA, and post-read the returned commit/blob/head |
| document `PUT` new | `document_absent` with ref and observed head SHA; recheck absence/head, create, and post-read exact bytes and returned commit |
| document `DELETE` | `document_match` with blob/content SHA, ref, and observed head SHA; send the required blob SHA and verify absence plus returned commit |
| state `PUT` | `state_match` with version and digest, or explicit `state_absent`; compare and write atomically in one bridge-local transaction |

GitHub's Contents API enforces the existing blob SHA for update/delete, but the observed branch head is preflight and reconciliation evidence unless the implementation selects a primitive that enforces it. A conflicting head, blob, issue representation, or state version is `denied/stale_precondition`, not silently overwritten.

For creates, the bridge injects only the correlation marker into the created body. The example marker is `cn-pi-effect:c2d69ae6de3900171057ffd05c0d50d6dc09c59f165543f680dad68cf78a326e`. Query can prove an existing matching effect; an absent result after an ambiguous timeout does not necessarily prove non-commit. If the backend cannot prove success or absence, the request remains `indeterminate` and is not automatically replayed.

Backend references: [GitHub issue operations](https://docs.github.com/en/rest/issues/issues), [issue comments](https://docs.github.com/en/rest/issues/comments), [repository contents](https://docs.github.com/en/rest/repos/contents), [Google Drive permissions](https://developers.google.com/workspace/drive/api/reference/rest/v3/permissions/list), and [Google Docs revision-guarded writes](https://developers.google.com/workspace/docs/api/reference/rest/v1/documents/batchUpdate).

## Durable ledger, replay, collision, and receipts

The local SQLite ledger is authoritative. Discovery is inserted and committed before admission; admission is committed before execution; `executing` plus an attempt token is committed before the external call. Each transition records source Doc/revision/ordinal, scoped ID, request digest, policy version, backend observations, attempt, timestamps, and receipt projection state.

| Dimension | States |
|---|---|
| delivery | `discovered` |
| admission | `pending`, `admitted`, `denied`, `parse_incident`, `trust_incident`, `policy_incident` |
| execution | `not_started`, `executing`, `succeeded`, `failed`, `indeterminate` |
| projection | `pending`, `projected` |

`succeeded`, `failed`, and `denied` are terminal only with a reason and retained evidence. `indeterminate` is nonterminal uncertainty requiring reconciliation or operator resolution. Exact scoped-ID + digest replay returns the retained state/receipt. Same scoped ID + different digest is `id_collision` and makes zero external calls. Different IDs with identical content are distinct intent.

After restart, `executing` is reconciled before any retry. Proven matching external state becomes `succeeded`; proven non-commit may retry under the original policy and budget; otherwise it becomes `indeterminate`. A terminal request never executes again.

Receipts use `cn-pi.effect-receipt.v0`. The paired Drive journal is a revision-guarded, reread-verified projection. Projection failure records `receipt_projection_pending`; retries read only the ledger and never call the effect backend.

```text
<<<CN-PI-EFFECT-RECEIPT-BEGIN id=req-cn-pi-tsc-20260807-0001>>>
{"schema":"cn-pi.effect-receipt.v0","id":"req-cn-pi-tsc-20260807-0001","request_digest":"sha256:b245954dcd2e1cb10d6c83319b1ef1b0eca73fe0370486b149eac057f306a467","status":"succeeded","reason":"created","source":{"doc_id":"1ExampleTscOutboxDoc000000000","revision_id":"rev-outbox-20260807-01","record_ordinal":7},"ledger_seq":41,"effect":{"backend":"github-rest","correlation":{"issue_number":84,"marker":"cn-pi-effect:c2d69ae6de3900171057ffd05c0d50d6dc09c59f165543f680dad68cf78a326e"},"observed_after":{"state":"open","title":"Define customer-case realization proof","updated_at":"2026-08-07T12:00:04Z","body_sha256":"sha256:c578c40a6fc04f1e7ba1ca1f6502bf56d69f734a3ee2e0c75c8a3adecf7f8e3e"}},"digest":"sha256:51d8a79526b08ac1d8dfd9e453fb6a082d4f7edf7ee130e1b0680862bbf72802"}
<<<CN-PI-EFFECT-RECEIPT-END id=req-cn-pi-tsc-20260807-0001>>>
```

Independent canonicalization with receipt `digest` omitted yields `sha256:51d8a79526b08ac1d8dfd9e453fb6a082d4f7edf7ee130e1b0680862bbf72802`.

## Failure scenarios and conformance proof

| Scenario | Durable disposition | External-call rule |
|---|---|---|
| malformed/mismatched/nested frame or invalid JSON | `parse_incident` with Doc/revision/ordinal | zero |
| duplicate key, float, unknown field, or bad digest | `parse_incident` | zero |
| wrong Doc/owner/issuer/locus/target/receipt route | `trust_incident` | zero |
| permission metadata unavailable or ACL/fingerprint drift | `trust_incident`; projection pending | zero |
| policy/resource/method/path/media/budget denial | `policy_incident` or terminal `denied` | zero |
| exact replay | retained receipt/state | zero |
| same ID, different digest | terminal `denied/id_collision` | zero |
| stale issue/blob/head/state evidence | terminal `denied/stale_precondition` | read only |
| definite backend rejection before commit | terminal `failed/backend_rejected` | one attempt |
| create returns, exact post-read matches | terminal `succeeded` | one attempt |
| timeout after possible commit, marker found | terminal `succeeded/reconciled` | reads only after timeout |
| timeout after possible commit, outcome unprovable | `indeterminate` | no automatic retry |
| post-read mismatch | `indeterminate/remote_mismatch` | no mutation retry |
| ledger unavailable before mutation | delivery error/incident | zero |
| receipt Doc append or verification fails | terminal outcome + `receipt_projection_pending` | receipt retry only |
| restart with `executing` | reconcile to success, proven absence, or indeterminate | never blind replay |

AC proof map: AC1 is the header/status and one-file diff; AC2 is paired Docs, ACL binding, framing, and incidents; AC3 is the strict fixture and recomputed digest; AC4 is the closed 14-row matrix; AC5 is the backend table and indeterminate rule; AC6 is ledger-before-effect, replay, collision, and projection isolation; AC7 is the proposed layout and evidence gate below.

Conformance must parse both fixture objects with duplicate-key rejection, recompute both digests, count exactly 14 matrix rows, exercise every failure row, verify all links/paths, scan negative space, and run `git diff --no-index --check /dev/null ops/drive-ingress/EFFECT-OPS-v0.md` while the file is untracked.

## Proposed source, deployment, state, and retirement layout

Later implementation may reconcile the experimental branch, but must not treat it as landed or canonical. Proposed repository source:

```text
ops/drive-ingress/EFFECT-OPS-v0.md
ops/drive-ingress/cn-pi-drive-ingress
ops/drive-ingress/test_drive_ingress.py
ops/drive-ingress/test_effect_ops.py
ops/drive-ingress/systemd/cn-pi-drive-ingress.service
ops/drive-ingress/systemd/cn-pi-drive-ingress.timer
```

Installed artifacts and mutable state remain derived/host-local:

```text
/usr/local/libexec/cn-pi-drive-ingress
/usr/local/sbin/cn-pi-drive-ingress-check
/etc/systemd/system/cn-pi-drive-ingress.{service,timer}
/var/lib/cn-pi-drive-ingress/effects/ledger.sqlite3
/var/lib/cn-pi-drive-ingress/effects/receipt-projections/
```

A later service update must add only the state write paths it needs and preserve current sandboxing. Cutover requires tests, backup/migration of mutable state, dry-run discovery, reconciliation of in-flight records, and rollback to the dialogue/memory-only bridge. Retire effect execution when Pi has a reviewed safer path or CNOS meets section 11; retain/migrate the ledger and receipts rather than deleting evidence.

## Evidence gate for later CNOS promotion

The bridge is an evidence generator, not a second canonical platform. CNOS may reconsider this boundary only when it has a real Go intake/execution consumer and retained bridge fixtures/receipts for exact replay, collision, policy denial, ACL drift/unavailable metadata, stale document evidence, the issue-update interval race, post-create crash, reconciliation, remote mismatch, and receipt-projection failure.

Promotion compares observed invariants with then-current CNOS architecture. It may keep the stable ID/digest split, policy non-widening, backend-honest evidence, ledger-before-effect, visible uncertainty, and receipt projection. It need not preserve Drive framing or experimental syntax.

Process economics: the paired Docs cost eight one-time operator-created files and ACL maintenance; they prevent unauthenticated source writes and give Pi receipts. The ledger adds host state but prevents duplicate effects and silent loss. Framing and the closed matrix are mechanical checks. No DAG, provider ABI, or generic URI/canonicalization layer earns present cost. Review this experiment after the first complete failure corpus; automate repeated permission/digest checks, and retire the Drive process when a stronger authenticated boundary replaces it.

## Non-goals

- No implementation, schema file, test, service, timer, Drive object, ledger, credential, ref, repository, or issue mutation in this design cycle.
- No dialogue/memory parsing as effects; no change to r0, activation, dialogue, memory, or state-ref grammar.
- No direct Pi execution or credentials; no raw shell, HTTP, Git, workflow, settings, or policy operation.
- No multi-operation plan, DAG, dependency scheduler, aggregate plan status, CTB compiler, provider host, hypermedia, cache, capability registry, canonical `cn:` URI, or generic canonicalization subsystem.
- No atomic-CAS claim for GitHub issues/comments and no silent terminalization of uncertainty.
- No canonical CNOS protocol until the evidence and runtime gates pass.
