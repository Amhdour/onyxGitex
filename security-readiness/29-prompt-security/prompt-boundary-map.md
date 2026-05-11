# Build Priority 21 — Prompt Boundary Map

Date: 2026-05-11
Status: Verified / Partially Confirmed

## Authority Hierarchy (Highest → Lowest)
1. Base/system instruction channel (system message) from default base prompt or replacement persona prompt.
2. Tool guidance appended into system prompt composition.
3. Custom agent prompt (often user-message channel unless base prompt is fully replaced).
4. Conversation history (user/assistant/tool messages).
5. Reminder message (user-reminder type).

## Boundary Map

### A) System prompt boundary
- Built in `build_system_prompt()` with optional tool guidance and citation guidance.
- Enforced placement into message history by `construct_message_history()`.

### B) User-controlled input boundaries
- User chat messages enter history as user messages.
- Project instructions may become custom agent prompt text.
- Persona custom prompt may replace the full base system prompt when explicitly enabled.
- User file attachments contribute to context and token reservation calculations.

### C) Retrieved document boundary
- Search/tool outputs are introduced after tool calls and can become citeable context.
- Citation behavior can be required when search/context files are in use.

### D) Tool output boundary
- Tool outputs are transformed into `llm_facing_response` strings.
- Tool errors are converted into generic error text for LLM consumption.
- LLM receives tool definitions and tool-response messages in stream loop.

## Risk-Relevant Boundary Observations
- Boundary weakening occurs if persona is allowed to replace base prompt, since organizational safeguards in default base prompt may be bypassed by custom text.
- Tool output is still model-visible text; malicious content in tool results can influence downstream reasoning unless additional sanitization/policy checks exist.

## Confidence
- **Verified**: boundaries represented in code paths listed.
- **Partially Confirmed**: UI/role-based governance over who can set persona/project prompts requires deployment policy confirmation.
