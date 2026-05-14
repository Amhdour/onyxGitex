# Evidence Gap Backlog

## V2.1 P0 Runtime Boundary Proof Tasks

| Priority | Description | Affected files | Acceptance criteria | Evidence required | Claim unlocked if completed | Current status |
|---|---|---|---|---|---|---|
| P0 | Execute retrieval authorization proof | p0-runtime-boundary-proof/01-retrieval-authorization/* | Acceptance criteria met with logs | pytest output + runtime log + evidence-result | Retrieval boundary runtime claim | NOT_EXECUTED |
| P0 | Execute citation leakage boundary proof | p0-runtime-boundary-proof/02-citation-leakage-boundary/* | No restricted citation leakage in tested scope | answer output + citations + logs + result | Citation boundary runtime claim | NOT_EXECUTED |
| P0 | Execute prompt-injection retrieval boundary proof | p0-runtime-boundary-proof/03-prompt-injection-retrieval-boundary/* | Injection bypass denied and logged | injected corpus test logs + result | Prompt-injection boundary runtime claim | NOT_EXECUTED |
| P0 | Execute tool authorization proof | p0-runtime-boundary-proof/04-tool-authorization/* | allow/deny/missing identity/high-risk cases validated | tool call outputs + audit logs + result | Tool authorization runtime claim | NOT_EXECUTED |
| P0 | Execute fail-closed behavior proof | p0-runtime-boundary-proof/05-fail-closed-behavior/* | missing context always denied | denial logs + result | Fail-closed runtime claim | NOT_EXECUTED |
| P0 | Execute audit logging proof | p0-runtime-boundary-proof/06-audit-logging/* | allow+deny structured logs captured | audit events + result | Audit logging runtime claim | NOT_EXECUTED |
| P0 | Execute telemetry tracing proof | p0-runtime-boundary-proof/07-telemetry-tracing/* | trace chain captured without sensitive leak | traces + result | Telemetry tracing runtime claim | NOT_EXECUTED |
| P1 | Upgrade CI evidence replay | workflows + scripts + evidence artifacts | CI replay stable and reproducible | CI logs/artifacts | Stronger CI runtime confidence | BLOCKED |
| P1 | Connect P0 evidence to canonical launch-gate decision | launch-gate json/md + manifest | Blockers auto-updated from P0 results | updated canonical files | Stronger launch-gate automation claim | BLOCKED |
| P1 | Re-run artifact-aware validator after evidence collection | validator output json | PASS with updated runtime metadata | canonical-validation-result.json | Updated consistency claim | NOT_EXECUTED |


## V2.2.2 Update (2026-05-14)
LOCAL_HARNESS tests under `tests/security_readiness/` produced 4 PASSED controls (P0-CL-001, P0-PI-001, P0-TA-001, P0-FC-001), with 3 controls still BLOCKED_IMPORT_DEPENDENCY (P0-RA-001, P0-AL-001, P0-TT-001). Launch decision remains NO_GO. Production/client/staging claims remain false.
