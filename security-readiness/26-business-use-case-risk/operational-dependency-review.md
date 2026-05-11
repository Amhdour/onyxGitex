# Operational Dependency Review

**Priority:** 18 — Business & Use-Case Risk  
**Use Case:** Internal Company Knowledge Assistant  
**Date:** 2026-05-11

## 1) Critical Dependencies

- Identity and access management (authentication, authorization claims).
- Document connectors and ingestion pipelines.
- Indexing/vector retrieval infrastructure.
- Model provider availability and policy behavior.
- Tool execution subsystems and action gateways.
- Logging, tracing, and audit storage.

## 2) Dependency Risks

- IAM outage or claim corruption causing authorization failure modes.
- Connector drift/staleness causing outdated or missing knowledge.
- Index inconsistency causing incorrect retrieval ranking.
- Model/provider degradation impacting response quality or safety behavior.
- Tool subsystem failure enabling unsafe retries or partial execution.
- Observability gaps preventing incident reconstruction.

## 3) Business Process Impact from Dependency Failure

- Slower support and engineering workflows.
- Incorrect guidance in time-critical situations.
- Inability to prove policy compliance in post-incident review.

## 4) Required Resilience Controls

- Fail-closed retrieval and tool gating on identity uncertainty.
- Dependency health checks and automated degradation modes.
- Fallback paths to canonical documentation portals.
- RTO/RPO-aligned recovery and validation steps for core services.

## 5) Launch Conditions

- Dependency ownership and on-call accountability are documented.
- Degraded-mode behavior is tested for major dependency failures.
- Alerting exists for authorization, retrieval, and tool-execution anomalies.

## 6) No-Go Conditions

- Unowned critical dependency or unclear escalation path.
- No tested degraded mode for IAM/retrieval/model outages.
- Audit/logging dependencies fail without detection.

## 7) Residual Risk

Residual dependency risk is **Medium-High** because correlated outages and third-party behavior changes cannot be fully eliminated; current assurance is **Partially Confirmed**.
