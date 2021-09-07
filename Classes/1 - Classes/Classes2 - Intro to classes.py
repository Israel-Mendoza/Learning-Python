"""WORKING WITH CLASS ATTRIBUTES"""


class Program:
    # Setting attributed from within the class
    language = "Python"
    version = "3.6"

    @staticmethod
    def say_hello():
        print(f"Hello from {Program.language}")


#######################################################################
#######################################################################

"""CLASS ATTRIBUTES LOCATION"""

# Object dictionary (mappingproxy)
print(type(Program.__dict__))
# <class 'mappingproxy'>

# Iterating through the mappingproxy:
for k in Program.__dict__:
    print(f"{Program.__name__}.{k}: {Program.__dict__[k]}")
# Program.__module__: __main__
# Program.language: Python
# Program.version: 3.8
# Program.say_hello: <staticmethod object at 0x7f474ea1aee0>
# Program.__dict__: <attribute '__dict__' of 'Program' objects>
# Program.__weakref__: <attribute '__weakref__' of 'Program' objects>
# Program.__doc__: None

#######################################################################
#######################################################################

"""ACCESSING CLASS ATTRIBUTES"""

print(Program.language)
# Python
print(Program.version)
# 3.6
print(getattr(Program, "language", None))
# Python
print(getattr(Program, "version", None))
# 3.6

# Accessing attributes that don't exist results in an AttributeError:
try:
    print(f"{Program.operating_system}")
except AttributeError:
    print("We're sorry, but the 'operating_system' attribute doesn't exist\n")
# We're sorry, but the 'operating_system' attribute doesn't exist

# Avoiding the try-except block by using the "getattr" function
if getattr(Program, "operating_system", None):
    print(print(f"{Program.operating_system}"))
else:
    print("We're sorry, but the 'operating_system' attribute doesn't exist\n")
# We're sorry, but the 'operating_system' attribute doesn't exist

#######################################################################
#######################################################################

"""SETTING ATTRIBUTES TO CLASSES"""

Program.version = "3.7"
print(Program.version)
# 3.7
print(getattr(Program, "version", None))
# 3.7

Program.version = "3.8"
print(Program.version)
# 3.8
print(getattr(Program, "version", None))
# 3.8

# Setting inexistent attributes
setattr(Program, "operating_system", "Windows 10")
print(Program.operating_system)
# Windows 10
print(getattr(Program, 'operating_system', None))
# Windows 10


#######################################################################
#######################################################################

"""DELETING ATTRIBUTES TO CLASSES"""

delattr(Program, "operating_system")
for k in Program.__dict__:
    print(f"Program.{k}: {Program.__dict__[k]}")
# Program.__module__: __main__
# Program.language: Python
# Program.version: 3.8
# Program.say_hello: <staticmethod object at 0x7f96f89b6e20>
# Program.__dict__: <attribute '__dict__' of 'Program' objects>
# Program.__weakref__: <attribute '__weakref__' of 'Program' objects>
# Program.__doc__: None

# Retrieving callables from the class' namespace:
a_func = getattr(Program, "say_hello", None)
if a_func:
    a_func()
# Hello from Python
