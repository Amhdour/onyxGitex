# Dependency Sync Analysis

1. `numpy==2.4.1` is declared directly in `pyproject.toml` and also pinned in lock/requirements artifacts.
2. `numpy` is a direct dependency in this repository (not only transitive).
3. `uv.lock` pins `numpy==2.4.1`.
4. Current sync failures appear to be `network/tunnel error` (multiple failed fetch + tunnel error messages for PyPI wheel downloads).
5. Prior onnxruntime CPython 3.14 blocker is resolved for Python 3.12 selection path (sync now fails later on network downloads).
6. `fastapi-users` is declared in dependency groups (`backend`).
7. Package index configuration is standard PyPI (`https://pypi.org/simple` references in lock); no custom authenticated index setting found in searched repo files.
8. Repository-specific install command documented and used: `uv sync --python 3.12 --group backend --group dev`.
