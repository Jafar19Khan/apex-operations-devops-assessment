import pytest


@pytest.mark.intentional_failure
def test_controlled_failure_for_release_gate_demo():
    # Expected to fail when explicitly run; excluded from normal CI.
    assert "release-approved" == "release-blocked"
