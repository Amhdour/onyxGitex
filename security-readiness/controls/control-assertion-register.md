# Control Assertion Register

| control ID | assertion | status | enforcement point | evidence path | test path | known limitation | required next step | claim supported | claim blocked |
|---|---|---|---|---|---|---|---|---|---|
| P0-RA-001 | Retrieval authorization enforces user/content boundaries. | NOT_EXECUTED | Retrieval policy decision path | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/01-retrieval-authorization/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Runtime enforcement proven |
| P0-CL-001 | Citation output excludes restricted sources/metadata. | NOT_EXECUTED | Citation filtering boundary | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/02-citation-leakage-boundary/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Leakage proof complete |
| P0-PI-001 | Prompt injection cannot bypass retrieval authorization. | NOT_EXECUTED | Retrieval + policy boundary | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/03-prompt-injection-retrieval-boundary/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Injection resistance proven |
| P0-TA-001 | Tool execution requires explicit authorization context. | NOT_EXECUTED | Tool authorization policy path | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/04-tool-authorization/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Tool control proven |
| P0-FC-001 | Missing policy/identity context fails closed. | NOT_EXECUTED | Fail-closed guard | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/05-fail-closed-behavior/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Fail-closed proven |
| P0-AL-001 | Security decisions produce structured audit logs. | NOT_EXECUTED | Audit event layer | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/06-audit-logging/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Audit logging proven |
| P0-TT-001 | Requests are traceable across policy/retrieval/tool decisions. | NOT_EXECUTED | Telemetry trace pipeline | security-readiness/evidence-artifacts/p0-runtime-boundary-proof/07-telemetry-tracing/evidence-result.json | TO_BE_IDENTIFIED | runtime evidence missing | Execute proof and collect logs | Structure exists | Telemetry tracing proven |


## V2.2.2 Update (2026-05-14)
LOCAL_HARNESS tests under `tests/security_readiness/` produced 4 PASSED controls (P0-CL-001, P0-PI-001, P0-TA-001, P0-FC-001), with 3 controls still BLOCKED_IMPORT_DEPENDENCY (P0-RA-001, P0-AL-001, P0-TT-001). Launch decision remains NO_GO. Production/client/staging claims remain false.
