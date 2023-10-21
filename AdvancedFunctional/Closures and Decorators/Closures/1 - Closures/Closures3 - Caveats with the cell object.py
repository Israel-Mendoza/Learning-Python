"""Caveats concerning the creation of the intermediary cell object"""

# Empty list to contain the adder closures

my_adders = []

# The following loop will NOT append "closures" to the "my_adders" list
# because "num" is a GLOBAL VARIABLE, therefore no itermediary cell object is created
for num in range(1, 4):
    my_adders.append(lambda x: x + num)

# We have 3 different closures now, riiiight?
for closure in my_adders:
    print(closure.__code__.co_freevars)
    print(closure.__closure__)
# ()
# None
# ()
# None
# ()
# None

# As mentioned above, "num" is a global variable, and it still exists:
print(num)  # 3

# Testing each of the adders with a loop
for adder in my_adders:
    print(adder(10))
# 13, 13, 13 (global num is 3)


print("\n" * 5)


########################################################################################
########################################################################################

# Clear my list
my_adders.clear()

# Defining a function to create closures and append them to the list,
# so "n" is not a global variable:
def adder_list_creator(add_list: list, num_of_functions: int):
    """Runs a loop 'num' times and adds an adder closure to the passed list"""
    for num in range(1, num_of_functions + 1):
        # "num" will always point to the same cell object
        add_list.append(lambda x: x + num)


adder_list_creator(my_adders, 3)

# We have 3 different closures now, riiiight? YES!
# However, all three closures point at the same cell object:
for closure in my_adders:
    print(closure.__code__.co_freevars)
    print(closure.__closure__)
# ('num',)
# (<cell at 0x000002BAA4315190: int object at 0x000002BAA4056970>,)
# ('num',)
# (<cell at 0x000002BAA4315190: int object at 0x000002BAA4056970>,)
# ('num',)
# (<cell at 0x000002BAA4315190: int object at 0x000002BAA4056970>,)

# Accessing the contents of the free variables:
for closure in my_adders:
    for i in range(len(closure.__closure__)):
        print(
            f"{closure.__code__.co_freevars[i]}: {closure.__closure__[i].cell_contents}"
        )
# num: 3
# num: 3
# num: 3

# Testing each of the adders with a loop
# The free variable in all closures in the list point to the same cell object
for adder in my_adders:
    print(adder(10))
# 13, 13, 13


print("\n" * 5)


########################################################################################
########################################################################################

my_adders.clear()

# Defining a function to create closures and append them to the list
def adder_appender(adder_list: list, num: int):
    """Appends an adder with 'num' as the free variable"""
    adder_list.append(lambda x: x + num)


# Looping to add adders to the "my_adders":
# Notice how the adder_appender scope is created and destroyed every time
for i in range(1, 4):
    adder_appender(my_adders, i)


# Now, we DO have individual cell objects per closure, because each scope started
# and ended as the closures were created:
for closure in my_adders:
    print(closure.__code__.co_freevars)
    print(closure.__closure__)
# ('num',)
# (<cell at 0x0000019BB9D33910: int object at 0x0000019BB9A76930>,)
# ('num',)
# (<cell at 0x0000019BB9D338E0: int object at 0x0000019BB9A76950>,)
# ('num',)
# (<cell at 0x0000019BB9D338B0: int object at 0x0000019BB9A76970>,)

# Accessing the contents of the free variables:
for closure in my_adders:
    for i in range(len(closure.__closure__)):
        print(
            f"{closure.__code__.co_freevars[i]}: {closure.__closure__[i].cell_contents}"
        )
# num: 1
# num: 2
# num: 3

# Testing each of the adders with a loop
for adder in my_adders:
    print(adder(10))
# 11, 12, 13


print("\n" * 5)

########################################################################################
########################################################################################

# Clear the list
my_adders.clear()

# Function that returns a closure, where the free variable is the argument passed:
def create_adder(num_to_add):
    return lambda number: number + num_to_add


for i in range(1, 4):
    # We will be appending the returned closure to the list.
    # The appended object is a closure because the scope starts and ends
    # in every iteration:
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

# Accessing the contents of the free variables:
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
