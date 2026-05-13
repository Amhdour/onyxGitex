"""FUTURE_ONYX_BACKEND_INTEGRATION_PATH.

This file is not the canonical Version 2A local harness because backend/tests
loads backend/tests/conftest.py and full backend dependencies. Canonical harness:
tests/version_2a/test_rag_runtime_evidence_gate.py
"""

import pytest

pytestmark = pytest.mark.skip(reason="FUTURE_ONYX_BACKEND_INTEGRATION_PATH")
