from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    field: int


try:
    Model(field=None)
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 1 validation error for Model
# field
#   Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
#     For further information visit https://errors.pydantic.dev/2.5/v/int_type


class Model(BaseModel):
    field: int | None  # Field is nullable. Warning! Not Optional, as the value is required!


m1 = Model(field=None)
print(repr(m1))
# Model(field=None)


class Model(BaseModel):
    field: int | None = None


print(Model.model_fields)
# {'field': FieldInfo(annotation=Union[int, NoneType], required=False)}

m1 = Model()  # field is optional
m2 = Model(field=None)  # field is nullable

print(repr(m1))
# Model(field=None)
print(repr(m2))
# Model(field=None)
