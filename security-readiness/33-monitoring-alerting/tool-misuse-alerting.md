# Tool Misuse Alerting

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Alert Definition
- **Signal**: blocked tool actions tied to misuse patterns (exfiltration attempts, privilege overreach, repeated policy bypass prompts).
- **Severity**: High; Critical for confirmed exfiltration attempts.
- **Threshold**: >3 high-risk denied tool calls per actor in 10 minutes, or any critical misuse signature.
- **Owner**: Agent Platform Security + SOC.
- **Evidence Source**: Tool invocation audit trail, policy denial reason codes, agent execution traces.
- **Response Action**: Session containment, temporary actor/tool restrictions, incident ticket with evidence bundle.
- **Launch Gate Impact**: Launch pause for repeated unresolved misuse patterns in pre-launch validation window.

## Event Mapping Requirements
- Required event types: `tool_call_requested`, `tool_call_allowed`, `tool_call_denied`, `tool_misuse_detected`.
- Required fields: `tool_name`, `actor_id`, `denial_reason`, `risk_tag`, `request_id`.

## Evidence Notes
- No production alert transport is configured by this artifact.
