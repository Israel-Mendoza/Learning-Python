import requests
import json


items_url: str = "http://localhost:8000/api/items"
message_body: dict[str, str | int | float] = {"name": "Eggs", "price": 34.2}


response = requests.post(
    items_url,
    # data=json.dumps(message_body),
    # headers={"Content-Type": "application/json"},
    json=message_body,  # We can use the "json" argument, instead of data, since we're sending JSON
    allow_redirects=False
)

print(f"{response.request.headers["content-type"] = }")
# response.request.headers["content-type"] = 'application/json'   // JSON!!!
print(f"{response.request.body = }")
# response.request.body = b'"{\\"name\\": \\"Eggs\\", \\"price\\": 34.2}"'  // Serialized JSON!!!

# Making sure our entry was stored:
response = requests.get(items_url)
print(response.json()[len(response.json()) - 1])
# {'name': 'Eggs', 'price': 34.2}
print(response.json()[len(response.json()) - 1] == message_body)
# True
