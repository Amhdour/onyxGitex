#!/usr/bin/env bash
set -euo pipefail

OUT="agent-security-readiness/23-langgraph-agent-lab/ci-fetch-output.txt"
ART_DIR="agent-security-readiness/23-langgraph-agent-lab/ci-downloaded-artifact"
WORKFLOW=".github/workflows/langgraph-agent-lab-evidence.yml"
ART_NAME="langgraph-agent-lab-evidence"

mkdir -p "$(dirname "$OUT")" "$ART_DIR"
: > "$OUT"

if ! command -v gh >/dev/null 2>&1; then
  echo "GH_CLI_NOT_AVAILABLE" | tee -a "$OUT"
  exit 0
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "GH_NOT_AUTHENTICATED" | tee -a "$OUT"
  exit 0
fi

echo "Listing recent runs for $WORKFLOW" | tee -a "$OUT"
gh run list --workflow "$WORKFLOW" --limit 5 | tee -a "$OUT"
LATEST_RUN_ID="$(gh run list --workflow "$WORKFLOW" --limit 1 --json databaseId --jq '.[0].databaseId' 2>/dev/null || true)"
if [[ -z "${LATEST_RUN_ID}" || "${LATEST_RUN_ID}" == "null" ]]; then
  echo "NO_RUN_ID_FOUND" | tee -a "$OUT"
  exit 0
fi

echo "LATEST_RUN_ID=${LATEST_RUN_ID}" | tee -a "$OUT"
echo "Attempting download of artifact: $ART_NAME" | tee -a "$OUT"
if gh run download "$LATEST_RUN_ID" -n "$ART_NAME" -D "$ART_DIR" >> "$OUT" 2>&1; then
  echo "ARTIFACT_DOWNLOAD_ATTEMPTED" | tee -a "$OUT"
  echo "Run local verifier next:" | tee -a "$OUT"
  echo "python agent-security-readiness/23-langgraph-agent-lab/verify-ci-artifacts-local.py --artifact-dir $ART_DIR" | tee -a "$OUT"
else
  echo "ARTIFACT_DOWNLOAD_FAILED_OR_NOT_FOUND" | tee -a "$OUT"
fi
