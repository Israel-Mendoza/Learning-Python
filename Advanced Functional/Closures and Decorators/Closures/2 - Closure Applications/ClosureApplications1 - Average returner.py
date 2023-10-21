# Average returner with classes


class Averager:
    def __init__(self):
        print("Creating a new Averager instance...")
        self._total = 0
        self._count = 0

    @property
    def total(self):
        return self._total

    @property
    def count(self):
        return self._count

    def add(self, number: int):
        self._total += number
        self._count += 1
        return self.total / self.count


a = Averager()  # Creating a new Averager instance...

print(a.__class__)  # <class '__main__.Averager'>
print(type(a))  # <class '__main__.Averager'>
print(a.add(10))  # 10.0
print(a.add(15))  # 12.5
print(a.add(30))  # 18.333333333333332
print(a.total)  # 55
print(a.count)  # 3
print()


###############################################################################
###############################################################################


# Average returner with functions


def averager():
    print("Creating a new averager function...")
    total = 0
    count = 0

    def inner(x: int):
        nonlocal total, count
        total += x
        count += 1
        return total / count

    return inner


a = averager()  # Creating a new averager function...

# Printing the closure's information:

print(a.__closure__)  # A tuple containing the cell objects:
# (<cell at 0x0000018C882A3670: int object at 0x0000018C87C86910>, <cell at 0x0000018C882A3640: int object at 0x0000018C87C86910>)
print(a.__code__.co_freevars)  # A tuple with the names of the free variables:
# ('count', 'total')
print(a.__code__.co_argcount)  # Number of accepted arguments by the closure:
# 1
print(a.__code__.co_name)  # Name of the returned closure:
# inner
print(a.__code__.co_varnames)  # Tuple with the names of the variables in the closure
# ('x',)


print(a(10))  # 10.0
print(a(15))  # 12.5
print(a(30))  # 18.333333333333332
for i in range(len(a.__closure__)):
    print(f"{a.__code__.co_freevars[i]}: {a.__closure__[i].cell_contents}")
# count: 3
# total: 55
print()
