# Tool Runtime Context Guard Evidence Summary

Date (UTC): see `timestamp.txt`.

## Scope
Dependency-light unit tests for runtime context enforcement guard in `RAG_ONLY` and `RAG_PLUS_TOOLS` launch modes.

## Test Cases (Verified)
1. RAG_ONLY with no tool calls allowed.
2. RAG_ONLY with tool calls fails closed.
3. RAG_PLUS_TOOLS missing router fails closed.
4. RAG_PLUS_TOOLS missing user_id fails closed.
5. RAG_PLUS_TOOLS missing tool_policy fails closed.
6. RAG_PLUS_TOOLS with full context allowed.
7. Deny emits audit event.
8. Deny emits runtime trace.

## Command
See `test-command.txt`.

## Result
See `test-output.txt`.

- dependency_light_status: PASS
- runtime_wiring_status: NOT_PASS
- RAG_PLUS_TOOLS: NOT_READY
- launch_gate: NOT_ENOUGH_EVIDENCE
