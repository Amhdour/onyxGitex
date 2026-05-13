# RAG Primary CI Artifact Verification Plan

- Local verifier script: `security-readiness/evidence-artifacts/runtime-rag-boundary/verify-rag-primary-ci-artifacts-local.py`
- Downloaded artifact directory: `security-readiness/evidence-artifacts/runtime-rag-boundary/ci-downloaded-artifact/`
- Expected output file: `security-readiness/evidence-artifacts/runtime-rag-boundary/rag-ci-artifact-verification-output.json`

Status vocabulary:
- `RAG_CI_ARTIFACT_NOT_AVAILABLE`
- `RAG_CI_ARTIFACT_INCOMPLETE`
- `RAG_CI_ARTIFACT_VERIFIED`

Do not upgrade `final-run-status.json` for RAG without direct primary artifact proof.
