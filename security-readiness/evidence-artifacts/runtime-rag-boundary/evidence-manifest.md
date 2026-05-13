| Artifact | Status | Notes |
|---|---|---|
| ci-runtime-precheck.md | PRESENT | CI readiness precheck completed. |
| ci-rerun-instructions.md | PRESENT | Manual rerun and review process documented. |
| .github/workflows/rag-boundary-runtime-evidence.yml | CI_WORKFLOW_DEFINED | Evidence collection workflow defined for GitHub Actions. |
| dependency-sync-precheck.md | PRESENT | Precheck captured with command evidence. |
| dependency-sync-analysis.md | PRESENT | Dependency source and blocker classification documented. |
| dependency-sync-output.txt | BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD | Latest local sync failed on wheel fetch tunnel errors. |
| dependency-sync-status.txt | BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD | Classified from sync output. |
| dependency-import-check.txt | PARTIAL | Import checks remain partial due incomplete sync. |
| pytest-output.txt | PARTIAL | Runtime execution did not fully verify controls. |
| runtime-status.txt | BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD | Latest local blocker classification. |
| final-run-status.json | CI_NOT_RUN | CI metadata defined; workflow not yet executed. |
| backend-logs.txt | MISSING | Runtime test execution evidence missing. |
| docker-compose-ps.txt | NOT_AVAILABLE | Docker unavailable locally. |

| ci-run-precheck.md | PRESENT | CI run precheck recorded for this execution context. |
| ci-trigger-output.txt | CI_TRIGGER_UNAVAILABLE | gh CLI unavailable; workflow trigger could not be executed. |
| ci-run-list.txt | CI_TRIGGER_UNAVAILABLE | gh CLI unavailable; workflow run list unavailable. |
| ci-run-summary.md | CI_NOT_RUN | No CI run could be verified from this environment. |
| ci-run-log.txt | NOT_AVAILABLE | No run ID available to retrieve logs. |
| ci-run-metadata.json | NOT_AVAILABLE | No run ID available to retrieve metadata. |
| ci-artifact-download-output.txt | CI_NOT_RUN | No run ID available; artifact download not attempted. |
| ci-artifact-file-list.txt | CI_NOT_RUN | No artifact downloaded in this run. |
| ci-artifact-analysis.md | CI_NOT_RUN | No artifact available to analyze. |
| ci-downloaded-artifact/ | CI_NOT_RUN | No downloaded artifact directory populated in this run. |
| ci-result-summary.md | PRESENT | CI result summary added with evidence-limited conclusion. |
