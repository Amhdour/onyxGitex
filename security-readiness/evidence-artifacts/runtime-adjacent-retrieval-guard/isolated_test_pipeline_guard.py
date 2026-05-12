"""Dependency-isolated runtime-adjacent retrieval guard checks.

This test intentionally lives outside backend/tests so pytest does not load
backend/tests/conftest.py and its broader harness dependencies.
"""

from types import SimpleNamespace

import pytest

from onyx.context.search.models import BaseFilters
from onyx.context.search.pipeline import _build_index_filters
from onyx.error_handling.error_codes import OnyxErrorCode
from onyx.error_handling.exceptions import OnyxError


def _user(user_id: str | None) -> SimpleNamespace:
    return SimpleNamespace(id=user_id)


def test_build_index_filters_allows_authorized_document_sets(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: document_set_names,
    )
    monkeypatch.setattr(
        "onyx.context.search.pipeline.build_access_filters_for_user",
        lambda user, db_session: ["acl:u-1"],
    )

    filters = _build_index_filters(
        user_provided_filters=BaseFilters(document_set=["finance"]),
        user=_user("u-1"),
        project_id_filter=None,
        persona_id_filter=None,
        persona_document_sets=None,
        persona_time_cutoff=None,
        db_session=object(),
    )

    assert filters.document_set == ["finance"]


def test_build_index_filters_denies_unauthorized_document_set(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: [],
    )

    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["restricted"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS


def test_build_index_filters_fails_closed_without_identity() -> None:
    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["restricted"]),
            user=_user(None),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS


def test_build_index_filters_fails_closed_without_document_permission_context() -> None:
    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["restricted"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=None,
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS


def test_build_index_filters_emits_audit_and_trace_for_allow(monkeypatch: pytest.MonkeyPatch) -> None:
    emitted_events: list[dict[str, str | bool | None]] = []
    emitted_traces: list[dict[str, object]] = []

    class _AuditStub:
        def emit_authorization_event(self, **kwargs: str | bool | None) -> dict[str, str | bool | None]:
            emitted_events.append(kwargs)
            return kwargs

    class _TracerStub:
        def emit(self, trace_name: str, payload: dict[str, object]) -> dict[str, object]:
            trace = {"trace_name": trace_name, "payload": payload}
            emitted_traces.append(trace)
            return trace

    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: document_set_names,
    )
    monkeypatch.setattr(
        "onyx.context.search.pipeline.build_access_filters_for_user",
        lambda user, db_session: ["acl:u-1"],
    )
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_audit_logger", _AuditStub())
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_runtime_tracer", _TracerStub())

    _build_index_filters(
        user_provided_filters=BaseFilters(document_set=["finance"]),
        user=_user("u-1"),
        project_id_filter=None,
        persona_id_filter=None,
        persona_document_sets=None,
        persona_time_cutoff=None,
        db_session=object(),
    )

    assert emitted_events
    assert emitted_events[0]["action_type"] == "retrieval.allow"
    assert emitted_events[0]["decision"] == "allow"
    assert emitted_events[0]["resource_type"] == "document_set"
    assert emitted_events[0]["resource_id"] == "finance"
    assert emitted_traces
    assert emitted_traces[0]["trace_name"] == "retrieval.authorization"
    assert emitted_traces[0]["payload"] == {"document_set": "finance", "decision": "allow"}
