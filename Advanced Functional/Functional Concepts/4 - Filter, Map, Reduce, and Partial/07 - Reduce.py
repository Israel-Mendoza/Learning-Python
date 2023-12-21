from typing import Any

"""
Built-in reducing functions.
    max
    min
    sum
    any
    all
"""

a_set: set[int] = {2, 6, 4, 9, 10, 2, 3}
another_set1: set[Any] = {"", 10, True, None, False}
another_set2: set[Any] = {"0", 10, True, "Python"}

max_result: int = max(a_set)
min_result: int = min(a_set)
sum_result: int = sum(a_set)
any_set1: bool = any(another_set1)
any_set2: bool = any(another_set2)
all_set1: bool = all(another_set1)
all_set2: bool = all(another_set2)

print(max_result)  # 10
print(min_result)  # 2
print(sum_result)  # 34
print(any_set1)  # True
print(any_set2)  # True
print(all_set1)  # False
print(all_set2)  # True
