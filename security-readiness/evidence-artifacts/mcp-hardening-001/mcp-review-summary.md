# MCP Review Summary

- MCP status: **Present**.
- Server entrypoint identified: `backend/onyx/mcp_server_main.py`.
- Auth path identified: `backend/onyx/mcp_server/auth.py` delegates token verification to API `/me`.
- Tool registration identified in `backend/onyx/mcp_server/tools/search.py`.
- Tool execution path includes `require_access_token()` fail-closed enforcement.
- Existing integration tests for auth and search were identified.
- Attempted MCP auth integration test execution blocked by missing local dependency (`fastapi_users`).
