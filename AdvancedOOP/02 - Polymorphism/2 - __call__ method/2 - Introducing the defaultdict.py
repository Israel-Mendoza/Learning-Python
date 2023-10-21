from __future__ import annotations
from collections import defaultdict

"""
Implementing a class, which instances will be callables.
We can use these callable objects as "callback" functions
for the defaultdict dictionary. 
The instance will keep track of the times we use the callback, 
and will also return the default value the defaultdict will 
use to assign to missing keys. 
"""


class DefaultValue:
    def __init__(self, default_value: str) -> None:
        """
        Initializes the default value attribute and the counter. 
        Args:
            default_value [str]: The default value to be returned every
                                    time we call the DefaultValue instance.
        """
        self.default_value: str = default_value
        self._counter: int = 0

    @property
    def counter(self: DefaultValue) -> int:
        """The counter attribute of the object"""
        return self._counter

    def __call__(self) -> str:
        """
        Whenever the instance is called, it will return the 
        value stored in the "default_value" instance attribute
        and will increase the _counter attribute by one. 
        """
        self._counter += 1
        return self.default_value


# Creating a couple of DefaultValue instances:
counter_1: DefaultValue = DefaultValue("N/A")
counter_2: DefaultValue = DefaultValue("Undefined")

# Creating a couple of defaultdict instances with our
# DefaultValue instances (remember that they're callable):
my_dict_1: defaultdict[str, str] = defaultdict(counter_1)
my_dict_2: defaultdict[str, str] = defaultdict(counter_2)

# Let's create some key/value pairs in both dictionaries:
my_dict_1["a"] = "Alpha"
my_dict_1["b"] = "Beta"
my_dict_2["g"] = "Gamma"
my_dict_2["d"] = "Delta"

# Trying accessing some keys in both dictionaries:
for letter in "abcde":
    print(f"'{letter}' in my_dict_1 = {my_dict_1[letter]}")
    print(f"'{letter}' in my_dict_2 = {my_dict_2[letter]}")
# 'a' in my_dict_1 = Alpha
# 'a' in my_dict_2 = Undefined
# 'b' in my_dict_1 = Beta
# 'b' in my_dict_2 = Undefined
# 'c' in my_dict_1 = N/A
# 'c' in my_dict_2 = Undefined
# 'd' in my_dict_1 = N/A
# 'd' in my_dict_2 = Delta
# 'e' in my_dict_1 = N/A
# 'e' in my_dict_2 = Undefined

print(f"{counter_1.counter = }")
# counter_1.counter = 3
print(f"{counter_2.counter = }")
# counter_2.counter = 4

########################################################################

# We can create these instances as we are creating the defaultdict instances:

dummy_factory: DefaultValue = DefaultValue("Undefined")
dummy_factory_address: str = hex(id(dummy_factory)).upper()
my_dict_3: defaultdict[str, str] = defaultdict(dummy_factory)

my_dict_3["a"] = "Alpha"
my_dict_3["b"] = "Beta"
my_dict_3["g"] = "Gamma"
my_dict_3["d"] = "Delta"

for char in "abcdefg":
    print(my_dict_3[char])
# Alpha
# Beta
# Undefined
# Delta
# Undefined
# Undefined
# Gamma

# The DefaultValue instance we created for my_dict_3 is stored in .default_factory
print(f"{my_dict_3.default_factory.counter = }")
# my_dict_3.default_factory.counter = 3

print(dummy_factory_address)
# 0X1005F2150
print(hex(id(my_dict_3.default_factory)))
# 0x1005f2150
