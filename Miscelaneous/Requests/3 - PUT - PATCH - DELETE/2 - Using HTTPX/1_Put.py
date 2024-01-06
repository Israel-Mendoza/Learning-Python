import httpx


items_url: str = "http://localhost:8000/api/items"
item_one_put_url: str = "http://localhost:8000/api/items/1"
new_item: dict[str, str | int | float] = {"name": "Updated by PUT", "price": 9999.99}

client: httpx.Client = httpx.Client()

client.put(item_one_put_url, json=new_item)  # Using PUT - Ignoring return value

response = client.get(items_url)

print(response.json()[1])
# {'name': 'Updated by PUT', 'price': 9999.99}
print(response.json()[1] == new_item)
# True
