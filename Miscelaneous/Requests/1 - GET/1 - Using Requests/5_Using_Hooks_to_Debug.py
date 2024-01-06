import requests

"""
    Using hooks can be useful when troubleshooting. 
    
    In this example, let's see how the requests library redirects our requests.
    
    We'll use a couple of urls, one with a trailing slash, and the other without it. 
    
    When we use the trailing slash, the server figures out we didn't mean to
    use the trailing slash and redirects us to the path without the slash. 
    
    That's not a big deal with GET requests, but it can lead to unexpected behavior
    with POST request because the redirect might return into a GET request.
"""


url_no_slash: str = "http://localhost:8000/api/items"
url_with_slash: str = "http://localhost:8000/api/items/"


def log_url(response: requests.models.Response, *args, **kwargs) -> None:
    print(f"Requested URL: {response.url} - Response object @ {hex(id(response)).upper()}")


response_no_slash = requests.get(url_no_slash, hooks={"response": log_url})
# Requested URL: http://localhost:8000/api/items - Response object @ 0X101D9E7E0
print(f"response_no_slash @ {hex(id(response_no_slash)).upper()}")
# response_no_slash @ 0X101D9E7E0

response_with_slash = requests.get(url_with_slash, hooks={"response": log_url})
# Requested URL: http://localhost:8000/api/items/ - Response object @ 0X1020B7F20  <--- What happened here?
# Requested URL: http://localhost:8000/api/items - Response object @ 0X1012E40B0
print(f"response_no_slash @ {hex(id(response_with_slash)).upper()}")
# response_no_slash @ 0X1012E40B0
