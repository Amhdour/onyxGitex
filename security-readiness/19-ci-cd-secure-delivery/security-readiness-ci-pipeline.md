# Security Readiness CI Pipeline (Non-Destructive)

## Status
- **Type:** Additive CI workflow (manual dispatch only)
- **Workflow file:** `.github/workflows/security-readiness.yml`
- **Decision:** Manual-only execution to avoid impact to existing Onyx CI branch protections and merge latency.

## Safety Rationale
- The workflow is isolated from existing PR/merge workflows.
- The job uses `continue-on-error: true` to avoid blocking delivery pipelines while evidence automation matures.
- No secrets are consumed.
- No external LLM API calls are required.
- Artifact upload is best-effort (`if-no-files-found: warn`) to preserve non-destructive behavior.

## Pipeline Steps
1. Install backend dependencies via the repository standard action:
   - `./.github/actions/setup-python-and-install-dependencies`
   - Requirements:
     - `backend/requirements/default.txt`
     - `backend/requirements/dev.txt`
     - `backend/requirements/model_server.txt`
     - `backend/requirements/ee.txt`
2. Run readiness unit tests:
   - `py.test -q backend/tests/unit/onyx/security_readiness`
3. Run RAG boundary tests (if available):
   - `py.test -q backend/tests/unit/onyx/security_readiness -k rag_boundary`
4. Run policy-as-code tests:
   - `py.test -q security-readiness/policies/tests`
5. Run evidence validation:
   - `python3 security-readiness/scripts/validate-launch-evidence.py`
6. Run launch gate in evidence mode:
   - `python3 security-readiness/scripts/run-launch-gate.py`
7. Upload evidence artifacts:
   - `security-readiness/evidence-artifacts/`
   - `security-readiness/19-ci-cd-secure-delivery/artifacts/`

## Known Limits / Evidence Posture
- Current output is intended for **readiness evidence generation** and does not assert production launch approval.
- Failing controls or incomplete evidence should be interpreted as **Partially Confirmed** or **Unknown** until remediated.
