# External CI Signal — Strict Scope Boundary

## 1. Signal observed.
Yes. External related CI activity was observed.

## 2. Source workflow.
`tier4-runtime-collection.yml`

## 3. Why it is related.
It is part of the broader runtime evidence ecosystem and can provide contextual CI activity indicators.

## 4. Why it is insufficient.
It is not `.github/workflows/rag-boundary-runtime-evidence.yml`, and it does not provide direct run metadata or artifact proof for the primary RAG boundary workflow.

## 5. Claims allowed.
- An external related CI signal was observed and recorded.
- The signal was scoped separately from primary workflow evidence.

## 6. Claims not allowed.
- Primary RAG boundary workflow ran.
- Primary RAG boundary artifacts were verified.
- RAG boundary runtime evidence passed.
- Launch gate can be upgraded.

## 7. Handling decision.
`EXTERNAL_SIGNAL_INSUFFICIENT_FOR_PRIMARY_RAG_BOUNDARY_CI_CLASSIFICATION`

## 8. Impact on final-run-status.json.
Set `external_ci_signal_status` to `EXTERNAL_SIGNAL_INSUFFICIENT`; keep `ci_workflow_status` as `CI_NOT_RUN`, `evidence_status` as `NOT_ENOUGH_EVIDENCE`, and launch gate as `NO_GO`.
