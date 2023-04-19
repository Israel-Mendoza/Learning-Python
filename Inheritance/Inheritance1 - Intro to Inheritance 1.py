"""Intro to inheritance"""

# Creating a base class to inherit from:
class Shape:
    pass


# How we will be creating subclasses:
# Shape -> Ellipse -> Circle
# Shape -> Polygone ->  Rectangle -> Square
# Shape -> Polygone -> Triangle


# Ellipse inherits from Shape
class Ellipse(Shape):
    pass


# Circle inherits from Ellipse -> Shape
class Circle(Ellipse):
    pass


# Polygone inherits from Shape
class Polygone(Shape):
    pass


# Triangle inherits from Polygone
class Triangle(Polygone):
    pass


# Rectangle inherits from Polygone -> Shape
class Rectangle(Polygone):
    pass


# Square inherits from Rectangle -> Polygone -> Shape
class Square(Rectangle):
    pass


shape: Shape = Shape()
circle: Circle = Circle()
square: Square = Square()
triangle: Triangle = Triangle()


# Testing subclasses
print(f"{issubclass(Shape, Square)  = }")
# issubclass(Shape, Square)  = False
print(f"{issubclass(Shape, object) = }")
# issubclass(Shape, object) = True
print(f"{isinstance(circle, type(shape)) = }")
# isinstance(circle, type(shape)) = True
print(f"{isinstance(square, Polygone) = }")
# isinstance(square, Polygone) = True
print(f"{isinstance(triangle, Shape) = }")
#  isinstance(triangle, Shape) = True
print(f"{issubclass(Shape, Shape) = }!!!")
# issubclass(Shape, Shape) = True!!!
