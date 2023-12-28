from fastapi import (
    FastAPI,
    Form,
    Body,
    HTTPException,
    Response,
    UploadFile,
    File,
    Request,
    Depends,
    Cookie,
    Header,
    status
)
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from jinja2 import Environment, select_autoescape, BaseLoader
from typing import Optional, List, Annotated
from pydantic import BaseModel
import xml.etree.ElementTree as ET
import uvicorn
import secrets
import random
import time


app = FastAPI()

new_item_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Item</title>
</head>
<body>
    <h1>Create a New Item</h1>

    {% for message in flash_messages %}
    <div style="background: greenyellow">{{ message }}</div>
    <br>
    {% endfor %}

    <form action="/items/new" method="post">
        <label for="name">Item Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01" required><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

flash_messages = []
user_id_hash = "0000"

jinja_env = Environment(loader=BaseLoader, autoescape=select_autoescape(["html"]))

items_db = [
    {"name": "Foo", "price": 23.45},
    {"name": "Bar", "price": 67.89},
    {"name": "Baz", "price": 12.34},
    {"name": "Qux", "price": 56.78},
    {"name": "Quux", "price": 45.67},
    {"name": "Corge", "price": 78.90},
    {"name": "Grault", "price": 90.12},
    {"name": "Garply", "price": 34.56},
    {"name": "Waldo", "price": 89.01},
    {"name": "Fred", "price": 67.23},
    {"name": "Plugh", "price": 45.89},
    {"name": "Xyzzy", "price": 23.78},
    {"name": "Thud", "price": 90.23},
]


