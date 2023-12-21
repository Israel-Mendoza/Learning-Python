from functools import partial


def my_func(a: str, b: str, *args: str, k1: int, k2: int, **kwargs: int) -> None:
    print(f"Required positional arguments: a='{a}', b='{b}'")
    print(f"Extra positional arguments: args={args}")
    print(f"Keyword arguments: k1={k1}, k2={k2}")
    print(f"Extra keyword arguments: kwargs={kwargs}")


my_func("A", "B", "C", "D", "E", k1=1, k2=2, k3=3, k4=4)
# Required positional arguments: a='A', b='B'
# Extra positional arguments: args=('C', 'D', 'E')
# Keyword arguments: k1=1, k2=2
# Extra keyword arguments: kwargs={'k3': 3, 'k4': 4}


"""Using partial to have predetermined values"""

# We want to have a and k1 as defaults
my_partial = partial(my_func, "Alpha", k1=1000)
my_partial("B", "C", "D", "E", k2=2, k3=3, k4=4)
# Required positional arguments: a='Alpha', b='B'
# Extra positional arguments: args=('C', 'D', 'E')
# Keyword arguments: k1=1000, k2=2
# Extra keyword arguments: kwargs={'k3': 3, 'k4': 4}

# Specifying other positional arguments other than the first one


def power[T: (int, float)](base: T, exponent: T) -> T:
    """Returns the base elevated to the exponent"""
    return base ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))  # 125

# Overriding named variables saved by the partial
print(square(5, exponent=3))  # 125
print(cube(5, exponent=2))  # 25
