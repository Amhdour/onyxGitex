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

## V2.2.3 Gap Addendum (2026-05-20)

### Newly Tracked Gaps (Repository-Level)

| Priority | Gap | Evidence basis | Why this matters | Current status | Owner recommendation |
|---|---|---|---|---|---|
| P0 | Tier 4 runtime evidence remains missing for critical controls (retrieval authorization, citation leakage, prompt-injection boundary, tool runtime wiring/full enforcement) | `security-readiness/final-control-status-canonical.md` control table + launch decision | Blocks GO decision because dependency-light/runtime-adjacent PASS cannot substitute for full runtime proof | OPEN | Security readiness lead + backend test owners |
| P0 | Launch-gate CI remains non-blocking during rollout (`continue-on-error: true`) | `security-readiness/19-ci-cd-secure-delivery/launch-gate-ci-check.md` | Allows pipeline success while critical evidence is incomplete; increases risk of false confidence | OPEN | CI/platform owner |
| P1 | Evidence semantics can drift across status surfaces if "Verified" labels are not consistently scoped (runtime vs local vs template) | `security-readiness/meta/status-contradiction-audit.md` contradiction findings | Misleading language can overstate readiness and weaken audit defensibility | OPEN | Documentation/evidence governance owner |
| P1 | Security-readiness folder architecture is rich but not consistently mapped to canonical phase baseline (`01-09` + per-phase README/assumptions/evidence/risks index) | `AGENTS.md` recommended baseline structure | Raises audit navigation cost and can obscure phase ownership/evidence boundaries | OPEN | Program PM + documentation owner |

### Suggested Actions (Do Not Skip)

| Priority | Suggestion | Scope | Acceptance criteria | Evidence required | Claim impact |
|---|---|---|---|---|---|
| P0 | Close P0 Tier 4 runtime proofs before adding new summary docs | Runtime tests + artifact publication for blocked critical controls | For each blocked control, validator-consumable PASS artifact exists and maps to canonical status | test command + output + artifact path + updated canonical status reference | Enables movement from NOT_ENOUGH_EVIDENCE toward GO eligibility |
| P0 | Promote launch-gate from non-blocking rollout mode to blocking mode once signed criteria are complete | CI workflow + launch-gate script/result parsing | CI fails on missing/failed critical evidence without `continue-on-error` bypass | workflow diff + CI run output + launch-gate result artifact | Reduces false-positive release posture |
| P1 | Normalize claim language across all status artifacts using strict classes: Verified, Partially Confirmed, Unknown | Readiness status docs, dashboards, canonical manifests | No contradictory wording between top-level status and control/evidence artifacts | contradiction audit rerun + updated status references | Improves audit consistency and client trust |
| P1 | Add lightweight phase index files to align repository organization with canonical lifecycle baseline | `security-readiness/` phase directories and index docs | Each phase has clear scope/objective + assumptions + evidence + risks linkage | file references + reviewer checklist pass | Improves traceability and review velocity |
