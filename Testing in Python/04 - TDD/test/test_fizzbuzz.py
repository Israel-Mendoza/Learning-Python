from src.fizzbuzz import fizzbuzz, print_fizzbuzz


def test_fizzbuzz_normal_number() -> None:
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"


def test_fizzbuzz_three_is_fizz() -> None:
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_five_is_buzz() -> None:
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_fifteen_is_fizzbuzz() -> None:
    assert fizzbuzz(15) == "FizzBuzz"


def test_print_fizzbuzz_up_to_16(capsys) -> None:  # capsys is a fixture that captures what's printed to stdout
    # Calling the function to test:
    print_fizzbuzz(16)
    # Grabbing what was printed to stdout:
    printed_to_std: str = capsys.readouterr().out
    assert printed_to_std == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n"
