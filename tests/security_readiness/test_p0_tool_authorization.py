from onyx.tools.tool_authorization_router import ToolAuthorizationRouter


def test_tool_authorization_fail_closed_and_allow_paths() -> None:
    router = ToolAuthorizationRouter()
    policy = {
        "search": {"allowed": True, "risk_level": "low"},
        "python": {"allowed": True, "risk_level": "high"},
    }

    assert router.authorize(tool_name="unknown", user_id="u1", policy=policy, approval_id=None).allowed is False
    assert router.authorize(tool_name="search", user_id=None, policy=policy, approval_id=None).reason == "missing_user_identity"
    assert router.authorize(tool_name="python", user_id="u1", policy=policy, approval_id=None).reason == "missing_explicit_approval"

    allowed = router.authorize(tool_name="search", user_id="u1", policy=policy, approval_id=None)
    assert allowed.allowed is True
    assert allowed.reason == "authorized"
