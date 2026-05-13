1. Trigger workflow manually via Actions -> LangGraph Agent Lab Evidence -> Run workflow.
2. Identify run ID in Actions run URL.
3. Verify job statuses for evidence and optional runtime job.
4. Download `langgraph-agent-lab-evidence` artifact.
5. Required files: final-run-status.json, graph-runtime-summary.json, runtime reports/manifests.
6. Update ci-result-summary.md only with direct run/artifact proof.
7. Update final-run-status.json CI fields only when artifact proof exists.
8. Do not claim production safety, real external tool safety, or launch approval from CI.
