"""
Built-in reducing functions.
    max
    min
    sum
    any
    all
"""

a_set = {2, 6, 4, 9, 10, 2, 3}
another_set1 = {"", 10, True, None, False}
another_set2 = {"0", 10, True, "Python"}


max_result = max(a_set)
min_result = min(a_set)
sum_result = sum(a_set)
any_set1 = any(another_set1)
any_set2 = any(another_set2)
all_set1 = all(another_set1)
all_set2 = all(another_set2)

print(max_result)  # 10
print(min_result)  # 2
print(sum_result)  # 34
print(any_set1)  # True
print(any_set2)  # True
print(all_set1)  # False
print(all_set2)  # True
