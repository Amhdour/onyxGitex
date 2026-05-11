# Build Priority 21 — Prompt Change Review Workflow

Date: 2026-05-11
Status: Proposed

## Workflow
1. **Change request intake**
   - Submit PR with prompt diff, rationale, risk impact, and targeted tests.
2. **Security triage**
   - Classify impact: injection resistance, leakage risk, tool misuse risk, factuality/citation behavior.
3. **Two-person review**
   - One code owner + one security reviewer required for prompt files and orchestration prompt plumbing.
4. **Test execution**
   - Run prompt leakage and prompt injection regression suite.
5. **Evidence update**
   - Append outcomes to prompt security evidence report with command outputs and pass/fail status.
6. **Approval gate**
   - Merge only when no critical regression or explicit temporary risk exception is documented.
7. **Post-merge runtime verification**
   - Validate deployed prompt version/hash and monitoring events.

## Files in Scope for Mandatory Review
- `backend/onyx/prompts/chat_prompts.py`
- `backend/onyx/chat/prompt_utils.py`
- `backend/onyx/chat/llm_loop.py`
- `backend/onyx/chat/chat_utils.py`
- Any file adding prompt/tool-instruction text paths.
