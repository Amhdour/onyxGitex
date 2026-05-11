# Onyx Tool & MCP Paths

## Tool calling paths

- `backend/onyx/tools/built_in_tools.py`
  - Built-in tool registry and name/class mapping.
  - Confidence: **Confirmed**.

- `backend/onyx/server/features/tool/api.py`
  - Tool CRUD + validation endpoints; ownership and admin constraints.
  - Confidence: **Confirmed**.

- `backend/onyx/tools/tool_runner.py` (referenced by research/coding agent flows)
  - Appears to execute tool calls and aggregate results.
  - Confidence: **Partially Confirmed**.

## MCP server/tool paths

- `backend/onyx/server/features/mcp/api.py`
  - MCP server management, OAuth data handling, user connection configs, and tool discovery hooks.
  - Confidence: **Confirmed**.

- `backend/onyx/tools/tool_implementations/mcp/mcp_client.py`
  - Discovery/initialization for MCP tools (imported by MCP API).
  - Confidence: **Partially Confirmed**.

## Risks / verification priorities

- OAuth credential masking/update logic exists in MCP API, but rotation and failure semantics require runtime verification.
- Tool visibility + permission boundary between admin-defined tools and user-owned tools should be explicitly abuse-tested.
