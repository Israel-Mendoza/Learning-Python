import asyncio
from collections.abc import Coroutine

dummy_names: list[str] = ["uno", "dos", "tres"]


async def perform_task(name: str) -> str:
    """An async function that does something really cool."""
    print(f"Task: '{name}' started.")
    await asyncio.sleep(3)
    print(f"Task: '{name}' finished.")
    return f"Task: '{name}'"


async def handling_tasks_one() -> None:
    """
    Creating a list of tasks, which are created by wrapping
    the called async function with asyncio's "create_task".

    These tasks will be passed to asyncio's "wait" method,
    which will launch all tasks at the same time, and return
    a tuple of sets.
    Each set contains the tasks that have been "waited".
        1. The first element in the tuple will contain the
        tasks that were fully awaited.
        2. The second element in the tuple will contain the
        tasks that were not fully awaited, due to an optional
        timeout.
    """
    tasks: list[asyncio.Task] = []
    for name in dummy_names:
        tasks.append(asyncio.create_task(perform_task(name)))

    # Sets containing done and pending tasks (pending will be populated if timeout is given)
    done, pending = await asyncio.wait(tasks)
    for task in done:
        result: str = (
            task.result()
        )  # Calling "result" in a pending tasks will result in an "InvalidStateError"
        print(result)


async def handling_tasks_two() -> None:  # 3.11+
    """Same as the previous function, but using a context manager."""
    async with asyncio.TaskGroup() as task_group:
        tasks: list[asyncio.Task] = []
        for name in dummy_names:
            tasks.append(task_group.create_task(perform_task(name)))
        # Sets containing done and pending tasks (pending will be populated if timeout is given)
        done, pending = await asyncio.wait(tasks)
        for task in done:
            result: str = (
                task.result()
            )  # Calling "result" in a pending tasks will result in an "InvalidStateError"
            print(result)


async def handling_single_task() -> None:
    """
    Creating a task, which is created by XXXXXXXX
    the called async function with asyncio's "create_task".

    This task will be passed to asyncio's "wait" method,
    which will launch this task at the same time, and return
    a tuple of sets.
    Each set contains the tasks that have been "waited".
        1. The first element in the tuple will contain the
        tasks that were fully awaited.
        2. The second element in the tuple will contain the
        tasks that were not fully awaited, due to an optional
        timeout.
    """
    task_one: asyncio.Task = asyncio.create_task(perform_task("diez"))
    task_two: asyncio.Task = asyncio.create_task(perform_task("veinte"))

    # result_one: str = await task_one
    # result_two: str = await task_two

    # print(result_one, result_two)


async def handling_coroutines() -> None:
    """
    Creating a list of coroutines, which are created
    by calling the async function.

    These coroutines will be passed to asyncio's "gather" method,
    which will launch all coroutines and return a tuple of the
    coroutines' return values.
    """
    coroutines: list[Coroutine] = []
    for name in dummy_names:
        coroutines.append(perform_task(name))

    results: list[str] = await asyncio.gather(*coroutines)
    for result in results:
        print(result)


# asyncio.run(handling_tasks_one())
# Task: 'tres'
# Task: 'uno'
# Task: 'dos'


# asyncio.run(handling_tasks_two())
# Task: 'uno'
# Task: 'tres'
# Task: 'dos'

# asyncio.run(handling_coroutines())
# Task: 'uno'
# Task: 'dos'
# Task: 'tres'

asyncio.run(handling_single_task())
