from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


p = Person(first_name="Israel", last_name="Mendoza", age=31)  # Passing arguments as named arguments only!

print(str(p))
# first_name='Israel' last_name='Mendoza' age=31
print(repr(p))
# Person(first_name='Israel', last_name='Mendoza', age=31)

print(p.model_fields)
# {
# 'first_name': FieldInfo(annotation=str, required=True),  // Values are required!!!
# 'last_name': FieldInfo(annotation=str, required=True),
# 'age': FieldInfo(annotation=int, required=True)
# }

try:
    Person(first_name="Israel")
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 2 validation errors for Person
# last_name
#   Field required [type=missing, input_value={'first_name': 'Israel'}, input_type=dict]
#   For further information visit https://errors.pydantic.dev/2.5/v/missing
# age
#   Field required [type=missing, input_value={'first_name': 'Israel'}, input_type=dict]
#   For further information visit https://errors.pydantic.dev/2.5/v/missing

try:
    Person(first_name="Israel", last_name="Mendoza", age="thirty-one")
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 1 validation error for Person
# age
#   Input should be a valid integer, unable to parse string as an integer
#   [type=int_parsing, input_value='thirty-one', input_type=str]
#   For further information visit https://errors.pydantic.dev/2.5/v/int_parsing


try:
    _ = Person(first_name="Israel", last_name="Mendoza", age="31")
    print(repr(_))
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# Person(first_name='Israel', last_name='Mendoza', age=31)  // NO VALIDATION ERROR. STRING WAS PARSED TO AN INT

print(p.display_name)

# We can change the fields:

p.first_name = "Ezra"
p.last_name = "Kaltenberg"
p.age = 14

print(repr(p))
# Person(first_name='Ezra', last_name='Kaltenberg', age=14)

# We can also change the field to incorrect types:
p.age = "ten"
print(repr(p))
# Person(first_name='Ezra', last_name='Kaltenberg', age='ten')
