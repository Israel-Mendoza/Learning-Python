import asyncio
from collections.abc import Coroutine


"""
    We'll see how to use the asyncio module in Python for asynchronous code. 
    
    We have to main objects:
    
        1. A coroutine - It's an async function that is just called.
        2. A task - A wrapper around a coroutine. 
        
    In order to launch coroutines at the same time, we must create a task.
    A task can be awaited.
    A collection of tasks can be awaited using the asyncio.wait() method.
    
    A coroutine can only be called by using the asyncio.gather() method, 
    or the asyncio.run() method. 
    
    Notice that we can only use the return value of the coroutine when using
    the asyncio.gather method. 
"""

dummy_names: list[str] = ["uno", "dos", "tres"]


async def perform_task(name: str) -> str:
    """An async function that does something really cool."""
    await asyncio.sleep(1)
    return f"Task: '{name}'"


async def handling_tasks_one() -> None:
    """
    Creating a list of tasks, which are created by wrapping
    the called async function with asyncio's "create_task".
    At this point, the tasks are launched.

    These tasks will be passed to asyncio's "wait" method,
    which will await the already launched tasks, and return
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
        result: str = (task.result())  # Calling "result" in a pending tasks will result in an "InvalidStateError"
        print(result)


async def handling_tasks_two() -> None:  # 3.11+
    """
    Same as the previous function, but using a context manager.
    It seems that the context manager will make sure the tasks are done.
    """
    async with asyncio.TaskGroup() as task_group:
        tasks: list[asyncio.Task] = []
        for name in dummy_names:
            tasks.append(task_group.create_task(perform_task(name)))
        # Sets containing done and pending tasks (pending will be populated if timeout is given)
        done, pending = await asyncio.wait(tasks)
        for task in done:
            result: str = (task.result())  # Calling "result" in a pending tasks will result in an "InvalidStateError"
            print(result)


async def handling_single_task() -> None:
    """
    Creating a couple of tasks, which is created by wrapping
    the called async function with asyncio's "create_task".
    At this point, the task is launched.

    We will await them separately, without using any asyncio's methods.
    """
    task_one: asyncio.Task = asyncio.create_task(perform_task("diez"))
    task_two: asyncio.Task = asyncio.create_task(perform_task("veinte"))

    result_one: str = await task_one
    result_two: str = await task_two

    print(result_one, result_two)


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


asyncio.run(handling_tasks_one())
# Task: 'tres'
# Task: 'uno'
# Task: 'dos'


asyncio.run(handling_tasks_two())
# Task: 'uno'
# Task: 'tres'
# Task: 'dos'

asyncio.run(handling_coroutines())
# Task: 'uno'
# Task: 'dos'
# Task: 'tres'

asyncio.run(handling_single_task())
# Task: 'diez' Task: 'veinte'
