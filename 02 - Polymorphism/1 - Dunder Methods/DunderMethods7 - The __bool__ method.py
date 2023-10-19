from __future__ import annotations

"""Working with the __bool__ method"""


# If the __bool__ method is not implemented, it will fall back to __len__.
#
# If none of them are implemented, the object will always be True.


class MyClass:
    pass


obj = MyClass()

# Neither __bool__ nor __len__ has been implemented
print(f"Is 'obj' True or False: {bool(obj)}")  # True


class MyList1:
    def __init__(self: MyList1, length: int) -> None:
        self._length: int = length

    def __len__(self: MyList1) -> int:
        return self._length


obj_1: MyList1 = MyList1(0)
obj_2: MyList1 = MyList1(10)

# __len__ has been implemented
print(f"{bool(obj_1) = }")
print(f"{bool(obj_2) = }")
# bool(obj_1) = False
# bool(obj_2) = True
print()


class MyList2:
    def __init__(self: MyList2, length: int) -> None:
        self._length: int = length

    def __len__(self: MyList2) -> int:
        return self._length

    def __bool__(self) -> bool:
        print("__bool__ called!")
        return self._length > 0


obj_1 = MyList2(0)
obj_2 = MyList2(10)

# __len__ and __bool have been implemented
print(f"{bool(obj_1) = }")
# __bool__ called!
# bool(obj_1) = False
print(f"{bool(obj_2) = }")
# __bool__ called!
# bool(obj_2) = True
