# Data Quality Risk Assessment
Date: 2026-05-11 (UTC)
Scope: Retrieval quality and governance risk
Status: Baseline risk register (evidence-first)

## Key Risks
1. **Metadata integrity risk** (owner/ACL/classification fields missing or malformed).
2. **Content extraction risk** (parser/OCR errors causing misleading retrieval context).
3. **Duplication/conflict risk** (multiple versions of same doc with no canonical ranking).
4. **Lineage opacity risk** (insufficient trace from response back to source object).
5. **Lifecycle mismatch risk** (deleted/restricted sources still retrievable from derived stores).

## Risk Rating (Initial)
- Metadata integrity: High
- Lifecycle mismatch: High
- Content extraction: Medium
- Duplication/conflict: Medium
- Lineage opacity: High

## Control/Evidence Requirements
- Mandatory metadata schema validation before indexing.
- Data quality sampling with documented defect rates per connector.
- Automated tombstone/deletion propagation checks.
- Response-to-source traceability test evidence.

## Verification Labels
All ratings are **Partially Confirmed** pending measured defect/incident data.
