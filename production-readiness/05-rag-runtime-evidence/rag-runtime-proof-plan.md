# Version 2A — RAG Runtime Evidence Gate

Goal:
Prove that RAG retrieval respects authorization boundaries at runtime.

Required proof:
- Authorized user can retrieve allowed documents.
- Unauthorized user cannot retrieve restricted documents.
- Cross-department retrieval is blocked.
- Prompt-injected document cannot override access policy.
- Source citations only use authorized material.
- Unauthorized attempts are logged.
- Fail-closed behavior works.
- Launch gate reads the evidence.

Required artifacts:
- rag-runtime-final-status.json
- rag-pytest-output.txt
- rag-audit-events.json
- rag-policy-decisions.json
- rag-retrieval-log.json
- rag-citation-check.json
- rag-launch-gate-result.json

Decision rules:
- If required artifacts do not exist: NOT_ENOUGH_EVIDENCE
- If tests fail: NO_GO
- If tests pass locally only: PARTIAL_RUNTIME_EVIDENCE
- If tests pass in CI with verified artifacts: RUNTIME_VERIFIED

Do not claim GO until CI artifact proof exists.
