"""Introducing decorators for dispatching - Part 2"""

from typing import Any
from html import escape
from collections.abc import Callable


def single_dispatch(a_func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Single dispatch decorator used with a function that
    takes 1 parameter.
    That function will be stored in the registry dictionary
    as the default function to be call when an object type
    instance is passed as arg to the returned closure.
    Cons:
        Unable to inject external functions.
    """
    registry = {}
    registry[object] = a_func
    registry[int] = lambda a: f"{a} ({hex(a)})"
    registry[str] = lambda a: escape(a).replace("\n", "<br/>\n")

    def inner(arg: Any):
        """
        Dispatching the function from the free variable dictionary 
        'registry' based on the passed argument's type (arg's type)
        """
        dispatched_function = registry.get(type(arg), registry[object])
        return dispatched_function(arg)

    return inner


"""Declaring a function"""


@single_dispatch
def htmlize(arg: Any) -> str:
    return escape(str(arg))


print(htmlize("AT&T"))
# AT&amp;T  // Str was hardcoded in decorator
print(htmlize(10))
# 10 (0xa)  // Int was hardcoded in decorator
print(htmlize([1, 2, 3]))
# [1, 2, 3] // list type was not hardcoded in decorator
