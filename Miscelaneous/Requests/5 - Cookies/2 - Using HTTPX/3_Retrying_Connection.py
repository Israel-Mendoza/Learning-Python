import logging
import httpx

"""
Setting the retries...

We can add transport settings for the client to retry a failed connection.

For example:
    
    transport = httpx.HTTPTransport(retries=5)
    client = httpx.Client(transport=transport)
    
    
Notice that this will only work for httpx:connectError or httpx.ConnectTimeout. 

If you need other retry settings, consider using general-purpose tools such as tenacity.

"""


url: str = "http://localhost:8000/flaky"  # Endpoint that will randomly return 200 or 500

# Setting the logger
logging.basicConfig(level=logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


transport = httpx.HTTPTransport(retries=5)
client = httpx.Client(transport=transport)

try:
    response: httpx.Response = client.get(url)
except Exception as ex:
    print(ex)
