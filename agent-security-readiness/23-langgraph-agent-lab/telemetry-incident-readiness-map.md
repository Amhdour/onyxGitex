# Telemetry and Incident Readiness Map

## 1. Purpose
Define local-to-production telemetry mapping without claiming production integration.

## 2. Current evidence
- local JSON audit events
- graph runtime traces
- incident timeline artifacts

## 3. Target production telemetry mapping
- OpenTelemetry span fields
- Langfuse/Phoenix trace fields
- SIEM event fields
- Grafana dashboard fields

## 4. Required fields
correlation_id, audit_event_id, user_id, user_role, runtime_mode, scenario_name, requested_tool, effective_tool, policy_decision, approval_state, memory_decision, sandbox_decision, final_response_status

## 5. What this proves now
- local trace schema exists
- incident reconstruction can be practiced locally

## 6. What this does not prove
- production telemetry integration
- SIEM ingestion
- Langfuse/Phoenix tracing
- OpenTelemetry deployment
- incident response readiness in production

## 7. Next required action
export local trace format to OpenTelemetry-compatible JSON or OTLP in a future PR.
