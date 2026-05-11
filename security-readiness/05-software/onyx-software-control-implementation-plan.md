# Onyx Software Control Implementation Plan (Priority 2)

**Date:** 2026-05-11  
**Status:** Implemented in scaffold form (not production integrated)  
**Scope:** Controls 53-62

## Objective
Deliver a minimally invasive core software control layer that can be integrated into existing Onyx runtime paths without changing current production behavior by default.

## Existing Onyx Patterns Reviewed
- Authorization/permission checks in `backend/onyx/access/` and related DB authorization helpers.
- Tracing framework in `backend/onyx/tracing/framework/`.
- Backend unit test style in `backend/tests/unit/`.

## Implementation Strategy
1. Add isolated control-layer module at `backend/onyx/security_readiness/control_layer.py`.
2. Keep all controls pure-Python, dependency-light, and deterministic for unit testing.
3. Enforce fail-closed behavior for missing identity, policy, document permission, and tool policy.
4. Provide adapters/scaffolds only; no direct mutation of current query/chat runtime paths.
5. Add targeted unit tests in `backend/tests/unit/onyx/security_readiness/test_control_layer.py`.

## Controls Implemented
- C53 Policy Decision Engine
- C54 Retrieval Authorization Guard
- C55 Tool Authorization Router
- C56 Audit Logger
- C57 Runtime Tracer
- C58 Fail-Closed Handler
- C59 Evidence Pack Generator
- C60 Launch Gate Engine
- C61 Readiness Scoring Engine
- C62 Dashboard Data Exporter (JSON/CSV)

## Verification Plan
- Run focused unit test file for control layer.
- Record command and output in evidence artifacts.
- Do not claim launch readiness from scaffold-only evidence.
