from __future__ import annotations
from typing import Any


def print_address(obj_name: str, any_object: Any) -> None:
    print(f"{obj_name} @ {hex(id(any_object)).upper()}")


def print_obj_namespace(an_obj: Any) -> None:
    """
    A simple function that prints the namespace of any passed object.
    This is just for debugging purposes.
    """
    print(f"{an_obj}'s NAMESPACE:")
    for k, v in an_obj.__dict__.items():
        print(f"{an_obj}.{k:12} -> {v}")
    print()


def print_obj_simple_namespace(an_obj: any) -> None:
    print(f"{an_obj}'s NAMESPACE:")
    print(f"{an_obj.__dict__}\n")


def display_obj_namespace_with_class(an_object: any) -> None:
    for k, v in vars(an_object).items():
        print(f"Class attribute '{k}': {v} ({type(v)})")


def get_ref_count(address: int) -> int:
    """
    A simple function that returns the number of
    references to a given object in memory.
    Args:
        address [int]: The address in memory.
    Returns:
        Integer representing the amount of references.
    """
    import ctypes
    return ctypes.c_long.from_address(address).value