from __future__ import annotations
from typing import override, Any


class BaseValidator:
    def __init__(self, min_value: int = None, max_value: int = None):
        if self._init_validator(min_value, max_value):
            self._min = min_value
            self._max = max_value
        else:
            raise ValueError("Initial min and max values are invalid.")

    def __set_name__(self, _: type, attr_name: str) -> None:
        """
        __set_name__ method. Stores the descriptor's instance name.
        """
        self.attr_name: str = attr_name

    def __set__(self, obj: Any, value: Any) -> None:
        """
        __set__ method. Stores the value in the passed object's __dict__
        only if the value is within the valid ranges defined at the
        descriptor's initialization time.
        """
        if self._validator(value):
            obj.__dict__[self.attr_name] = value

    def __get__(self, obj: Any, _: type) -> object:
        """
        __get__ method. Returns the value stored by the __set__ method in
        the object's __dict__. None if the __set__ has not been used.
        Returns the descriptor's instance if called from a class.
        """
        if obj is None:
            return self
        return obj.__dict__.get(self.attr_name, None)

    def _validator(self, value: Any) -> bool:
        """
        Validates that the passed value matches the min and max values.
        To be overriden by subclasses.
        """
        return True

    @staticmethod
    def _init_validator(value_1: int, value_2: int):
        """
        Validates the initial min and max values.
        To be overriden by subclasses.
        """
        return True


class IntegerField(BaseValidator):
    @staticmethod
    def _init_validator(value_1: int, value_2: int) -> bool:
        return (
            isinstance(value_1, int) and isinstance(value_2, int) and value_1 <= value_2
        )

    @override
    def _validator(self, value) -> bool:
        if not isinstance(value, int):
            raise ValueError(f"'{self.attr_name}' must be of type int")
        if self._min is not None and value < self._min:
            raise ValueError(f"'{self.attr_name}' can't be less than {self._min}")
        if self._max is not None and value > self._max:
            raise ValueError(f"'{self.attr_name}' can't be more than {self._max}")
        return True


class CharField(BaseValidator):
    @staticmethod
    def _init_validator(value_1: int, value_2: int) -> bool:
        return (
                isinstance(value_1, int)
                and isinstance(value_2, int)
                and value_2 >= value_1 > 0
        )

    @override
    def _validator(self, value) -> bool:
        if not isinstance(value, str):
            raise ValueError(f"'{self.attr_name}' must be of type str")
        if self._min is not None and len(value) < self._min:
            raise ValueError(
                f"Length of '{self.attr_name}' can't be " f"less than {self._min}"
            )
        if self._max is not None and len(value) > self._max:
            raise ValueError(
                f"Length of '{self.attr_name}' can't be " f"more than {self._max}"
            )
        return True


class Person:
    age = IntegerField(12, 42)
    name = CharField(3, 25)

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.age})"


try:
    p = Person("Israel", "28")
    print(p)
except BaseException as ex:
    print(f"{type(ex).__name__}: {ex}")
# ValueError: 'age' must be of type int
