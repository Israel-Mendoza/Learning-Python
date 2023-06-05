"""Working with class functions"""


# A function in a class can be called from both,
# the class itself, and an instance of the class.
# When called by the class, it behaves exactly as a regular function.
# When called by the instance, the instance is passed as the first 
# argument:
# instance.function() = class.function(instance)
# instance.function() = instance.function.__func__(instance.function.__self__)


class Person:
    # Defining a class function
    def say_hello():
        print("Hello")


# Analyzing the class
print(f"{hex(id(Person)) = }")
print(f"{Person.say_hello = }\n")
# hex(id(Person)) = '0xecd6b0'
# Person.say_hello = <function Person.say_hello at 0x7fe591004700>

# Creating an instance of Person
p = Person()

# Analyzing the instance:
print(f"{hex(id(p)) = }")
print(f"{p.say_hello = }\n")
# hex(id(p)) = '0x7fe591010fa0'
# p.say_hello = <bound method Person.say_hello of <__main__.Person object at 0x7fe591010fa0>>

# Comparing types of "say_hello" depending on how we're calling it:
print(f"{type(Person.say_hello) = }")
print(f"{type(p.say_hello) = }\n")
# type(Person.say_hello) = <class 'function'>
# type(p.say_hello) = <class 'method'>


# Calling the "say_hello" function from the class
Person.say_hello()
# Hello

# Calling the "say_hello" function from the instance.
# Python calls the function as: Person.say_hello(p)
try:
    p.say_hello()
except TypeError as error:
    print(f"{error = }")
# say_hello() takes 0 positional arguments but 1 was given


"""Fixing the TypeError when calling the 'say_hello' from an instance"""


class Person:
    # Defininf an instance method
    def say_hello(*args):
        print(f"Passed arguments to say_hello: {args}")


p = Person()
print(f"{hex(id(p)).upper() = }\n")
# hex(id(p)).upper() = '0X7FE591010F70'

# Trying to call the method again:
p.say_hello()
# Passed arguments to say_hello: (<__main__.Person object at 0x7fe591010f70>,)


"""Working with instance methods"""


class Person:
    def set_name(self, new_name):
        self.name = new_name


p = Person()
p.set_name("Israel")
print(f"{p.__dict__ = }")
# p.__dict__ = {'name': 'Israel'}


"""Working with the method's attributes"""

# Among others, the method contains two important attributes:
# __func__: The function as defined by the class
# __self__: The class instance the method is bound to

print(f"{p.set_name.__func__ = }")
# p.set_name.__func__ = <function Person.set_name at 0x7fe591004820>
print(f"{p.set_name.__self__ = }")
# p.set_name.__self__ = <__main__.Person object at 0x7fe591010fa0>


# Calling the method the way Python does it under the hood
p.set_name.__func__(p.set_name.__self__, "Arturo")

# Checking the namespace one last time:
print(f"{p.__dict__ = }\n")
# p.__dict__ = {'name': 'Arturo'}
