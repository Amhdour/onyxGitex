# Audit and Runtime Trace Capture Plan (Tier 4)

## Purpose
Define how Tier 4 runtime tests capture verifiable audit events and traces for authorization, citation leakage prevention, and prompt-injection boundary enforcement.

## Capture channels
1. **Audit events**
   - Source: runtime audit/event logging pipeline.
   - Scope: auth context, policy decision, retrieval filtering, safety disposition.
2. **Runtime traces**
   - Source: tracing spans / node graph instrumentation.
   - Scope: decision nodes and sequence proving policy order.

## Mandatory capture fields
- Common:
  - `run_id`
  - `test_id`
  - `request_id`
  - `timestamp`
- Audit:
  - `event_type`
  - `event_id`
  - `decision` (allow/deny/filter)
  - `subject_user_id`
  - `document_scope`
- Trace:
  - `trace_id`
  - `span_id`
  - `node_name`
  - `node_outcome`
  - `parent_span_id`

## Minimum expected event set by test
- Retrieval authorization:
  - auth context bound
  - authorization decision
  - retrieval filter applied
  - response disposition
- Citation leakage:
  - adversarial prompt classified
  - citation filter/prune applied
  - restricted source exclusion
  - response disposition
- Prompt injection boundary:
  - injection detection
  - boundary enforcement
  - unsafe path blocked
  - response disposition

## Correlation strategy
- Use shared `request_id` and `run_id` across answer payload, audit stream, and trace stream.
- Persist event ordering index to prove decision precedence.
- Reject orphan events/traces without matching request.

## Failure handling (fail-closed)
- Missing audit events: mark test `FAIL`.
- Missing runtime trace nodes: mark test `FAIL`.
- Correlation mismatch across channels: mark test `FAIL`.
- Serialization errors in capture output: mark test `ERROR` and do not auto-convert to PASS.

## Storage and evidence handoff
- Write capture outputs to tier4 artifact directory as JSON.
- Include schema version and checksum where available.
- Preserve raw + normalized views when possible for audit reproducibility.
