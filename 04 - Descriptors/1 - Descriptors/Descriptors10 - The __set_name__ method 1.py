from __future__ import annotations

"""Using the __set_name__ method"""

# The __set_name__ is run just after __init__ and allows us
# to keep track of the class and the attribute name it's
# assigned to.
# This is useful when using the __set__ method in order
# to use the instance itself to store the value.


class ValidString:
    def __init__(self, min_length: int = 0, max_length: int = 25) -> None:
        """
        Defines the minimum and maximum length
        of the string we wanto to validate.
        """
        self.min_length: int = min_length
        self.max_length: int = max_length

    def __set_name__(self, owner: type, property_name: str) -> None:
        """
        Set name descriptor method.
        Stores the class attribute name in self.property_name,
        and the attribute name the instance will use to store
        the value, which will simulate a private attribute name.
        """
        print(f"__set_name__({owner = }, {property_name = }) ")
        self.property_name: str = property_name
        self.instance_attribute_name: str = f"_{owner.__name__}__{property_name}"

    def __get__(self, instance: object, owner: type):
        """
        Returns the descriptor if called from the class,
        or the value assigned to the instance attribute,
        if called from the instance.
        """
        if instance is None:
            return self
        return getattr(instance, self.instance_attribute_name)

    def __set__(self, instance: object, value: str):
        """
        Checks if the value is a valid string, as defined by the
        self.check_valid_string method.
        If it is, stores the value in the instance's namespace,
        with the attribute name stored in self.instance_attribute_name
        """
        if self.check_valid_string(value):
            setattr(instance, self.instance_attribute_name, value)
        else:
            raise ValueError(
                f"{self.property_name} must be a string between "
                f"{self.min_length} and {self.max_length} characters long!"
            )

    def check_valid_string(self, a_string: str):
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


# __set_name__(owner = <class '__main__.Person'>, property_name = 'first_name')
# __set_name__(owner = <class '__main__.Person'>, property_name = 'last_name')


p = Person(28)
print(f"{hex(id(p)).upper() = }")
# hex(id(p)).upper() = '0X10477F490'

p.first_name = "Israel"
p.last_name = "Mendoza"
print(vars(p))
# {'_Person__age': 28, '_Person__first_name': 'Israel', '_Person__last_name': 'Mendoza'}
