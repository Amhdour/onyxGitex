# Onyx Runtime Trace Plan (runtime-tracing-001)

Date: 2026-05-12

## Scope
Wire `RuntimeTracer` into a verified narrow end-to-end path for:
1. RAG request authorization flow.
2. Tool authorization flow.

Status: **Partially Confirmed** for full production E2E path, **Verified** for tested runtime authorization path instrumentation.

## Required Trace Schema
Structured JSONL event fields:
- `trace_id`
- `span_id`
- `parent_span_id`
- `timestamp`
- `request_id`
- `actor_id` (or null/missing)
- `step_name`
- `component`
- `decision`
- `duration_ms` (nullable)
- `evidence_ref`
- `error`
- `fail_closed`

## RAG Trace Steps
1. `request.received`
2. `identity.resolved`
3. `policy.context.built`
4. `retrieval.requested`
5. `retrieval.authorization.checked`
6. `retrieval.allowed_or_denied`
7. `citation.checked`
8. `response.generated_or_blocked`
9. `audit.event.emitted`

## Tool Trace Steps
1. `tool.requested`
2. `tool.policy.checked`
3. `tool.allowed_or_denied`
4. `tool.execution.blocked_or_completed`
5. `audit.event.emitted`

## Evidence Strategy
- Use targeted unit test to emit structured trace events through `RuntimeTracer.emit_structured`.
- Validate retrieval authorization decision (`allow`) and tool authorization decision (`deny`, fail-closed).
- Export JSONL artifact under `security-readiness/evidence-artifacts/runtime-tracing-001/runtime-trace.jsonl`.
- Record test command and raw output.

## Limitations
- Full API-to-LLM-to-streaming E2E tracing across all production components is **not fully wired** in this change.
- This increment verifies the narrowest feasible runtime path with explicit policy decision and audit-step traces for launch-gate evidence.
