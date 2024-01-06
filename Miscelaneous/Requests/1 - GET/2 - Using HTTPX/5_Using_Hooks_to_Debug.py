import httpx

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


def log_url(response: httpx.Response, *args, **kwargs) -> None:
    print(f"Requested URL: {response.url} - Response object @ {hex(id(response)).upper()}")


# Creating the client and "hooking" it up with the event hooks:
client = httpx.Client(event_hooks={"response": [log_url]})


response_no_slash = client.get(url_no_slash)
# Requested URL: http://localhost:8000/api/items - Response object @ 0X1078C7110
print(f"response_no_slash @ {hex(id(response_no_slash)).upper()}")
# response_no_slash @ 0X1078C7110

response_with_slash = client.get(url_with_slash)
# Requested URL: http://localhost:8000/api/items/ - Response object @ 0X107982930  <--- We can see the URL's slash
print(f"response_no_slash @ {hex(id(response_with_slash)).upper()}")
# response_no_slash @ 0X107982930
