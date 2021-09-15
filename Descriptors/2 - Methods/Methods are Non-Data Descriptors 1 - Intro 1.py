"""Functions (and methods) are non-data descriptors"""

# Function objects implement the __get__ method,
# which makes them non-data descriptors.
# We'll see how to get the return value of
# a function's __get__ method in this file.


import sys


def add(a, b):
    return a + b


# Checking what type of descriptor we have:
print(f"{hasattr(add, '__get__') = }")
# hasattr(add, '__get__') = True
print(f"{hasattr(add, '__set__') = }")
# hasattr(add, '__set__') = False

# Getting my main module into a variable,
# which will act as the owner class once
# we get to call the __get__ method on 'add':
current_module = sys.modules["__main__"]

# Analyzing the module:
print(f"{type(current_module) = }")
# type(current_module) = <class 'module'>

# Getting the return value from the __get__ method.
# Remember that we must pass two arguments to the 
# __get__ method: the instance and the owner class.
# PWe'll pass None as the instance, and current_module
# as the owner class, because we're at module level.
f = add.__get__(None, current_module)

print(f"{add = }")
# add = <function add at 0x7ff50d1ec700>
print(f"{f = }")
# f = <function add at 0x7ff50d1ec700>
print(f"{f is add = }")
# f is add = True
