from __future__ import annotations


class Integer:

    """Data-descriptor that will allow the instance attribute to store integers in a given range."""

    def __init__(self, min_value: int, max_value: int) -> None:
        if (
            isinstance(min_value, int)
            and isinstance(max_value, int)
            and min_value < max_value
        ):
            self.min_value: int = min_value
            self.max_value: int = max_value
        else:
            raise ValueError("Integer limits are two ints, one smaller than the other")
        print("Integer descriptor instance successfully created.")

    def __set_name__(self, _: type, attr_name: str) -> None:
        # Storing the name of the attribute we'll use to
        # write to and read from the instance's namespace.
        self.attr_name: str = attr_name

    def __set__(self, instance: object, new_value: int) -> None:
        """
        Makes sure the value is an integer in between the previously set range.
        """
        if not isinstance(new_value, int):
            raise ValueError(f"'{self.attr_name}' must be if type 'int'.")
        if self.min_value <= new_value <= self.max_value:
            instance.__dict__[self.attr_name] = new_value
        else:
            raise ValueError(
                f"'{self.attr_name}' must be >= {self.min_value} and <= {self.max_value}"
            )

    def __get__(self, instance: object, _: type) -> Integer | int:
        """
        Returns the Integer instance if called from a class.
        Returns a valid integer in between the ranges previously set,
        provided the __set__ method has been used to set the attribute's value.
        Otherwise, raises an "Attribute Error".
        """
        if instance is None:
            return self
        value_to_return: int | None = instance.__dict__.get(self.attr_name, None)
        if value_to_return:
            return value_to_return
        else:
            raise AttributeError(f"'{self.attr_name}' has not been set yet.")


class String:
    def __init__(self, min_length: int, max_length: int) -> None:
        if String._min_and_max_validator(min_length, max_length):
            self.min_length: int = min_length
            self.max_length: int = max_length
        else:
            raise ValueError(
                "String must be delimited by positive numbers, one smaller than the other."
            )
        print("String descriptor instance successfully created.")

    def __set_name__(self, owner: type, attr_name: str) -> None:
        # Storing the name of the attribute we'll use to
        # write to and read from the instance's namespace.
        self.class_name: str = owner.__name__
        self.attr_name: str = attr_name

    def __set__(self, instance: object, new_value: str) -> None:
        """
        Makes sure the value is an integer in between the previously set range.
        """
        if (
            isinstance(new_value, str)
            and self.min_length <= len(new_value.strip()) <= self.max_length
        ):
            instance.__dict__[self.attr_name] = new_value.strip()
        else:
            raise ValueError(
                f"'{self.attr_name}' must be a string between {self.min_length} and {self.max_length} characters long."
            )

    def __get__(self, instance: object, _: type) -> str | String:
        """
        Returns the String instance if called from a class.
        Returns a valid string, which length is in between the ranges previously set,
        provided the __set__ method has been used to set the attribute's value.
        Otherwise, raises an "Attribute Error".
        """
        if instance is None:
            return self
        value_to_return: str | None = instance.__dict__.get(self.attr_name, None)
        if value_to_return is None:
            raise AttributeError(f"'{self.attr_name}' has not been set yet.")
        return value_to_return

    @staticmethod
    def _min_and_max_validator(num_1: int, num_2: int) -> bool:
        """
        Private static method, used by the __init__ method to initialize the String instance.
        It makes sure the passed ranges are possitive ints, one langer than the other.
        Returns True if the previous conditions apply, otherwise returns False.
        """
        if isinstance(num_1, int) and isinstance(num_2, int):
            return num_1 < num_2 and num_1 >= 0
        return False


try:

    class Person:
        name: String = String(-2, 10)
        age: Integer = Integer(18, 19)

except ValueError as ex:
    print(ex)
# String must be delimited by positive numbers, one smaller than the other.

try:

    class Person:
        name: String = String(0, "10")
        age: Integer = Integer(18, 19)

except ValueError as ex:
    print(ex)
# String must be delimited by positive numbers, one smaller than the other.

try:

    class Person:
        name: String = String(0, 10)
        age: Integer = Integer("18", 19)

except ValueError as ex:
    print(ex)
# String descriptor instance successfully created.
# Integer limits are two ints, one smaller than the other

try:

    class Person:
        name: String = String(2, 10)
        age: Integer = Integer(18, 19)

except ValueError as ex:
    print(ex)
# String descriptor instance successfully created.
# Integer descriptor instance successfully created.

p: Person = Person()

try:
    print(p.name)
except AttributeError as ex:
    print(ex)
# 'name' has not been set yet.

try:
    p.name = ""
except ValueError as ex:
    print(ex)
# 'name' must be a string between 2 and 10 characters long.

try:
    p.age
except AttributeError as ex:
    print(ex)
# 'age' has not been set yet.

try:
    p.age = 15
except ValueError as ex:
    print(ex)
# 'age' must be >= 18 and <= 19
