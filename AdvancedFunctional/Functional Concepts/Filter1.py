"""Filter"""

list1 = [1, 0, "", None, [], {}, [1, 2], False]


# When the callback function is set to None, the results
# will be only the "truthy" ones from the iterable
results = filter(None, list1)

print(results)  # <filter object at 0x0000027C939B0FA0>

"""The filter object is a non-reusable generator"""

for result in results:
    print(result)
# 1
# [1, 2]

# Let's iterate through the map object again
for result in results:
    print(result)
# (No output)


"""Passing a callback function"""

results = list(filter(lambda x: x % 3 == 0, range(25)))

print(results)  # [0, 3, 6, 9, 12, 15, 18, 21, 24]
