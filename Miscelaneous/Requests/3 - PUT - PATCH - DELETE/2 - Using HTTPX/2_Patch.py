import httpx

items_url: str = "http://localhost:8000/api/items"
item_one_patch_url: str = "http://localhost:8000/api/items/1"
new_item: dict[str, str | int | float] = {"name": "Updated by PATCH"}  # Updating only the "name"

client: httpx.Client = httpx.Client()

client.patch(item_one_patch_url, json=new_item)  # Using PUT - Ignoring return value

response = client.get(items_url)

print(response.json()[1])
# {'name': 'Updated by PATCH', 'price': 67.89}
print(response.json()[1]["name"] == new_item["name"])
# True
