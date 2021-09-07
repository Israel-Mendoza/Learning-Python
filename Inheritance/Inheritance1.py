class Shape:
    pass


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


class Triangle(Polygone):
    pass


shape = Shape()
circle = Circle()
square = Square()


# Testing subclasses
print(f"Is Ellipse a subclass of Shape? {issubclass(Shape, Square)}")
print(f"Is Ellipse a subclass of object? {issubclass(Shape, object)}")
print(f"Is circle an instance of the class of Shape? {isinstance(circle, type(shape))}")
print(f"Is Shape a subclass of Shape? {issubclass(Shape, Shape)}!!!")
