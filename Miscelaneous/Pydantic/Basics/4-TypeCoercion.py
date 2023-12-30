from pydantic import BaseModel, ValidationError


"""
    What happens when the provided data is not the requested one?
    
    Pydantic will try to coerce it to the right type.
"""


class Coordinates(BaseModel):
    x: float
    y: float


p1 = Coordinates(x=1.1, y=2.2)

print(repr(p1))
# Coordinates(x=1.1, y=2.2)
print(type(p1.x), type(p1.y))
# <class 'float'> <class 'float'>


"""Default coercion (lax)"""


p2 = Coordinates(x="1", y="2.2")

print(repr(p2))
# Coordinates(x=1.0, y=2.2)
print(type(p2.x), type(p2.y))
# <class 'float'> <class 'float'>


# There is no type coercion between any object to str. And that's a good thing!!!


class MyModel(BaseModel):
    name: str


try:
    MyModel(name=12345)
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 1 validation error for MyModel
# name
#   Input should be a valid string [type=string_type, input_value=12345, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.5/v/string_type
