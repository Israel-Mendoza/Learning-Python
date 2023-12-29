import pytest
from src.fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "number, expected", [
        (2, "2"),
        (3, "Fizz"),
        (4, "4"),
        (5, "Buzz"),
        (6, "Fizz"),
        (7, "7"),
        (9, "Fizz"),
        (10, "Buzz"),
        (11, "11"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (33, "Fizz"),
        (35, "Buzz")
    ]
)
def test_fizzbuzz(number, expected) -> None:
    assert fizzbuzz(number) == expected


@pytest.mark.parametrize(
    "number, additional_rules, expected", [
        (7, {7: "Whizz"}, "Whizz")
    ]
)
def test_fizzbuzz(number, additional_rules, expected) -> None:
    assert fizzbuzz(number, additional_rules) == expected
