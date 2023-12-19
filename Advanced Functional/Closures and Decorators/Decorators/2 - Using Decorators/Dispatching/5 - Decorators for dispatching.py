import html
from functools import wraps
from typing import Any
from collections.abc import Callable


"""Creating a simple dispatching decorator"""


def single_dispatch(a_func: Callable[[Any], str]) -> Callable[[Any], str]:
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
    registry: dict[type, Callable[[Any], str]] = {object: a_func}

    @wraps(a_func)
    def decorated_function(arg: Any) -> str:
        """
        Wrapper function.
        Dispatching the function from the free variable dictionary 
        'registry' based on the passed argument's type (arg's type)
        """
        dispatched_function: Callable[[Any], str] = registry.get(type(arg), registry[object])
        return dispatched_function(arg)

    """
    Implementing a parameterized decorator to add types and
    their respective functions to the registry dictionary
    """

    def func_adder(type_: type) -> Callable[[Callable[[Any], str]], Callable[[Any], str]]:
        """
        Decorator factory.
        Uses the passed type as the key in the registry dictionary.
        """

        def _func_adder(new_func: Callable[[Any], Any]) -> Callable[[Any], Any]:
            """
            When called by the decorator factory, _func_adder
            will add/update an entry in the registry dictionary,
            where the type passed to the decorator factory is the key,
            and the passed function, the value.
            Returns the passed function as it is.
            """
            registry[type_] = new_func
            return new_func

        return _func_adder

    """Implementing an accessor to the registry functions based on types"""

    def get_function(type_: type) -> Callable[[Any], str] | None:
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
    return html.escape(str(a))


@htmlize.add_function(int)
def html_int(a: int) -> str:
    return f"{a}: {hex(a).upper()}"


@htmlize.add_function(str)
def html_str(arg: str) -> str:
    """
    Returns a string formatted so it can
    be used as html code.
    """
    return html.escape(arg).replace("\n", "<br/>\n")


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

a: str = """This is
a freaking
string
"""
b: int = 100
c: list[int] = [1, 2, 3]
d: list[Any] = [a, b, c]

print(htmlize(d))
# <ul>
# 	<li>This is<br/>
# a freaking<br/>
# string<br/>
# </li>
# 	<li>100: 0X64</li>
# 	<li><ul>
# 	<li>1: 0X1</li>
# 	<li>2: 0X2</li>
# 	<li>3: 0X3</li>
# </ul></li>
# </ul>


print(htmlize.get_function(type(a)))
# <function html_str at 0x100be9a80>
print(htmlize.get_function(type(b)))
# <function html_int at 0x100be99e0>
print(htmlize.get_function(type(c)))
# <function html_list at 0x100be9b20>
print(htmlize.get_function(type(d)))
# <function html_list at 0x100be9b20>

help(htmlize)
# Help on function htmlize in module __main__:
#
# htmlize(a: Any) -> str
#     Returns a valid html string
