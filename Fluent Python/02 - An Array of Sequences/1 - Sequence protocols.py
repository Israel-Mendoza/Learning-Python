from collections import deque
from collections.abc import Sequence, MutableSequence
from array import array

"""CONFIRMING PROTOCOLS"""

sequences: list[type] = [tuple, list, array, str, deque, bytes]


def print_implements_protocol(list_of_types: list[type], protocol: type):
    for type_ in list_of_types:
        print(f"Type '{type_.__name__}' is {"" if issubclass(type_, protocol) else "NOT "}a {protocol.__name__}")


print_implements_protocol(sequences, Sequence)
# Type 'tuple' is a Sequence
# Type 'list' is a Sequence
# Type 'array' is a Sequence
# Type 'str' is a Sequence
# Type 'deque' is a Sequence
# Type 'bytes' is a Sequence

print_implements_protocol(sequences, MutableSequence)
# Type 'tuple' is NOT a MutableSequence
# Type 'list' is a MutableSequence
# Type 'array' is a MutableSequence
# Type 'str' is NOT a MutableSequence
# Type 'deque' is a MutableSequence
# Type 'bytes' is NOT a MutableSequence
