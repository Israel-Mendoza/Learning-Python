import requests


items_url: str = "http://localhost:8000/api/items"
post_url: str = "http://localhost:8000/items/new"
message_body: dict[str, str | int | float] = {"name": "Eggs", "price": 34.2}

response = requests.post(
    post_url,
    data=message_body,
    allow_redirects=False  # Prevents the redirection (which is the default), so we'll get the actual POST request
)

print(f"{response.request.headers["content-type"] = }")
# response.request.headers["content-type"] = 'application/x-www-form-urlencoded'  // NO JSON!!!
print(f"{response.request.body = }")
# response.request.body = 'name=Eggs&price=34.2'

# Making sure our entry was stored:
response = requests.get(items_url)
print(response.json()[len(response.json()) - 1])
# {'name': 'Eggs', 'price': 34.2}
