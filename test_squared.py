import pytest
from squared import get_squared
from typing import Dict, Optional


@pytest.mark.parametrize(
    argnames="test_input,expected",
    argvalues=[
        ({"num": 5, "limit": None}, 25),
        ({"num": 8, "limit": None}, 64),
        ({"num": 10, "limit": None}, 100),
        ({"num": 5, "limit": 30}, 25),
        ({"num": 5, "limit": 25}, 25),
        ({"num": 5, "limit": 20}, None),
    ],
)
def test_squared(test_input: Dict[str, Optional[int]], expected: int):
    assert get_squared(**test_input) == expected
