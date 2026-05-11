# Build Priority 21 — System Prompt Inventory

Date: 2026-05-11
Status: Verified / Partially Confirmed

## Objective
Inventory repository-visible system prompt sources and the runtime code paths that compose them.

## Inventory

### 1) Default base system prompt template (code constant)
- Location: `backend/onyx/prompts/chat_prompts.py`
- Symbol: `DEFAULT_SYSTEM_PROMPT`
- Notes:
  - Contains core assistant behavior and formatting instructions.
  - Uses replacement tokens for current datetime and citation guidance.

### 2) Runtime resolver for default prompt
- Location: `backend/onyx/chat/prompt_utils.py`
- Function: `get_default_base_system_prompt(db_session)`
- Behavior:
  - Reads default behavior persona prompt from DB when set.
  - Falls back to `DEFAULT_SYSTEM_PROMPT` constant if DB value absent.

### 3) Runtime system prompt composer
- Location: `backend/onyx/chat/prompt_utils.py`
- Function: `build_system_prompt(...)`
- Behavior:
  - Applies date awareness replacement.
  - Applies citation guidance placeholder replacement and fallback append behavior.
  - Adds company/user-memory sections.
  - Adds tool-specific guidance blocks based on enabled tools.

### 4) Persona/project custom prompt inputs
- Location: `backend/onyx/chat/chat_utils.py`
- Function: `get_custom_agent_prompt(persona, chat_session)`
- Behavior:
  - Priority for custom agent text: custom persona prompt (non-default persona) then project instructions (default persona + project context).

### 5) Final system prompt selection in chat orchestration
- Location: `backend/onyx/chat/llm_loop.py`
- Behavior:
  - If `persona.replace_base_system_prompt` is true, persona prompt replaces base system prompt entirely.
  - Otherwise, composed default system prompt is used and custom agent prompt is inserted as a separate message.

## Hidden Prompt Exposure Statement
- This inventory only references prompts present in repository code and documented DB-driven fields.
- No hidden or external prompt text is asserted.

## Confidence
- **Verified**: code constants and orchestration functions listed above.
- **Partially Confirmed**: exact DB prompt values at runtime (depends on deployment data, not repository-only evidence).
