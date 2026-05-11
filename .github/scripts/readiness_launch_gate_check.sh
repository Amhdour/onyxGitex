#!/usr/bin/env bash
set -euo pipefail

ARTIFACT_DIR="security-readiness/19-ci-cd-secure-delivery/artifacts"
SUMMARY_FILE="${ARTIFACT_DIR}/launch-gate-summary.md"

mkdir -p "${ARTIFACT_DIR}"

required_files=(
  "security-readiness/19-ci-cd-secure-delivery/security-test-ci-pipeline.md"
  "security-readiness/19-ci-cd-secure-delivery/policy-test-ci-pipeline.md"
  "security-readiness/19-ci-cd-secure-delivery/evidence-generation-ci-pipeline.md"
  "security-readiness/19-ci-cd-secure-delivery/launch-gate-ci-check.md"
  "security-readiness/19-ci-cd-secure-delivery/regression-test-pack.md"
  "security-readiness/19-ci-cd-secure-delivery/control-drift-detection.md"
  "security-readiness/19-ci-cd-secure-delivery/release-readiness-checklist.md"
)

missing=0
{
  echo "# Launch Gate Summary"
  echo
  echo "Date (UTC): $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
  echo
  echo "## Required Artifact Check"
} > "${SUMMARY_FILE}"

for file in "${required_files[@]}"; do
  if [[ -f "${file}" ]]; then
    echo "- PASS: ${file}" >> "${SUMMARY_FILE}"
  else
    echo "- FAIL: ${file} (missing)" >> "${SUMMARY_FILE}"
    missing=1
  fi
done

if [[ ${missing} -ne 0 ]]; then
  echo >> "${SUMMARY_FILE}"
  echo "Launch gate result: FAIL (missing required artifacts)." >> "${SUMMARY_FILE}"
  exit 1
fi

echo >> "${SUMMARY_FILE}"
echo "Launch gate result: PASS (all required artifacts present)." >> "${SUMMARY_FILE}"
