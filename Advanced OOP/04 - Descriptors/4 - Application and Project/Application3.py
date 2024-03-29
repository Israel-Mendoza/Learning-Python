from __future__ import annotations
from collections.abc import Sequence
from typing import Any
#

class Integer:
    """
    A data descriptor that will set and get integer values in a given range.
    """

    def __init__(self, min_value: int = None, max_value: int = None) -> None:
        """
        __init__ method.
        Initializes the minimum and the maximum values an Integer object may contain.
        """
        self.min_value: int = min_value
        self.max_value: int = max_value

    def __set_name__(self, cls: type, name: str) -> None:
        """
        __set_name__ method saves the class attribute name in the descriptor's instance namespace.
        """
        self.name: str = name

    def __set__(self, obj: Any, value: int) -> None:
        """
        Stores a valid integer in the obj's __dict__, if the number
        is between the ranges defined in self.min and self. max
        Raises ValueError if the passed value doesn't meet this condition.
        """
        if not isinstance(value, int):
            raise ValueError(f"'{self.name}' must be a valid integer")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"'{self.name}' must be >= {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"'{self.name}' must be <= to {self.max_value}")
        # Setting attribute using the instance's __dict__ (otherwise we fall into recursion)
        obj.__dict__[self.name] = value

    def __get__(self, obj: Any, cls: type) -> int | Integer:
        """
        Returns the value stored in the obj's __dict__ or None if this has not been set yet.
        """
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    @property
    def min_value(self) -> int:
        """The minimum value the Integer object can contain."""
        return self._min

    @min_value.setter
    def min_value(self, value: int) -> None:
        try:
            self._min = self._valid_integer(value)
        except ValueError:
            raise ValueError("min_value must be a valid integer")

    @property
    def max_value(self) -> int:
        """The maximum value the Integer object can contain."""
        return self._max

    @max_value.setter
    def max_value(self, value) -> None:
        try:
            value = self._valid_integer(value)
            self._max = value
        except ValueError:
            raise ValueError("max_value must be a valid integer")

    def __repr__(self) -> str:
        return f"Integer(min_value={self.min_value}, max_value={self.max_value})"

    @staticmethod
    def _valid_integer(a_number: Any) -> int | None:
        """
        For descriptor's internal use only, used to validate passed values.
        Returns a valid int representation of the passed argument.
        Raises ValueError only.
        """
        if isinstance(a_number, int) or isinstance(a_number, float):
            return int(a_number)
        elif a_number is None:
            return None
        else:
            try:
                a_number = int(a_number)
                return a_number
            except ValueError:
                raise ValueError()
            except TypeError:
                raise ValueError()


class Point2D:
    x = Integer(0, 100)
    y = Integer(0, 100)

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes the x and y attributes.
        Setter called from the Integer data descriptor.
        """
        self.x = x
        self.y = y

    def __eq__(self, other: Point2D) -> bool:
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"


class Point2DSequence:
    def __init__(self, min_length: int = None, max_length: int = None):
        self._min_length: int = min_length
        self._max_length: int = max_length

    def __set_name__(self, cls: type, name: str) -> None:
        self.name: str = name

    def __set__(self, obj: Any, value: int) -> None:
        if not isinstance(value, Sequence):
            raise TypeError(f"{self.name} must be a sequence type.")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(
                f"Length of '{self.name}'sequence must be "
                f"at least {self.min_length}"
            )
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(
                f"Length of '{self.name}' sequence must be "
                f"less than {self.max_length}"
            )
        for index, point in enumerate(value):
            if not isinstance(point, Point2D):
                raise ValueError(
                    f"Item at index {index} of '{self.name}' "
                    f"must be of type 'Point2D'"
                )
        obj.__dict__[self.name] = value

    def __get__(self, obj: Any, cls: type) -> Point2DSequence | int | None:
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    @property
    def min_length(self) -> int:
        return self._min_length

    @min_length.setter
    def min_length(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be a valid integer")
        if value < 0:
            raise ValueError(f"{self.name} must be equal or greater than zero")
        self._min_length = value

    @property
    def max_length(self) -> int:
        return self._max_length

    @max_length.setter
    def max_length(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be a valid integer")
        if value < 0:
            raise ValueError(f"{self.name} must be equal or greater than zero")
        self._max_length = value


class Polygon:
    vertices = Point2DSequence(3)

    def __init__(self, *vertices) -> None:
        self.vertices = list(vertices)

    def __contains__(self, point: Point2D) -> bool:
        return point in self.vertices

    def __getitem__(self, index: int) -> tuple[..., Point2D]:
        if not isinstance(index, int):
            raise TypeError("Polygon indices must be integers")
        return self.vertices[index]

    def append(self, point: Point2D) -> None:
        if not isinstance(point, Point2D):
            raise TypeError(f"appended vertex must be of type Point2D")
        if self.__class__.vertices.max_length is not None:
            if self.__class__.vertices.max_length > len(self.vertices):
                self.vertices.append(point)
            else:
                raise IndexError(
                    f"{self.__class__.__name__} can't " f"accept any more points."
                )
        self.vertices.append(point)

    def pop(self) -> Point2D:
        if self.__class__.vertices.min_length is not None:
            if self.__class__.vertices.min_length < len(self.vertices):
                return self.vertices.pop()
            else:
                raise IndexError(
                    f"can't pop from {self.__class__.__name__}. "
                    f"{self.__class__.__name__} has reached its minimum length."
                )
        else:
            if len(self.vertices) == 0:
                raise IndexError(
                    f"can't pop from an " f"empty {self.__class__.__name__}"
                )
            else:
                return self.vertices.pop()

    def __repr__(self) -> str:
        points = ", ".join([repr(point) for point in self.vertices])
        return f"Polygon({points})"


class Triangle(Polygon):
    vertices = Point2DSequence(3, 3)


class Rectangle(Polygon):
    vertices = Point2DSequence(4, 4)


try:
    t = Triangle(Point2D(10, 0), Point2D(20, 0), Point2D(15, 20))
    t.append(Point2D(1, 1))
except IndexError as ex:
    print(type(ex))
except ValueError as ex:
    print(ex)
except TypeError as ex:
    print(ex)
# Triangle can't accept any more points.
