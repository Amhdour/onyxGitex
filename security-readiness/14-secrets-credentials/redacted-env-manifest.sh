#!/usr/bin/env bash
set -euo pipefail

# Generates a name-only manifest of potential secret environment variables.
# Never prints values.

ROOT_DIR="${1:-.}"
OUT_FILE="${2:-security-readiness/14-secrets-credentials/redacted-env-manifest.txt}"

rg -n --no-heading -o "[A-Z][A-Z0-9_]*(SECRET|TOKEN|PASSWORD|API_KEY)" \
  "$ROOT_DIR/deployment" "$ROOT_DIR/backend" \
  -g '*.yml' -g '*.yaml' -g '*.env*' -g '*.py' 2>/dev/null \
  | awk -F: '{print $NF}' \
  | sort -u \
  | awk '{print $1"=[REDACTED]"}' > "$OUT_FILE"

echo "Wrote redacted manifest to $OUT_FILE"
