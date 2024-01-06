import httpx

"""Adding query parameters"""

url: str = "http://localhost:8000/api/items"

# Creating a client
client: httpx.Client = httpx.Client()

# The request library allows us to create an external dictionary with the query parameters
query_params: dict[str, int] = {"offset": 2, "limit": 2, "max_price": 40}

# We can add the query parameters to the keyword argument "params" in the get method:
response: httpx.Response = client.get(url, params=query_params)

print(response.json())
# [{'name': 'Garply', 'price': 34.56}, {'name': 'Xyzzy', 'price': 23.78}]
