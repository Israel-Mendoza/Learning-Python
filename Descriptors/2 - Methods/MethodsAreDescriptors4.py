from types import FunctionType
from typing import Any, NamedTuple


class MyClassMethod:

    def __init__(self, a_func: FunctionType) -> None:
        self.wrapped_function = a_func

    def __get__(self, instance, owner) -> Any:
        """__get__ method which will return self.__call__"""
        if instance is None:
            self.owner = owner
        else:
            self.owner = instance.__class__
        return self.__call__
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        When called, passing the self.owner as the first argument,
        then all *args and **kwargs to the function stored in
        self.wrapped_function.
        Returns the result of the called function.
        """
        return self.wrapped_function(self.owner, *args, **kwds)


class MyStaticMethod:

    def __init__(self, a_func: FunctionType) -> None:
        self.wrapped_function = a_func

    def __get__(self, instance, owner) -> Any:
        return self.__call__

    def __call__(self, *args, **kwargs) -> Any:
        """
        When called, all *args and **kwargs to the function stored in
        self.wrapped_function. Returns the result of the called function.
        """
        return self.wrapped_function(*args, **kwargs)



class Person:

    def __init__(self, name: str) -> None:
        self.name = name

    @MyClassMethod
    def say_hello(cls, name, times):
        return f"{cls.__name__} says hi to {name} {times} times!"

    @MyStaticMethod
    def say_hi():
        return f"I just wanna say hi!"


class Student(Person):
    pass


p = Person("Israel")
s = Student("Israel")
print(Person.say_hello("Mago", 1000))
print(p.say_hello("Mago", 1000))
print(Person.say_hi())
print(p.say_hi())
print()
print(Student.say_hello("Mago", 1000))
print(s.say_hello("Mago", 1000))
print(Student.say_hi())
print(s.say_hi())