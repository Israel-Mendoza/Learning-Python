# Working with the __bool__ method
# If the __bool__ method is not implemented, it will fall
# back to __len__. If not implemented, the object will always be True


class MyClass:
    pass


obj = MyClass()
# Neither __bool__ nor __len__ has been implemented
print(f"Is 'obj' True or False: {bool(obj)}")  # True


class MyList:
    def __init__(self, length):
        self._length = length

    def __len__(self):
        return self._length


obj_1 = MyList(0)
obj_2 = MyList(10)
# __len__ has been implemented
print(f"Is 'obj_1' True or False: {bool(obj_1)}")  # False (obj._length = 0)
print(f"Is 'obj_2' True or False: {bool(obj_2)}")  # True (obj._length = 10)
print()


class MyList:
    def __init__(self, length):
        self._length = length

    def __len__(self):
        return self._length

    def __bool__(self):
        print("__bool__ called!")
        return self._length > 0


obj_1 = MyList(0)
obj_2 = MyList(10)
# __len__ and __boole hava been implemented
print(f"Is 'obj_1' True or False: {bool(obj_1)}")  # False
print(f"Is 'obj_2' True or False: {bool(obj_2)}")  # True
