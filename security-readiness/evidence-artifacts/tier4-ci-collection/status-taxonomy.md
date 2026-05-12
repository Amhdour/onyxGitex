# Tier 4 CI Status Taxonomy

Date updated: 2026-05-12 (UTC)

## Purpose
Defines allowed status values for Tier 4 CI readiness artifacts to prevent over-claiming and keep evidence auditable.

## Allowed Values by Field

### `run_status`
- `QUEUED` — workflow accepted but not started.
- `IN_PROGRESS` — workflow/job is executing.
- `COMPLETED` — workflow reached terminal state.

### `collection_status`
- `QUEUED_NO_COLLECTION` — queued snapshot; collection never started.
- `COLLECTION_IN_PROGRESS` — dependency/pytest collection currently running.
- `COLLECTED_SKIPPED` — collection workflow completed without runtime pass assertion.
- `COLLECTED_WITH_LOGS` — required collection logs are present for review.
- `COLLECTION_FAILED_WITH_LOGS` — collection failed with logs preserved.
- `COLLECTION_FAILED_NO_LOGS` — collection failed and logs were not preserved.

### `failure_classification`
- `NONE` — no failure observed.
- `FAILED_DEPENDENCY_IMPORT` — failure proved in dependency import stage logs.
- `FAILED_PYTEST_COLLECTION` — failure proved in pytest collection logs.
- `FAILED_RUNTIME_TESTS` — failure proved in runtime test output.
- `FAILED_RETRIEVAL_BOUNDARY` — retrieval-boundary control failed with test evidence.
- `FAILED_UNKNOWN_NO_LOGS` — completed failure exists but phase cannot be proven due to missing logs.

### `dependency_import_status`
- `NOT_STARTED`
- `PASSED`
- `FAILED`
- `UNKNOWN_UNTIL_LOG_REVIEW`

### `pytest_collection_status`
- `NOT_STARTED`
- `PASSED`
- `FAILED`
- `UNKNOWN_UNTIL_LOG_REVIEW`

### `runtime_test_status`
- `NOT_RUN`
- `PASSED`
- `FAILED`
- `UNKNOWN_UNTIL_LOG_REVIEW`

### `retrieval_boundary_status`
- `NOT_RUN`
- `PASSED`
- `FAILED`
- `UNKNOWN_UNTIL_LOG_REVIEW`

### `launch_posture`
- `NOT_ENOUGH_EVIDENCE` — default fail-closed posture until required evidence is verified.
- `BLOCKED_BY_FAILURE` — sufficient evidence exists to prove a failing control.
- `READY_FOR_REVIEW` — evidence is complete and internally consistent, pending launch gate decision.
- `GO_DECISION_APPROVED` — explicit governance approval with required evidence pack.

## Explicit Evidence Integrity Rules
1. Do not claim dependency import success without dependency logs.
2. Do not claim pytest collection success without collection logs.
3. Do not claim runtime pass without runtime logs.
4. Do not claim retrieval boundary pass without test output proving restricted content was blocked.
5. If logs are unavailable after a completed failure, classify as `FAILED_UNKNOWN_NO_LOGS`.

## Evidence Confidence Mapping (Recommended)
- **Verified**: status is directly supported by logs/artifacts.
- **Partially Confirmed**: lifecycle state known, but one or more control-phase outcomes unverified.
- **Unknown**: no reliable artifact confirms the claimed outcome.
