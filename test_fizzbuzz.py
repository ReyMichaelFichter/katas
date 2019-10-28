import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("num, expected", [(1, 1), (3, "Fizz"), (6, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")])
def test_fizzbuzz(num, expected):
    assert fizzbuzz(num) == expected