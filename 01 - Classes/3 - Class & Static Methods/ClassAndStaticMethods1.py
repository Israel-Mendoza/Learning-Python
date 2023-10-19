class MyClass:
    def hello() -> None:
        """
        When called from the class:
            It doesn't pass anything as an argument. Runs as expected.
        When called from an instance:
            It passes the instance as the argument. Raises an error.
        Note: we should never declare a method like this!!!
        """
        print("Hello...")

    def instance_hello(self) -> None:
        """
        When called from the class:
            It doesn't pass anything as an argument.
            If we wanted it to run without raising an error,
            we must pass the instance as an argument.
        When called from an instance:
            It passes the instance as the argument. Runs as expected.
        """
        print(f"Hello from {self}")

    @classmethod
    def class_hello(cls) -> None:
        """
        When called from the class:
            It  passes the class as an argument. Runs as expected.
        When called from an instance:
            It  passes the class it was instantiated from as an argument. 
            Runs as expected.
        """
        print(f"Hello from {cls}")

    @staticmethod
    def static_hello() -> None:
        """
        When called from the class:
            It doesn't pass anything as an argument. Runs as expected.
        When called from an instance:
            It doesn't pass anything as an argument. Runs as expected.
        """
        print("Hello statically!")


o: MyClass = MyClass()

##########################################################################
##########################################################################

"""Running the first function in the class"""

MyClass.hello()
# Hello...
try:
    o.hello()
except TypeError as error:
    print(error, end="\n\n")
# hello() takes 0 positional arguments but 1 was given


##########################################################################
##########################################################################

"""Running the second function in the class (instance method)"""

try:
    MyClass.instance_hello()
except TypeError as error:
    print(error)
# instance_hello() missing 1 required positional argument: 'self'

o.instance_hello()
# Hello from <__main__.MyClass object at 0x7fafd149ff70>
print()

##########################################################################
##########################################################################

"""Running the third function in the class (class method)"""

MyClass.class_hello()
# Hello from <class '__main__.MyClass'>
o.class_hello()
# Hello from <class '__main__.MyClass'>
print()

##########################################################################
##########################################################################

"""Running the fourth function in the class (static method)"""

MyClass.static_hello()
# Hello statically!
o.static_hello()
# Hello statically!
print()
