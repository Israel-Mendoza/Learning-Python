from types import FunctionType, MethodType
from typing import Any, Type


class BaseValidator:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min = min_value
        self._max = max_value

    def __set_name__(self, cls: Type, name: str) -> None:
        """
        __set_name__ method. Stores the descriptor's instance name.
        """
        self.name = name

    def __set__(self, obj: Any, value: Any) -> None:
        """
        __set__ method. Stores the value in the passed object's __dict__
        only if the value is within the valid ranges defined at the
        descriptor's initialization time.
        """
        if self._validator(value):
            obj.__dict__[self.name] = value

    def __get__(self, obj: Any, cls: Type) -> Any:
        """
        __get__ method. Returns the value stored by the __set__ method in
        the object's __dict__. None if the __set__ has not been used.
        Returns the descriptor's instance if called from a class.
        """
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)

    def _validator(self, value) -> bool:
        """
        Validates that the passed value matches the min and max values.
        To be overriden by subclasses.
        """
        return True


class IntegerField(BaseValidator):

    def _validator(self, value) -> bool:
        if not isinstance(value, int):
            raise ValueError(f"'{self.name}' must be of type int")
        if self._min is not None and value < self._min:
            raise ValueError(f"'{self.name}' can't be less than {self._min}")
        if self._max is not None and value > self._max:
            raise ValueError(f"'{self.name}' can't be more than {self._max}")
        return True


class CharField(BaseValidator):

    def _validator(self, value) -> bool:
        if not isinstance(value, str):
            raise ValueError(f"'{self.name}' must be of type str")
        if self._min is not None and len(value) < self._min:
            raise ValueError(f"Length of '{self.name}' can't be "
                             f"less than {self._min}")
        if self._max is not None and len(value) > self._max:
            raise ValueError(f"Length of '{self.name}' can't be "
                             f"more than {self._max}")
        return True


class Person:

    age = IntegerField(3, 99)
    name = CharField(3, 25)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.age})"


try:
    p = Person("Israel", "28")
    print(p)
except BaseException as ex:
    print(f"{type(ex).__name__}: {ex}")
