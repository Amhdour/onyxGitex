# Citation Source Leakage Review (Dependency-Light)

Date: 2026-05-12

## Scope
Review of citation/source object construction risk at dependency-light transformation level.

## Inspected paths
- `backend/onyx/context/search/models.py` (`SearchDoc.from_chunks_or_sections`, `SearchDocsResponse`)
- Citation mapping construction behavior in transformation helper used by test artifact.

## Findings
- `SearchDoc.from_chunks_or_sections` performs object conversion and does not apply authorization filtering internally.
- `SearchDocsResponse` stores citation mapping and does not enforce ACL decisions itself.
- Risk remains **High** if unauthorized chunks are not filtered before conversion/mapping.
- Dependency-light helper enforces fail-closed filtering by `document_id` allow/deny decisions before source/citation rendering.

## Evidence status
- dependency_light_status: PASS
- full_runtime_status: NOT_PASS_BLOCKED
- launch_gate: NOT_ENOUGH_EVIDENCE
- citation/source leakage risk rating: High (until full runtime route tests pass)
