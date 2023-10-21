"""Item getters"""

import operator
from operator import attrgetter, ge

# Creating a list
my_list = [1, 2, 3, 4, 5]

print(my_list[2])  # 3
print(operator.getitem(my_list, 2))  # 3

# Setting items in a mutable sequence
my_list[0] = 100
operator.setitem(my_list, 1, 200)
print(my_list)  # [100, 200, 3, 4, 5]

# Deleting items in a mutable sequence
del my_list[-1]
operator.delitem(my_list, -1)
print(my_list)  # [100, 200, 3]

"""Using itemgetter"""

# Think of itemgetter as a partial function that receives an index.
# It returns a callable, which will then receive a sequence.
# This callable returns the item at the provided index.

get_first_item = operator.itemgetter(0)
print(get_first_item("python"))  # "p"
print(get_first_item([2, 1, 4, 0]))  # 2
print(get_first_item(("G", "O", 2, 0)))  # "G"

get_second_item = operator.itemgetter(1)
print(get_second_item("python"))  # "y"
print(get_second_item([2, 1, 4, 0]))  # 1
print(get_second_item(("G", "O", 2, 0)))  # "O"

# When itemgetter is passed more than one argument,
# the returning function will return a tuple
get_first_second = operator.itemgetter(0, 1)
print(get_first_second("python"))  # ('p', 'y')
print(get_first_second([2, 1, 4, 0]))  # (2, 1)
print(get_first_second(("G", "O", 2, 0)))  # ('G', 'O')


"""Using attrgetter"""

# Think of attrgetter as a partial function that receives an attribute name.
# It returns a callable, which will then receive an only.
# This callable return the object's attribute's value.


class MyClass:
    def __init__(self):
        self.a = "A"
        self.b = "B"

    def test(self):
        print(f"Object says hello!")


my_obj = MyClass()

getting_a = operator.attrgetter("a")
getting_b = operator.attrgetter("b")
getting_test = operator.attrgetter("test")
print(f"{type(getting_a(my_obj))} - {getting_a(my_obj)}")  # <class 'str'> - 'A'
print(f"{type(getting_b(my_obj))} - {getting_b(my_obj)}")  # <class 'str'> - 'B'
print(type(getting_test(my_obj)))  # <class 'method'>
getting_test(my_obj)()  # Object says hello!
