import operator
from functools import reduce

"""Arithmetic operations"""

print(1 + 2)  # 3
print(operator.add(1, 2))  # 3

print(1 - 2)  # -1
print(operator.sub(1, 2))  # -1

print(5 * 3)  # 15
print(operator.mul(5, 3))  # 15

print(10 / 3)  # 3.33333
print(operator.truediv(10, 3))  # 3.33333

print(10 // 3)  # 3
print(operator.floordiv(10, 3))  # 3

print(3 % 2)  # 1
print(operator.mod(3, 2))  # 1


"""Boolean operators"""

print(1 < 2)  # True
print(operator.lt(1, 2))  # True

print(1 > 2)  # False
print(operator.gt(1, 2))  # False

print(1 == 1)  # True
print(operator.eq(1, 1))  # True

print("abc" is "abs")  # True
print(operator.is_("abc", "abc"))  # True

print(operator.truth(""))  # False

"""Why can this be useful?"""

my_nums = [1, 3, 5, 7, 9]

product1 = reduce(lambda x, y: x * y, my_nums)
product2 = reduce(operator.mul, my_nums)

print(product1)  # 945
print(product2)  # 945
