from types import FunctionType, MethodType
from typing import Any, Type


class IntegerField:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min = min_value
        self._max = max_value

    def __set_name__(self, cls: Type, name: str) -> None:
        """
        __set_name__ method. Stores the descriptor's instance name.
        """
        self.name = name

    def __set__(self, obj: Any, value: int) -> None:
        """
        __set__ method. Stores the value in the passed object's __dict__
        only if the value is within the valid ranges defined at the
        descriptor's initialization time.
        """
        if self._validator(value):
            obj.__dict__[self.name] = value

    def __get__(self, obj: Any, cls: Type) -> bool:
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)

    def _validator(self, value):
        if not isinstance(value, int):
            raise ValueError(f"'{self.name}' must be of type int")
        if self._min is not None and value < self._min:
            raise ValueError(f"'{self.name}' can't be less than {self._min}")
        if self._max is not None and value > self._max:
            raise ValueError(f"'{self.name}' can't be more than {self._max}")
        return True


class CharField:

    def __init__(self, min_length: int = 0, max_length: int = None):
        self._min = min_length
        self._max = max_length

    def __set_name__(self, cls: Type, name: str) -> None:
        """
        __set_name__ method. Stores the descriptor's instance name.
        """
        self.name = name

    def __set__(self, obj: Any, value: str) -> None:
        """
        __set__ method. Stores the value in the passed object's __dict__
        only if the value's length is within the valid ranges defined 
        at the descriptor's initialization time.
        """
        if self._validator(value):
            obj.__dict__[self.name] = value

    def __get__(self, obj: Any, cls: Type) -> Any:
        if obj is None:
            return self
        return obj.__dict__.get(self.name, None)

    def _validator(self, value: Any) -> bool:
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

    name = CharField(3, 25)
    age = IntegerField(3, 99)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.age})"


try:
    p = Person("Isra", 28)
    print(p)
except BaseException as ex:
    print(f"{type(ex).__name__}: {ex}")
