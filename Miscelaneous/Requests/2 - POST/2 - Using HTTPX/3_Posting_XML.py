import httpx
import xml.etree.ElementTree as ET


items_url: str = "http://localhost:8000/api/items"
post_url: str = "http://localhost:8000/api/items/xml"
message_body = """
<item>
    <name>Some Item</name>
    <price>333.33</price>
</item>
"""
client: httpx.Client = httpx.Client()

response = client.post(
    post_url,
    data=message_body,  # Expects a dictionary, though...
    headers={"Content-Type": "application/xml"}
)


name = ET.fromstring(response.text).find("name").text
price = ET.fromstring(response.text).find("price").text

print(f"{name = } - {price = }")
# name = 'Some Item' - price = '333.33'

# Making sure our entry was stored:
response = client.get(items_url)
print(response.json()[len(response.json()) - 1])
# {'name': 'Some Item', 'price': '333.33'}
