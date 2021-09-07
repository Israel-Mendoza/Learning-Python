""""""


from typing import Any


class Descriptor:

    def __init__(self, descriptor_value: Any) -> None:
        """
        Initializing the value the Descriptor's 
        instance will hold and return.
        """
        self.value = descriptor_value

    def __get__(self, instance, owner) -> Any:
        """Returns self.value, no mather who calls the descriptor"""
        return self.value

    def __set__(self, instance: Any, value: Any) -> None:
        """
        Prints the instance, the passed value, and
        sets the "value" attribute with the passed value
        """
        print(f"Instance: {instance}")
        print(f"Value: {value}")
        instance.value = value


class Person:

    eye_color = Descriptor("Brown")

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Israel Mendoza", 25)

# Initial Person class' __dict__
for k, v in vars(Person).items():
    print(f"{k:12} - {v}")
print()
# __module__   - __main__
# eye_color    - <__main__.Descriptor object at 0x0167F5C8>
# __init__     - <function Person.__init__ at 0x034B0190>
# __dict__     - <attribute '__dict__' of 'Person' objects>
# __weakref__  - <attribute '__weakref__' of 'Person' objects>
# __doc__      - None

# Overriding the "eye_color" class attribute with a string
# Remember that the __set__ descriptor method will only be called
# when accesed by a class instance, not a class.
Person.eye_color = "Blue"

# Final Person class' __dict__
print("FINAL PERSON NAMESPACE: ")
for k, v in vars(Person).items():
    print(f"{k:12} - {v}")
# __module__   - __main__
# eye_color    - Blue
# __init__     - <function Person.__init__ at 0x03510190>
# __dict__     - <attribute '__dict__' of 'Person' objects>
# __weakref__  - <attribute '__weakref__' of 'Person' objects>
# __doc__      - None