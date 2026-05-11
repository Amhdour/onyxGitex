# Model Change Approval Workflow

## Scope
Controls for model version/provider changes, including embedding models and rerankers.

## Workflow
1. Submit `AI Change Request` with **Change Type = Model**.
2. Perform risk assessment focused on model behavior drift, data handling changes, and licensing/compliance.
3. Define and execute required tests:
   - quality/regression benchmarks,
   - safety and refusal behavior tests,
   - latency/cost/SLO checks,
   - retrieval compatibility checks.
4. Update evidence package with test commands, outputs, and version deltas.
5. Obtain approvals (owner + security + service owner).
6. Schedule deployment with rollback readiness.
7. Re-check launch gate impact and authorize go/no-go.
8. Deploy, monitor, and document post-change verification.

## Required Control Fields
- **Change Type:** Model
- **Risk Assessment:** Mandatory
- **Required Tests:** Mandatory
- **Evidence Update:** Mandatory
- **Approval Owner:** AI Platform Owner
- **Rollback:** Required (model pin or prior provider fallback)
- **Launch Gate Impact:** Required

## Minimum Approval Criteria
- No unreviewed policy/safety regressions.
- Security tests remain **Verified** or clearly documented as **Partially Confirmed/Unknown**.
- Rollback tested in staging or previously validated with evidence.
