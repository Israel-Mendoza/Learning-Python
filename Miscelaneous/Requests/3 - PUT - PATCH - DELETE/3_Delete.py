import requests


items_url: str = "http://localhost:8000/api/items"
item_to_delete_url: str = "http://localhost:8000/api/items/0"

original_first_item = requests.get(items_url).json()[0]
print(original_first_item)
# {'name': 'Foo', 'price': 23.45}

del_response = requests.delete(item_to_delete_url)
print(del_response.json())
# {{'status': 'Item deleted', 'item': {'name': 'Foo', 'price': 23.45}}

deleted_item = del_response.json()["item"]
print(original_first_item == deleted_item)
# True

new_first_item = requests.get(items_url).json()[0]
print(new_first_item)
# {'name': 'Bar', 'price': 67.89}

print(original_first_item == new_first_item)
# False
