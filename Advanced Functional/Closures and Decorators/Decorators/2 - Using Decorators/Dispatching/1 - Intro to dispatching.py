import html
from typing import Any, Sequence

"""Making a use case for dispatching - Part 1"""

"""Creating functions that will be then dispatched by another function"""


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


def html_sequence_v2(arg: Sequence[Any]) -> str:
    """
    Returns a string where each item is wrapped in a
    <li></li> tag and a new line (\\n).
    The string is wrapped in a <ul></ul>
    """
    arg: str = "\n".join((f"\t<li>{html_format_v2(item)}</li>" for item in arg))
    return f"<ul>\n{arg}\n</ul>"


def html_mapping_v2(arg: dict[Any, Any]) -> str:
    """
    Returns a string where each key-value pair
    is wrapped in a <li></li> tag and a new line(\\n).
    The string is wrapped by <ul></ul>.
    """
    arg: str = "\n".join((f"\t<li>{k}: {html_format_v2(v)}</li>" for k, v in arg.items()))
    return f"<ul>\n{arg}\n</ul>"




"""Creating a dispatch function using if else statements"""


def html_format(arg: Any) -> str:
    """
    Dispatcher function:
    Pros:
        Cleaner than the convoluted type-checking
        logic using the isinstance() function.
    Cons:
        Still ugly code.
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


def html_format_v2(arg: Any) -> str:
    """
        Dispatcher function:
        Cons:
            Awful code full of if-else statements.
            Hard coded logic.
            Difficult to modify from the outside.
    """
    match arg:
        case str(arg):
            return html_str(arg)
        case int(arg):
            return html_int(arg)
        case float(arg):
            return html_float(arg)
        case list(arg) | tuple(arg):
            return html_sequence_v2(arg)
        case dict(args):
            return html_mapping_v2(arg)
        case _:
            return html_escape(arg)


a: tuple[str, tuple[int, int, int], int, dict[str, str]] = (
    """Company:
    Steinway & Sons
    """,
    (1, 2, 3),
    100,
    {"uno": "un", "dos": "deux", "tres": "trois"},
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
# 	<li>uno: un</li>
# 	<li>dos: deux</li>
# 	<li>tres: trois</li>
# </ul></li>
# </ul>

print(html_format_v2(a))
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

one: str = html_format(a)
two: str = html_format_v2(a)
print(one == two)