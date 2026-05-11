# AI Change Request Template

## Purpose
Use this template for all AI system changes (model, prompt, retrieval source, tool permission, policy, and emergency changes) to ensure auditable, fail-closed change control.

## Change Metadata
- **Change ID:**
- **Requested Date (UTC):**
- **Requested By:**
- **Change Type:** (Model | Prompt | Retrieval Source | Tool Permission | Policy | Emergency)
- **Environment(s):** (Dev | Staging | Production)
- **Priority:** (Low | Medium | High | Critical)

## Change Description
- **Current State:**
- **Proposed State:**
- **Business/Security Rationale:**
- **Systems Affected:**
- **Dependencies:**

## Risk Assessment
- **Confidentiality Impact:** (Low/Medium/High + rationale)
- **Integrity Impact:** (Low/Medium/High + rationale)
- **Availability Impact:** (Low/Medium/High + rationale)
- **Abuse Case Exposure:**
- **Third-Party/Supply-Chain Impact:**
- **Risk Rating (Overall):** (Low | Medium | High | Critical)
- **Risk Decision:** (Accept | Mitigate | Reject)

## Required Tests
List required tests before approval and release.
- Unit/component tests:
- Integration tests:
- Security control tests:
- Abuse-case tests:
- Regression tests:
- Dry-run / staging validation:

## Evidence Update
Attach or link objective evidence.
- Test commands run:
- Test outputs/logs:
- Config/code references:
- Assumptions and confidence labels (Verified / Partially Confirmed / Unknown):
- Evidence location in `security-readiness/`:

## Approval Owner
- **Primary Approval Owner:**
- **Security Reviewer:**
- **Service Owner:**
- **Final Approval Timestamp (UTC):**

## Rollback Plan
- **Rollback Trigger(s):**
- **Rollback Procedure:**
- **Data/Index rollback needs:**
- **Validation after rollback:**
- **Rollback Owner:**

## Launch Gate Impact
- **Launch Gate Status Impact:** (No Impact | Conditional | Blocker)
- **Controls impacted:**
- **Residual risk after change:**
- **Go/No-Go recommendation:**

## Implementation and Post-Change Validation
- **Implementation Window (UTC):**
- **Change Executor:**
- **Post-change checks and outcomes:**
- **Audit event references:**
- **Follow-up actions and due dates:**
