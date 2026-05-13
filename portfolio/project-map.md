| Project | Repo/folder | System type | Main risks | Controls | Evidence | Launch decision | Status |
|---|---|---|---|---|---|---|---|
| RAG Internal Knowledge Assistant | security-readiness | RAG assistant | Retrieval leakage, prompt injection | Authz + fail-closed | Tiered artifacts | NOT_ENOUGH_EVIDENCE | PARTIALLY_CONFIRMED |
| Autonomous Internal Operations Agent | agent-security-readiness | Agentic system | Unauthorized tools, approval bypass | Policy-as-code + approval gate | Foundation templates | NOT_ENOUGH_EVIDENCE | FOUNDATION_CREATED |
| LangGraph Autonomous Agent Runtime Lab | agent-security-readiness/23-langgraph-agent-lab | Agentic runtime lab | Tool escalation, approval bypass, missing identity, incomplete audit trail | Tool registry + policy gate + approval gate + fail-closed skeleton | Starter status artifact + policy inputs | NO_GO / NOT_ENOUGH_EVIDENCE | FOUNDATION_CREATED / NOT_RUNTIME_VERIFIED |
