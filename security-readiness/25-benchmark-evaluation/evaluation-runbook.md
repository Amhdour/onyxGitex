# Evaluation Runbook

**Date:** 2026-05-11  
**Execution Status:** Ready to Run (not yet executed)

## Goal

Execute benchmark and regression evaluations for Priority 17 datasets while preserving auditable evidence.

## Preconditions

1. Fictional datasets are loaded into evaluation index only.
2. Test personas are configured (HR Analyst, Finance Analyst, Legal Counsel, Executive Staff, General Employee).
3. Output directory exists for logs/artifacts.

## Exact Commands

> Note: Commands below are the required execution sequence for this benchmark package. If project-specific scripts differ, update this runbook before use.

```bash
mkdir -p security-readiness/25-benchmark-evaluation/artifacts
```

```bash
python -m onyx.eval.run \
  --dataset security-readiness/25-benchmark-evaluation/evaluation-dataset-inventory.md \
  --cases security-readiness/25-benchmark-evaluation/prompt-injection-benchmark-set.md \
  --output security-readiness/25-benchmark-evaluation/artifacts/prompt_injection_results.json
```

```bash
python -m onyx.eval.run \
  --dataset security-readiness/25-benchmark-evaluation/retrieval-boundary-test-dataset.md \
  --output security-readiness/25-benchmark-evaluation/artifacts/retrieval_boundary_results.json
```

```bash
python -m onyx.eval.run \
  --dataset security-readiness/25-benchmark-evaluation/tool-misuse-test-dataset.md \
  --output security-readiness/25-benchmark-evaluation/artifacts/tool_misuse_results.json
```

```bash
python -m onyx.eval.regression \
  --inputs security-readiness/25-benchmark-evaluation/artifacts/*.json \
  --output security-readiness/25-benchmark-evaluation/artifacts/regression_summary.json
```

## Evidence Capture Checklist

For each executed command, record:

- command with timestamp,
- exit code,
- stdout/stderr,
- artifact filename and hash,
- reviewer identity.

## Result Handling Rules

- If commands are not executed, result documents must remain **Pending**.
- If execution partially fails, mark affected sections **Partially Confirmed**.
- Do not declare readiness from this phase alone.
