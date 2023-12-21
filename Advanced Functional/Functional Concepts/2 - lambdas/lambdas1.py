"""Creating basic lambda functions"""


def square(num: int) -> int:
    return num * num


square2 = lambda num: num * num  # Warning: PEP 8: E731 do not assign a lambda expression, use a def
square3 = square2

print(square)
# <function square at 0x1AE93999F70>
print(square2)
# <function <lambda> at 0x190E8DE4040>
print(square3)
# <function <lambda> at 0x190E8DE4040>
