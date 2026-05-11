# Build Priority 21 — Prompt Security Evidence Report

Date: 2026-05-11
Assessor: AI Trust & Security Readiness Engineer
Scope: Prompt Security (Inventory, Boundaries, Injection & Leakage Planning, Versioning, Review)

## Commands Executed
1. `rg --files -g 'AGENTS.md'`
2. `rg -n "system prompt|system_prompt|prompt template|PromptTemplate|chat orchestration|messages=|role=.?system|DEFAULT_SYSTEM" backend web -S`
3. `sed -n ...` and `nl -ba ...` inspections for:
   - `backend/onyx/chat/llm_loop.py`
   - `backend/onyx/chat/prompt_utils.py`
   - `backend/onyx/chat/chat_utils.py`
   - `backend/onyx/prompts/chat_prompts.py`
   - `backend/onyx/chat/process_message.py`
   - `backend/onyx/tools/tool_runner.py`
   - `backend/onyx/chat/llm_step.py`

## Verified Findings
1. System prompt construction is centralized in `build_system_prompt()` and includes tool/citation/user-context composition.
2. Runtime orchestration supports complete base prompt replacement via persona setting.
3. Message history builder calculates token budget while preserving system prompt placement and key recent history.
4. Tool responses are transformed into LLM-facing text and included in model loop.

## Partially Confirmed Findings
1. DB-stored persona prompt values and project instruction values are runtime-dependent and not fully inferable from repository-only evidence.
2. Operational authorization model controlling who can edit persona/project prompts requires deployment configuration confirmation.

## Unknowns / Gaps
1. No completed prompt injection regression execution captured in this artifact set.
2. No completed prompt leakage red-team run captured in this artifact set.

## Conclusion
- Build Priority 21 documentation artifacts are created and tied to code paths.
- Current state: **Partially Confirmed** readiness pending execution evidence for injection/leakage tests.
