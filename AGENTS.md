# AI TRUST & SECURITY READINESS AGENT GUIDE

This repository is being adapted into an **Internal Company Knowledge Assistant** readiness case study
("Morgan Stanley style" AI Trust & Security Readiness).

Role context for all agents working in this repo: **AI Trust & Security Readiness Engineer for RAG and Autonomous Agents**.

## 1. Project Mission

Build a real-world readiness project on top of Onyx to prove whether an internal RAG knowledge assistant can safely launch without:

- leaking private documents,
- bypassing identity boundaries,
- producing unsupported answers,
- misusing tools, or
- lacking audit evidence.

Primary project folder: `security-readiness/`.

Expected lifecycle (use this order as the canonical workflow):

Client Intake
→ AI System Scope
→ System Inventory
→ Scope & Assumptions
→ Assessment
→ Third-Party & Supply Chain Risk Assessment
→ System Mapping
→ Data-Flow Mapping
→ Data Classification
→ Trust-Boundary Mapping
→ Runtime Lifecycle Mapping
→ Threat Modeling
→ Abuse Cases
→ Attack Paths
→ Third-Party & Supply Chain Risks
→ Controls
→ Retrieval Authorization Controls
→ Control Ownership
→ Policy Decision Logging
→ Fail-Closed Rules
→ Software Retrofit
→ Secure Starter Kit Integration
→ Observability
→ Audit Events
→ Runtime Tracing
→ Dashboard
→ Control Testing
→ Abuse-Case Testing
→ Red Teaming
→ Control Verification
→ Evidence Acceptance Criteria
→ Evidence Pack
→ Residual Risk
→ Readiness Score
→ Launch Gate Decision
→ Final Report
→ Service Handoff
→ AI Management Alignment
→ Framework Control Mapping
→ Operational Runbook
→ Governance
→ Continuous Review

## 2. Safety Rules

1. Do not invent evidence.
2. Do not fake test results.
3. Do not claim production readiness unless tests and evidence support it.
4. Every security claim must reference code, config, test output, or documented assumption.
5. Prefer fail-closed behavior.
6. Preserve existing Onyx behavior unless a task explicitly asks for implementation changes.
7. Separate documentation-only tasks from application-code changes.
8. Never commit secrets, API keys, tokens, passwords, or private environment files.
9. Use redacted examples only.
10. If a control cannot be confirmed, mark it as **Unknown** or **Partially Confirmed**.

## 3. Evidence Rules

- Every readiness statement must be backed by one or more of:
  - code reference,
  - configuration reference,
  - test command + output,
  - explicit and documented assumption.
- Maintain an evidence trail in `security-readiness/` for:
  - what was tested,
  - how it was tested,
  - the result,
  - and remaining gaps.
- Distinguish clearly between:
  - **Verified** (observed in tests/logs/code),
  - **Partially Confirmed** (incomplete coverage),
  - **Unknown** (no reliable confirmation yet).
- Never convert assumptions into facts without new evidence.

## 4. Documentation Rules

- Keep documentation scoped to the current phase; do not pre-fill future conclusions.
- Use concise, auditable language and explicit dates in findings.
- Mark redactions as `[REDACTED]`.
- For documentation-only tasks, avoid touching application code.
- When creating or updating artifacts in `security-readiness/`, keep phase boundaries clear and avoid mixing intake, testing, and final sign-off content in one file unless explicitly required.

## 5. Testing Rules

Required Codex behavior:

- Before changing code, inspect relevant files.
- Before adding tests, inspect existing test conventions.
- Use the existing project style.
- Run the narrowest relevant tests first.
- Record commands executed.
- Record test outputs.
- Report blockers clearly.
- Do not over-scope a task.
- Create small commits per phase.

Testing execution guidance:

- Start with targeted tests for changed components.
- Expand to broader suites only when needed.
- If a test is skipped or cannot run, state why and what evidence is still missing.

## 6. Security Readiness Folder Structure

Use `security-readiness/` as the canonical workspace for this program. Organize by lifecycle phase with clear evidence traceability.

Recommended baseline:

- `security-readiness/01-client-intake/`
- `security-readiness/02-system-scope/`
- `security-readiness/03-inventory-and-assumptions/`
- `security-readiness/04-threat-modeling-and-abuse-cases/`
- `security-readiness/05-controls-and-retrofit/`
- `security-readiness/06-observability-and-audit/`
- `security-readiness/07-testing-and-verification/`
- `security-readiness/08-evidence-pack-and-readiness-decision/`
- `security-readiness/09-governance-and-continuous-review/`

Each phase folder should include:

- `README.md` (scope + objectives),
- `assumptions.md` (explicit assumptions and confidence),
- `evidence.md` (commands, outputs, references),
- `risks.md` (open issues, residual risk, owners).

## 7. Coding Standards

- Follow existing Onyx coding style and local conventions.
- Keep changes minimal and scoped to the request.
- Preserve behavior unless a task explicitly requests functional changes.
- Prefer explicit security controls and fail-closed outcomes.
- Keep security-related constants, policy decisions, and audit hooks easy to trace.
- Do not add placeholder security logic that simulates enforcement without real checks.

## 8. Prohibited Actions

- Claiming readiness without evidence.
- Fabricating logs, screenshots, metrics, or test outputs.
- Committing secrets or sensitive runtime artifacts (`.env`, tokens, private keys, credentials).
- Making broad refactors unrelated to the assigned readiness phase.
- Quietly changing security assumptions without documenting rationale and impact.
- Mixing documentation assertions with unverified implementation claims.

## 9. Definition of Done

A task is done only when all applicable items are satisfied:

- Requested scope is completed and constrained.
- Evidence is attached or referenced for all security-relevant claims.
- Unknowns and partial confirmations are explicitly labeled.
- Commands and test outputs are recorded.
- No secrets are introduced.
- Changes are separated appropriately (documentation-only vs code).
- Results are suitable for downstream audit and launch-gate review.
