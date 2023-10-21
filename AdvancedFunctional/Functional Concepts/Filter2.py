"""Using list comprehensions instead of the map object"""


# Creating a list out of a filter object
filter_results = list(filter(lambda x: x % 3 == 0, range(25)))
print(filter_results)
# [0, 3, 6, 9, 12, 15, 18, 21, 24]

# Using list comprehension
comp_results = [x for x in range(25) if x % 3 == 0]
print(comp_results)
# [0, 3, 6, 9, 12, 15, 18, 21, 24]

# Using a generator expresion
gen_results = (x for x in range(25) if x % 3 == 0)
print(gen_results)  # <generator object <genexpr> at 0x000002088B4BE890>

"""Generator expressions are non-reusable generators"""

for result in gen_results:
    print(result)
# 0
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24

for result in gen_results:
    print(result)
# (No output)