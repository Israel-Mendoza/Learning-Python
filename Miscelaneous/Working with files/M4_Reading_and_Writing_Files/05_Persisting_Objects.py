import pickle
from typing import Any


class Person:
    age: int = 45
    name: str = "Israel Mendoza"
    kids: list[str] = ["Robert", "Charlie", "Luis"]
    employers: dict[str, int] = {"AWS": 2022, "Microsoft": 2018, "Yahoo": 2005}
    show_size = (28.5, 29.0)


def serialize(obj: Person) -> bytes:
    pickled: bytes = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Serialized object: {pickled}")
    return pickled


def deserialize(obj: pickle) -> Any:
    unpickled = pickle.loads(obj)
    print(f"Deserialized object: {unpickled}")
    return unpickled


def deserialized_employers(obj: pickle) -> dict[str, int]:
    unpickled = pickle.loads(obj)
    employers_dict: dict[str, int] = unpickled.employers
    print(f"Deserialized employers: {employers_dict}")
    return employers_dict


def serialize_to_file(file_name: str, obj: Person) -> None:
    with open(file_name, "wb") as pickle_file:
        pickle.dump(obj, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)


def deserialized_from_file(file_name: str) -> Any:
    with open(file_name, "rb") as pickle_file:
        obj = pickle.load(pickle_file)
        print(f"Deserialized object from file: {obj}")
        return obj


serialized_obj: bytes = serialize(Person())
deserialized: Any = deserialize(serialized_obj)
employers: dict[str, int] = deserialized_employers(serialized_obj)

serialize_to_file("../files_to_read/serialized.xyz", Person())
deserialized_from_file("../files_to_read/serialized.xyz")
