from operator import attrgetter, methodcaller
from typing import Callable


class MyClass:
    def __init__(self) -> None:
        self.a: str = "A"
        self.b: str = "B"

    def test(self) -> None:
        print(f"Object @ {hex(id(self)).upper()} says hello!")

    def say_hello(self, name):
        print(f"Hello, {name}! - Said the object @ {hex(id(self)).upper()}")


my_obj = MyClass()

getting_test: attrgetter = attrgetter("test")
print(type(getting_test))  # <class 'operator.attrgetter'> // This is a Callable
test_gotten: Callable[[MyClass], None] = getting_test(my_obj)
print(type(test_gotten))
# <class 'method'>
test_gotten()
# Object @ 0X10306DF10 says hello!

# We can do this in one line
attrgetter("test")(my_obj)()
# Object @ 0X10306DF10 says hello!
attrgetter("say_hello")(my_obj)("Israel")
# Hello, Israel! - Said the object @ 0X10306DF10

"""Using methodcaller"""

getting_test = methodcaller("test")
print(type(getting_test))
# <class 'operator.methodcaller'>
getting_test(my_obj)
# Object @ 0X10306DF10 says hello!

# We can do this in one line
methodcaller("test")(my_obj)
# Object @ 0X10306DF10 says hello!

"""Using methodcaller with required parameters"""

try:
    methodcaller("say_hello")(my_obj)
except BaseException as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: MyClass.say_hello() missing 1 required positional argument: 'name'

# methodcaller will ask you to add the arguments when creating the methodcaller object:
methodcaller("say_hello", "Israel")(my_obj)
# Hello, Israel! - Said the object @ 0X10306DF10
