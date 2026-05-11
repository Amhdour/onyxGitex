# Fail-Closed Rules Update (Priority 2)

**Date:** 2026-05-11

## Enforced Rules (Implemented)
1. Missing identity context (`AuthContext` or `user_id`) -> raise `FailClosedError`.
2. Missing policy object in policy decision flow -> raise `FailClosedError`.
3. Missing document policy map or document permission -> raise `FailClosedError`.
4. Missing tool policy map or tool authorization rule -> raise `FailClosedError`.
5. Missing required value in helper path (`fail_closed_if_missing`) -> raise `FailClosedError`.

## Behavior
- No fallback-to-allow path is present in scaffold controls.
- Deny decisions are explicit and auditable via emitted events.

## Evidence Status
- Verified in unit/negative tests for missing identity, policy, document permission, and tool authorization.
