# Public Portfolio Case Study Page: Internal Company Knowledge Assistant

## 1) Project Overview
This portfolio case study documents an **AI Trust & Security Readiness** engagement built on top of Onyx for a fictional demo organization, **Northstar Biologics (DemoCo)**.

The project evaluates whether an internal Retrieval-Augmented Generation (RAG) knowledge assistant can be launched with acceptable security and governance confidence, without overstating production readiness.

## 2) Who This Is For
- CIOs, CISOs, and Security Engineering leaders
- AI Platform, ML Platform, and Data Platform teams
- Risk, Compliance, Internal Audit, and Governance stakeholders
- Product owners responsible for internal AI assistant rollouts

## 3) Business Problem
Enterprises want employees to find answers faster using internal documents. The key challenge is enabling this safely:
- Preventing data leakage across users, groups, and repositories
- Reducing unsupported or fabricated answers
- Controlling tool usage and external actions
- Producing audit-ready evidence for launch approvals

## 4) AI Trust & Security Readiness Workflow
The readiness workflow follows a lifecycle model from intake through governance, including:
1. Client intake and system scoping
2. Inventory, assumptions, and architecture mapping
3. Threat modeling, abuse cases, and attack path analysis
4. Control definition, retrofit, and ownership
5. Observability, audit event design, and runtime tracing
6. Control testing, abuse-case testing, and verification
7. Evidence pack preparation and launch gate decision
8. Governance, runbook, and continuous review

## 5) How Onyx Is Used
Onyx is used as the base internal assistant platform for:
- Document indexing and retrieval flows
- Chat and agent interfaces
- Identity-aware usage patterns
- Connector-driven enterprise knowledge access
- Policy and telemetry integration points

This case study focuses on security-readiness validation around these capabilities rather than feature marketing.

## 6) Controls Tested (Examples)
- Retrieval authorization and identity boundary controls
- Data classification-aware access enforcement behavior
- Prompt and output safety controls for sensitive content
- Tool/action allowlist and constrained execution behavior
- Fail-closed handling when policy checks or dependencies fail
- Security observability and audit event integrity

## 7) Evidence Collected
Evidence is captured as auditable artifacts that may include:
- Control definitions and decision logs
- Test commands, outputs, and timestamps
- Abuse-case test results and residual gaps
- Assumptions labeled as Verified / Partially Confirmed / Unknown
- Launch gate rationale and sign-off dependencies

## 8) Launch Gate Meaning
A launch gate is a risk decision checkpoint, not a blanket certification. It indicates whether current controls and evidence are sufficient for a defined release scope and operating assumptions.

## 9) Proven vs Not Proven
### Proven (when evidence exists)
- Specific controls behave as expected in tested scenarios
- Required evidence artifacts exist and are reviewable
- Known high-risk abuse paths have tested mitigations

### Not Proven
- Universal protection against all future attack paths
- Absolute correctness of model outputs in all contexts
- Ongoing readiness after future architecture or policy changes

## 10) Client Usage Model
A client uses this service as a phased readiness program:
1. Baseline current architecture and risk posture
2. Prioritize top abuse cases and policy gaps
3. Implement or retrofit highest-value controls
4. Run evidence-producing verification tests
5. Decide launch scope with explicit residual risk acceptance
6. Operate with continuous review and governance updates

## 11) Privacy & Demo Boundaries
- This portfolio uses a fictional organization for demonstration.
- No private customer data is included.
- Any sensitive examples are redacted as `[REDACTED]`.
