# Runtime / Integration Test Targets (V2.2.3)

- P0-RA-001: target `backend/tests/integration/tests/chat/test_chat_document_set_access.py`; current status BLOCKED_IMPORT_DEPENDENCY; action: keep runtime command and classify blocker honestly.
- P0-AL-001: backend test command present; currently BLOCKED_IMPORT_DEPENDENCY (`fastapi_users` import path during collection).
- P0-TT-001: backend test command present; currently BLOCKED_IMPORT_DEPENDENCY (`fastapi_users`).
- P0-CL-001, P0-PI-001, P0-TA-001, P0-FC-001: retained LOCAL_HARNESS commands under `tests/security_readiness/`; runtime fixture required for upgrade.
