import requests

correct_url: str = "http://localhost:8000/api/items"
incorrect_url: str = "http://localhost:8000/something"

"""Using the GET method"""

response: requests.models.Response = requests.get(correct_url)
print(f"{response} ({type(response)})")
# <Response [200]> (<class 'requests.models.Response'>)
print(f"{response.status_code} ({type(response.status_code)})")
# 200 (<class 'int'>)

response = requests.get(incorrect_url)
print(f"{response} - Code: {response.status_code}")
# <Response [404]> - Code: 404


"""Using the status code"""

response = requests.get(correct_url)

if response:  # The Response object implements the __bool__ method
    print("SUCCESS!!!")

# Testing against possible status codes:
match response.status_code:
    case 200:
        print("SUCCESS!!!")
    case 404:
        print("PAGE NOT FOUND")
    case 500:
        print("SERVER ERROR")


"""Using try-catch blocks"""

try:
    response = requests.get(incorrect_url)
    response.raise_for_status()  # Raising HTTPError, if one occurred
except requests.exceptions.HTTPError as http_error:
    print(f"{type(http_error).__name__} - {http_error}")
except Exception as err:
    print(f"{type(err).__name__}: {err}")
else:
    print(response.status_code)
# HTTPError - 404 Client Error: Not Found for url: http://localhost:8000/something
