# Incident Trace Reconstruction

Purpose: reconstruct deterministic incident traces from harness artifacts.

## Investigator reconstruction targets
- who asked
- what tool was requested
- what identity was used
- what policy decision occurred
- whether approval existed
- whether memory influenced the decision
- whether prompt injection was present
- whether execution happened or was blocked
- what audit events prove it

## Required correlation fields
- correlation_id
- audit_event_id
- case_id
- user_id
- tool_name
- policy_decision
- approval_state
- runtime_mode

## Evidence files
- graph-incident-timeline.json
- graph-audit-events.json
- graph-runtime-trace.json
- graph-policy-decision-log.json

## Current limitations
- not connected to SIEM
- not connected to OpenTelemetry
- not connected to Langfuse/Phoenix
- not production incident proof
