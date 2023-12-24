def fizzbuzz(number: int) -> str:
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def print_fizzbuzz(number: int) -> None:
    for i in range(1, number + 1):
        print(fizzbuzz(i))
