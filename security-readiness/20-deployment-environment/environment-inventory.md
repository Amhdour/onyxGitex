# Build Priority 12.123 — Environment Inventory

Date: 2026-05-11  
Status: Partially Confirmed

## Scope
Inventory of deployment environments and runtime components based on repository artifacts only (no live environment access).

## Evidence Sources
- `deployment/docker_compose/docker-compose.yml`
- `deployment/docker_compose/docker-compose.dev.yml`
- `deployment/docker_compose/docker-compose.prod.yml`
- `deployment/docker_compose/env.template`
- `deployment/docker_compose/env.prod.template`
- `deployment/README.md`
- `deployment/helm/charts/onyx/values.yaml`
- `deployment/helm/charts/onyx/templates/auth-secrets.yaml`

## Environment Surfaces
1. **Docker Compose (default / local baseline)**
   - Core services: `api_server`, `background`, `web_server`, `relational_db`, `inference_model_server`, `indexing_model_server`, `index`, `cache`, `nginx` (+ optional services).
   - Uses optional `.env` via `env_file`.
   - Default values include local/dev-style credentials for several components.

2. **Docker Compose Development Override**
   - `docker-compose.dev.yml` exposes internal service ports (Postgres, Redis, OpenSearch, model servers, etc.) to host for development/testing.

3. **Docker Compose Production Variant**
   - `docker-compose.prod.yml` provides hardened direction relative to default compose but still relies on operator-supplied `.env` values and secret hygiene.

4. **Kubernetes via Helm**
   - Chart in `deployment/helm/charts/onyx/` with configurable images/resources/autoscaling.
   - Secret templating fails install if required secret values are missing and no existing secret is present.

5. **Cloud-specific deployment options**
   - AWS ECS Fargate CloudFormation templates present under `deployment/aws_ecs_fargate/cloudformation/` (not deeply validated in this phase).
   - Terraform modules present under `deployment/terraform/modules/aws/` (not deeply validated in this phase).

## Inventory Confidence
- **Verified:** Environment definitions and templates in repo.
- **Partially Confirmed:** Expected runtime separation and hardening posture (depends on operator config).
- **Unknown:** Actual live production settings, network policy enforcement, and secret manager integration in active deployments.
