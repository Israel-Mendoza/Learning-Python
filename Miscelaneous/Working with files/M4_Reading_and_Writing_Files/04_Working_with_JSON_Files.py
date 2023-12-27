import json


def read_print_json(file_name: str, pretty: bool, sort) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=sort, indent=4 if pretty else None))


def update_author_json(file_name: str, arr_name: str, position: int, key: str, value: str) -> None:
    with open(file_name) as read_file:
        data = json.load(read_file)
        data[arr_name][position][key] = value
        with open(file_name, "w") as write_file:
            json.dump(data, write_file)


read_print_json("../files_to_read/authors.json", True, None)
# {
#     "authors": [
#         {
#             "name": "John Doe",
#             "courses": 10
#         },
#         {
#             "name": "Jane Smith",
#             "courses": 0
#         },
#         {
#             "name": "Foo Fighter",
#             "courses": 5
#         }
#     ]
# }

update_author_json("../files_to_read/authors.json", "authors", 2, "name", "Israel")
read_print_json("../files_to_read/authors.json", True, None)
# {
#     "authors": [
#         {
#             "name": "John Doe",
#             "courses": 10
#         },
#         {
#             "name": "Jane Smith",
#             "courses": 0
#         },
#         {
#             "name": "Israel",
#             "courses": 5
#         }
#     ]
# }
