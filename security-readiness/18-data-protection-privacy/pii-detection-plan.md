# PII Detection Plan (Build Priority 10.109)
Date: 2026-05-11 (UTC)
Status: Readiness planning artifact (not a compliance attestation)

## Objective
Define a fail-closed readiness plan for identifying Personal Data and Sensitive Data in Onyx knowledge-assistant flows before launch.

## In-Scope Data Surfaces
- Chat content and metadata in `chat_message` (`message`, `reasoning_tokens`, `files`, `error`).
- Session-level metadata in `chat_session` (`description`, sharing status, IDs).
- Tool-call payloads in `tool_call` (`tool_call_arguments`, `tool_call_response`, `reasoning_tokens`).
- Retrieval replay objects in `search_doc` (`semantic_id`, `blurb`, `link`).

## PII/Sensitive Data Classes for Detection
Use fictional examples only, e.g., `Alex Rivera, 555-0102, acct# FIC-12345`.

- Direct identifiers: personal name + contact, government ID equivalents, internal employee IDs.
- Financial-like fields: account numbers, transaction references.
- Health-like references: diagnoses, treatment notes.
- Secrets: tokens, API keys, passwords, private keys.
- High-risk context combinations: user name + project + document URL.

## Detection Approach
1. **Ingress checks** (before persistence where possible):
   - Pattern-based detectors for common identifiers/secrets.
   - Context-based risk scoring for mixed fields.
2. **At-rest sweep jobs**:
   - Scheduled scans across `chat_message`, `tool_call`, and trace-linked payload stores.
3. **Egress controls**:
   - Response redaction or block when high-confidence sensitive matches are found.
4. **Fail-closed policy**:
   - If detector health is unavailable, block storage of new prompt/response content pending override.

## Evidence Required Before Launch Gate
- Detector configuration inventory and versioned rule set.
- Test evidence with fictional payload corpus and expected outcomes.
- False-positive/false-negative tuning report.
- Runtime alert evidence that blocked events are auditable.

## Current Verification Status
- **Partially Confirmed**: Candidate storage surfaces identified from models.
- **Unknown**: Runtime detector coverage and suppression workflows.

## Launch Gate Effect
- If ingress + at-rest PII detection is not verifiably active for chat/tool payloads, set launch gate to **No-Go** for production handling of internal personal data.
