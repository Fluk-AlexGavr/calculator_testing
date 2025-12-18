import pytest
from calculator import Calculator

calc = Calculator()


@pytest.mark.parametrize("a, b, expected", [
    (6, 8, 14),
    (-5, 5, 0),
    (0, 0, 0),
    (14.5, 0.5, 15.0)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (63, 8, 55),
    (0, -12, 12),
    (-7, -8, 1),
    (12.5, 0.5, 12.0)
])
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 13, 26),
    (-1, 5, -5),
    (0, 3, 0),
    (2.5, 2.5, 6.25)
])
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (24, 2, 12),
    (18, 3, 6),
    (7, 2, 3.5),
    (4, 0, ValueError)
])
def test_divide(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calc.divide(a, b)
    else:
        assert calc.divide(a, b) == expected


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (13, True),
    (1, False),
    (0, False)
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
