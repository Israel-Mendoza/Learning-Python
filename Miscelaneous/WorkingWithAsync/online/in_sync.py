import asyncio
import random
from collections.abc import Coroutine


async def fetch_data() -> str:
    print("Fetching data...")
    await asyncio.sleep(2)
    return "Connard"


async def send_data(data: str, to: str) -> None:
    print(f"Sanding important data '{data}' to {to}...")
    await asyncio.sleep(2)
    print(f"Data sent to {to} successfully!")


async def main() -> None:
    list_of_names: list[str] = [
        "Israel",
        "Luis",
        "Diana",
        "Miguel",
        "Sandra",
        "Victor",
        "Alex"
    ]
    data: str = await fetch_data()

    list_of_coros: list[Coroutine] = [send_data(data, random.choice(list_of_names)) for _ in range(100)]

    await asyncio.gather(*list_of_coros)


if __name__ == "__main__":
    asyncio.run(main())
