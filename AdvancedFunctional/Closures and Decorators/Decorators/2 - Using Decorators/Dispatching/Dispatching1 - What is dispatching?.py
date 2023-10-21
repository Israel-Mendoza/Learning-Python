"""Making a use case for dispatching - Part 1"""

from typing import Any
from html import escape
from collections.abc import Sequence, Mapping

"""Creating functions that will be then dispatch by another function"""


def html_escape(arg: Any):
    """
    Arg:
        arg (Any): Any object to be formatted as valid HTML code.
    Return:
        A string, HTML-ready.
    """
    return escape(str(arg))


def html_str(arg: str) -> str:
    """
    Returns a string formated so it can
    be used as HTML code.
    """
    return html_escape(arg).replace("\n", "<br/>\n")


def html_int(arg: int) -> str:
    """
    Returns a string containing the int and it's
    hex representation.
    """
    return f"{arg} ({hex(arg)})"


def html_sequence(arg: Sequence[Any]) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag and a new line (\\n).
    The string is wrapped in a <ul></ul>
    """
    arg = (f"\t<li>{html_format(item)}</li>" for item in arg)
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


def html_mapping(arg: Mapping[Any, Any]) -> str:
    """
    Returns a string where each key-value pair
    is wrapped in a <li></li> tag and a new line(\\n).
    The string is wrapped by <ul></ul>.
    """
    arg = (f"\t<li>{k}: {html_format(v)}</li>" for k, v in arg.items())
    arg = "\n".join(arg)
    return f"<ul>\n{arg}\n</ul>"


def html_float(arg: float) -> str:
    """
    Returns a string containing the float
    formated to contain 2 decimals.
    """
    return f"{arg:.2f}"


"""Creating a dispatch function using if else statements"""


def html_format(arg: Any) -> str:
    """
    Dispatcher function:
    Cons:
        Awful code full of if-else statements.
        Hard coded logic.
        Difficult to modify from the outside.
    """
    if isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float):
        return html_float(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_sequence(arg)
    elif isinstance(arg, dict):
        return html_mapping(arg)
    else:
        return html_escape(arg)


a = [
    """Company:
    Steinway & Sons
    """,
    (1, 2, 3),
    100,
    {"uno": "un", "dos": "deux", "tres": "trois"},
]

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
# 	<li>uno: un</li>
# 	<li>dos: deux</li>
# 	<li>tres: trois</li>
# </ul></li>
# </ul>
