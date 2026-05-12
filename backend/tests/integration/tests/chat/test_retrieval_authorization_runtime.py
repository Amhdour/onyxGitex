"""Tier 4 runtime integration skeleton for retrieval authorization launch blocker.

This file intentionally defines blocked/skip-only runtime tests until the
required Tier 4 environment and fixtures are available.

Required runtime prerequisites (not yet available in current host):
- running backend API stack with retrieval path enabled
- seeded authorized and unauthorized users
- seeded allowed and restricted documents with explicit ACL boundaries
- chat/retrieval execution path exercising real tool invocation
- audit/trace capture for authorization decision evidence
- artifact emission into
  security-readiness/evidence-artifacts/test-results/
"""

import pytest

from .tier4_artifact_writer import mark_blocked
from .tier4_runtime_fixtures import authorized_user

TIER4_SCAFFOLD_BLOCKED = mark_blocked(
    suite_id="tier4_runtime_scaffold",
    blockers=["Runtime fixtures are scaffolded but not implemented."],
)
TIER4_AUTHORIZED_USER_FIXTURE = authorized_user()

pytestmark = pytest.mark.skip(
    reason="Tier 4 runtime environment/fixtures not available yet"
)


def test_retrieval_authorization_blocks_unauthorized_runtime_access() -> None:
    """Validate that unauthorized users cannot retrieve restricted content.

    Expected runtime behavior:
    - an unauthorized user executes a real chat/retrieval request
    - retrieval excludes restricted documents fail-closed
    - authorization denial is visible in runtime traces/audit events

    TODO:
    - add seeded authorized and unauthorized users
    - add seeded allowed and restricted documents
    - exercise real chat/retrieval execution path
    - capture audit/trace events for evidence
    - emit blocked/passed artifact JSON into
      security-readiness/evidence-artifacts/test-results/
    """


def test_retrieval_authorization_allows_permitted_runtime_access() -> None:
    """Validate that authorized users can retrieve allowed content only.

    Expected runtime behavior:
    - an authorized user executes a real chat/retrieval request
    - allowed documents can be retrieved while restricted documents remain
      inaccessible
    - runtime traces/audit events confirm policy-conformant access checks

    TODO:
    - add seeded authorized and unauthorized users
    - add seeded allowed and restricted documents
    - exercise real chat/retrieval execution path
    - capture audit/trace events for evidence
    - emit blocked/passed artifact JSON into
      security-readiness/evidence-artifacts/test-results/
    """
