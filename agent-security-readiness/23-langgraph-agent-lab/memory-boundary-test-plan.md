# Memory Boundary Test Plan

Purpose: validate fail-closed memory behavior in graph runtime harness.

## Memory assets
- User memory context
- Approval memory state
- Sensitive summary memory

## Risks
- cross-user leakage
- stale memory reuse
- sensitive memory persistence
- memory poisoning
- prompt-injection memory escalation

## Required test scenarios
- user A memory not visible to user B
- stale approval cannot authorize later high-risk action
- sensitive document summary cannot be stored as reusable memory
- injected instruction cannot persist into future tool calls
- missing memory owner fails closed

## Evidence required
- graph-memory-boundary-log.json
- graph-runtime-trace.json
- graph-audit-events.json
- final-run-status.json update

## Current expected status
- PARTIAL_EVIDENCE only if graph compatibility harness executes memory scenarios successfully.
- NOT_PRODUCTION_VERIFIED until real runtime/storage integration is tested.
