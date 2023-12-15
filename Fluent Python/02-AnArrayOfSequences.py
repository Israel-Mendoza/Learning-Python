from collections import abc, deque
from array import array

"""CONFIRMING PROTOCOLS"""

# SEQUENCE
print(issubclass(tuple, abc.Sequence))  # True
print(issubclass(list, abc.Sequence))  # True
print(issubclass(array, abc.Sequence))  # True
print(issubclass(str, abc.Sequence))  # True
print(issubclass(deque, abc.Sequence))  # True
print(issubclass(bytes, abc.Sequence))  # True
print()

# MUTABLE SEQUENCE
print(issubclass(list, abc.MutableSequence))  # True
print(issubclass(array, abc.MutableSequence))  # True
print(issubclass(deque, abc.MutableSequence))  # True
print(issubclass(str, abc.MutableSequence))  # False
print(issubclass(tuple, abc.MutableSequence))  # False
print(issubclass(bytes, abc.MutableSequence))  # False
print()

