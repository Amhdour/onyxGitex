# bypass_acl Contract Review

Date: 2026-05-12  
Status: **Partially Confirmed**  
Launch gate impact: **NOT_ENOUGH_EVIDENCE** (unchanged)

## Scope
Review of all `bypass_acl` call sites and whether callers can set `bypass_acl=True` without trusted system context.

## Call Site Review Matrix

| Call site | Caller type | Trust assumption | User-controlled? | Risk severity | Required guard | Audit/trace requirement | Recommended code change |
|---|---|---|---|---|---|---|---|
| `backend/onyx/server/features/search/api.py` (`SearchTool(... bypass_acl=False)`) | API caller | HTTP user search must always enforce ACL | No (hard-coded false) | Medium (future regression risk) | Fail closed if bypass requested without trusted context | Emit allow/deny authorization audit for any bypass attempt | Keep explicit `False`; add contract enforcement in retrieval pipeline |
| `backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py` (`bypass_acl=False`) | Internal system path (Slack integration) | Slack path currently does not request bypass | No (hard-coded false) | Medium (if later toggled true) | Require explicit trusted system context if switched to true | Audit event must include actor/system identity + decision | If Slack ever enables bypass, pass `trusted_system_context=True` only from vetted path |
| `backend/onyx/chat/process_message.py` (`_stream_chat_turn` and wrappers with `bypass_acl` param) | Internal system path / potential API plumbing | Parameter must not be user-settable from normal chat requests | **Unknown** from this review alone | High (parameter already threaded through core chat path) | Central contract check before ACL suppression | Emit deny event on untrusted bypass attempt, fail_closed=true | Add centralized `enforce_bypass_acl_contract` in retrieval filter builder |
| `backend/onyx/context/search/pipeline.py` (`_build_index_filters`) | Internal retrieval core | ACL suppression is security-critical branch | Indirectly yes if upstream incorrectly maps request | High | Enforce `bypass_acl => trusted_system_context` | Emit structured bypass allow/deny authorization event | Added `trusted_system_context` field/arg + contract check |
| `backend/onyx/context/search/models.py` (`ChunkSearchRequest.bypass_acl`) | Internal request model | Bypass flag exists; must be paired with trusted context marker | Potentially yes if deserialized from unsafe input | High | Add explicit trusted context field default false | Audit deny when bypass requested without trust flag | Added `trusted_system_context: bool = False` and contract tests |
| `backend/tests/...` references | Tests only | Test code may set bypass for simulation | N/A | Low | Keep explicit test intent | Test should assert auditing/fail-closed behavior | Added unit tests for contract helper |

## Findings
1. No production call site currently hard-codes `bypass_acl=True` in this repository snapshot.
2. The primary risk is **future or hidden plumbing** that could propagate a user-provided bypass flag.
3. A fail-closed contract is now implemented centrally in retrieval path to block untrusted bypass usage and emit audit evidence.

## Contract (required)
- `bypass_acl=True` is only valid when `trusted_system_context=True`.
- Any `bypass_acl=True` with `trusted_system_context=False` must:
  - fail closed with `INSUFFICIENT_PERMISSIONS`, and
  - emit `retrieval.bypass_acl.deny` audit event.
- Trusted bypass path must emit `retrieval.bypass_acl.allow` audit event.

## Residual Risk
- **Unknown/Partially Confirmed:** upstream origin/authentication of `trusted_system_context` is not fully proven in this artifact.
- **Launch gate:** remain `NOT_ENOUGH_EVIDENCE` until integration-level proof shows only trusted internal callers can set the trusted context bit.
