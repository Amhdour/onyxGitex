# Final Portfolio Demo Pack

**Project:** Onyx Internal Company Knowledge Assistant — AI Trust & Security Readiness  
**Date:** 2026-05-12 (UTC)  
**Positioning:** Security-readiness case study for an internal RAG assistant pattern inspired by a **Morgan Stanley-style** deployment model (inspiration only; no affiliation claim).

## 1) Scenario in One Page

This project demonstrates how to evaluate whether an internal company knowledge assistant can be launched safely without:
- leaking sensitive documents,
- breaking identity boundaries,
- producing unsupported claims,
- misusing tools,
- or lacking auditable evidence.

The system pattern is an internal enterprise assistant with RAG and optional tool execution modes, assessed using fail-closed launch criteria.

## 2) Fictional Organization Scope

The demo assumes a fictional regulated enterprise with:
- mixed confidential/internal/public document classes,
- role-based and group-based access boundaries,
- internal users plus administrative operators,
- audit and evidence requirements before production launch.

No real customer or employer data is used in this package.

## 3) What Was Built

The readiness work built a **security overlay and evidence workflow** around Onyx-style assistant behavior:
- policy boundaries for input, retrieval, and citation output,
- runtime and audit observability hooks,
- evidence validators and launch gate logic,
- artifact generation for review audiences (client, technical, and governance).

## 4) Launch Modes

### RAG_ONLY
- Assistant can answer using retrieval-augmented generation only.
- No external tool execution path is enabled.
- Lower attack surface than tool-enabled mode.

### RAG_PLUS_TOOLS
- RAG plus runtime tool invocation support.
- Requires additional identity propagation and tool authorization controls.
- Not launchable without complete tool-policy evidence.

## 5) Evidence Maturity Tiers

- **Tier 1 — Design Intent:** architecture, control definitions, and documented assumptions.
- **Tier 2 — Static/Config Evidence:** code/config references proving controls exist.
- **Tier 3 — Test/Execution Evidence:** targeted tests, validator outputs, generated artifacts.
- **Tier 4 — Runtime Adversarial Evidence:** runtime red-team/prompt-injection/authorization outcomes in realistic environment.
- **Tier 5 — Launch-Grade Evidence:** complete, repeatable, auditable pack with no critical unknowns.

Current state is **below Tier 5**, so launch must remain non-GO.

## 6) Controls Implemented in Scope

- `RetrievalAuthorizationGuard`
- `RetrievalGuardAdapter`
- `BypassACLContract`
- `TrustedSystemContextInputBoundary`
- `CitationSourceLeakageFilter`
- `PromptInjectionBoundary`
- `AuditLogger`
- `RuntimeTracer`
- `LaunchGateEngine`

These controls are represented in project artifacts and mapped to launch criteria; however, some runtime validations remain incomplete.

## 7) What Passed

- dependency-light test runs,
- runtime-adjacent test runs,
- validator and dashboard generation flows.

“Passed” here means available artifacts show successful execution for those categories; it does **not** imply all critical launch evidence is complete.

## 8) What Remains Blocked / Incomplete

- full backend runtime retrieval authorization proof,
- full runtime citation leakage proof,
- full runtime prompt-injection and red-team proof,
- complete evidence pack closure,
- `RAG_PLUS_TOOLS` end-to-end tool authorization wiring proof.

## 9) Launch Gate Decision

- **Current decision:** `NOT_ENOUGH_EVIDENCE`.
- **Why this is correct:** fail-closed gate policy requires complete critical evidence; unresolved critical gaps must block GO.

## 10) Professional Positioning

This portfolio demonstrates practical capability in:
- Layer Retrofit,
- Secure Starter Kits,
- Launch Gates,
- AI Security Evals & Red Teaming,
- Policy-as-Code & Runtime Guardrails,
- Retrieval Security & Data Boundary Design,
- Agent Identity, Tool Authorization & MCP Hardening,
- Telemetry, Auditability & Incident Readiness.

## How to Use This Pack

- Recruiters/partners: start with this README and `what-is-proven-vs-not-proven.md`.
- Clients: use `client-demo-script.md`.
- Interviewers: use `interview-demo-script.md`.
- Technical reviewers: use `technical-review-guide.md` and `evidence-map.md`.
