from typing import Any

"""Filter"""

list1: list[Any] = [1, 0, "", None, [], {}, [1, 2], False]


# The "filter" function accepts a Callable[[T], bool] as a callback and an iterable.
# When we pass None as the callback function,
# the returned list will only include the "truthy" ones.
results: filter = filter(None, list1)

print(results)  # <filter object at 0x0000027C939B0FA0>

"""The filter object is a non-reusable generator"""

for result in results:
    print(result)
# 1
# [1, 2]

# Let's iterate through the filter object again
for result in results:
    print(result)
# (No output)


"""Passing a callback function"""

results_list: list[Any] = list(filter(lambda x: x % 3 == 0, range(25)))

print(results_list)  # [0, 3, 6, 9, 12, 15, 18, 21, 24]
