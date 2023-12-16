from time import perf_counter, sleep
from typing import Callable

"""USING A CLASS"""


class Timer:
    def __init__(self) -> None:
        # Initializing self._start as the current time
        # returned by time.perf_counter()
        self._start: float = perf_counter()

    def __call__(self) -> float:
        # When the instance is called, it'll return the difference
        # in seconds between the self._start timestamp and the
        # time when the instance is called
        return perf_counter() - self._start


t1 = Timer()
# Waiting two seconds:
sleep(2)
print(t1())  # 2.0116509


###############################################################################
###############################################################################

"""USING A CLOSURE"""


def timer() -> Callable[[], float]:
    # Initializing the free variable "start"
    # with the current time returned by time.perf_counter()
    start: float = perf_counter()

    def inner() -> float:
        # When the closure is called, it'll return the difference
        # in seconds between the free variable "start" timestamp
        # and the time when the closure is called
        return perf_counter() - start

    return inner


t2 = timer()
print(t2.__closure__)
# (<cell at 0x0000023209FB2DC0: float object at 0x0000023209D902F0>,)

# Waiting two seconds:
sleep(2)

print(t2())  # 2.0038031000000003
