from pydantic import BaseModel, ValidationError
import json


class Circle(BaseModel):
    center_x: int = 0
    center_y: int = 0
    radius: int = 1
    name: str | None = None


unit_circle = Circle(radius=1, name=None)

# Inspecting the fields using a Circle instance
print(unit_circle.model_fields)
# {
#   'center_x': FieldInfo(annotation=int, required=False, default=0),
#   'center_y': FieldInfo(annotation=int, required=False, default=0),
#   'radius': FieldInfo(annotation=int, required=False, default=1),
#   'name': FieldInfo(annotation=Union[str, NoneType], required=False)
# }

# Inspecting the fields that were set (not the ones using the default value):
print(unit_circle.model_fields_set)
# {'radius', 'name'}  // "name" was set. It doesn't matter if we used the default value to initialize it

# What field were NOT set? We can use a set operation to figure this out:
print(unit_circle.model_fields.keys() - unit_circle.model_fields_set)
# {'center_y', 'center_x'}

"""Using inspection to return a JSON with the values that were provided"""

incoming_data = {"radius": 5, "name": "five units"}

# Deserializing the incoming_data dictionary:
requested_circle = Circle.model_validate(incoming_data)

# Serializing our circle to a dictionary, only including the provided fields
provided_data = requested_circle.model_dump(include=requested_circle.model_fields_set)

# Serializing our circle to a dictionary, only including the defaulted fields
defaulted_data = requested_circle.model_dump(exclude=requested_circle.model_fields_set)

print(provided_data)
# {'radius': 5, 'name': 'five units'}
print(defaulted_data)
# {'center_x': 0, 'center_y': 0}

# The initial and final dictionary (the one including the provided data) are equal:
print(incoming_data == provided_data)
# True
