"""Intro to inheritance"""


class Shape:
    pass


# Shape -> Ellipse -> Circle
# Shape -> Polygone ->  Rectangle -> Square
# Shape -> Polygone -> Triangle


class Ellipse(Shape):
    pass


class Circle(Ellipse):
    pass


class Polygone(Shape):
    pass


class Rectangle(Polygone):
    pass


class Square(Rectangle):
    pass


shape = Shape()
circle = Circle()
square = Square()


# Testing subclasses
print(f"{issubclass(Shape, Square)  = }")
# issubclass(Shape, Square)  = False
print(f"{issubclass(Shape, object) = }")
# issubclass(Shape, object) = True
print(f"{isinstance(circle, type(shape)) = }")
# isinstance(circle, type(shape)) = True
print(f"{issubclass(Shape, Shape) = }!!!")
# issubclass(Shape, Shape) = True!!!
