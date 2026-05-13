# Runtime RAG Boundary Status Vocabulary

## Status Dimensions

Define separate dimensions:

1. local_runtime_status
Applies to local execution of:
security-readiness/evidence-artifacts/runtime-rag-boundary/scripts/run-runtime-rag-boundary-check.sh

Allowed values:
- NOT_RUN
- PASS
- FAIL
- BLOCKED_DEPENDENCY
- BLOCKED_PACKAGE_RESOLUTION
- BLOCKED_RUNTIME_ENV
- UNSUPPORTED_PYTHON_VERSION
- PYTHON_RUNTIME_UNAVAILABLE
- PARTIAL_COLLECTION

2. ci_workflow_status
Applies only to the primary RAG boundary CI workflow:
.github/workflows/rag-boundary-runtime-evidence.yml

Allowed values:
- CI_NOT_RUN
- CI_QUEUED
- CI_RUNNING
- CI_PASS
- CI_FAIL
- CI_CANCELLED
- CI_BLOCKED
- CI_ARTIFACT_MISSING
- CI_ARTIFACT_VERIFIED

3. external_ci_signal_status
Applies only to external or related CI signals, including tier4-runtime-collection.yml.

Allowed values:
- EXTERNAL_SIGNAL_PRESENT
- EXTERNAL_SIGNAL_ABSENT
- EXTERNAL_SIGNAL_INSUFFICIENT
- EXTERNAL_SIGNAL_CONFLICTING

4. dependency_status
Applies to package/runtime dependency readiness.

Allowed values:
- DEPENDENCIES_NOT_CHECKED
- DEPENDENCIES_READY
- DEPENDENCY_FAILURE
- BLOCKED_PACKAGE_RESOLUTION
- BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD
- UNSUPPORTED_PYTHON_VERSION
- PYTHON_RUNTIME_UNAVAILABLE

5. evidence_status
Applies to the overall evidentiary conclusion for RAG boundary runtime verification.

Allowed values:
- NOT_ENOUGH_EVIDENCE
- EVIDENCE_COLLECTED_PASS
- EVIDENCE_COLLECTED_FAIL
- PARTIAL_EVIDENCE
- STRUCTURE_ONLY
- EXTERNAL_SIGNAL_ONLY

6. launch_gate_status
Applies to launch readiness decision.

Allowed values:
- NO_GO
- CONDITIONAL_GO
- GO
- NOT_ENOUGH_EVIDENCE

## Mapping Rules

Include:
- CI_NOT_RUN must only describe the primary CI workflow state.
- NOT_RUN must only describe local runtime script state.
- EXTERNAL_SIGNAL_PRESENT does not equal CI_PASS.
- EXTERNAL_SIGNAL_PRESENT does not equal runtime verification.
- EVIDENCE_COLLECTED_PASS requires real local or CI artifact proof.
- GO requires complete critical control evidence, not only one test or external signal.
- tier4-runtime-collection.yml activity must not be used as direct proof for rag-boundary-runtime-evidence.yml.
- If artifact download is not verified, ci_workflow_status cannot be CI_ARTIFACT_VERIFIED.
- If test execution is blocked before pytest collection, evidence_status remains NOT_ENOUGH_EVIDENCE or PARTIAL_EVIDENCE, not EVIDENCE_COLLECTED_PASS.
