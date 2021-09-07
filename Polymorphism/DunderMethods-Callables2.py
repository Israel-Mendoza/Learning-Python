from collections import defaultdict

# Creating a case use of the callable method of an object

# First, let's see how the "defaultdict" works

# Defining a "default_value" function to be used by the defaultdict
def default_value():
    return "N/A"


# Instantiating a dictionary
my_dict = defaultdict(default_value)
print(my_dict)
# Creating a couple of keys:
my_dict["a"] = "Alpha"
my_dict["b"] = "Beta"

# Accesing the available keys and one not available:
print(f"Accessing keys 'a', 'b', and 'c' in the dictionary: ")
for letter in "abc":
    print(my_dict[letter])

# The 'c' key was not found, and was assigned the default value from the "default_value" function

# Let's suppose we want to know how may times the "default_value" function was called
# We can implement the function as follows:


def default_value():
    global counter
    counter += 1
    return "N/A"


# The previous function will always need a global counter variable to update
counter = 0

# Re-instantiating the defaultdict with the new function
my_dict = defaultdict(default_value)

# Creating a couple of keys:
my_dict["a"] = "Alpha"
my_dict["b"] = "Beta"

# Accesing the available keys and one not available:
print(f"Accessing keys 'a', 'b', 'c', and 'd' in the dictionary: ")
for letter in "abcd":
    print(my_dict[letter])

# Checking the global "counter" variable:
print(f"Mismatch counter: {counter}")

# The drawback with this implementation is that every instantiated "defaultdict"
# will use the same function, and therefore, the same counter.
# We can create instances of the default_value "function" using a custom class
