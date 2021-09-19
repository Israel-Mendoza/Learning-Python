"""Methods (and functions) are non-data descriptors"""

# Method objects also implement the __get__ method.
# We'll see how to get the return value of
# a method's __get__ method in this file.


class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"{self.name} says hello!"


p = Person("Israel")

# Getting the return value from the __get__ method.
# Remember that the __get__ method must be passed
# two arguments: the instance and the owner class:

# Getting the FunctionType by calling the __get__
# using None as the instance, and Person as the owner:
a_function = Person.say_hello.__get__(None, Person)
# Getting the MethodType by accessing the __get__
# using p as the instance, and Person as the owner:
a_method = Person.say_hello.__get__(p, Person)

print(Person.say_hello, a_function)
# <function Person.say_hello at 0x7f5a153ec790> 
# <function Person.say_hello at 0x7f5a153ec790>
print(p.say_hello, a_method)
# <bound method Person.say_hello of <__main__.Person object at 0x7f0759c42fd0>> 
# <bound method Person.say_hello of <__main__.Person object at 0x7f0759c42fd0>>

# Furthermore, a MethodType object 
# stores the function under __func__:
print(p.say_hello.__func__)
# <function Person.say_hello at 0x7f5a153ec790> 
print(f"{p.say_hello.__func__ is Person.say_hello = }")
# p.say_hello.__func__ is Person.say_hello = True
