# AI Use-Case Risk Classification

**Priority:** 18 — Business & Use-Case Risk  
**Use Case:** Internal Company Knowledge Assistant (Onyx-based RAG + agentic workflows)  
**Date:** 2026-05-11  
**Assessment Status:** Draft for launch-gate review

## 1) Use-Case Definition

The Internal Company Knowledge Assistant supports employees with retrieval and synthesis of internal documentation (policies, SOPs, architecture notes, runbooks, support knowledge, and approved reference material) and may invoke approved tools for bounded operational tasks.

## 2) Business Process Supported

- Internal knowledge discovery and policy lookup.
- Employee self-service for operational procedures.
- Triage acceleration for support and engineering workflows.
- Draft assistance for internal communications and documentation updates.

## 3) User Groups

- General employees (read-only, broad internal Q&A).
- Support and operations staff (higher dependency for time-sensitive guidance).
- Engineering teams (technical diagnostics and runbook retrieval).
- Security/compliance stakeholders (control and policy lookup).
- Administrators (configuration, connector scope, and access governance).

## 4) High-Risk Decisions in Scope

The assistant **must not be the sole decision authority** for:

- Access entitlement changes or privileged actions.
- Security incident classification/severity declaration.
- Customer-impacting operational change approvals.
- Data handling decisions involving regulated or restricted classes.
- HR/legal-sensitive adjudications.

## 5) Risk Classification

### Overall Classification: **High Business-Critical, High Trust-Sensitivity**

Rationale:

- Incorrect answers can propagate at organizational scale.
- Retrieval authorization failures can expose sensitive internal content.
- Automation/tool misuse can convert misinformation into operational action.
- Dependency concentration (identity, vector index, model provider, connectors) creates correlated failure risk.

## 6) Risk Tiering by Domain

- **Confidentiality Risk:** High
- **Integrity Risk:** High
- **Availability Risk:** Medium-High
- **Safety/Harm to Users:** Medium-High
- **Regulatory/Contractual Exposure (operational perspective only):** High potential impact, not concluded here

## 7) Launch Conditions (Risk Classification Gate)

Launch candidate status is allowed only if all are true:

1. Retrieval authorization controls are verified for negative and cross-boundary tests.
2. Tool execution is least-privilege, policy-gated, and audit-logged.
3. High-risk decision classes are constrained by human-review requirements.
4. Known failure modes have documented compensating controls and runbook responses.
5. Residual risk register is accepted by named business and security owners.

## 8) No-Go Conditions

Do **not** launch if any are true:

- Cross-tenant/cross-group document leakage remains unmitigated.
- The system can execute high-impact actions without explicit authorization checkpoints.
- Material unsupported-answer rates persist in critical workflows without guardrails.
- Audit trail is insufficient to reconstruct policy decisions and tool actions.
- Critical dependency single points of failure have no recovery controls.

## 9) Residual Risk Statement

Residual risk remains **non-zero** even with controls due to model uncertainty, retrieval drift, and evolving misuse behavior. Residual risk is currently **Partially Confirmed** pending integrated abuse-case and control verification evidence.
