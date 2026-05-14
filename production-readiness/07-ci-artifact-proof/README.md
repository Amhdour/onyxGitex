# Version 2B — CI Artifact Proof

Purpose:
Prove that Version 2A RAG runtime evidence can be generated in GitHub Actions and preserved as downloadable artifacts.

Current status:
CI_WORKFLOW_CONFIGURED_NOT_VERIFIED

This is not production proof.
This is not staging proof.
This is not client proof.
This does not allow GO.

Required proof:
- GitHub Actions workflow exists.
- Workflow runs Version 2A evidence command.
- Workflow runs Version 2A validator.
- Workflow prints Version 2A status.
- Workflow uploads Version 2A evidence artifact.
- Artifact contains all required evidence files.
- Artifact can be downloaded and verified.
- production_ready remains false.
- go_decision remains false.

Canonical Version 2A evidence:
security-readiness/evidence-artifacts/version-2a-rag-runtime/

Canonical Version 2B proof:
security-readiness/evidence-artifacts/version-2b-ci-artifact-proof/

How to validate local CI contract:
python scripts/validate-ci-artifact-proof.py --mode local-ci-contract

How to print status:
python scripts/print-ci-artifact-status.py

How to validate downloaded artifact:
python scripts/validate-ci-artifact-proof.py --mode artifact-directory --artifact-dir <downloaded-artifact-dir>

Allowed claims:
- Version 2B CI workflow is configured.
- Version 2B artifact contract is defined.
- If real artifact verification succeeds: Version 2B CI artifact proof is verified.
- Production readiness is not claimed.

Blocked claims:
- Production ready
- GO launch decision
- Staging verified
- Client verified
- Full production RAG security proven
