def fizzbuzz(n: int, additional_rules: dict[int, str] | None = None) -> str:
    """
    Converts a number to its name in the game FizzBuzz
    :param n: The number to convert.
    :param additional_rules: A dictionary containing custom additional rules.
    :return: The name in the game.
    """
    answer: str = ""
    rules: dict[int, str] = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer
