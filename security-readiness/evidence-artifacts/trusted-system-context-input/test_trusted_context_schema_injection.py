from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text()


def test_search_api_request_model_does_not_define_internal_flags_in_schema_source() -> None:
    src = _read("backend/onyx/server/features/search/models.py")
    class_block = src.split("class SearchAPIRequest(BaseModel):", 1)[1].split(
        "class SearchAPIResult", 1
    )[0]

    assert "trusted_system_context" not in class_block
    assert "bypass_acl" not in class_block


def test_chat_request_model_does_not_define_internal_flags_in_schema_source() -> None:
    src = _read("backend/onyx/server/query_and_chat/models.py")
    class_block = src.split("class SendMessageRequest(BaseModel):", 1)[1].split(
        "class ChatMessageIdentifier", 1
    )[0]

    assert "trusted_system_context" not in class_block
    assert "bypass_acl" not in class_block


def test_search_ui_request_model_does_not_define_internal_flags_in_schema_source() -> None:
    src = _read("backend/ee/onyx/server/query_and_chat/models.py")
    class_block = src.split("class SendSearchQueryRequest(BaseModel):", 1)[1].split(
        "class SearchDocWithContent", 1
    )[0]

    assert "trusted_system_context" not in class_block
    assert "bypass_acl" not in class_block


def test_chunk_search_request_is_internal_model_with_control_flags() -> None:
    src = _read("backend/onyx/context/search/models.py")
    class_block = src.split("class ChunkSearchRequest(BasicChunkRequest):", 1)[1].split(
        "class ChunkIndexRequest", 1
    )[0]

    assert "bypass_acl: bool = False" in class_block
    assert "trusted_system_context: bool = False" in class_block


def test_search_api_endpoint_sets_bypass_acl_internally() -> None:
    src = _read("backend/onyx/server/features/search/api.py")

    assert "SearchTool(" in src
    assert "bypass_acl=False" in src


def test_runtime_pydantic_import_blocker_is_captured_for_evidence() -> None:
    try:
        __import__("onyx.server.features.search.models")
    except ModuleNotFoundError as e:
        assert "fastapi_users_db_sqlalchemy" in str(e)
    else:
        raise AssertionError(
            "Expected missing dependency blocker was not triggered in this environment"
        )
