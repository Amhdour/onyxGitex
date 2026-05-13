# External CI Signal Note (Reviewer-Provided)

- Date captured: 2026-05-12 (UTC)
- Source: reviewer-provided inline note in PR feedback.
- Raw signal:
  - `Requested labels: ubuntu-latest`
  - `Job defined at: Amhdour/onyxGitex/.github/workflows/tier4-runtime-collection.yml@refs/heads/main`
  - `Waiting for a runner to pick up this job...`
  - `Evaluating tier4-runtime-collection.if`
  - `Evaluating: success()`
  - `Result: true`
  - Badge link: `[![Tier 4 Runtime Collection](https://github.com/Amhdour/onyxGitex/actions/workflows/tier4-runtime-collection.yml/badge.svg)](https://github.com/Amhdour/onyxGitex/actions/workflows/tier4-runtime-collection.yml)`

## Evidence handling decision
- This signal refers to `tier4-runtime-collection.yml`, not the primary workflow `.github/workflows/rag-boundary-runtime-evidence.yml`.
- This signal does not include a run ID, conclusion, or artifact proof for `rag-boundary-runtime-evidence`.
- Therefore, `final-run-status.json` remains `CI_NOT_RUN` for the RAG Boundary Runtime Evidence workflow until direct run metadata/artifact evidence is collected.
