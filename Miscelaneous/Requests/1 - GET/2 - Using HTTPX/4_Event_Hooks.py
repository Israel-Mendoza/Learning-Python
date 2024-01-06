import httpx

"""
    We can pass a callback function to the hooks argument in the get method. 

    The argument passed to the hooks parameter must be a dictionary, which key
    is the name of the available hook (right know, I'm only aware of 'response')
    and the value is the actual callback function (or a list of functions).

    When the get method is invoked, the callback functions will be called
    and the request object will be passed to the callback functions before
    being returned from the get method. 

    If the callback function returns anything, it must be a Response object.
"""

url: str = "http://localhost:8000/api/items"


def response_information(response: httpx.Response) -> str:
    return (f"Response object @ {hex(id(response)).upper()}\n\t"
            f"URL: {response.url}\n\tStatus code: {response.status_code}")


def my_first_hook(response: httpx.Response, *args, **kwargs) -> None:
    print(f"Argument passed to the first hook: {response_information(response)}")


def print_request_url(response: httpx.Response, *args, **kwargs) -> httpx.Response:
    print(f"Adding hook attribute to {response_information(response)}")
    setattr(response, "hook_called", True)
    return response


# Creating the client and "hooking" it up with the event hooks:
client: httpx.Client = httpx.Client(event_hooks={"response": [my_first_hook, print_request_url]})
# my_response: httpx.Response = httpx.get(url, hooks={"response": [my_first_hook, print_request_url]})

my_response: httpx.Response = client.get(url)
# Argument passed to the first hook: Response object @ 0X1036A78F0
# 	URL: http://localhost:8000/api/items
# 	Status code: 200
# Adding hook attribute to Response object @ 0X1036A78F0
# 	URL: http://localhost:8000/api/items
# 	Status code: 200

try:
    print(response_information(my_response))
    print(f"{my_response.hook_called = }")  # Attribute seems to be monkey patched by the client...
except AttributeError as err:
    print(f"{type(err).__name__}: {err}")
# Response object @ 0X104FD3F20
# 	URL: http://localhost:8000/api/items
# 	Status code: 200
# my_response.hook_called = True
