from pydantic import BaseModel

"""
    SERIALIZATION means taking a Pydantic valid Model and convert
    it to any other data structure.

    There are two ways to deserialize data with Pydantic. 
        1. To a dictionary.
        2. To a JSON string.
"""


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int


p1 = Person(first_name="Israel", last_name="Mendoza", age=31)
p2 = Person(first_name="Rachel", last_name="Watts", age=29)

print(repr(p1))
# Person(first_name='Israel', last_name='Mendoza', age=31)
print(repr(p2))
# Person(first_name='Rachel', last_name='Watts', age=29)

# Instances have own namespaces:
print(p1.__dict__)
# {'first_name': 'Israel', 'last_name': 'Mendoza', 'age': 31}
print(p2.__dict__)
# {'first_name': 'Rachel', 'last_name': 'Watts', 'age': 29}


"""TO DICTIONARY"""


d1 = p1.model_dump()
d2 = p2.model_dump()

print(f"{d1} ({type(d1)})")
# {'first_name': 'Israel', 'last_name': 'Mendoza', 'age': 31} (<class 'dict'>)
print(f"{d2} ({type(d2)})")
# {'first_name': 'Rachel', 'last_name': 'Watts', 'age': 29} (<class 'dict'>)


"""TO JSON"""


j1 = p1.model_dump_json()
j2 = p2.model_dump_json()

print(f"{j1} ({type(j1)})")
# {"first_name":"Israel","last_name":"Mendoza","age":31} (<class 'str'>)
print(f"{j2} ({type(j2)})")
# {"first_name":"Rachel","last_name":"Watts","age":29} (<class 'str'>)


# MODIFYING JSON OUTCOME

j1 = p1.model_dump_json(indent=2)
j2 = p2.model_dump_json(indent=4)

print(j1)
# {
#   "first_name": "Israel",
#   "last_name": "Mendoza",
#   "age": 31
# }
print(j2)
# {
#     "first_name": "Rachel",
#     "last_name": "Watts",
#     "age": 29
# }


"""EXCLUDING"""


d1 = p1.model_dump(exclude={"age"})
d2 = p2.model_dump(exclude={"last_name"})

print(d1)
# {'first_name': 'Israel', 'last_name': 'Mendoza'}
print(d2)
# {'first_name': 'Rachel', 'age': 29}


j1 = p1.model_dump_json(indent=4, exclude={"age"})
j2 = p2.model_dump_json(indent=4, exclude={"last_name"})

print(j1)
# {
#     "first_name": "Israel",
#     "last_name": "Mendoza"
# }
print(j2)
# {
#     "first_name": "Rachel",
#     "age": 29
# }


"""INCLUDING"""


d1 = p1.model_dump(include={"age"})
d2 = p2.model_dump(include={"last_name"})

print(d1)
# {'age': 31}
print(d2)
# {'last_name': 'Watts'}


j1 = p1.model_dump_json(indent=4, include={"age"})
j2 = p2.model_dump_json(indent=4, include={"last_name"})

print(j1)
# {
#     "age": 31
# }
print(j2)
# {
#     "last_name": "Watts"
# }
