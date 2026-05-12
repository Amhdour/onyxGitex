"""Tier 4 runtime fixture scaffolding for blocked integration launch-gate tests."""

from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any, Callable


def _blocked_fixture(name: str, reason: str) -> dict[str, Any]:
    return {
        "fixture": name,
        "status": "BLOCKED",
        "reason": reason,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def authorized_user() -> dict[str, Any]:
    return _blocked_fixture("authorized_user", "Tier 4 seeded authorized user missing")


def unauthorized_user() -> dict[str, Any]:
    return _blocked_fixture(
        "unauthorized_user", "Tier 4 seeded unauthorized user missing"
    )


def allowed_document() -> dict[str, Any]:
    return _blocked_fixture("allowed_document", "Tier 4 allowed document fixture missing")


def restricted_document() -> dict[str, Any]:
    return _blocked_fixture(
        "restricted_document", "Tier 4 restricted document fixture missing"
    )


def build_runtime_context(fixtures: dict[str, Any]) -> dict[str, Any]:
    """Build executable runtime context only when explicitly enabled.

    This remains fail-closed by default and returns non-executable context unless
    ``TIER4_RUNTIME_FIXTURES_READY=true`` is set by real runtime provisioning.
    """

    runtime_ready = os.getenv("TIER4_RUNTIME_FIXTURES_READY", "false").lower() == "true"
    if not runtime_ready:
        return {"runtime_ready": False, "fixtures": fixtures}

    def _not_wired(*_: Any, **__: Any) -> Any:
        raise NotImplementedError("Tier 4 runtime callables are not wired yet")

    return {
        "runtime_ready": True,
        "fixtures": fixtures,
        "run_authorized_allowed": _not_wired,
        "run_unauthorized_restricted": _not_wired,
        "capture_answer_text": _not_wired,
        "capture_retrieved_snippets": _not_wired,
        "capture_citation_metadata": _not_wired,
        "capture_audit_event": _not_wired,
        "capture_runtime_trace": _not_wired,
    }
