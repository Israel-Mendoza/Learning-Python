import asyncio
import httpx
from collections.abc import Coroutine
from typing import Any
from time import perf_counter

correct_url: str = "http://localhost:8000/api/items"


async def get_request(client: httpx.AsyncClient) -> list[dict]:
    response: httpx.Response = await client.get(correct_url)
    return response.json()


async def main_with_context_manager() -> None:
    async with httpx.AsyncClient() as client:
        coros: list[Coroutine] = []
        for _ in range(1_000):
            coros.append(get_request(client))
        results: tuple[Any] = await asyncio.gather(*coros)
        for r in results:
            print(r)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main_with_context_manager())
    duration = perf_counter() - start
    print(f"Duration: {duration}")

