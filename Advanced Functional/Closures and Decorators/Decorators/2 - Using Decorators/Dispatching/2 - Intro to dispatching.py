from typing import Any, Sequence, Mapping, Callable
import html
# from collections.abc import Sequence, Mapping

"""Making a use case for dispatching - Part 2"""

"""Creating functions that will be then dispatch by another function"""


def html_escape(arg: Any) -> str:
    """
    Arg:
        arg (Any): Any object to be formatted as valid HTML code.
    Return:
        A string, HTML-ready.
    """
    return html.escape(str(arg))


def html_str(arg: str) -> str:
    """Returns a formatted string which can be used as HTML code."""
    return html_escape(arg).replace("\n", "<br/>\n")


def html_int(arg: int) -> str:
    """Returns a string containing the int in hex representation."""
    return f"{arg} ({hex(arg)})"


def html_float(arg: float) -> str:
    """
    Returns a string containing the float
    formatted to contain 2 decimals.
    """
    return f"{arg:.2f}"


def html_sequence(arg: Sequence[Any]) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag and a new line (\\n).
    The string is wrapped in a <ul></ul>
    """
    arg: str = "\n".join((f"\t<li>{html_format(item)}</li>" for item in arg))
    return f"<ul>\n{arg}\n</ul>"


def html_mapping(arg: dict[Any, Any]) -> str:
    """
    Returns a string where each key-value pair
    is wrapped in a <li></li> tag and a new line(\\n).
    The string is wrapped by <ul></ul>.
    """
    arg: str = "\n".join((f"\t<li>{k}: {html_format(v)}</li>" for k, v in arg.items()))
    return f"<ul>\n{arg}\n</ul>"


"""Creating a dispatch function using a registry dictionary"""


def html_format(arg: Any) -> str:
    """
    Dispatcher function:
    Cons:
        Hard coded registry, difficult to modify from the outside.
    """
    registry: dict[type, Callable[[Any], str]] = {
        object: html_escape,
        str: html_str,
        int: html_int,
        float: html_float,
        list: html_sequence,
        tuple: html_sequence,
        dict: html_mapping,
    }

    return registry.get(type(arg), registry[object])(arg)


a: tuple[str, tuple[int, int, int], int, dict[str, str]] = (
    """Company:
    Steinway & Sons
    """,
    (1, 2, 3),
    100,
    {"uno": "eins", "dos": "zwei", "tres": "drei"},
)

print(html_format(a))
# <ul>
# 	<li>Company:<br/>
#     Steinway &amp; Sons<br/>
#     </li>
# 	<li><ul>
# 	<li>1 (0x1)</li>
# 	<li>2 (0x2)</li>
# 	<li>3 (0x3)</li>
# </ul></li>
# 	<li>100 (0x64)</li>
# 	<li><ul>
# 	<li>uno: eins</li>
# 	<li>dos: zwei</li>
# 	<li>tres: drei</li>
# </ul></li>
# </ul>
