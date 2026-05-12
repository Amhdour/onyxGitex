"""Unit tests for MCP server utility auth enforcement."""

from fastmcp.server.auth.auth import AccessToken

from onyx.mcp_server import utils


def test_require_access_token_raises_when_missing(monkeypatch) -> None:
    """Missing identity should fail closed."""
    monkeypatch.setattr(utils, "get_access_token", lambda: None)

    try:
        utils.require_access_token()
        raise AssertionError("Expected ValueError for missing access token")
    except ValueError as exc:
        assert "requires an Onyx access token" in str(exc)


def test_require_access_token_returns_token_when_present(monkeypatch) -> None:
    """Valid identity should be returned for downstream tool calls."""
    token = AccessToken(
        token="abc",
        client_id="mcp",
        scopes=["mcp:use"],
        expires_at=None,
        resource=None,
        claims={},
    )
    monkeypatch.setattr(utils, "get_access_token", lambda: token)

    assert utils.require_access_token() == token
