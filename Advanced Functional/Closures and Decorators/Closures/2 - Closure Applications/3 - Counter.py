from collections.abc import Callable


"""CREATING A COUNTER USING A CLOSURE"""


def counter(initial_value: int) -> Callable[[int], int]:
    """
    Returns a closure function that,
    when called, will return a integer,
    which will increment each time the closure is called
    """
    def inner(increment: int = 1):
        # Telling Python initial_value is to be braught into this scope from the enclosing scope.
        # Otherwise, line 16 would through an error saying that initial_value hasn't been declared:
        nonlocal initial_value
        initial_value += increment
        return initial_value

    return inner


c1 = counter(0)

print(c1.__closure__)
# (<cell at 0x000001F39E762FD0: int object at 0x000001F39E4A6910>,)
print(c1.__code__.co_freevars)
# ('initial_value',) -- a tuple with the names of the free variables
print(c1())  # 1
print(c1())  # 2
print(c1(10))  # 12
