# Runtime Environment Requirements

- Required Python version for this evidence attempt: **3.12**.
- Dependency install command attempted:
  - `uv sync --python 3.12 --group backend --group dev`
- RAG evidence rerun command:
  - `bash security-readiness/evidence-artifacts/runtime-rag-boundary/scripts/run-runtime-rag-boundary-check.sh`
- Known unsupported interpreter:
  - **CPython 3.14 currently blocked by `onnxruntime==1.20.1` resolution** in this environment.

## Evidence status implications
- If interpreter is not selected supported runtime: classify as `UNSUPPORTED_PYTHON_VERSION`.
- If selected runtime is unavailable: classify as `PYTHON_RUNTIME_UNAVAILABLE`.
- If selected runtime exists but sync still fails: classify as `BLOCKED_PACKAGE_RESOLUTION`.
- Runtime security-control verification remains blocked unless pytest actually executes target test logic.
