from __future__ import annotations


"""Working with the iterable and iterator protocols"""


#####################################################################
# By implementing the __iter__ method, our object is an iteraBLE    #
# By implementing the __iter__ and __next__ methods, our object     #
# will be an iteraTOR                                               #
# The __iter__ method must return the iterator  object and          #
# the __next__ method must implement the logic to return object     #
# when iterated over.                                               #
#####################################################################


"""Implementing the iterator protocol to the same object holding the collection."""


class Cities:
    """Iterator object"""

    def __init__(self) -> None:
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]
        self._index: int = 0

    def __iter__(self) -> Cities:
        """Implementing the iterator protocol"""
        print("Calling __iter__!")
        return self

    def __next__(self) -> str:
        if self._index >= len(self._cities):
            raise StopIteration("Cities are up!")
        result: str = self._cities[self._index]
        self._index += 1
        return result


cities = Cities()

for city in cities:
    print(city)
# Calling __iter__!
# Paris
# London
# Mexico City
# Tokyo

try:
    next(cities)
except StopIteration as ex:
    print(f"{type(ex).__name__}: {ex}")
# StopIteration: Cities are up!


"""Delegating the iterator protocol to another object"""


class Cities:
    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]

    @property
    def cities(self) -> list[str]:
        return self._cities

    def __len__(self) -> int:
        return len(self._cities)


class CitiesIterator:
    def __init__(self, cities_obj: Cities):
        self._cities_obj: Cities = cities_obj
        self._index: int = 0

    def __iter__(self):
        print("Calling __iter__!")
        return self

    def __next__(self):
        if self._index >= len(self._cities_obj):
            raise StopIteration("Cities are up!")
        result: str = self._cities_obj.cities[self._index]
        self._index += 1
        return result


cities_iterator = CitiesIterator(Cities())

print("Using an iterator: ")
for city in cities_iterator:
    print(city)
# Using an iterator:
# Calling __iter__!
# Paris
# London
# Mexico City
# Tokyo

try:
    next(cities_iterator)
except StopIteration as ex:
    print(f"{type(ex).__name__}: {ex}")
# StopIteration: Cities are up!


"""Implementing the iterable protocol in the same class"""


class Cities:
    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]
        self._index = 0

    @property
    def cities(self) -> list[str]:
        return self._cities

    def __iter__(self):
        print("Calling __iter__!")
        return CitiesIterator(self)

    def __next__(self):
        if self._index >= len(self):
            raise StopIteration("Cities are up!")
        result = self._cities[self._index]
        self._index += 1
        return result

    def __len__(self):
        return len(self._cities)


cities_iterator = Cities()

print("Using an iterator: ")
for city in cities_iterator:
    print(city)
# Using an iterator:
# Calling __iter__!
# Paris
# London
# Mexico City
# Tokyo

print("Using an iterator AGAIN: ")
for city in cities_iterator:
    print(city)
# Using an iterator AGAIN:
# Calling __iter__!
# Paris
# London
# Mexico City
# Tokyo


"""Implementing the iterable and the iterator in the same class"""


class Cities:
    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]
        self._index = 0

    class CitiesIterator:
        def __init__(self, cities_obj: Cities):
            self._cities_obj = cities_obj
            self._index = 0

        def __iter__(self):
            print("Calling __iter__!")
            return self

        def __next__(self):
            if self._index >= len(self._cities_obj):
                raise StopIteration("Cities are up!")
            result = self._cities_obj.cities[self._index]
            self._index += 1
            return result

    @property
    def cities(self) -> list[str]:
        return self._cities

    def __getitem__(self, index: int):
        print("Accessing the sequence by index...")
        return self._cities[index]

    def __iter__(self):
        print("Calling __iter__!")
        return CitiesIterator(self)

    def __next__(self):
        if self._index >= len(self):
            raise StopIteration("Cities are up!")
        result = self._cities[self._index]
        self._index += 1
        return result

    def __len__(self):
        return len(self._cities)


cities = Cities()

print(cities[0])
# Accessing the sequence by index...
# Paris
print(cities[1])
# Accessing the sequence by index...
# London
print(cities[2])
# Accessing the sequence by index...
# Mexico City


# Python prefers calling the __iter__ method even though
# there is a __getitem__ method implemented. If no __iter__
# method is found, then it will look for the __getitem__ one.

for city in cities:
    print(city)
# Calling __iter__!
# Paris
# London
# Mexico City
# Tokyo

for city in cities:
    print(city)
# Calling __iter__!
# Paris
# London
# Mexico City
# Tokyo


class Cities:
    def __init__(self):
        self._cities: list[str] = ["Paris", "London", "Mexico City", "Tokyo"]
        self._index = 0

    def __getitem__(self, index: int):
        print("Accessing the sequence by index...")
        return self._cities[index]

    def __len__(self):
        return len(self._cities)


# If no __iter__ method is found, then it will look for the __getitem__ one.

for city in cities:
    print(city)
# Accessing the sequence by index...
# Paris
# Accessing the sequence by index...
# London
# Accessing the sequence by index...
# Mexico City
# Accessing the sequence by index...
# Tokyo
# Accessing the sequence by index...

for city in cities:
    print(city)
# Accessing the sequence by index...
# Paris
# Accessing the sequence by index...
# London
# Accessing the sequence by index...
# Mexico City
# Accessing the sequence by index...
# Tokyo
# Accessing the sequence by index...
