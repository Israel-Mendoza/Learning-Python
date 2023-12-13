from typing import Callable


"""What is a closure?"""


def outer() -> Callable[[], None]:
    x: str = "Python"
    y: str = "Java"

    def inner():
        # "x" and "y" are free variables because they were not defined locally
        print(f'My languages: "{x}" and "{y}"')

    return inner


fn: Callable[[], None] = outer()  # Assigning the closure to a variable

# Printing the closure information:
print(fn.__code__.co_freevars)  # A tuple[str, ...] with the names of the free variables
# ('x', 'y')

print(fn.__closure__)  # A tuple[<class 'cell'>, ...] containing the free variables
# (<cell at 0x000001C768CB2FD0: str object at 0x000001C768C59DF0>,
#  <cell at 0x000001C768CB2FA0: str object at 0x000001C768C668F0>)

print(fn.__code__.co_argcount)  # Number of accepted arguments by the closure
# 0
print(fn.__code__.co_name)  # Name of the returned closure:
# inner
print(fn.__code__.co_varnames)  # A tuple[str, ...] with the names of the variables in the closure
# ()

# Accessing the contents of the free variables:
for i in range(len(fn.__closure__)):
    print(f"{fn.__code__.co_freevars[i]}: {fn.__closure__[i].cell_contents}")
# x: Python
# y: Java

fn()
# My languages: "Python" and "Java"
