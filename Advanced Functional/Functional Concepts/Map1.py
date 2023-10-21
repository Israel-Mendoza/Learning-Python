"""Maps"""

"""Creating two iterables"""

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30]
list3 = [100, 200, 300, 400, 500]


"""Creating a callback function"""


def sum_two_items(x: int, y: int) -> int:
    """Returns the sum of two items"""
    return x + y


"""The map object is a non-reusable generator"""

# Capturing the map object
results = map(sum_two_items, list1, list2)

print(results)  # <map object at 0x0000019E6EAF3F70>

# Let's iterate through the map object
for result in results:
    print(result)
# 11
# 22
# 33

# Let's iterate through the map object again
for result in results:
    print(result)
# (No output)


# Capturing a list out of the map object
results = list(map(sum_two_items, list1, list2))

print(results)  # [11, 22, 33]

"""Passing more iterables than the function can work with"""

# Passing the incorrect parameters to the map function won't raise an exception
try:
    results = map(sum_two_items, list1, list2, list3)
except BaseException as error:
    print(f"{type(error).__name__}: {error}")
    results = []
else:
    print("No error so far!")
# No error so far!

# Iterating through the map object when this has been provided
# with the incorrect parameters will raise an error
try:
    for result in results:
        print(result)
except BaseException as error:
    print(f"{type(error).__name__}: {error}")
else:
    print("Didn't find any errors!")
# TypeError: sum_two_items() takes 2 positional arguments but 3 were given
