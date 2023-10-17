"""Monkeypatching"""

# Python allows us to monkeypatch our objects on the fly.
# Our classes might be declared, but we can still add 
# functions/methods to them by adding these new pieces of code 
# to the class' namespace.


class Person:
    """A class that only has one simple method"""
    def say_hello(self):
        """Prints a greeting, coming from the Person instance"""
        print(f"{self} instance says hello!")


# Creating two instances of the Person class
p1: Person = Person()
p2: Person = Person()

# Calling the methods on the two recently created instances:
p1.say_hello()
# <__main__.Person object at 0x7f165c01ffd0> instance says hello!
p2.say_hello()
# <__main__.Person object at 0x7f165c01ffa0> instance says hello!

# Checking the Person's namespace:
for k in Person.__dict__:
    print(f"Person.{k}: {Person.__dict__[k]}")
# Person.__module__: __main__
# Person.say_hello: <function Person.say_hello at 0x7f435cf95790>
# Person.__dict__: <attribute '__dict__' of 'Person' objects>
# Person.__weakref__: <attribute '__weakref__' of 'Person' objects>
# Person.__doc__: None

"""Adding a instance method to the class on the fly"""


def do_work(self):
    return f"{self} is working"


setattr(Person, "do_work", do_work)

# Checking the Person's namespace:
for k in Person.__dict__:
    print(f"Person.{k}: {Person.__dict__[k]}")
# .
# .
# .
# Person.do_work: <function do_work at 0x1048942c0>

# Calling the new method on both instances:
print(f"{p1.do_work = }")
# p1.do_work = <bound method do_work of <__main__.Person object at 0x7f8aa335bfd0>>
print(p1.do_work())
# <__main__.Person object at 0x7f8aa335bfd0> is working! 
print(f"{p2.do_work = }")
# p2.do_work = <bound method do_work of <__main__.Person object at 0x7f8aa335bfa0>>
print(p2.do_work())
# <__main__.Person object at 0x7f8aa335bfa0> is working! 


"""Adding a function to an instance on the fly:"""


setattr(p1, "other_func", lambda *args: f"Other function with args: {args}")

# Checking the type of the recently add function:
print(f"{type(p1.other_func) = }")
# type(p1.other_func) = <class 'function'> // This is not a method!

print(p1.other_func())  # No self argument is passed
# Other function with args: ()

class Person:
    pass


def a_func(*args) -> None:
    print("Passed arguments", args)


p: Person = Person()

setattr(Person, "class_func", a_func)
setattr(p, "instance_func", a_func)

print(type(p.class_func))
print(type(p.instance_func))