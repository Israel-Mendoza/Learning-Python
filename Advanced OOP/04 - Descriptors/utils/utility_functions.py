from __future__ import annotations
from typing import Any


def print_address(obj_name: str, any_object: Any) -> None:
    print(f"{obj_name} @ {hex(id(any_object)).upper()}")
