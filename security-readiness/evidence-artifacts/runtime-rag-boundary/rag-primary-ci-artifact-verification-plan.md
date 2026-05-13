# RAG Primary CI Artifact Verification Plan

## 1. Purpose
Define direct artifact-proof steps for primary RAG CI evidence.

## 2. Current RAG status
- primary CI workflow not verified unless direct evidence exists
- external signal insufficient
- local runtime previously blocked
- launch remains NO_GO / NOT_ENOUGH_EVIDENCE

## 3. Required workflow
.github/workflows/rag-boundary-runtime-evidence.yml

## 4. Required proof
workflow run ID, job status, artifact name, artifact download, artifact file list, pytest output, dependency logs, backend logs if available, final-run-status.json from artifact

## 5. What to do after artifact proof
update ci-result-summary.md, final-run-status.json, launch-gate index, and portfolio proof checklist.

## 6. Non-claims
Do not use agent CI as RAG proof. Do not use external tier4 signal as RAG proof. Do not claim RAG PASS without direct artifact logs.
