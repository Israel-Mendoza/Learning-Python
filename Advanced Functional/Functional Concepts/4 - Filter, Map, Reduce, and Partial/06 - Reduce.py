from functools import reduce

"""Using the reduce function from the functools module."""

a_set: set[int] = {5, 8, 6, 10, 9}


def _max(x: int, y: int) -> int:
    """Returns the biggest of two numbers"""
    return x if x > y else y


def _min(x: int, y: int) -> int:
    """Returns the smallest of two numbers"""
    return x if x < y else y


def _sum(x: int, y: int) -> int:
    """Returns the sum of two numbers"""
    return x + y


"""Using the reduce function"""

max_result: int = reduce(_max, a_set)
min_result: int = reduce(_min, a_set)
sum_result: int = reduce(_sum, a_set)

print(max_result)  # 5
print(min_result)  # 10
print(sum_result)  # 38

# Using the initial value

some_words: list[str] = ["I", "love", "Python"]
initial_word: str = "Message:"

sentence: str = reduce(lambda acc, n: f"{acc} {n}", some_words, initial_word)

print(sentence)
# Message: I love Python
