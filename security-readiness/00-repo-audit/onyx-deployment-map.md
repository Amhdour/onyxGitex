# Onyx Deployment Map

## Container images

- `backend/Dockerfile`
- `backend/Dockerfile.model_server`
- `cli/Dockerfile`
- Confidence: **Confirmed**.

## Docker Compose deployments

- `deployment/docker_compose/docker-compose.yml` (base)
- `docker-compose.dev.yml`, `docker-compose.prod.yml`, `docker-compose.multitenant-dev.yml`
- MCP-focused compose files: `docker-compose.mcp-api-key-test.yml`, `docker-compose.mcp-oauth-test.yml`
- Confidence: **Confirmed**.

## Helm / Kubernetes

- Helm chart: `deployment/helm/charts/onyx/`
- Templates include API/web/celery/model/mcp ingress/service/deploy manifests.
- Confidence: **Confirmed**.

## Terraform / Infra

- `deployment/terraform/modules/aws/onyx/` plus modules for `eks`, `redis`, `postgres`, `opensearch`, `vpc`, `waf`, `s3`.
- Confidence: **Confirmed**.

## Security-relevant deployment concerns (repo-observed)

- Secret-driven config appears expected via values/env templates; plaintext secret hygiene in deployed environments is **Needs Verification**.
- MCP ingress and oauth callback manifests exist; end-to-end external exposure controls are **Unknown** without runtime env review.
