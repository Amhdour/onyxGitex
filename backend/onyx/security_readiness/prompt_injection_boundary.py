from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PromptInjectionBoundaryResult:
    prompt: str
    authorization_decisions: dict[str, bool]
    allowed_context_document_ids: list[str]
    source_docs: list[dict[str, Any]]
    citations: dict[int, str]
    audit_events: list[dict[str, Any]]


def _filter_allowed_ids(authorization_decisions: dict[str, bool]) -> list[str]:
    return [doc_id for doc_id, allowed in authorization_decisions.items() if allowed]


def evaluate_prompt_injection_boundary(
    *,
    prompt: str,
    authorization_decisions: dict[str, bool],
    candidate_source_docs: list[dict[str, Any]],
    audit_logger: Any,
) -> PromptInjectionBoundaryResult:
    """Enforce retrieval authorization as the boundary for hostile prompt text.

    This intentionally does not call external LLM APIs. It validates policy/adapter
    behavior only and cannot prove full runtime prompt-injection resilience.
    """
    baseline_decisions = dict(authorization_decisions)
    allowed_document_ids = _filter_allowed_ids(authorization_decisions)

    filtered_source_docs = [
        source_doc
        for source_doc in candidate_source_docs
        if source_doc.get("document_id") in allowed_document_ids
    ]
    citation_mapping = {
        idx: source_doc["document_id"]
        for idx, source_doc in enumerate(filtered_source_docs, start=1)
    }

    denied_doc_ids = [doc_id for doc_id, allowed in authorization_decisions.items() if not allowed]
    for denied_doc_id in denied_doc_ids:
        audit_logger.emit_authorization_event(
            action_type="retrieval.prompt_injection_boundary.deny",
            decision="deny",
            reason="Authorization deny is immutable to prompt text",
            actor_id="test-user",
            resource_type="document",
            resource_id=denied_doc_id,
            policy_id="retrieval_authorization_decisions",
            evidence_status="Verified",
        )

    return PromptInjectionBoundaryResult(
        prompt=prompt,
        authorization_decisions=baseline_decisions,
        allowed_context_document_ids=allowed_document_ids,
        source_docs=filtered_source_docs,
        citations=citation_mapping,
        audit_events=list(audit_logger.events),
    )
