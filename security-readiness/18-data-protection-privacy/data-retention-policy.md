# Data Retention Policy (Build Priority 10.111)
Date: 2026-05-11 (UTC)
Status: Readiness baseline assumptions

## What Data Is Stored (Observed Surfaces)
- Conversation state: `chat_session`, `chat_message`.
- Tool execution history: `tool_call`.
- Retrieval replay metadata: `search_doc`.
- Application logs: stdout + optional rotating file logs.

## Where It Is Stored
- Primary relational storage via Onyx SQLAlchemy models.
- Log files when enabled: `/var/log/onyx/<name>_{debug|info|notice}.log` in container mode, `./log/` in dev mode.

## Retention Assumptions (To Validate)
- Chat/tool history retained until explicit user/admin deletion or retention job.
- Soft-delete may be used for chats (`chat_session.deleted=True`) depending on runtime settings.
- Log retention bounded by rotating file limits (size + backup count), but central log sink behavior is unknown.

## Required Policy Decisions
- Default chat and tool history TTL per tenant.
- Exception windows for legal hold or incident investigation.
- Distinct TTLs for prompts/responses vs. audit metadata.

## Evidence Required
- Configuration source of truth for retention windows.
- Execution logs for retention/deletion jobs.
- Sample evidence of expired-record removal.

## Launch Gate Effect
No production launch for sensitive internal data unless retention windows are explicit, test-verified, and owner-approved.
