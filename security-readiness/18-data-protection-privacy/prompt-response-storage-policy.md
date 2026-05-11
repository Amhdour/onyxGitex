# Prompt / Response Storage Policy (Build Priority 10.113)
Date: 2026-05-11 (UTC)
Status: Readiness policy draft

## Stored Prompt/Response Surfaces
- `chat_message.message` stores user and assistant message text.
- `chat_message.reasoning_tokens` may store model reasoning content when present.
- `tool_call.tool_call_arguments` and `tool_call.tool_call_response` store tool interaction content.

## Risks
- PII entry by users into prompts.
- Sensitive data leakage into tool responses and model outputs.
- Reasoning/token fields may contain extra sensitive context not meant for long-term storage.

## Policy Rules
1. Minimum-necessary storage: disable optional high-risk fields unless needed.
2. Sensitive-field scanning at write time.
3. Redaction-at-rest for detected high-risk tokens/identifiers.
4. Separate retention class for prompt/response payloads from operational metadata.
5. Explicit tenant-level opt-in for long-term history.

## Evidence Required
- Config and code references showing storage behavior controls.
- Tests using fictional sensitive examples demonstrating block/redact.
- Verification that exports/share features respect redaction.

## Launch Gate Effect
Without verified guardrails for prompt/response persistence, production readiness is **Blocked** for regulated or confidential workloads.
