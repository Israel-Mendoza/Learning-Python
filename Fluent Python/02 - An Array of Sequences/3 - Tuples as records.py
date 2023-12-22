from typing import TypeAlias

Traveler_ID: TypeAlias = tuple[str, str]

traveler_ids: list[Traveler_ID] = [
    ('USA', '31195855'),
    ('BRA', 'CE342567'),
    ('ESP', 'XDA205856'),
    ('MEX', 'MXC123456')
]

# We know the first element of the tuple is the country code, and the second, the code:
for passport in sorted(traveler_ids):
    print(f"{passport[0]}/{passport[1]}")
# BRA/CE342567
# ESP/XDA205856
# MEX/MXC123456
# USA/31195855

# We can then get the country code:
for country, _ in sorted(traveler_ids):
    print(f"Country: {country}")
# Country: BRA
# Country: ESP
# Country: MEX
# Country: USA
