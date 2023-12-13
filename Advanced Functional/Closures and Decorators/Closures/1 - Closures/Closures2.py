"""Simple closure functions"""
from typing import Callable


def counter(start: int = 0) -> Callable[[], int]:
    """Creates a counter closure function"""
    count: int = start

    def incrementer() -> int:
        nonlocal count
        # Increment the final object "indirectly"
        count += 1
        return count

    return incrementer


# Creating different closures:
counter_from_0: Callable[[], int] = counter()
counter_from_10: Callable[[], int] = counter(10)
counter_from_20: Callable[[], int] = counter(20)

for i in range(3):
    print(counter_from_0())

for i in range(3):
    print(counter_from_10())

for i in range(3):
    print(counter_from_20())


print(counter_from_0.__code__.co_freevars)  # A tuple[str, ...] with the names of the free variables
# ('count',)
print(counter_from_0.__closure__)  # A tuple[<class 'cell'>, ...] containing the free variables
# (<cell at 0x0000012E4BF23FD0: int object at 0x0000012E4B8F6970>,)

# Accessing the contents of the free variables:
for i in range(len(counter_from_0.__closure__)):
    print(f"{counter_from_0.__code__.co_freevars[i]}: {counter_from_0.__closure__[i].cell_contents}")
# count: 3
