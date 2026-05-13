| Project | Repo/folder | System type | Main risks | Controls | Evidence | Launch decision | Status |
|---|---|---|---|---|---|---|---|
| RAG Internal Knowledge Assistant | security-readiness | RAG assistant | Retrieval leakage, prompt injection | Authz + fail-closed | Tiered artifacts | NOT_ENOUGH_EVIDENCE | PARTIALLY_CONFIRMED |
| Autonomous Internal Operations Agent | agent-security-readiness | Agentic system | Unauthorized tools, approval bypass | Policy-as-code + approval gate | Foundation templates | NOT_ENOUGH_EVIDENCE | FOUNDATION_CREATED |
| LangGraph Autonomous Agent Runtime Lab | agent-security-readiness/23-langgraph-agent-lab | Agentic runtime lab | Tool escalation, approval bypass, missing identity, incomplete audit trail | Tool registry + policy gate + approval gate + fail-closed harness | Mock runtime artifacts + status checker evidence | NO_GO / PARTIAL_EVIDENCE | MOCK_RUNTIME_PARTIAL_EVIDENCE |
