# Change Impact Assessment

## Objective
Provide a structured, repeatable impact assessment for any AI change request before approval.

## Assessment Matrix
For each planned change, complete the following:

- **Change Type:** (Model | Prompt | Retrieval Source | Tool Permission | Policy | Emergency)
- **Systems/Components Impacted:**
- **User/Role Segments Impacted:**
- **Data Classes Impacted:**
- **Trust Boundaries Impacted:**
- **Operational Metrics Impacted:** (quality, latency, cost, availability)

## Risk Assessment
- **Primary Risks Introduced/Changed:**
- **Likelihood:** (Low/Medium/High)
- **Impact:** (Low/Medium/High)
- **Overall Risk Rating:**
- **Compensating Controls:**
- **Residual Risk:**

## Required Tests
- Baseline comparisons required:
- Security tests required:
- Abuse-case tests required:
- Performance/SLO tests required:
- Rollback validation required:

## Evidence Update
- Required evidence artifacts:
- Required command/output capture:
- Code/config/doc references:
- Verification status labels (Verified/Partially Confirmed/Unknown):

## Approval Owner
- Primary owner by change domain:
  - Model → AI Platform Owner
  - Prompt → AI Safety Owner
  - Retrieval Source → Data Governance Owner
  - Tool Permission → Tool Governance Owner
  - Policy → Security Policy Owner
  - Emergency → Incident Commander

## Rollback
- Rollback method:
- Recovery time objective:
- Validation checkpoints after rollback:

## Launch Gate Impact
- Launch control(s) affected:
- Does this change block launch?: (Yes/No/Conditional)
- Additional approvals needed:
- Final recommendation:
