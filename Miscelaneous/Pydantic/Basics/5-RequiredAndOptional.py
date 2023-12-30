from pydantic import BaseModel, ValidationError


class Circle(BaseModel):
    center: tuple[int, int]
    radius: int


print(Circle.model_fields)
# {
#   'center': FieldInfo(annotation=tuple[int, int], required=True),
#   'radius': FieldInfo(annotation=int, required=True)
# }


class Circle(BaseModel):
    # Giving the field a default value makes the field "optional"
    center: tuple[int, int] = (0, 0)  # Be careful with defaults! They won't be validated!!!
    radius: int


print(Circle.model_fields)
# {
#   'center': FieldInfo(annotation=tuple[int, int], required=False, default=(0, 0)),
#   'radius': FieldInfo(annotation=int, required=True)
# }


"""Deserialization with optional fields"""


data_dict: dict[str, int] = {"radius": 5}
data_json: str = """
{
    "radius": 12
}
"""

c1 = Circle.model_validate(data_dict)
c2 = Circle.model_validate_json(data_json)

print(repr(c1))
# Circle(center=(0, 0), radius=5)

print(repr(c2))
# Circle(center=(0, 0), radius=12)


class Circle(BaseModel):
    # Giving the field a default value makes the field "optional"
    center: tuple[int, int] = "Junk"  # Be careful with defaults! They won't be validated!!!
    radius: int


try:
    c1 = Circle(center="More junk", radius=4)
except ValidationError as ex:
    print(f"{type(ex).__name__}: {ex}")
# ValidationError: 1 validation error for Circle
# center
#   Input should be a valid tuple [type=tuple_type, input_value='More junk', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.5/v/tuple_type
