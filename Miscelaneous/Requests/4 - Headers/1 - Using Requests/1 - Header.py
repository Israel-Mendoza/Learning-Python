import requests


"""Inspecting the GET response header"""


items_url: str = "http://localhost:8000/api/items"


response: requests.models.Response = requests.get(items_url)

print(response.request.headers, type(response.request.headers))  # The response contains the headers of the original request.
# {
#     'User-Agent': 'python-requests/2.31.0',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept': '*/*',
#     'Connection': 'keep-alive'
# }
# <class 'requests.structures.CaseInsensitiveDict'>

print(response.headers, type(response.headers))  # Taking a look at the response headers
# {
#     "date": "Fri, 29 Dec 2023 22:56:45 GMT",
#     "server": "uvicorn",
#     "content-length": "394",
#     "content-type": "application/json"
# }
# <class 'requests.structures.CaseInsensitiveDict'>
