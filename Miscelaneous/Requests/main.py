from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"value": "Hola, Chatom!"}


@app.get("/mogom")
async def mogom() -> dict[str, str]:
    return {"value": "Hola, Mogom!"}

