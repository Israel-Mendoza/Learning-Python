"""Using the singledispatch decorator from the functools module"""

"""
Important methods and properties in a singledispatch object:
    register(a_type): Adds a type and a function to the registry mapping proxy
    registry: Property containing the mapping proxy
    dispatch(a_type): Returns the function linked to the passed type
"""

from typing import Any
from html import escape
from numbers import Integral
from functools import singledispatch
from collections.abc import Sequence


# Defining the default function to be called
# in case no type is found in the registry
@singledispatch
def htmlize(a: Any) -> str:
    """Returns a valid html string"""
    return escape(str(a))


# Using the "register" decorator factory 
# to add a new function to the registry MappingProxy
# Integral will be the type html_integral will be bound to.
@htmlize.register(Integral)
def html_integral(a: Integral) -> str:
    return f"{a}: {hex(a).upper()}"


# Using the "register" decorator factory 
# to add a new function to the registry MappingProxy
# Sequence will be the type html_sequence will be bound to.
@htmlize.register(Sequence)
def html_sequence(arg: Sequence) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{htmlize(item)}</li>" for item in arg)
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


"""ANALIZING THE "HTMLIZE" DECORATED FUNCTION"""

# The mapping proxy holding the functions 
# and their types is found under the "registry" property:
print(type(htmlize.registry))
# <class 'mappingproxy'>

# What's in the registry dictionary?
print(htmlize.registry)
# {
#   <class 'object'>: <function htmlize at 0x7feb03b39670>, 
#   <class 'numbers.Integral'>: <function html_integral at 0x7feb03a22280>, 
#   <class 'collections.abc.Sequence'>: <function html_sequence at 0x7feb03a22310>
# }

# What function will you use if I give you a string?
print(htmlize.dispatch(str))
# <<function html_sequence at 0x7feb03a22310>

# What function will you use if I give you a boolean?
print(htmlize.dispatch(bool))
# <function html_integral at 0x7feb03a22280>


"""Using decorated function"""

try:
    print(htmlize("1 < 10"))
except RecursionError as ex:
    print(f"{type(ex).__name__}: {ex}")
# RecursionError: maximum recursion depth exceeded while calling a Python object

# As no function for the type str has been registered, the function called will
# be that of the Sequence type, which calls htmlize for each item.
# Because each item of the string is also a string, htmlize will also be
# be called for that Sequence type. Thus, a RecursionError is raised.


# Implementing a function for the string type
@htmlize.register(str)
def html_str(arg: str) -> str:
    """
    Returns a string formated so it can
    be used as html code.
    """
    return escape(arg).replace("\n", "<br/>\n")


try:
    print(htmlize("1 < 10"))
except RecursionError as ex:
    print(f"{type(ex).__name__}: {ex}")
# 1 &lt; 10
