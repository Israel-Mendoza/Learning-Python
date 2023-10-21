"""Simple closure functions"""


def counter(start: int = 0):
    """Creates a counter closure function"""
    count = start

    def incrementer():
        nonlocal count
        # Increment the final object "indirectly"
        count += 1
        return count

    return incrementer


# Creating different closures:
counter_from_0 = counter()
counter_from_10 = counter(10)
counter_from_20 = counter(20)

for i in range(3):
    print(counter_from_0())

print()
for i in range(3):
    print(counter_from_10())

print()
for i in range(3):
    print(counter_from_20())


print(counter_from_0.__code__.co_freevars)
# ('count',)
print(counter_from_0.__closure__)  # The cell object containing the free variable:
# (<cell at 0x0000012E4BF23FD0: int object at 0x0000012E4B8F6970>,)

# Accessing the contents of the free variables:
for i in range(len(counter_from_0.__closure__)):
    print(
        f"{counter_from_0.__code__.co_freevars[i]}: {counter_from_0.__closure__[i].cell_contents}"
    )
# count: 3