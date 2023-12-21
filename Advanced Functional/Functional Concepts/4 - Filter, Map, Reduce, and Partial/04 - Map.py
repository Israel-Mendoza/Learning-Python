"""Maps"""
from collections.abc import Generator

# Creating two iterables:
list1: list[int] = [1, 2, 3, 4, 5]
list2: list[int] = [10, 20, 30]


"""Using list comprehensions instead of the map object"""


# Creating a list out of a map object
map_results: list[int] = list(map(lambda x, y: x + y, list1, list2))
print(map_results)
# [11, 22, 33]

# Using list comprehension
list_comp_results: list[int] = [x + y for x, y in zip(list1, list2)]
print(list_comp_results)
# [11, 22, 33]

# Using a generator expression
gen_results: Generator = (x + y for x, y in zip(list1, list2))
print(gen_results)  # <generator object <genexpr> at 0x000002C90DF7E890>

"""Generator expressions are non-reusable generators"""

for result in gen_results:
    print(result)
# 11
# 22
# 33

for result in gen_results:
    print(result)
# (No output)
