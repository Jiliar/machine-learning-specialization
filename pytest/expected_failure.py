import pytest

@pytest.mark.xfail
def test_always_fails():
    assert 1 + 1 == 3