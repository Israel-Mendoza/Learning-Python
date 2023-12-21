from random import random

"""Using sorted and lambdas to randomize an iterable"""

a_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffled_list: list[int] = sorted(a_list, key=lambda _: random())

print(shuffled_list)
# [3, 5, 10, 1, 9, 8, 7, 2, 4, 6]
