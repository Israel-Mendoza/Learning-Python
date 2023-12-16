from typing import Callable

"""
    We'll recreate an averager class with a closure. 
    
    A class has properties we can access. 
    We can replicate the same thing by accessing the free variable's
    values (through the cell objects) on the closure. 
"""


"""USING A CLASS"""


class Averager:
    def __init__(self) -> None:
        self._count: int = 0
        self._total: int | float = 0

    @property
    def total(self) -> int | float:
        return self._total

    @property
    def count(self) -> int:
        return self._count

    def add(self, number: int) -> float:
        self._total += number
        self._count += 1
        return float(self.total / self.count)


avg_obj = Averager()

print(avg_obj.__class__)  # <class '__main__.Averager'>
print(type(avg_obj))  # <class '__main__.Averager'>
print(avg_obj.add(10))  # 10.0
print(avg_obj.add(15))  # 12.5
print(avg_obj.add(30))  # 18.333333333333332
print(avg_obj.total)  # 55
print(avg_obj.count)  # 3
print()


###############################################################################
###############################################################################


"""USING A CLOSURE"""


def averager() -> Callable[[int], float]:
    count: int = 0
    total: int | float = 0

    def inner(x: int) -> float:
        nonlocal total, count
        total += x
        count += 1
        return total / count

    return inner


avg_closure = averager()

# Printing the closure's information:

print(avg_closure.__closure__)  # A tuple containing the cell objects:
# (<cell at 0x0000018C882A3670: int object at 0x0000018C87C86910>,
# <cell at 0x0000018C882A3640: int object at 0x0000018C87C86910>)
print(avg_closure.__code__.co_freevars)  # Free var names
# ('count', 'total')
print(avg_closure.__code__.co_argcount)  # Number of accepted arguments by the closure:
# 1
print(avg_closure.__code__.co_name)  # Name of the returned function:
# inner
print(avg_closure.__code__.co_varnames)  # Tuple with the names of the variables in the closure
# ('x',)


print(avg_closure(10))  # 10.0
print(avg_closure(15))  # 12.5
print(avg_closure(30))  # 18.333333333333332
for i in range(len(avg_closure.__closure__)):
    print(f"{avg_closure.__code__.co_freevars[i]}: {avg_closure.__closure__[i].cell_contents}")
# count: 3
# total: 55
