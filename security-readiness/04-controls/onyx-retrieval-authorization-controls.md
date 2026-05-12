# Retrieval Authorization Controls

Date: 2026-05-11
Status: Partially Confirmed

## Control Objective
Ensure unauthorized content is blocked before retrieval output can flow into answer context or citations.

## Runtime Control
- Control: `RetrievalAuthorizationGuard`
- Enforced at: `backend/onyx/context/search/pipeline.py::_build_index_filters`
- Enforcement timing: before `IndexFilters` are finalized and before retrieval execution.

## Decision Inputs
- Identity context: `user.id`
- Requested resources: `BaseFilters.document_set`
- Permission context: `filter_document_set_names_by_user_access(...)` output

## Fail-Closed Conditions
- Missing identity context -> deny (`INSUFFICIENT_PERMISSIONS`)
- Missing document permission context -> deny (`INSUFFICIENT_PERMISSIONS`)
- Missing per-resource policy in guard policy map -> deny (`INSUFFICIENT_PERMISSIONS`)

## Decision Logging
- Audit event: `retrieval_authorization_decision`
- Runtime trace: `retrieval.authorization`

## Evidence
- Code path updated: `backend/onyx/context/search/pipeline.py`
- Targeted tests: `backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Execution artifact set: `security-readiness/evidence-artifacts/rag-boundary-001/`

## Assurance Statement
- **Partially Confirmed**: guard is now called in a real retrieval path.
- **Unknown**: full end-to-end validation for final-answer/citation exclusion remains pending successful integration test execution in a fully provisioned environment.
