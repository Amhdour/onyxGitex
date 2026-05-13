# Version 2B — CI Artifact Proof

Goal:
Prove that runtime test results are produced by CI and preserved as reviewable artifacts.

Required evidence:
- Workflow run ID
- Job status
- Artifact name
- Artifact download result
- Artifact file list
- final-run-status.json
- pytest output
- runtime trace
- audit events

Decision rules:
- No workflow run ID: NOT_ENOUGH_EVIDENCE
- No downloadable artifact: NOT_ENOUGH_EVIDENCE
- Missing final-run-status.json: NOT_ENOUGH_EVIDENCE
- Missing pytest output: NOT_ENOUGH_EVIDENCE
- Failed test: NO_GO
- Complete artifact set with passing runtime proof: RUNTIME_VERIFIED
