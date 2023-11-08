from __future__ import annotations
from enum import Enum


"""Creating enumerations"""

"""
    Enumerations are classes that inherit from enum.Enum
    
    Things to know about theses:
        
        1. The type of the enumeration member is the class
"""


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"


class Vector(Enum):
    V1D = (1, )
    V2D = (1, 1)
    V3D = (1, 1, 1)


# Printing the enumeration members
print(Color.RED)
# Color.RED

# The type of the enumeration member is the same as the class
print(type(Color))
# <class 'enum.EnumType'>
print(type(Color.RED))
# <enum 'Color'>
print(isinstance(Color.RED, Color))
# True

# Playing with the member's properties
print(Color.RED.name, type(Color.RED.name))  # RED <class 'str'>
print(Status.PENDING.name, type(Status.PENDING.name))  # PENDING <class 'str'>
print(Vector.V3D.name, type(Vector.V3D.name))  # V3D <class 'str'>

print(Color.RED.value, type(Color.RED.value))  # 1 <class 'int'>
print(Status.PENDING.value, type(Status.PENDING.value))  # pending <class 'str'>
print(Vector.V3D.value, type(Vector.V3D.value))  # (1, 1, 1) <class 'tuple'>


"""When testing equality of a value and an enum member, always use 'is'..."""

a: Color = Color.BLUE

if a is Color.BLUE:
    print("Sacré bleu!")
else:
    print("I don't know what color it is...")
# Sacré bleu!


"""We cannot use comparators with enum members"""

try:
    print(Color.RED < Color.BLUE)
except TypeError as err:
    print(f"{err.__class__.__name__}: {err}")
# TypeError: '<' not supported between instances of 'Color' and 'Color'


"""We can test if a member exist in an enum using the member. Always use the member object!!!"""

print(f"{Status.PENDING in Status = }")  # <-- This is what we should be using!
# Status.PENDING in Status = True
print(f"{'pending' in Status = }")  # <-- Pre-Python 3.12 would return False
# 'pending' in Status = True
print(f"{1 in Color = }")  # <-- Pre-Python 3.12 would return False
# 1 in Color = True


# TODO: Enums are callables and we can pass the value

print(Color(1))
