"""Remembering how the property class works"""

from numbers import Integral


#####################################################################
#####################################################################

# Using the descriptor's @ notation:


class Person1:

    @property
    def age(self):
        return getattr(self, "_age", None)

    @age.setter
    def age(self, value: int):
        if not isinstance(value, Integral):
            raise ValueError("Age must be a valid integer")
        if value < 0:
            raise ValueError("Age must be a positive instance")
        setattr(self, "_age", value)


p = Person1()

try:
    p.age = -10
except ValueError as error:
    print(error)
# Age must be a positive instance


#####################################################################
#####################################################################

# Using the "traditional" notation:

class Person2:

    def get_age(self):
        return getattr(self, "_age", None)

    def set_age(self, value: int):
        if not isinstance(value, Integral):
            raise ValueError("Age must be a valid integer")
        if value < 0:
            raise ValueError("Age must be a positive instance")
        setattr(self, "_age", value)

    age = property(get_age, set_age)


p = Person2()

try:
    p.age = -10
except ValueError as error:
    print(error)
# Age must be a positive instance


print(f"{Person2.age = }")
# Person2.age = <property object at 0x1043bbd80>
print(f"{hasattr(Person2.age, '__get__') = }")
# hasattr(Person2.age, '__get__') = True
print(f"{hasattr(Person2.age, '__set__') = }")
# hasattr(Person2.age, '__set__') = True
print(f"{hasattr(Person2.age, '__del__') = }")
# hasattr(Person2.age, '__del__') = False
print(f"{hasattr(Person2.age, '__set_name__') = }")
# hasattr(Person2.age, '__set_name__') = True
