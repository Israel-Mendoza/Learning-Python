from types import MethodType


def say_hello(this, message):
    print(f"{this.name} says {message}!")


class FuncDescriptor:

    def __init__(self, a_func):
        self.a_func = a_func

    def __set_name__(self, cls, name):
        self.name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self.a_func
        return MethodType(self.a_func, obj)


class Person:

    say_somethig = FuncDescriptor(say_hello)

    def __init__(self, name):
        self.name = name


p = Person("Israel")
p.say_somethig("Fuck you")
