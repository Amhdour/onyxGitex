| Artifact | Present | Scope | Status | Notes |
|---|---|---|---|---|
| final-run-status.json | YES | MACHINE_STATUS | PRESENT | Canonical machine-readable status source. |
| status-vocabulary.md | YES | VOCABULARY | PRESENT | Canonical status value and mapping rules. |
| status-normalization-precheck.md | YES | MANIFEST | PRESENT | Pre-normalization findings and decisions. |
| ci-result-summary.md | YES | CI_PRIMARY | CI_NOT_RUN | Primary workflow run/artifact not directly verified. |
| ci-external-signal.md | YES | CI_EXTERNAL | EXTERNAL_SIGNAL_INSUFFICIENT | External tier4 signal scoped as insufficient. |
| ci-run-precheck.md | YES | CI_PRIMARY | PRESENT | CI precheck record. |
| ci-run-summary.md | YES | CI_PRIMARY | CI_NOT_RUN | No verified primary run. |
| ci-trigger-output.txt | YES | CI_PRIMARY | CI_NOT_RUN | No verified trigger from this environment. |
| ci-run-list.txt | YES | CI_PRIMARY | CI_NOT_RUN | No verified run list result. |
| ci-artifact-download-output.txt | YES | CI_PRIMARY | CI_NOT_RUN | No artifact download proof. |
| ci-artifact-file-list.txt | YES | CI_PRIMARY | CI_NOT_RUN | No primary artifact verified. |
| runtime-execution-report.md | YES | LOCAL_RUNTIME | BLOCKED_DEPENDENCY | Local runtime blocked by dependencies. |
| runtime-status.txt | YES | LOCAL_RUNTIME | BLOCKED_DEPENDENCY | Latest local status remains blocked. |
| pytest-output.txt | YES | LOCAL_RUNTIME | BLOCKED_DEPENDENCY | No complete verified boundary behavior execution. |
| python-runtime-precheck.md | YES | PYTHON_RUNTIME | PRESENT | Python runtime precheck captured. |
| runtime-environment.md | YES | PYTHON_RUNTIME | PRESENT | Runtime environment context documented. |
| python-runtime-sync-output.txt | YES | PYTHON_RUNTIME | BLOCKED_PACKAGE_RESOLUTION | Python/runtime sync evidence captured with blockers. |
| dependency-precheck.md | YES | DEPENDENCY | PRESENT | Dependency precheck captured. |
| dependency-resolution.md | YES | DEPENDENCY | BLOCKED_DEPENDENCY | Dependency resolution attempt documented. |
| dependency-install-output.txt | YES | DEPENDENCY | BLOCKED_PACKAGE_RESOLUTION | Install/sync did not complete. |
| git-commit.txt | YES | LAUNCH_GATE_SUPPORT | PRESENT | Commit trace artifact present. |
| timestamp.txt | YES | LAUNCH_GATE_SUPPORT | PRESENT | Timestamp trace artifact present. |
