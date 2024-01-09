import requests

login_url: str = "http://localhost:8000/api/login"
protected_url: str = "http://localhost:8000/protected"

with requests.Session() as session:
    credentials: dict = {"username": "some_name", "password": "pass"}

    # We don't have to store the response. Just by sending the login request,
    # any returned cookies will be stored in the session's namespace.
    # But we'll store the response here, so we can take a look at it.
    login_response: requests.models.Response = session.post(login_url, data=credentials)

    print(f"Cookies returned from login:\n\t{session.cookies.get_dict()}")
    print(f"Login response:\n\t{login_response.text}")

    response: requests.models.Response = session.get(protected_url)  # No need to provide the cookies again!

    print(f"Protected route:\n\t{response.status_code}\n\t{response.text}")
