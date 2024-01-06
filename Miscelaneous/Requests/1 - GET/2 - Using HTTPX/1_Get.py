import httpx


correct_url: str = "http://localhost:8000/api/items"
incorrect_url: str = "http://localhost:8000/something"

"""Using the GET method"""

# Creating a client
client: httpx.Client = httpx.Client()

response: httpx.Response = client.get(correct_url)
print(f"{response} ({type(response)})")
# <Response [200 OK]> (<class 'httpx.Response'>)
print(f"{response.status_code} ({type(response.status_code)})")
# 200 (<class 'int'>)

response = client.get(incorrect_url)
print(f"{response} - Code: {response.status_code}")
# <Response [404 Not Found]> - Code: 404


"""Using the status code"""

response = client.get(correct_url)

if response:  # The Response object implements the __bool__ method
    print("SUCCESS!!!")
# SUCCESS!!!

# Testing against possible status codes:
match response.status_code:
    case 200:
        print("SUCCESS!!!")
    case 404:
        print("PAGE NOT FOUND")
    case 500:
        print("SERVER ERROR")
# SUCCESS!!!

"""Using try-catch blocks"""

try:
    response = client.get(incorrect_url)
    response.raise_for_status()  # Raising HTTPError, if one occurred
except httpx.HTTPError as http_error:
    print(f"{type(http_error).__name__} - {http_error}")
except Exception as err:
    print(f"{type(err).__name__}: {err}")
else:
    print(response.status_code)
# HTTPStatusError - Client error '404 Not Found' for url 'http://localhost:8000/something'
# For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
