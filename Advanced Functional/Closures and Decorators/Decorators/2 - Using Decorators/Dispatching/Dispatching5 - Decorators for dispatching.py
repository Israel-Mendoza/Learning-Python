"""Creating a simple dispathing decorator"""

from typing import Any
from html import escape
from functools import wraps
from collections.abc import Callable


def single_dispatch(a_func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """
    Single dispatch decorator used with a function that takes 1 parameter.
    That function will be stored in the registry dictionary
    as the default function to be call when an object type
    instance is passed as arg to the returned closure.
    Cons:
        When the decorated function is invoked, the function is looked up
        in the registry dictionary based in the type of the passed argument,
        ignoring parent classes.
        i.e. bool won't return the function in the int entry.
    """
    registry = {}
    registry[object] = a_func

    @wraps(a_func)
    def decorated_function(arg: Any) -> Any:
        """
        Wrapper function.
        Dispatching the function from the free variable dictionary 
        'registry' based on the passed argument's type (arg's type)
        """
        dispatched_function = registry.get(type(arg), registry[object])
        return dispatched_function(arg)

    """
    Implementing a parameterized decorator to add types and
    their respective functions to the registry dictionary
    """

    def func_adder(type_: type) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
        """
        Decorator factory.
        Uses the passed type as the key in the registry dictionary.
        """

        def _func_adder(a_func: Callable[[Any], Any]) -> Callable[[Any], Any]:
            """
            When called by the decorator factory, _func_adder
            will add/update an entry in the registry dictionary,
            where the type passed to the decorator factory is the key,
            and the passed function, the value.
            Returns the passed function as it is.
            """
            registry[type_] = a_func
            return a_func

        return _func_adder

    """Implementing an accesor to the registry functions based on types"""

    def get_function(type_: type) -> Callable:
        """
        Returns the function associated to the passed type
        from the registry dictionary.
        """
        return registry.get(type_, None)

    # Making the func_adder parameterized decorator
    # available through the decorated function
    decorated_function.add_function = func_adder
    # Making the get_function function available
    # through the decorated function
    decorated_function.get_function = get_function
    # Making the registry dictionary available
    # through the decorated function
    decorated_function._registry = registry

    return decorated_function


@single_dispatch
def htmlize(a: Any) -> str:
    """Returns a valid html string"""
    return escape(str(a))


@htmlize.add_function(int)
def html_int(a: int) -> str:
    return f"{a}: {hex(a).upper()}"


@htmlize.add_function(str)
def html_str(arg: str) -> str:
    """
    Returns a string formated so it can
    be used as html code.
    """
    return escape(arg).replace("\n", "<br/>\n")


@htmlize.add_function(list)
def html_list(arg: list) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag.
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{htmlize(item)}</li>" for item in arg)
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


"""Testing our new dispatching function"""

a = """This is
a fucking
string
"""
b = 100
c = [1, 2, 3]
d = [a, b, c]

print(htmlize(d))
# <ul>
# 	<li>This is<br/>
# a fucking<br/>
# string<br/>
# </li>
# 	<li>100: 0X64</li>
# 	<li><ul>
# 	<li>1: 0X1</li>
# 	<li>2: 0X2</li>
# 	<li>3: 0X3</li>
# </ul></li>
# </ul>

print(htmlize.get_function(type(d)))
# <function html_list at 0x2168522F0D0>

help(htmlize)
# Help on function htmlize in module __main__:

# htmlize(a: Any) -> str
#     Returns a valid html string
