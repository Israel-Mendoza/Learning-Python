import httpx

login_url: str = "http://localhost:8000/api/login"
protected_url: str = "http://localhost:8000/protected"

with httpx.Client() as client:
    credentials: dict = {"username": "some_name", "password": "pass"}

    # We don't have to store the response. Just by sending the login request,
    # any returned cookies will be stored in the session's namespace.
    # But we'll store the response here, so we can take a look at it.
    login_response: httpx.Response = client.post(login_url, data=credentials)

    print(f"Cookies returned from login:\n\t{tuple(client.cookies.items())}")
    # Cookies returned from login:
    #     (('user_id', 'cc883f15c5793c42e4e9f4f6201c7830'),)
    print(f"Login response:\n\t{login_response.text}")
    # Login response:
    #     {"message": "Login successful"}
    response: httpx.Response = client.get(protected_url)  # No need to provide the cookies again!

    print(f"Protected route:\n\t{response.status_code}\n\t{response.text}")
    # Protected route:
    # 	200
    # 	{"message":"You have access to this protected route"}
    