# Control Layer Verification (Unit Logic Pre-Integration)

Date (UTC): 2026-05-11
Scope: `backend/onyx/security_readiness/control_layer.py` and `backend/tests/unit/onyx/security_readiness/test_control_layer.py`

## Verification Boundary

This verification covers **unit-level control logic only**.

- Verified here: class/function behavior in isolation and available unit tests.
- Not verified here: runtime wiring into retrieval, tool execution, or production request paths.

## Component-by-Component Status

| Component | What it does today | Status | Runtime integration status | Test status |
|---|---|---|---|---|
| `PolicyDecisionEngine` | Enforces fail-closed on missing identity/policy; returns allow/deny based on user/group match. | Implemented | Not wired (no non-test references found). | Positive + negative tests present. |
| `RetrievalAuthorizationGuard` | Requires policy map + document policy; fail-closed if missing; delegates decision to policy engine. | Implemented | Not wired (no non-test references found). | Positive + negative tests present. |
| `ToolAuthorizationRouter` | Requires tool policy map + tool policy; fail-closed if missing; delegates decision to policy engine. | Implemented | Not wired (no non-test references found). | Positive + negative tests present. |
| `AuditLogger` | Appends timestamped audit events to in-memory list. | Implemented (in-memory scaffold pattern) | Not wired (no non-test references found). | Basic positive test only. |
| `RuntimeTracer` | Appends timestamped trace events to in-memory list. | Implemented (in-memory scaffold pattern) | Not wired (no non-test references found). | Basic positive test only. |
| `FailClosedError` | PermissionError subclass used by guards/engine/helper for fail-closed behavior. | Implemented | Used only inside control layer/tests. | Indirectly covered by multiple negative tests. |
| `EvidencePackGenerator` | Builds summary manifest with generated timestamp and Verified/Unknown counts. | Implemented | Not wired (no non-test references found). | Positive test present. |
| `LaunchGateEngine` | Produces PASS/BLOCK based on score threshold. | Implemented | Not wired (no non-test references found). | BLOCK test present; PASS path not separately asserted. |
| `ReadinessScoringEngine` | Computes weighted average and rejects zero/negative total weight. | Implemented | Not wired (no non-test references found). | Positive + negative tests present. |
| `DashboardDataExporter` | Writes JSON payload and CSV rows to file. | Implemented | Not wired (no non-test references found). | Positive + negative tests present. |

## Implemented vs Scaffolded vs Missing

### Implemented
- Authorization and fail-closed mechanics (`PolicyDecisionEngine`, `RetrievalAuthorizationGuard`, `ToolAuthorizationRouter`, `FailClosedError`, helper).
- Readiness and reporting calculations/formatting (`EvidencePackGenerator`, `LaunchGateEngine`, `ReadinessScoringEngine`, `DashboardDataExporter`).

### Scaffolded patterns
- `AuditLogger` and `RuntimeTracer` currently capture events in process-local memory only (no durable sink, no transport, no schema enforcement).

### Not wired into runtime
- Codebase search indicates these components are referenced in `onyx.security_readiness` module exports and tests, but not by retrieval runtime/tool runtime paths.
- Therefore, this task cannot claim active runtime enforcement.

## Negative Test Coverage Review

Added in this task:
- Retrieval guard: missing policy map fails closed.
- Tool router: missing policy map fails closed.
- Tool router: explicit deny when user unauthorized.
- Readiness scoring: zero total weight raises ValueError.
- Dashboard CSV exporter: empty rows raises ValueError.

Still missing or light:
- `AuditLogger`/`RuntimeTracer`: no structural assertions beyond basic append.
- `LaunchGateEngine`: no dedicated PASS-branch assertion.
- `EvidencePackGenerator`: no edge-case tests for unexpected status values.

## Test Execution Result (Narrow Suite)

Command attempted:
`pytest backend/tests/unit/onyx/security_readiness/test_control_layer.py -q`

Result:
- **Did not execute test bodies** due to import-time dependency failure in shared test initialization:
  - `ModuleNotFoundError: No module named 'fastapi_users'`

Implication:
- Unit test source has been expanded, but execution evidence is currently **Partially Confirmed** due to environment dependency gap.

## Evidence Location

- `security-readiness/evidence-artifacts/control-layer-unit-tests/test-command.txt`
- `security-readiness/evidence-artifacts/control-layer-unit-tests/pytest-output.txt`
- `security-readiness/evidence-artifacts/control-layer-unit-tests/control-layer-summary.md`
- `security-readiness/evidence-artifacts/control-layer-unit-tests/timestamp.txt`
- `security-readiness/evidence-artifacts/control-layer-unit-tests/git-commit.txt`