class Item(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


app = FastAPI()

security = HTTPBasic()
USERNAME = 'username'
PASSWORD = 'pass'


@app.get("/", tags=["Items API"], summary="Retrieve a list of items")
@app.get("/api/items", tags=["Items API"], summary="Retrieve a list of items")
async def read_items(
    offset: Optional[int] = None,
    limit: Optional[int] = None,
    max_price: Optional[float] = None,
):
    """
    Retrieve all of the items or a subset of items from the database based on pagination parameters and price parameters.

    - **offset**: (Optional) Starting position for fetching the items.
    - **limit**: (Optional) Maximum number of items to fetch.
    - **max_price**: (Optional) Maximum price for filtering items.

    Returns a list of items within the given range and below the given price.
    """
    filtered_items = items_db

    # Good enough for mock database
    if max_price is not None:
        filtered_items = [item for item in items_db if item["price"] <= max_price]

    if offset is None:
        offset = 0
    if limit is None:
        limit = len(filtered_items) - offset

    return filtered_items[offset : offset + limit]


@app.get(
    "/items/new", tags=["Items HTML"], summary="Serve a form for creating a new item"
)
async def new_item_form():
    """
    Serve an HTML page with a form to submit a new item's name and price.
    """
    messages = list(flash_messages)
    flash_messages.clear()

    rendered_template = jinja_env.from_string(new_item_template).render(
        flash_messages=messages
    )
    return HTMLResponse(content=rendered_template)


@app.post("/items/new", tags=["Items HTML"], summary="Handle the items form submission")
async def create_item_from_form(name: str = Form(...), price: float = Form(...)):
    """
    Handle form submission to add a new item to items_db.
    """
    item = {"name": name, "price": price}
    items_db.append(item)
    flash_messages.append(f"Item {name} added successfully!")
    return RedirectResponse(url="/items/new", status_code=303)


@app.post("/api/items", tags=["Items API"], summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **price**: required
    """
    items_db.append(item.model_dump())
    return item


@app.post("/api/items/xml", tags=["Items API"], summary="Create an item with XML")
async def create_item_xml(xml_body: str = Body(..., media_type="application/xml")):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **price**: required
    """
    try:
        root = ET.fromstring(xml_body)
        name = root.find("name").text
        price = root.find("price").text
        item = {"name": name, "price": price}
        items_db.append(item)

        xml_response = f"""
        <response>
            <name>{name}</name>
            <price>{price}</price>
        </response>
        """
        return Response(content=xml_response, media_type="application/xml")
    except ET.ParseError:
        raise HTTPException(status_code=400, detail="Invalid XML")


@app.post("/upload-files", summary="Upload multiple CSV files", tags=["Upload files"])
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Upload one or more CSV files to the server.

    - **files**: A list of CSV files to be uploaded.

    Returns a dictionary with the names of the uploaded files.
    """
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")

    filenames = []
    for file in files:
        contents = await file.read()
        filenames.append(file.filename)

    return {"uploaded_files": filenames}


@app.put(
    "/api/items/{item_id}", tags=["Items API"], summary="Update an item completely"
)
async def update_item(item_id: int, item: Item):
    """
    Update all fields of an existing item:

    - **name**: each item must have a name.
    - **price**: required.
    """
    if 0 <= item_id < len(items_db):
        items_db[item_id] = item.dict()
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")


@app.patch(
    "/api/items/{item_id}",
    tags=["Items API"],
    summary="Update specific fields of an item",
)
async def patch_item(item_id: int, item: Item):
    """
    Update specific fields of an existing item:

    - **name**: optional new name for the item.
    - **price**: optional new price for the item.
    """
    if 0 <= item_id < len(items_db):
        if item.name:
            items_db[item_id]["name"] = item.name
        if item.price:
            items_db[item_id]["price"] = item.price
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/api/items/{item_id}", tags=["Items API"], summary="Delete an item")
async def delete_item(item_id: int):
    """
    Delete an existing item:

    - **item_id**: the ID of the item to be deleted.
    """
    if 0 <= item_id < len(items_db):
        deleted_item = items_db.pop(item_id)
        return {"status": "Item deleted", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/api/items/{item_id}", tags=["Items API"], summary="Retrieve a single item")
async def get_item(item_id: int):
    """
    Retrieve a specific item based on its ID:

    - **item_id**: the ID of the item to be retrieved.
    """
    if 0 <= item_id < len(items_db):
        return items_db[item_id]
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/api/cookies", summary="Get back cookies from the request", tags=["Cookies"])
async def get_cookies(request: Request):
    """
    Send cookies with the request and get them from the response.
    """
    response = JSONResponse(content={"message": "ok"})
    for cookie_name, cookie_value in request.cookies.items():
        response.set_cookie(key=cookie_name, value=cookie_value)
    return response


@app.post("/api/login", summary="User 'remember me' login", tags=["Authentication"])
async def login(username: str = Form(...), password: str = Form(...)):
    """
    Authenticate a user with a username and password.

    - **username**: User's username.
    - **password**: User's password.
    """
    if username == "some_name" and password == "pass":
        global user_id_hash
        user_id_hash = secrets.token_hex(16)

        content = {"message": "Login successful"}
        response = JSONResponse(content=content)

        response.set_cookie(key="user_id", value=user_id_hash)

        return response
    else:
        return {"message": "Invalid credentials"}


def verify_user_id(user_id: str = Cookie(None)):
    if user_id_hash != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/protected", summary="Access a protected route with a cookie", tags=["Authentication"])
async def protected_route(user_id_verified: str = Depends(verify_user_id)):
    """
    Access a route that is protected by user ID verification.
    """
    return {"message": "You have access to this protected route"}


@app.get("/flaky", summary="Simulate a flaky endpoint", tags=["Simulation"])
async def flaky_endpoint():
    """
    Simulate a flaky endpoint that randomly fails or succeeds.
    """
    if random.choice([True, False]):
        raise HTTPException(status_code=500, detail="Server Error")
    else:
        return {"message": "Success"}


@app.get("/old-route", summary="Redirect from old to new route", tags=["Redirection"])
async def old_route():
    """
    Redirect requests from an old route to a new route.
    """
    return RedirectResponse(url="/new-route")


@app.head("/old-route", summary="Head request for old route redirection", tags=["Redirection"])
async def old_route_head():
    """
    Handle HEAD requests for the old route, redirecting to the new route.
    """
    return RedirectResponse(url="/new-route")


@app.get("/new-route", summary="New route endpoint", tags=["Redirection"])
async def new_route():
    """
    Respond to requests at the new route.
    """
    return {"message": "This is the new route!"}


@app.head("/new-route", summary="Head request for new route", tags=["Redirection"])
async def new_route_head():
    """
    Handle HEAD requests for the new route.
    """
    return Response(content=None, media_type="application/json")


@app.get("/slow-response", summary="Simulate a slow response", tags=["Simulation"])
async def slow_response():
    """
    Simulate a slow response from the server (5 seconds).
    """
    time.sleep(5)
    return {"message": "Response after delay"}


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials

@app.get("/protected-endpoint", summary="Access a basic auth protected route", tags=["Authentication"])
def read_protected_route(user: HTTPBasicCredentials = Depends(get_current_user)):
    """
    Access a route protected by HTTP Basic Authentication.

    You need to provide HTTPBasic Authentication username and password to access this route.
    If you want to access it from the documentation, you can click on the Authorize button at the top of  the page.
    """
    return {"message": "Welcome, authenticated user!"}


@app.get("/jwt-protected-route", summary="Access a JWT protected route", tags=["Authentication"])
async def protected_route(authorization: str = Header(None)):
    """
    Access a route protected by JWT (JSON Web Token) authorization.

    - **authorization**: JWT token in the authorization header.
    """
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1]
        if token == "abcde123":
            return {"message": "Access to protected route granted"}
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
    else:
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid")


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
