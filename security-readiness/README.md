# AI Trust & Security Readiness (Phase 2 Scaffold)

## Project Goal
This workspace structures the Onyx AI Trust & Security Readiness program for an internal knowledge assistant deployment. It is intended to organize evidence-driven assessment artifacts without changing application behavior.

## Folder Structure
The scaffold is organized into lifecycle-aligned phases:
- `00-service-workflow`: intake, scope, inventory, and engagement workflow artifacts.
- `01-assessment`: baseline AI system and risk assessment artifacts.
- `02-mapping`: system, data flow, classification, trust boundary, and lifecycle maps.
- `03-threat-model`: threat model, abuse cases, and attack path artifacts.
- `04-controls`: control matrices, control points, ownership, and fail-closed rules.
- `05-software`: implementation planning artifacts for control retrofits.
- `06-observability`: audit, telemetry, and runtime tracing planning artifacts.
- `07-dashboard`: readiness and risk dashboard requirement artifacts.
- `08-testing`: control, abuse-case, and red-team testing plans and results.
- `09-evidence`: evidence acceptance and verification reporting artifacts.
- `10-decision`: residual risk, remediation, launch-gate, and final decision artifacts.
- `11-governance`: ongoing governance, framework mapping, incident readiness, and runbook artifacts.

## Lifecycle
Artifacts follow the engagement sequence from service workflow and assessment through mapping, threat modeling, controls, implementation planning, observability, testing, evidence acceptance, launch decision, and continuous governance.

## How Evidence Is Handled
- All security statements must be traceable to code, configuration, test outputs, logs, or explicit assumptions.
- Each template distinguishes **Verified**, **Partially Confirmed**, and **Unknown** states.
- Completion requires linked evidence and explicit ownership.

## How Launch Decisions Are Made
Launch readiness is determined only after evidence-backed control verification, residual risk evaluation, and explicit launch-gate decision artifacts in `10-decision/`.

## What Is Not Yet Proven
This Phase 2 scaffold does **not** prove control effectiveness, production readiness, or launch approval. It only provides the artifact structure and templates required to collect and evaluate evidence.
