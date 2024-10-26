import pytest


def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])

def test_add(a,b, expected):
    assert add(a, b) == expected