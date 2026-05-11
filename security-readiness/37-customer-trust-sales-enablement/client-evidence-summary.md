# Client Evidence Summary

_Last updated: 2026-05-11_

## Purpose
This summary is a client-facing index of evidence categories used to support trust discussions. It is intentionally conservative and does not replace detailed technical review.

## Evidence Classification
- **Verified**: Directly observed in code/config, test outputs, or logs.
- **Partially Confirmed**: Some evidence exists but coverage is incomplete.
- **Unknown**: No reliable confirmation currently available.

## Evidence Pack Components (Client-Shareable View)
1. **Control Catalog Snapshot**
   - Access controls, retrieval constraints, policy enforcement points.
2. **Test Execution Record**
   - Commands run, environments used, dates, and summarized outcomes.
3. **Negative-Path / Abuse-Case Results**
   - Prompt abuse attempts, authorization bypass attempts, and observed handling.
4. **Audit & Observability Artifacts**
   - Policy decision traces, key events, and logging coverage boundaries.
5. **Residual Risk Register Excerpt**
   - Open risks, owners, mitigation plans, and review cadence.
6. **Assumptions & Scope Boundaries**
   - Conditions under which evidence remains valid.

## Demo Evidence vs Real Client Evidence

### Demo Evidence (Illustrative)
- Controlled, repeatable examples used for explanation.
- Useful for understanding control intent and user experience.
- Not sufficient alone for client security acceptance.

### Real Client Evidence (Decision-Grade)
- Environment-relevant controls and test outputs.
- Time-bounded artifacts linked to current deployment posture.
- Includes limitations, unknowns, and residual risks.

## How to Use This Summary in Sales Cycles
- Use as an index during security discovery.
- Escalate to technical review for high-sensitivity workloads.
- Align claims to current evidence date and deployment scope.
- Avoid absolute statements (e.g., “fully secure,” “no hallucinations,” “zero leakage”).

## Standard Statement for Customer Calls
“We use an evidence-backed readiness model. We can share what is verified today, what is partially confirmed, and what remains unknown, along with residual risks and mitigation plans.”
