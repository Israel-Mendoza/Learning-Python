import httpx


"""Customizing the GET request header"""

client: httpx.Client = httpx.Client()

custom_headers: dict[str, str] = {
    "Authorization": "Bearer ACCESS_TOKEN",  # Adding authentication header
    "Accept": "application/json"  # Adding the type of data we'd like to receive
}


items_url: str = "http://localhost:8000/api/items"


response = client.get(items_url, headers=custom_headers)

print(response.request.headers)
# Headers({
#   'host': 'localhost:8000',
#   'accept-encoding': 'gzip, deflate',
#   'connection': 'keep-alive',
#   'user-agent': 'python-httpx/0.25.1',
#   'authorization': '[secure]',
#   'accept': 'application/json'
# })
print(response.headers)
# Headers({
#   'date': 'Sat, 06 Jan 2024 05:44:03 GMT',
#   'server': 'uvicorn',
#   'content-length': '394',
#   'content-type': 'application/json'
# })
