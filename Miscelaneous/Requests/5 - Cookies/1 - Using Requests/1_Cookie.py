import requests

cookie_url: str = "http://localhost:8000/api/cookies"
login_url: str = "http://localhost:8000/api/login"
protected_url: str = "http://localhost:8000/protected"

"""ACCESSING THE COOKIES"""

custom_cookies: dict[str, str] = {"user_id": "2"}

response: requests.models.Response = requests.get(cookie_url, cookies=custom_cookies)

print(response.cookies.get_dict())
# {'user_id': '2'}

"""LOGIN"""

credentials: dict[str, str] = {"username": "some_name", "password": "pass"}

login_response: requests.models.Response = requests.post(login_url, data=credentials)

login_cookies: requests.cookies.RequestsCookieJar = login_response.cookies

print(f"Cookies returned from login:\n\t{login_cookies.get_dict()}")
# Cookies returned from login:
# 	{'user_id': '9975418cfaefa864f2ec620f80c10909'}
print(f"Login response:\n\t{login_response.text}")
# Login response:
# 	{"message":"Login successful"}

protected_response: requests.models.Response = requests.get(protected_url, cookies=login_cookies)

print(f"Protected route:\n\t{protected_response.status_code}\n\t{protected_response.text}")
# Protected route:
# 	200
# 	{"message":"You have access to this protected route"}
