import pytest

from onyx.security_readiness.control_layer import (
    AuthContext,
    FailClosedError,
    PolicyDecisionEngine,
    ResourcePolicy,
)


def test_fail_closed_when_context_or_policy_missing() -> None:
    engine = PolicyDecisionEngine()
    with pytest.raises(FailClosedError):
        engine.evaluate(None, ResourcePolicy(resource_id="d1"))
    with pytest.raises(FailClosedError):
        engine.evaluate(AuthContext(user_id="u1"), None)


def test_allow_when_context_and_policy_present() -> None:
    engine = PolicyDecisionEngine()
    decision = engine.evaluate(
        AuthContext(user_id="u1", groups=frozenset({"eng"})),
        ResourcePolicy(resource_id="d1", allowed_groups=frozenset({"eng"})),
    )
    assert decision.allowed is True
