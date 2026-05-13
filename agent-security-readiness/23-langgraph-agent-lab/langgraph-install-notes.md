# Purpose
Enable optional local LangGraph runtime while preserving deterministic compatibility fallback.

Supported modes: REAL_LANGGRAPH_RUNTIME and DETERMINISTIC_GRAPH_COMPATIBILITY_MODE.

Install optional dependency:
- `uv pip install langgraph` or `pip install langgraph` in an isolated dev env.

Run real runtime path:
- `python agent-security-readiness/23-langgraph-agent-lab/run-real-langgraph-or-compat-harness.py` (auto-selects REAL_LANGGRAPH_RUNTIME when installed).

Run compatibility mode:
- same command without langgraph installed.

Evidence implications:
- Real mode = local real-LangGraph harness evidence only.
- Compatibility mode = deterministic graph-compatible evidence only.

Non-claims: no production deployment/safety/launch approval claims.
