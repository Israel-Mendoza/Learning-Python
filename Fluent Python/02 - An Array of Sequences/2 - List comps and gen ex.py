from array import array
from typing import TypeAlias

T_Shirt: TypeAlias = tuple[str, str]

"""USING LIST COMPREHENSIONS"""

colors: list[str] = ["black", "grey", "white"]
sizes: list[str] = ["S", "M", "L", "XL"]

available_t_shirts: list[T_Shirt] = [(size, color) for size in sizes for color in colors]

for t_shirt in available_t_shirts:
    print(t_shirt)
# ('S', 'black')
# ('S', 'grey')
# ('S', 'white')
# ('M', 'black')
# ('M', 'grey')
# ('M', 'white')
# ('L', 'black')
# ('L', 'grey')
# ('L', 'white')
# ('XL', 'black')
# ('XL', 'grey')
# ('XL', 'white')


##########

"""USING GENERATOR EXPRESSIONS"""

array_of_symbols: array[int] = array("I", (ord(s) for s in "$¢£¥€¤"))

print(array_of_symbols)
# array('I', [36, 162, 163, 165, 8364, 164])

"""T-shirt example"""


for t_shirt in (f"{size} - {color}" for size in sizes for color in colors):
    print(t_shirt)
# S - black
# S - grey
# S - white
# M - black
# M - grey
# M - white
# L - black
# L - grey
# L - white
# XL - black
# XL - grey
# XL - white
