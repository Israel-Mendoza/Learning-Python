import httpx


"""Inspecting the GET response header"""


items_url: str = "http://localhost:8000/api/items"

client: httpx.Client = httpx.Client()


response: httpx.Response = client.get(items_url)

# The response contains the headers of the original request.
print(response.request.headers, type(response.request.headers))
# Headers({
#   'host': 'localhost:8000',
#   'accept': '*/*',
#   'accept-encoding': 'gzip, deflate',
#   'connection': 'keep-alive',
#   'user-agent': 'python-httpx/0.25.1'
# })
# <class 'httpx.Headers'>

print(response.headers)  # Taking a look at the response headers
# Headers({
#   'date': 'Sat, 06 Jan 2024 05:40:29 GMT',
#   'server': 'uvicorn',
#   'content-length': '394',
#   'content-type': 'application/json'
# })
# <class 'httpx.Headers'>
