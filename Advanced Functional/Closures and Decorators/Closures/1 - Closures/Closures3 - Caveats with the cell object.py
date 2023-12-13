from typing import Callable

"""
    Caveats concerning the creation of the intermediary cell object.
    
    Remember that, in order for a cell object to be created, 
    the "free" variable's scope must end upon closure's creation. 
    
    If you try to create a "closure" that "captures" an object which
    scope does not end (ex. a global variable), no cell object will be
    created and we'll end up with a simple function that contains a 
    reference to that still existing object. 
"""

# Empty list to contain the adder closures
my_adders: list[Callable[[int], int]] = []

# The following loop will NOT append "closures" to the "my_adders" list because
# "num" is a GLOBAL VARIABLE, therefore no intermediary cell object is created.
for num in range(1, 4):
    my_adders.append(lambda x: x + num)

# We might think we have 3 different closures, riiiight?
for closure in my_adders:
    print(closure.__code__.co_freevars)  # Checking the tuple containing the names of the free variables
    print(closure.__closure__)  # Checking the tuple containing the cell objects
# ()
# None
# ()
# None
# ()
# None

# "num" is a global variable, and it still exists.
# (in Python, a variable created in a for-loop won't cease to exist)
print(num)
# 3


# Testing each of the adders with a loop
for adder in my_adders:
    print(adder(10))
# 13, 13, 13 (global num is 3)


########################################################################################
########################################################################################

# Clearing the list
my_adders.clear()


# Let's try to trick the system by defining a function that creates
# closures and appends them to the list, so "n" is not a global variable:
def adder_list_creator(add_list: list[Callable[[int], int]], num_of_functions: int) -> None:
    """Runs a loop 'num' times and adds an adder closure to the passed list"""
    for n in range(1, num_of_functions + 1):
        # "n" will always point to the same cell object
        add_list.append(lambda x: x + n)


adder_list_creator(my_adders, 3)


# We might think we have 3 different closures now, riiiight?
# YES! The free variable's scope was ended as we left the "adder_list_creator" function.
# However, all three closures point at the same cell object.
for closure in my_adders:
    print(closure.__code__.co_freevars)
    print(closure.__closure__)
# ('num',)
# (<cell at 0x000002BAA4315190: int object at 0x000002BAA4056970>,)
# ('num',)
# (<cell at 0x000002BAA4315190: int object at 0x000002BAA4056970>,)
# ('num',)
# (<cell at 0x000002BAA4315190: int object at 0x000002BAA4056970>,)


# Accessing free variables' information:
for closure in my_adders:
    for i in range(len(closure.__closure__)):
        free_var_name: str = closure.__code__.co_freevars[i]
        free_var_value: int = closure.__closure__[i].cell_contents
        print(f"{free_var_name}: {free_var_value}")
# num: 3
# num: 3
# num: 3


# Testing each of the adders using a loop.
# Remember that the free variable in all closures points to the same cell object.
for adder in my_adders:
    print(adder(10))
# 13, 13, 13


########################################################################################
########################################################################################

# Clearing the list again
my_adders.clear()


# This time, we'll define a function that creates a closure and appends it to the list we'll pass it
def adder_appender(adder_list: list[Callable[[int], int]], n: int) -> None:
    """Appends an adder with 'n' as the free variable"""
    adder_list.append(lambda x: x + n)


# Looping to add adders to the "my_adders":
# Notice how the adder_appender scope is created and destroyed in every loop iteration.
for i in range(1, 4):
    adder_appender(my_adders, i)


# Now, we DO have individual cell objects per closure, because
# each scope started and ended as the closures were created:
for closure in my_adders:
    print(closure.__code__.co_freevars)
    print(closure.__closure__)
# ('num',)
# (<cell at 0x0000019BB9D33910: int object at 0x0000019BB9A76930>,)
# ('num',)
# (<cell at 0x0000019BB9D338E0: int object at 0x0000019BB9A76950>,)
# ('num',)
# (<cell at 0x0000019BB9D338B0: int object at 0x0000019BB9A76970>,)


# # Accessing free variables' information:
for closure in my_adders:
    for i in range(len(closure.__closure__)):
        free_var_name: str = closure.__code__.co_freevars[i]
        free_var_value: int = closure.__closure__[i].cell_contents
        print(f"{free_var_name}: {free_var_value}")
# num: 1
# num: 2
# num: 3


# Testing each of the adders with a loop
for adder in my_adders:
    print(adder(10))
# 11, 12, 13

########################################################################################
########################################################################################

# Clearing the list again
my_adders.clear()


# Function that returns a closure, where the free variable is the argument passed:
def create_adder(num_to_add: int) -> Callable[[int], int]:
    return lambda number: number + num_to_add


# We will be appending the returned closure to the list.
# The appended object is a closure because the wrapper function's scope starts and ends in every iteration:
for i in range(1, 4):
    my_adders.append(create_adder(i))


for closure in my_adders:
    print(closure.__code__.co_freevars)
    print(closure.__closure__)
# ('num_to_add',)
# (<cell at 0x000001F8FFC63940: int object at 0x000001F8FF9A6930>,)
# ('num_to_add',)
# (<cell at 0x000001F8FFC63910: int object at 0x000001F8FF9A6950>,)
# ('num_to_add',)
# (<cell at 0x000001F8FFC635B0: int object at 0x000001F8FF9A6970>,)


# Accessing free variables' information:
for closure in my_adders:
    for i in range(len(closure.__closure__)):
        print(
            f"{closure.__code__.co_freevars[i]}: {closure.__closure__[i].cell_contents}"
        )
# num: 1
# num: 2
# num: 3


# Testing the adders

for adder in my_adders:
    print(adder(10))
# 11, 12, 13...
