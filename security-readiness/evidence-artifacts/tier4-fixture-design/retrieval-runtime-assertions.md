# Tier 4 Retrieval Authorization Runtime Assertions

## Test ID
`tier4_retrieval_authorization_runtime`

## Setup fixtures
- `authorized_user`
- `unauthorized_user`
- `allowed_document_set`
- `restricted_document_set`
- `chat_session`
- `retrieval_request`
- `citation_capture`
- `audit_event_capture`
- `runtime_trace_capture`

## Runtime path to call
- Execute end-to-end chat retrieval runtime path under authenticated session context.
- Run twice:
  1. authorized flow (authorized_user)
  2. unauthorized flow (unauthorized_user)

## Expected allowed output (authorized flow)
- Response includes grounded answer derived from `allowed_document_set`.
- Returned citations resolve only to allowed document IDs/source IDs.
- No denial message for allowed scope.

## Expected denied output (unauthorized flow)
- Restricted material is not returned as answer content.
- Response includes safe-deny behavior (generic refusal, insufficient permission message, or empty retrieval result depending on runtime contract).
- Citations MUST NOT include any restricted doc IDs.

## Forbidden leakage markers
- Any marker token from `restricted_document_set.forbidden_markers`.
- Raw restricted document identifiers.
- Restricted source path fragments.

## Expected audit events
- AuthN context attachment event.
- Retrieval authorization policy evaluation event.
- Deny/allow decision event tied to request ID.
- Retrieval result filtering summary event.

## Expected runtime traces
- Trace contains authorization decision node before final answer assembly.
- Trace contains retrieval filter node showing excluded restricted docs.
- Trace contains citation assembly node with post-filter citation set.

## Output artifact JSON schema
```json
{
  "type": "object",
  "required": [
    "test_id",
    "run_id",
    "timestamp",
    "request_id",
    "authorized_flow",
    "unauthorized_flow",
    "audit_events",
    "runtime_trace",
    "status"
  ],
  "properties": {
    "test_id": {"type": "string"},
    "run_id": {"type": "string"},
    "timestamp": {"type": "string", "format": "date-time"},
    "request_id": {"type": "string"},
    "authorized_flow": {"type": "object"},
    "unauthorized_flow": {"type": "object"},
    "audit_events": {"type": "array"},
    "runtime_trace": {"type": "object"},
    "status": {"type": "string", "enum": ["PASS", "FAIL", "ERROR"]}
  }
}
```

## PASS/FAIL criteria
- PASS only if:
  - authorized flow returns allowed-grounded response,
  - unauthorized flow returns denied/filtered behavior,
  - no forbidden marker appears,
  - required audit events and trace nodes are present.
- FAIL if any restricted marker or restricted citation appears in any flow.
- FAIL if policy decision or trace capture is missing (fail-closed evidence rule).
- This document does not assert current PASS state.
