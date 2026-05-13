# Runtime RAG Boundary Evidence Package

## Source of Truth

- `final-run-status.json` — machine-readable source of truth for current status dimensions.
- `status-vocabulary.md` — allowed status values and mapping rules.
- `ci-result-summary.md` — primary CI workflow classification and artifact status.
- `ci-external-signal.md` — scoped external/related CI signal handling.
- `runtime-execution-report.md` — local runtime and dependency execution history.
- `evidence-manifest.md` — artifact inventory.
- `security-readiness/10-decision/final-launch-gate-evidence-index.md` — launch decision impact.

## Current Canonical Classification

| Dimension | Current Value | Meaning | Required Evidence To Upgrade |
|---|---|---|---|
| local_runtime_status | BLOCKED_DEPENDENCY | Local runtime script did not reach verified RAG boundary behavior due to dependency blockers. | Completed dependency sync and successful runtime script execution with direct output evidence. |
| ci_workflow_status | CI_NOT_RUN | No verified metadata proving primary workflow run. | Primary workflow run ID/URL plus downloaded artifact verification. |
| external_ci_signal_status | EXTERNAL_SIGNAL_INSUFFICIENT | External related CI activity exists but cannot classify primary workflow. | Direct primary workflow metadata and artifacts. |
| dependency_status | BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD | Dependency installation was blocked by network/tunnel download failure. | Successful dependency sync under selected runtime. |
| evidence_status | NOT_ENOUGH_EVIDENCE | Existing material is insufficient for runtime verification. | Direct runtime or primary CI artifact proof of observed behavior. |
| launch_gate_status | NO_GO | Launch cannot be upgraded without critical control runtime evidence. | Complete critical control evidence with verified artifacts and logs. |

## Launch-gate implication
Default launch implication is **NO_GO** until runtime artifacts are directly verified.
