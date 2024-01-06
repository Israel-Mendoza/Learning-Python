import asyncio
import httpx
from collections.abc import Coroutine
from typing import Any

correct_url: str = "http://localhost:8000/api/items"


async def get_request(client: httpx.AsyncClient) -> list[dict]:
    response: httpx.Response = await client.get(correct_url)
    return response.json()


async def main_with_context_manager() -> None:
    async with httpx.AsyncClient() as client:
        coros: list[Coroutine] = []
        for _ in range(100):
            coros.append(get_request(client))
        results: tuple[Any] = await asyncio.gather(*coros)
        for r in results:
            print(r)


async def main_without_context_manager() -> None:
    client = httpx.AsyncClient()
    coros: list[Coroutine] = []
    for _ in range(100):
        coros.append(get_request(client))
    results = await asyncio.gather(*coros)
    for r in results:
        print(r)
    await client.aclose()


if __name__ == "__main__":
    asyncio.run(main_with_context_manager())
