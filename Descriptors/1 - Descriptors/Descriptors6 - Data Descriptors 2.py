from __future__ import annotations


"""Data Desriptors"""


class Descriptor:

    def __init__(self, descriptor_value: str) -> None:
        """
        Initializing the value the Descriptor's 
        instance will hold and return.
        """
        self.value: str = descriptor_value

    def __get__(self, instance: any, owner: type) -> str:
        """Returns self.value, no mather who calls the descriptor"""
        return self.value

    def __set__(self, instance: any, value: str) -> None:
        """
        Prints the instance, the passed value, and
        sets the "value" attribute with the passed value
        """
        print(f"Instance: {instance}")
        print(f"Value: {value}")
        instance.value = value

    def __repr__(self) -> str:
        return f"Descriptor object @ {hex(id(self)).upper()}"


class Person:

    eye_color = Descriptor("Brown")

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        return f"Person {self.name} ({self.age}) @ address {hex(id(self)).upper()}."


p = Person("Israel Mendoza", 31)


# Initial Person class' __dict__
for k, v in vars(Person).items():
    print(f"{k:12} - {v}")
print()
# __module__   - __main__
# eye_color    - Descriptor object @ 0X7FFB59E46DD0             <<<--- DESCRIPTOR!!!
# __init__     - <function Person.__init__ at 0x7f4a462f1260>
# __repr__     - <function Person.__repr__ at 0x7f4a462f1300>
# __dict__     - <attribute '__dict__' of 'Person' objects>
# __weakref__  - <attribute '__weakref__' of 'Person' objects>
# __doc__      - None

# Overriding the "eye_color" class attribute with a string.
# Remember that the __set__ descriptor method will only be called
# when accesed by a class instance, not a class.
Person.eye_color = "Blue"

# Final Person class' __dict__
print("FINAL PERSON NAMESPACE: ")
for k, v in vars(Person).items():
    print(f"{k:12} - {v}")
# __module__   - __main__
# eye_color    - Blue                                       <<<--- DESCRIPTOR NO MORE!
# __init__     - <function Person.__init__ at 0x03510190>
# __dict__     - <attribute '__dict__' of 'Person' objects>
# __weakref__  - <attribute '__weakref__' of 'Person' objects>
# __doc__      - None
