from pydantic import BaseModel, ValidationError


"""
    DESERIALIZATION means taking X data structure and convert
    it to a Pydantic valid Mode. 
    
    There are two ways to deserialize data with Pydantic. 
        1. From a dictionary.
        2. From a JSON string.
"""


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


"""DICTIONARY"""


# The dictionary keys must match the fields in the class
good_data = {
    "first_name": "Israel",
    "last_name": "Mendoza",
    "age": 31
}

bad_data = {
    "first_name": "Israel",
    "lastname": "Mendoza",
    "age": 31
}

p1 = Person.model_validate(good_data)
print(repr(p1))
# Person(first_name='Israel', last_name='Mendoza', age=31)

try:
    p2 = Person.model_validate(bad_data)
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 1 validation error for Person
# last_name
#   Field required [type=missing, input_value={'first_name': 'Israel', ...': 'Mendoza', 'age': 31}, input_type=dict]
#     For further information visit https://errors.pydantic.dev/2.5/v/missing
# Person(first_name='Israel', last_name='Mendoza', age=31)


"""JSON STRING"""


good_json = """
{
    "first_name": "Israel",
    "last_name": "Mendoza",
    "age": 31
}
"""

bad_json_missing_field = """
{
    "first_name": "Israel",
    "lastname": "Mendoza",
    "age": 31
}
"""

bad_json = """
{
    "first_name": "Israel",
}
"""

p3 = Person.model_validate_json(good_json)
print(repr(p3))
# Person(first_name='Israel', last_name='Mendoza', age=31)

try:
    Person.model_validate_json(bad_json)
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 1 validation error for Person
#   Invalid JSON: trailing comma at line 4 column 1
#   [type=json_invalid, input_value='\n{\n    "first_name": "Israel",\n}\n', input_type=str]
#   For further information visit https://errors.pydantic.dev/2.5/v/json_invalid

try:
    Person.model_validate_json(bad_json_missing_field)
except ValidationError as err:
    print(f"{type(err).__name__}: {err}")
# ValidationError: 1 validation error for Person
# last_name
#   Field required [type=missing, input_value={'first_name': 'Israel', ...': 'Mendoza', 'age': 31}, input_type=dict]
#     For further information visit https://errors.pydantic.dev/2.5/v/missing
