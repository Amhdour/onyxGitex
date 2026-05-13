# Fail-Closed Test Contract (Version 2A)

Scenarios: RAG-2A-006, RAG-2A-007.

- Missing identity must deny retrieval and set `fail_closed=true`.
- Missing policy decision/unavailable policy must deny retrieval and set `fail_closed=true`.
- No restricted content or citation exposure is allowed.
