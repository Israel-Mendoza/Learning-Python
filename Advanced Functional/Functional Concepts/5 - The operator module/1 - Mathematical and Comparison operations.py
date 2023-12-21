import operator
from functools import reduce

"""
    The arithmetic operations are usually expressed using the arithmetic operators.

    However, the operator module offers functions that achieve the same thing as 
    the arithmetic operators, but through function calls.
    
    Furthermore, it also offers functions that achieve other type of operations, such as:
    
    1. Comparison Operations
    2. Logical Operations
    3. Bitwise Operations
    4. Sequence Operations
    5. In-place Operations
    
    See the following examples that shows how the mathematical operations work.
"""


"""Mathematical Operations"""

print(1 + 2, operator.add(1, 2))  # 3

print(1 - 2, operator.sub(1, 2))  # -1

print(5 * 3, operator.mul(5, 3))  # 15

print(10 / 3, operator.truediv(10, 3))  # 3.33333

print(10 // 3, operator.floordiv(10, 3))  # 3

print(3 % 2, operator.mod(3, 2))  # 1


"""Comparison Operations"""

print(1 < 2, operator.lt(1, 2))  # True

print(1 > 2, operator.gt(1, 2))  # False

print(1 == 1, operator.eq(1, 1))  # True

print("abc" is "abc", operator.is_("abc", "abc"))  # True

print(operator.truth(""))  # False


"""
    Why can this be useful?
    
    Having a function that takes two arguments
    can prevent us from having to create a lambda 
    function when a callback function is expected
"""

my_nums: list[int] = [1, 3, 5, 7, 9]

product1 = reduce(lambda x, y: x * y, my_nums)
product2 = reduce(operator.mul, my_nums)

print(product1)  # 945
print(product2)  # 945
