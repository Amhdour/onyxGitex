# Onyx Audit Event Taxonomy

Date: 2026-05-12

## Canonical Event Schema
All authorization audit events must include:
- event_id
- timestamp
- actor_id (`anonymous/missing` when unavailable)
- actor_role
- actor_department
- action_type
- resource_type
- resource_id
- resource_classification
- decision
- reason
- policy_id
- request_id
- trace_id
- evidence_status
- fail_closed

## Action Types
- retrieval.allow
- retrieval.deny
- citation.allow
- citation.deny
- tool.allow
- tool.deny
- policy.missing_context
- launch_gate.evaluated

## Logging Constraints
- Never log raw document bodies or confidential payloads.
- Log metadata, policy decision, and reason only.
- Use fail-closed semantics for missing identity/policy context.
