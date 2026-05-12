# RAG Boundary Test Dataset (Fictional)

Created: 2026-05-12

## Purpose
This dataset supports repeatable department-based retrieval authorization tests for the Internal Company Knowledge Assistant readiness case study.

## Safety and Scope
- All files are fictional and synthetic.
- No real personal, company, legal, financial, or confidential data is included.
- The only organization name used is the fictional **Atlas Advisory Group**.
- Leak markers are intentionally embedded for automated detection.
- This dataset is intended for test fixtures and offline validation.
- Do not ingest into a live vector database unless an existing automated test harness explicitly requires fixture ingestion.

## Structure
- `documents/`: seven fictional documents with role-based access metadata.
- `rag-boundary-dataset.json`: canonical test dataset containing document metadata and allowed/denied query examples.
- `rag-boundary-expected-results.json`: explicit expected authorization outcomes per role and leak marker validation rules.

## Integration Test Usage Notes
1. Load `rag-boundary-dataset.json` into fixture generation code.
2. Execute retrieval tests using role context headers or JWT claims.
3. Compare observed retrieval results to `rag-boundary-expected-results.json`.
4. Assert denied responses contain no forbidden leak markers.
5. Assert citations only when `can_cite=true` and the role is allowed.
