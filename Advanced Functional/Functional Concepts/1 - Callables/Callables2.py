from datetime import datetime

print(callable(datetime))
# True

result: datetime = datetime(2020, 10, 13)
print(result)
# 2020-10-13 00:00:00

print(type(result))
# <class 'datetime.datetime'>
print(callable(result))
# False

"""Making callable objects"""


class MyClass:
    def __call__(self):
        print("Object was called!")


my_obj = MyClass()
print(type(my_obj))
# <class '__main__.MyClass'>
print(callable(my_obj))
# True
