from __future__ import annotations

"""Applying descriptors to validate types"""


class IntDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.class_name: str = owner.__name__
        self.attribute_name: str = name

    def __get__(self, instance: object, owner: type) -> int | IntDescriptor:
        if instance is None:
            return self
        return getattr(instance, self.attribute_name)

    def __set__(self, instance: object, new_value: int) -> None:
        if isinstance(new_value, int):
            # Remember write on top of the dict to avoid recursive method calling:
            instance.__dict__[self.attribute_name] = new_value
            return
        raise ValueError(
            f"Attribute '{self.attribute_name}' of a '{self.class_name}' instance must be a valid int."
        )


class FloatDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.class_name = owner.__name__
        self.attribute_name: str = name

    def __get__(self, instance: object, owner: type) -> float | FloatDescriptor:
        if instance is None:
            return self
        return getattr(instance, self.attribute_name)

    def __set__(self, instance: object, new_value: float) -> None:
        if isinstance(new_value, float):
            # Remember write on top of the dict to avoid recursive method calling:
            instance.__dict__[self.attribute_name] = new_value
            return
        raise ValueError(
            f"Attribute '{self.attribute_name}' of a {self.class_name} instance must be a valid float."
        )


class StringDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.class_name: str = owner.__name__
        self.attribute_name: str = name

    def __get__(self, instance: object, owner: type) -> str | StringDescriptor:
        if instance is None:
            return self
        return getattr(instance, self.attribute_name)

    def __set__(self, instance: object, new_value: str) -> None:
        if isinstance(new_value, str):
            new_value = new_value.strip()
            if new_value:
                # Remember write on top of the dict to avoid recursive method calling:
                instance.__dict__[self.attribute_name] = new_value
                return
        raise ValueError(
            f"Attribute '{self.attribute_name}' of a {self.class_name} instance must be a non-empty string."
        )


class Person:
    name: StringDescriptor = StringDescriptor()
    age: IntDescriptor = IntDescriptor()
    height_in_meters: FloatDescriptor = FloatDescriptor()

    def __init__(self, name: str, age: int, height_in_meters: float) -> None:
        self.name: str = name
        self.age: int = age
        self.height_in_meters: float = height_in_meters
        print(
            f"Person instance successfully created at memory address: {hex(id(self)).upper()}"
        )


try:
    p1: Person = Person("", 31, 1.76)
except ValueError as err:
    print(err)
# Attribute 'name' of a Person instance must be a non-empty string.

try:
    p1: Person = Person("Israel", 31.5, 1.76)
except ValueError as err:
    print(err)
# Attribute 'age' of a 'Person' instance must be a valid int.

try:
    p1: Person = Person("Israel", 31, 176)
except ValueError as err:
    print(err)
# Attribute 'height_in_meters' of a Person instance must be a valid float.

p1: Person = Person("Israel", 31, 1.76)
# Person instance successfully created at memory address: 0X100C4C8D0
