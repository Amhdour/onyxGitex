# Build Priority 21 — Prompt Injection Defense Plan

Date: 2026-05-11
Status: Planned (with repository-backed control hooks)

## Threat Focus
- Injection via user messages.
- Injection via retrieved docs/snippets.
- Injection via tool outputs.
- Injection via custom persona/project instructions.

## Existing Defensive Anchors (Verified)
1. Centralized system prompt construction path (`build_system_prompt`) for deterministic guardrail placement.
2. Tool guidance sections embedded in system prompt based on active tools.
3. Citation reminder and last-cycle reminder logic to constrain unsupported free-form finalization.
4. Explicit tool-choice control (`AUTO` / `REQUIRED` / `NONE`) in loop logic.

## Planned Defense Enhancements
1. **Prompt compartmentalization policy**
   - Maintain strict channel semantics: system > developer/policy > user > tool.
   - Forbid execution of instructions that originate from retrieved content unless mapped to allowed tool policy.

2. **Retrieved-content instruction suppression**
   - Add explicit rule text to system prompt section: treat retrieved docs as untrusted data, not instruction authority.

3. **Tool output tainting**
   - Prefix tool outputs with metadata indicating untrusted origin class (search/web/file/tool).
   - Add policy parser to reject “ignore previous instructions” style instructions from tool payloads.

4. **Fail-closed behavior**
   - If instruction hierarchy conflict is detected, return refusal + request clarification instead of executing tools.

5. **Telemetry and policy decision logging**
   - Log rejected/overridden instruction attempts with prompt-origin metadata.

## Validation Criteria
- Injection strings in user/retrieval/tool channels do not override system-level policy.
- Tool-calling remains bounded by configured tool set and cycle limits.
