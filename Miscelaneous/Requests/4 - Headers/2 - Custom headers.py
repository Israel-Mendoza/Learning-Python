import requests


"""Customizing the GET request header"""


custom_headers: dict[str, str] = {
    "Authorization": "Bearer ACCESS_TOKEN",  # Adding authentication header
    "Accept": "application/json"  # Adding the type of data we'd like to receive
}


items_url: str = "http://localhost:8000/api/items"


response = requests.get(items_url, headers=custom_headers)

print(response.request.headers)
# {
#     'User-Agent': 'python-requests/2.31.0',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept': 'application/json',
#     'Connection': 'keep-alive',
#     'Authorization': 'Bearer ACCESS_TOKEN'
# }
print(response.headers)
# {
#     'date': 'Fri, 29 Dec 2023 23:08:16 GMT',
#     'server': 'uvicorn',
#     'content-length': '394',
#     'content-type': 'application/json'
# }
