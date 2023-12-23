"""
    Sequence patterns may be written as tuples or lists
    or any combination of nested tuples and lists, but
    it makes no difference which syntax you use: in a sequence
    pattern, square brackets and parentheses mean the same thing.

    The _ symbol is special in patterns: it matches any single
    item in that position, but it is never bound to the value of
    the matched item. Also, the _ is the only variable that can
    appear more than once in a pattern.

    If we want to add type checker in the pattern, we wrap the
    variable with the type we're checking against. It'll look
    something like this:
        case [str(name), _, _, (float(lat), float(lon))]

    The expressions str(name) and float(lat) look like constructor calls,
    which we’d use to convert name and lat to str and float. But in the
    context of a pattern, that syntax performs a runtime type check:
    the preceding pattern will match a four-item sequence in which
    item 0 must be a str, and item 3 must be a pair of floats.
    Although str(name) borrows the syntax of a constructor call,
    the semantics are completely different in the context of a pattern.
"""


metro_areas: list[tuple[str, str, float, tuple[float, float]]] = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
for city in metro_areas:
    match city:
        case [str(name), *_, [float(lat), float(lon)]] if lon <= 0:  # Grabbing the city in the western hemisphere
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
#                 |  latitude | longitude
# Mexico City     |   19.4333 |  -99.1333
# New York-Newark |   40.8086 |  -74.0204
# São Paulo       |  -23.5478 |  -46.6358


