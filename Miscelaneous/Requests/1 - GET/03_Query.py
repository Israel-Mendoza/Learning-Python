import requests

"""Adding query parameters"""

url: str = "http://localhost:8000/api/items"

# The request library allows us to create an external dictionary with the query parameters
query_params: dict[str, int] = {"offset": 2, "limit": 2, "max_price": 40}

# We can add the query parameters to the keyword argument "params" in the get method:
response: requests.models.Response = requests.get(url, params=query_params)

print(response.json())
# [{'name': 'Garply', 'price': 34.56}, {'name': 'Xyzzy', 'price': 23.78}]
