from __future__ import annotations
from typing import Any
from math import pi

"""
What does Python do when we declare a new class?
    1. The class body code is extracted.
    2. A new dictionary is created, which will be 
       the namespace of the new class.
    3. The extracted code will be run against the
       namespace dictionary, populating it.
    4. A new type instance is created using the name
       of the class, the base classes (in a tuple),
       and the recently populated dictionary.
"""

###################################################
# How to run code in a given namespace dictionary #
###################################################


# First, let's learn how to run code against a given namespace dictionary:
# exec() takes code (str or bytes), and executes it in
# a given namespace, filling out the namespace dictionary.

# Empty namespace dictionary
namespace1: dict[str, Any] = {}
namespace2: dict[str, Any] = {}

# Executing code into the namespace1 dictionary
exec(
    """
a = 10
b = 20

def __init__(self):
    pass
""",
    globals(),
    namespace1,
)

# Populated namespace1 dictionary
print(namespace1)
# {
# 'a': 10,
# 'b': 20,
# '__init__': <function __init__ at 0x1D82C979F70>
# }

# Executing code into the namespace2 dictionary
exec(
    """
def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y
""",
    globals(),
    namespace2,
)

# Populated namespace2 dictionary
print(namespace2)
# {
# 'add': <function add at 0x00000293DB1030D0>,
# 'sub': <function sub at 0x00000293DB103160>
# }

# All the run code was encapsulated into its own namespace,
# and it does not exist in the global scope:
print("a" in globals())  # False
print("b" in globals())  # False
print("add" in globals())  # False
print("sub" in globals())  # False


#####################################################################
# Creating the class body code to manually insert it to a namespace #
# We will use type(name, bases, namespace) to create the new type:  #
#   name (str) = The name of the class                              #
#   bases (tuple[type]) = The classes our class inherits from       #
#   namespace (dict[str, Any])  = The symbols and their objects     #
#####################################################################


"""Creating the contents of our new class"""


class_name: str = "Circle"
class_bases: tuple = ()  # A tuple containing the classes we'll inherit from. "object" will be inferred
class_namespace: dict[str, Any] = {}  # namespace to be populated
class_body: str = """
def __init__(self, radius: int | float) -> None:
        self.radius = radius

def area(self) -> float:
    return pi * self.radius ** 2
"""
# Populating the new class namespace
exec(class_body, globals(), class_namespace)

# Confirming the namespace is populated now
print(class_namespace)
# {
# '__init__': <function __init__ at 0x249F3723790>,
# 'area': <function area at 0x249F3723820>
# }

"""CREATING OUR OWN CLASS USING THE TYPE CLASS"""

"""
    When creating a new class using "type", type, being a type instance,  
    calls its __prepare__ static method to get the initial namespace      
    dictionary, which will then be populated with the code of the class   
    before being passed to the type.__call__ method. 
                         
    The type.__call__ implements two calls:                               
        1. type.__new__                                                     
        2. type.__init__        
                                                    
    The type.__call__ method will then return the recently created type 
    returned by the type.__new__ method.                                 
"""

Circle = type(class_name, class_bases, class_namespace)

# Circle is a type:
print(type(Circle))  # <class 'type'>

# Calling help on Circle
help(Circle)
# Help on class Circle in module __main__:

# class Circle(builtins.object)
#  |  Circle(radius: int | float) -> None
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, radius: Union[int, float]) -> None
#  |
#  |  area(self) -> float
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)

# Circle has a __dict__
print(Circle.__dict__)
# {'__init__': <function __init__ at 0x0000015CFD745700>,
# 'area': <function area at 0x0000015CFD745790>,
# '__module__': '__main__',
# '__dict__': <attribute '__dict__' of 'Circle' objects>,
# '__weakref__': <attribute '__weakref__' of 'Circle' objects>,
# '__doc__': None}

# Class name was taken as the first parameter in type()
print(Circle.__name__)  # Circle

"""Creating a Circle instance"""

c1 = Circle(10)
print(type(c1))  # <class '__main__.Circle'>
print(c1.__dict__)  # {'radius': 10}
print(c1.area())  # 314.1592653589793
