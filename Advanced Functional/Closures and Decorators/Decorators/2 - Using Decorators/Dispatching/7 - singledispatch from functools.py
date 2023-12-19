from typing import Any
import html
from numbers import Integral
from functools import singledispatch
from collections.abc import Sequence


"""Using the singledispatch decorator from the functools module"""

# Defining the default function to be called
# in case no type is found in the registry
@singledispatch
def htmlize(a: Any) -> str:
    """Returns a valid html string"""
    return html.escape(str(a))


@htmlize.register(Integral)
def _(a: Integral) -> str:
    return f"{a}: {hex(a).upper()}"


@htmlize.register(Sequence)
def _(arg: Sequence) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg: str = "\n".join((f"\t<li>{htmlize(item)}</li>" for item in arg))
    return f"<ul>\n{arg}\n</ul>"


@htmlize.register(str)
def _(arg: str) -> str:
    """Returns a string formatted which can be used as html code."""
    return html.escape(arg).replace("\n", "<br/>\n")


"""ANALYZING THE "HTMLIZE" DECORATED FUNCTION"""

# Python doesn't care about the name of the wrapped functions.
# It only looks at the address where these functions live.
# Remember that names are only labels.

# What's in the registry dictionary?
print(htmlize.registry)
# {
#   <class 'object'>: <function htmlize at 0x7facefc17670>, 
#   <class 'numbers.Integral'>: <function _ at 0x7facefb00280>, 
#   <class 'collections.abc.Sequence'>: <function _ at 0x7facefb00310>, 
#   <class 'str'>: <function _ at 0x7facefb003a0>
# }


# What function will you use if I give you a string?
print(htmlize.dispatch(str))
# <function _ at 0x7facefb003a0>

# What function will you use if I give you a boolean?
print(htmlize.dispatch(bool))
# <function _ at 0x7facefb00280> // Notice different address

# What function will you use if I give you a list?
print(htmlize.dispatch(list))
# <function _ at 0x7facefb00310> // Notice different address
