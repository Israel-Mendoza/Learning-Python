from __future__ import annotations

"""Creating a simple iterator object by implementing the __next__ and __iter__ methods"""


class SquareNumbers:
    def __init__(self, limit: int) -> None:
        print(f"The __init__ method on {hex(id(self)).upper()} was called!")
        self.index: int = 0
        self._limit: int = limit

    def __len__(self) -> int:
        return self._limit

    def __next__(self) -> int:
        address: str = hex(id(self)).upper()
        print(f"The __next__ method on {address} was called!")
        if self.index >= self._limit:
            print(f"The __next__ method on {address} is raising an exception!")
            raise StopIteration
        result: int = self.index ** 2
        self.index += 1
        return result

    def __iter__(self) -> SquareNumbers:
        address: str = hex(id(self)).upper()
        print(f"The __iter__ method on {address} was called!")
        return self


sq = SquareNumbers(10)
# The __init__ method on 0X2C2D35D4FD0 was called!

for i in sq:
    print(i)
# The __iter__ method on 0X2A4BC903FD0 was called! <-- Getting the iterator object
# The __next__ method on 0X2A4BC903FD0 was called!
# 0
# The __next__ method on 0X2A4BC903FD0 was called!
# 1
# The __next__ method on 0X2A4BC903FD0 was called!
# 4
# The __next__ method on 0X2A4BC903FD0 was called!
# 9
# The __next__ method on 0X2A4BC903FD0 was called!
# 16
# The __next__ method on 0X2A4BC903FD0 was called!
# 25
# The __next__ method on 0X2A4BC903FD0 was called!
# 36
# The __next__ method on 0X2A4BC903FD0 was called!
# 49
# The __next__ method on 0X2A4BC903FD0 was called!
# 64
# The __next__ method on 0X2A4BC903FD0 was called!
# 81
# The __next__ method on 0X2A4BC903FD0 was called!
# The __next__ method on 0X2A4BC903FD0 is raising an exception!
