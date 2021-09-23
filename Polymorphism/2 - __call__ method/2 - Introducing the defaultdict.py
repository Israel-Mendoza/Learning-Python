"""Introducing the defaultdict"""

from collections import defaultdict

# How does the defaultdict work?
#
# It works just like a dictionary.
# However, we must use a callback function when instantiating the dictionary.
# This function will be called whenever a key is not found.
# The return value will be then assigned to the previoysly missing key.


# Defining a "default_value" function to be used by the defaultdict
def default_value1() -> str:
    return "N/A"


# Instantiating a dictionary
my_dict1: defaultdict[str, str] = defaultdict(default_value1)

print(f"{my_dict1 = }")
# my_dict1 = defaultdict(<function default_value at 0x7f66872d8310>, {})

# Creating a couple of keys:
my_dict1["a"] = "Alpha"
my_dict1["b"] = "Beta"

# Accesing the available keys and one not available:
for letter in "abc":
    print(my_dict1[letter])
# Alpha
# Beta
# N/A // # 'c' not found. Callable assigned as default was called and returned instead.

# Final state of my_dict1:
print(f"{my_dict1 = }")
# my_dict1 = defaultdict(<function default_value1 at 0x7ffb56d58310>, {'a': 'Alpha', 'b': 'Beta', 'c': 'N/A'})


"""Counting missing key calls"""

# Let's suppose we want to know how may times the "default_value"
# function was called. We can implement the function as follows:

counter = 0


def default_value2():
    global counter
    counter += 1
    return "N/A"


# Re-instantiating the defaultdict with the new function
my_dict2: defaultdict[str, str] = defaultdict(default_value2)

print(f"{my_dict2 = }")
# my_dict2 = defaultdict(<function default_value2 at 0x7f7488458790>, {})

# Creating a couple of keys:
my_dict2["a"] = "Alpha"
my_dict2["b"] = "Beta"

# Accesing the available keys and a couple of missing ones:
for letter in "abcd":
    print(my_dict2[letter])

# Checking the global "counter" variable:
print(f"{counter}")

# Final state of my_dict1:
print(f"{my_dict2 = }")
# my_dict2 = defaultdict(<function default_value2 at 0x7f7488458790>, {'a': 'Alpha', 'b': 'Beta', 'c': 'N/A', 'd': 'N/A'})


# The drawback with this implementation is that every instantiated "defaultdict"
# will use the same function, and therefore, the same counter.
# We can create instances of the default_value "function" using a custom class
