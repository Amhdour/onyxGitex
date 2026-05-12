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
    assert emitted_traces[0]["payload"] == {
        "document_set": "finance",
        "decision": "allow",
    }


def test_build_index_filters_denies_when_any_document_set_is_unauthorized(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: ["finance"],
    )

    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["finance", "hr-restricted"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "hr-restricted" in str(exc.value)


def test_build_index_filters_emits_mixed_allow_and_deny_audit_events(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
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
        lambda db_session, document_set_names, user: ["finance"],
    )
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_audit_logger", _AuditStub())
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_runtime_tracer", _TracerStub())

    with pytest.raises(OnyxError):
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["finance", "legal"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert [event["action_type"] for event in emitted_events] == [
        "retrieval.allow",
        "retrieval.deny",
    ]
    assert [trace["payload"]["decision"] for trace in emitted_traces] == ["allow", "deny"]


def test_build_index_filters_fails_closed_when_authorizer_raises_fail_closed_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from onyx.security_readiness.control_layer import FailClosedError

    emitted_events: list[dict[str, str | bool | None]] = []

    class _AuditStub:
        def emit_authorization_event(self, **kwargs: str | bool | None) -> dict[str, str | bool | None]:
            emitted_events.append(kwargs)
            return kwargs

    class _TracerStub:
        def emit(self, trace_name: str, payload: dict[str, object]) -> dict[str, object]:
            return {"trace_name": trace_name, "payload": payload}

    class _GuardStub:
        def authorize_document(self, auth_context: object, document_id: str, policy_map: object) -> object:
            raise FailClosedError("policy backend unavailable")

    monkeypatch.setattr(
        "onyx.context.search.pipeline.filter_document_set_names_by_user_access",
        lambda db_session, document_set_names, user: document_set_names,
    )
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_audit_logger", _AuditStub())
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_runtime_tracer", _TracerStub())
    monkeypatch.setattr("onyx.context.search.pipeline._retrieval_auth_guard", _GuardStub())

    with pytest.raises(OnyxError) as exc:
        _build_index_filters(
            user_provided_filters=BaseFilters(document_set=["finance"]),
            user=_user("u-1"),
            project_id_filter=None,
            persona_id_filter=None,
            persona_document_sets=None,
            persona_time_cutoff=None,
            db_session=object(),
        )

    assert exc.value.error_code == OnyxErrorCode.INSUFFICIENT_PERMISSIONS
    assert "policy backend unavailable" in str(exc.value)
    assert emitted_events[0]["action_type"] == "policy.missing_context"
    assert emitted_events[0]["fail_closed"] is True
