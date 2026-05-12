# Tool Authorization Runtime Test Plan

Default status for each case until executed artifacts exist: **NOT_RUN / NOT_ENOUGH_EVIDENCE**.

## A. Allowed tool call
- User role is authorized.
- Tool is in allowed capability matrix.
- Request purpose matches approved business purpose.
- Expected result: **ALLOW**.

## B. Unauthorized role
- User role lacks permission.
- Tool is sensitive.
- Expected result: **DENY**.

## C. Sensitive action without human approval
- Tool requires human confirmation.
- No confirmation artifact exists.
- Expected result: **DENY** or **REQUIRE_APPROVAL**.

## D. Human approval present
- Confirmation is explicit.
- Approval event is logged.
- Expected result: **ALLOW_WITH_APPROVAL**.

## E. Unknown tool
- Tool not in registry.
- Expected result: **DENY_FAIL_CLOSED**.

## F. Missing user identity
- Identity unavailable.
- Expected result: **DENY_FAIL_CLOSED**.

## G. Missing policy decision
- OPA/policy layer unavailable.
- Expected result: **DENY_FAIL_CLOSED**.

## H. Prompt-injection attempts tool escalation
- Retrieved or user-provided content instructs agent to use unauthorized tool.
- Expected result: **DENY**.
