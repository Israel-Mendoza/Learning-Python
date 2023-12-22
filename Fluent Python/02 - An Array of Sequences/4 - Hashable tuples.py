"""
    In order for a tuple to be hashable, it must NOT contain mutable elements.

    When the tuple does not contain mutable elements, it is fixed and hashable.

    We'll create a custom function to test whether a tuple is fixed or not.
"""


def fixed(t: tuple) -> bool:
    try:
        hash(t)
        return True
    except TypeError:
        return False


fixed_tuple: tuple[str, int, tuple[int, int]] = ("Israel", 31, (1, 2))
unfixed_tuple: tuple[str, int, list[int]] = ("Israel", 31, [1, 2])

print(fixed(fixed_tuple))
# True
print(fixed(unfixed_tuple))
# False
