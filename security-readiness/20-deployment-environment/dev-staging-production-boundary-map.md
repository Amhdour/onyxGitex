# Build Priority 12.124 — Development / Staging / Production Boundary Map

Date: 2026-05-11  
Status: Partially Confirmed

## Logical Boundary Model

## Development
- Primary artifact: `docker-compose.yml` + `docker-compose.dev.yml`.
- Boundary characteristics:
  - Explicit host port exposure for internal services.
  - Convenience defaults and debug-forward posture.
  - Suitable for local testing, not production isolation.

## Staging
- No explicit staging compose file found.
- Inferred pattern: staging should be an environment-specific overlay (compose or Helm values) with production-like boundaries but lower scale.
- Current state: **Unknown** (no dedicated staging manifest discovered in this scope).

## Production
- Artifacts suggest two production patterns:
  - `docker-compose.prod.yml` and `env.prod.template`
  - Kubernetes Helm chart (`deployment/helm/charts/onyx`)
- Boundary expectations from artifacts:
  - Minimized exposed ports (front door through nginx/ingress only).
  - Authentication configured for enterprise IdP flows.
  - Secrets supplied externally (not default literals).

## Boundary Risks
1. **Boundary drift risk**: developers may deploy default compose settings to non-dev environments.
2. **Missing staging codification**: no clearly versioned staging boundary map in-repo.
3. **Config parity gap**: compose and helm may diverge without explicit controls.

## Required Control Direction
- Enforce separate env files/values per environment with change review.
- Gate production deploys on explicit boundary checklist sign-off.
- Require network exposure review for every environment update.
