import httpx


"""Analyzing the Response Object"""


correct_url: str = "http://localhost:8000/api/items"
incorrect_url: str = "http://localhost:8000/something"

# Creating a client
client: httpx.Client = httpx.Client()

response: httpx.Response = client.get(correct_url)


"""Status code"""

print(f"Status code: {response.status_code} ({type(response.status_code)})")
# Status code: 200 (<class 'int'>)

"""Content"""

print(f"Content:\n{response.content} ({type(response.content)})")
# Content:
# b'[{"name":"Foo","price":23.45},{"name":"Bar","price":67.89} . . . {"name":"Thud","price":90.23}]' (<class 'bytes'>)
print(f"Content in hex:\n{response.content.hex()}")
# Content in hex:
# 5b7b226e616d6522. . .62e3726

"""Text"""

response.encoding = "utf-8"  # Recommended if we already know the encoding we're waiting
print(f"Text:\n{response.text} ({type(response.text)})")
# Text:
# [{"name":"Foo","price":23.45},{"name":"Bar","price":67.89}, . . ., {"name":"Baz","price":12.34}] (<class 'str'>)

"""Headers"""

print(f"Headers: {response.headers} {type(response.headers)}")
# Headers({
# 'date': 'Fri, 05 Jan 2024 19:14:27 GMT',
# 'server': 'uvicorn',
# 'content-length': '394',
# 'content-type': 'application/json'
# })
# <class 'httpx.Headers'>

"""JSON"""

response_items: list[dict[str, str | float]] = response.json()
print(f"{type(response_items) = }")
# type(response_items) = <class 'list'>
for item in response_items:
    print(item)
# {'name': 'Foo', 'price': 23.45}
# {'name': 'Bar', 'price': 67.89}
# {'name': 'Baz', 'price': 12.34}
# .
# .
# .
# {'name': 'Xyzzy', 'price': 23.78}
# {'name': 'Thud', 'price': 90.23}

print(f"The price if one {response_items[12]["name"]} is ${response_items[12]["price"]}")
# The price if one Thud is $90.23
