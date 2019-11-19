import pytest

from hamming_numbers import brute_force, dynamic_programming

@pytest.mark.parametrize(
    "n, res",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 8),
        (8, 9),
        (9, 10),
        (10, 12),
        (15, 24),
        (150, 5832),
    ],
)
def test_brute_force(n, res):
    assert brute_force.hamming(n) == res

@pytest.mark.parametrize(
    "n, res",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 8),
        (8, 9),
        (9, 10),
        (10, 12),
        (15, 24),
        (150, 5832),
    ],
)
def test_dynamic_programming(n, res):
    assert dynamic_programming.hamming(n) == res
