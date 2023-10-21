"""Intro to inheritance"""


# Creating a base class to inherit from:
class Shape:
    pass


# How we will be creating subclasses:
# Shape -> Ellipse -> Circle
# Shape -> Polygone ->  Rectangle -> Square
# Shape -> Polygone -> Triangle


class Ellipse(Shape):
    pass


class Circle(Ellipse):
    pass


class Polygone(Shape):
    pass


class Triangle(Polygone):
    pass


class Rectangle(Polygone):
    pass


class Square(Rectangle):  # Square inherits from Rectangle -> Polygone -> Shape
    pass


shape: Shape = Shape()
circle: Circle = Circle()
square: Square = Square()
triangle: Triangle = Triangle()

# Testing subclasses
print(f"{issubclass(Shape, Square) = }")
# issubclass(Shape, Square) = False
print(f"{issubclass(Shape, object) = }")
# issubclass(Shape, object) = True
print(f"{isinstance(circle, type(shape)) = }")  # Is circle an instance of Shape?
# isinstance(circle, type(shape)) = True
print(f"{isinstance(square, Polygone) = }")
# isinstance(square, Polygone) = True
print(f"{isinstance(triangle, Shape) = }")
#  isinstance(triangle, Shape) = True
print(f"{issubclass(Shape, Shape) = }!!!")
# issubclass(Shape, Shape) = True!!!
