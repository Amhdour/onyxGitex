"""Tier 4 runtime fixture scaffolding for blocked integration launch-gate tests.

This module intentionally provides non-executable placeholders until a real
Tier 4 runtime environment is available. Helpers either raise
``NotImplementedError`` or return explicit BLOCKED-shaped metadata.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


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


def allowed_document_set() -> dict[str, Any]:
    return _blocked_fixture(
        "allowed_document_set", "Tier 4 allowed document set fixture missing"
    )


def restricted_document_set() -> dict[str, Any]:
    return _blocked_fixture(
        "restricted_document_set", "Tier 4 restricted document set fixture missing"
    )


def chat_session() -> dict[str, Any]:
    raise NotImplementedError("Tier 4 runtime chat session fixture is not implemented")


def retrieval_request() -> dict[str, Any]:
    raise NotImplementedError("Tier 4 runtime retrieval request fixture is not implemented")


def citation_capture() -> dict[str, Any]:
    return _blocked_fixture("citation_capture", "Tier 4 citation capture not wired")


def audit_event_capture() -> dict[str, Any]:
    return _blocked_fixture("audit_event_capture", "Tier 4 audit capture not wired")


def runtime_trace_capture() -> dict[str, Any]:
    return _blocked_fixture("runtime_trace_capture", "Tier 4 trace capture not wired")


def adversarial_prompt_corpus() -> dict[str, Any]:
    return _blocked_fixture(
        "adversarial_prompt_corpus", "Tier 4 adversarial prompts not provisioned"
    )
