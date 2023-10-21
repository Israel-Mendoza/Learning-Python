from operator import attrgetter, methodcaller


class MyClass:
    def __init__(self):
        self.a = "A"
        self.b = "B"

    def test(self):
        print(f"Object says hello!")

    def say_hello(self, name):
        print(f"Hello, {name}!")


my_obj = MyClass()

getting_test = attrgetter("test")
print(type(getting_test))  # <class 'operator.attrgetter'> (Callable)
test_gotten = getting_test(my_obj)
print(type(test_gotten))  # <class 'method'>
test_gotten()  # Object says hello!

# We can do this in one line
attrgetter("test")(my_obj)()  # Object says hello!
attrgetter("say_hello")(my_obj)("Israel")  # Hello, Israel!

"""Using methodcaller"""

getting_test = methodcaller("test")
print(type(getting_test))  # <class 'operator.methodcaller'>
getting_test(my_obj)  # Object says hello!

# We can do this in one line
methodcaller("test")(my_obj)  # Object says hello!

"""Using methodcaller with required parameters"""

try:
    methodcaller("say_hello")(my_obj)
except BaseException as error:
    print(f"{type(error).__name__}: {error}")
# TypeError: say_hello() missing 1 required positional argument: 'name'

# methodcaller will ask you to add the arguments
# when creating the methodcaller object:
methodcaller("say_hello", "Israel")(my_obj)  # Hello, Israel!
