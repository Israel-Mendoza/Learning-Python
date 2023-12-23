a, b, *rest = range(6)
print(f"{a = } {b = } {rest = }")
# a = 0 b = 1 rest = [2, 3, 4, 5]

a, b, *rest = range(2)
print(f"{a = } {b = } {rest = }")
# a = 0 b = 1 rest = []

a, *middle, c, d = range(10)
print(f"{a = } {middle = } {c = } {d = }")
# a = 0 middle = [1, 2, 3, 4, 5, 6, 7] c = 8 d = 9

*start, a, b, c = range(6)
print(f"{start = } {a = } {b = } {c = }")
# start = [0, 1, 2] a = 3 b = 4 c = 5

