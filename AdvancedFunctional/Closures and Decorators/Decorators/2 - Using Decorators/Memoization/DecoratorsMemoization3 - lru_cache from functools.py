"""Delegating the memoization mechanism to the functools.lru_cahe decorator"""

from functools import lru_cache

# Least-recently-used cache decorator.
# If *maxsize* is set to None, the LRU feature is disabled and the cache can grow without bound.
# If *typed* is True, arguments of different types will be cached separately. 
# For example, f(3.0) and f(3) will be treated as distinct calls with distinct results.
# Arguments to the cached function must be HASHABLE.

@lru_cache(3) # Up to 8 memoized items
def fibonacci(n):
    print(f"Calculating {n}!")
    return 1 if n < 3 else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10), end="\n\n")
# Calculating 10!
# Calculating 9!
# Calculating 8!
# Calculating 7!
# Calculating 6!
# Calculating 5!
# Calculating 4!
# Calculating 3!
# Calculating 2!
# Calculating 1!
# 55

print(fibonacci(8))
# 21

print(fibonacci(15))
# Calculating 15!
# Calculating 14!
# Calculating 13!
# Calculating 12!
# Calculating 11!
# 610

for k, v in vars(fibonacci).items():
    print(f"{k}: {v}")
# __module__: __main__
# __name__: fibonacci
# __qualname__: fibonacci
# __doc__: None
# __annotations__: {}
# __wrapped__: <function fibonacci at 0x7f1c94a98af0>
