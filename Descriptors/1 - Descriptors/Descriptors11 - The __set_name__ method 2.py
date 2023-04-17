from __future__ import annotations

"""Using the __set_name__ method"""


class ValidString:
    def __init__(self, min_length: int = 0, max_length: int = 25) -> None:
        """
        Defines the minimum and maximum length
        of the string we wanto to validate.
        """
        self.min_length: int = min_length
        self.max_length: int = max_length

    def __set_name__(self, owner_class: type, property_name: str) -> None:
        """
        Set name descriptor method.
        Stores the class attribute name in self.property_name.
        """
        self.property_name = property_name

    def __get__(self, instance, owner) -> str | ValidString:
        """
        Descriptor getter method.
        Returns the descriptor if called from the class.
        If called from the instance, it looks for the value
        using the instance's __dict__ attribute; looking it up
        otherwise we would end up in a recursive loop by calling
        the __get__ again.
        """
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def __set__(self, instance: object, value: str) -> None:
        """
        Descriptor setter method.
        Checks if the value is a valid string, as defined by the
        self.check_valid_string method.
        If it is, stores the value in the instance's namespace,
        with the stored property name itself, using the instance's
        __dict__ attribute, otherwise we would end up in a recursive
        loop by calling the __set__ again.
        """
        if self.check_valid_string(value):
            instance.__dict__[self.property_name] = value
        else:
            raise ValueError(
                f"{self.property_name} must be a string between "
                f"{self.min_length} and {self.max_length} characters long!"
            )

    def check_valid_string(self, a_string: str) -> bool:
        if isinstance(a_string, str):
            return self.min_length <= len(a_string) <= self.max_length
        else:
            raise ValueError(f"{self.property_name} must be a valid string!")


class Person:
    # Descriptors are instantiated at compile time
    first_name = ValidString()
    last_name = ValidString()

    def __init__(self, age):
        self.__age = age


p = Person(28)
print(f"{hex(id(p)).upper() = }")
# hex(id(p)).upper() = '0X7FD3885BB190'

p.first_name = "Israel"
p.last_name = "Mendoza"

print(vars(p))
# {'_Person__age': 28, 'first_name': 'Israel', 'last_name': 'Mendoza'}
