# Policy Failure Alerting

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Alert Definition
- **Signal**: policy engine errors, policy-evaluation timeouts, and deny-by-default fallbacks.
- **Severity**: Critical when fail-open risk exists; High for fail-closed denials with user impact.
- **Threshold**: Any fail-open indicator (0 tolerance); or >5 policy engine failures in 5 minutes.
- **Owner**: AI Security Engineering.
- **Evidence Source**: Policy decision logs, middleware audit events, distributed tracing spans around policy checks.
- **Response Action**: Enforce fail-closed mode, page incident commander, validate policy store integrity, and issue temporary launch freeze.
- **Launch Gate Impact**: Immediate hold; no launch/rollout allowed without restored deterministic policy enforcement evidence.

## Event Mapping Requirements
- Required event types: `policy_check_started`, `policy_check_completed`, `policy_check_failed`, `policy_fallback_applied`.
- Required fields: `tenant_id`, `request_id`, `policy_version`, `decision`, `fallback_mode`, `control_id`.

## Evidence Notes
- This file defines requirements only; no active alerting integration is configured here.
