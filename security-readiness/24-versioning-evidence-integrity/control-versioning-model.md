# Control Versioning Model

## Objective
Ensure each security control definition remains traceable as control logic, implementation ownership, and validation evidence evolve.

Date: 2026-05-11
Status: Draft for review

## Control Identity
Stable control key format:

`CTRL-<domain>-<number>`

Example: `CTRL-RAG-AUTHZ-012`

## Version Format
`<major>.<minor>.<patch>` tracked per control key.

## Version Increment Rules
- **Major**: Control objective or enforcement boundary changes.
- **Minor**: Implementation, ownership, or coverage enhancement.
- **Patch**: Clarifications and typo/reference corrections.

## Mandatory Fields Per Version
- Control key and version
- Objective statement
- Enforcement point(s)
- Failure mode (must state fail-open/fail-closed; prefer fail-closed)
- Owner and backup owner
- Linked policy version(s)
- Linked evidence versions
- Validation test references
- Status (`Verified`, `Partially Confirmed`, `Unknown`)

## Deprecation Rules
Deprecated control versions must include:
- Deprecation date
- Reason
- Replacement control/version mapping
- Residual risk note

## Audit Requirements
All control version changes must be reviewable via Git history and tied to evidence/test artifacts that justify the update.
