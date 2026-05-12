# Onyx Telemetry Plan - Authorization Decisions

Date: 2026-05-12

## Scope
This plan covers structured audit telemetry for retrieval authorization and tool authorization decisions.

## Runtime Integration Points
- Retrieval decision audit emission in `backend/onyx/context/search/pipeline.py`.
- Tool authorization decision audit emission in `backend/onyx/tools/tool_runner.py`.
- Shared structured schema emitter in `backend/onyx/security_readiness/control_layer.py`.

## Verification Strategy
- Unit test retrieval allow structured event emission.
- Unit test retrieval deny + missing identity fail-closed event emission.
- Unit test tool deny event emission via runtime tool authorization flow.

## Evidence Location
`security-readiness/evidence-artifacts/audit-logging-001/`
