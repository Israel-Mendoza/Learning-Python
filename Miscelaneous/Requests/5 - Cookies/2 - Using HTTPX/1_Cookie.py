import httpx

cookie_url: str = "http://localhost:8000/api/cookies"
login_url: str = "http://localhost:8000/api/login"
protected_url: str = "http://localhost:8000/protected"

"""ACCESSING THE COOKIES"""

custom_cookies: dict[str, str] = {"user_id": "2"}

response: httpx.Response = httpx.get(cookie_url, cookies=custom_cookies)

print(tuple(response.cookies.items()))
# (('user_id', '2'),)

"""LOGIN"""

credentials: dict[str, str] = {"username": "some_name", "password": "pass"}

login_response: httpx.Response = httpx.post(login_url, data=credentials)

login_cookies: httpx.Cookies = login_response.cookies

print(f"Cookies returned from login:\n\t{login_cookies}")
# Cookies returned from login:
# 	{'user_id': 'befff6fcecad47159e63288dc2e758a1'}
print(f"Login response:\n\t{login_response.text}")
# Login response:
# 	{"message":"Login successful"}

protected_response: httpx.Response = httpx.get(protected_url, cookies=login_cookies)

print(f"Protected route:\n\t{protected_response.status_code}\n\t{protected_response.text}")
# Protected route:
# 	200
# 	{"message":"You have access to this protected route"}
