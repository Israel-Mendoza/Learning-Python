import logging
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RetryError
from urllib3.util.retry import Retry


"""
Setting the retries...

We can mount settings for the session to retry a failed connection.

For example:
    
    session.mount(HTTPAdapter(max_retries=3))
    
In this example, the session will simply try three times and will stop.

We can also add a specific domain, on top of the max retries:

For example:

    session.mount("http://localhost", HTTPAdapter(max_retries=3))
    
This means that the repeated attempts will only be sent to the "localhost" domain. 

If we want to add more restrictions/conditions to the retries, we can use a Retry instance.

For example:

    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500], allowed_methods={"GET"})
    session.mount("http://localhost", HTTPAdapter(max_retries=retries))

In this example, on top of just giving a max number of retries, we can also specify the status code
we want to retry as well as the HTTP method. 

If the max retries are reached, but the code is still being returned, it raises the RetryError.

"""


url: str = "http://localhost:8000/flaky"  # Endpoint that will randomly return 200 or 500

# Setting the logger
logging.basicConfig(level=logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


session = requests.Session()
retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500], allowed_methods={"GET"})
session.mount("http://localhost", HTTPAdapter(max_retries=retries))
# session.mount(HTTPAdapter(max_retries=3))  # We can set up the retries with an int too and no domain


try:
    response: requests.models.Response = session.get(url)
    print(f"Final response status: {response.status_code}")
except RetryError as ex:
    print("Maximum retries exceeded Server is not available.")

