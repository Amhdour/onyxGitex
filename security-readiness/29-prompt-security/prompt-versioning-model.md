# Build Priority 21 — Prompt Versioning Model

Date: 2026-05-11
Status: Proposed

## Versioning Requirements
1. Every system prompt template change must have:
   - semantic version,
   - change author,
   - timestamp (UTC),
   - rationale,
   - risk classification,
   - rollback reference.
2. Runtime-resolved DB prompt overrides must include immutable audit history.
3. Prompt policy text and tool guidance changes require security review tag.

## Suggested Model
- `prompt_id`: stable identifier (e.g., `default_system_prompt`).
- `version`: `MAJOR.MINOR.PATCH`.
- `source`: `repo_constant` or `db_override`.
- `content_hash`: SHA-256 of normalized prompt content.
- `effective_from` / `effective_to`.
- `approved_by` and `review_ticket`.

## Release Rules
- MAJOR: authority hierarchy or safety policy semantic changes.
- MINOR: additive guidance, no policy downgrade.
- PATCH: typo/formatting/non-semantic edits.

## Verification Hooks
- CI check to diff prompt constants and require security-review label for prompt files.
- Runtime startup check to emit current active prompt version/hash.
