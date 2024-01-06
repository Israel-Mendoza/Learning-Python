import httpx


items_url: str = "http://localhost:8000/api/items"
post_url: str = "http://localhost:8000/items/new"
message_body: dict[str, str | int | float] = {"name": "Eggs", "price": 34.2}

client: httpx.Client = httpx.Client()

response = client.post(
    post_url,
    data=message_body,
    # allow_redirects=False  # Prevents the redirection (which is the default), so we'll get the actual POST request
    follow_redirects=False
)

print(f"{response.request.headers["content-type"] = }")
# response.request.headers["content-type"] = 'application/x-www-form-urlencoded'  // NO JSON!!!
print(f"{response.request.content = }")
# response.request.content = b'name=Eggs&price=34.2'

# Making sure our entry was stored:
response = client.get(items_url)
print(response.json()[len(response.json()) - 1])
# {'name': 'Eggs', 'price': 34.2}
