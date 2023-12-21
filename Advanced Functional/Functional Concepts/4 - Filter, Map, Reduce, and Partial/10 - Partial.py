from functools import partial
from math import sqrt
from typing import TypeAlias

"""Why would we ever need partial functions?"""

"""
    The sorted function's key argument needs a callable that only takes one argument.
    
    Let's suppose we want to sort a list of points represented by tuples,
    ordered based on their distance to the a given point (origin in this example).
    The function passed as the key to the sorted function must only take one argument,
    and return the value that will then be sorted.
    Partial functions may help us reducing the amount of parameters
    we pass to this key callback function
"""

# Creating a type alias for the Point
Point: TypeAlias = tuple[int | float, int | float]


# A function that takes 2 arguments.
def point_distance(a: Point, b: Point) -> float:
    """Returns the distance of two points represented by a tuple."""
    d: float = sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return d


# The list of points to sort
my_points: list[Point] = [(1, 2), (2, 3), (5, 5), (0, 0), (1, 1), (-5, 2)]

# Reducing the amount of arguments to the point_distance function.
distance_from_origin = partial(point_distance, (0, 0))

# Sorting the my_points list. Remember the key callback takes only one argument
my_ordered_points = sorted(my_points, key=distance_from_origin)

print(my_ordered_points)
# [(0, 0), (1, 1), (1, 2), (2, 3), (-5, 2), (5, 5)]
