from __future__ import annotations
from typing import Any


class Vector:
    def __init__(self, **components: dict[str, Any]):
        private_components: dict[str, Any] = {f"_{k}": v for k, v in components.items()}
        self.__dict__.update(private_components)

    def __repr__(self):
        components = ", ".join(f"{k[1:]}={v}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({components})"


a: Vector = Vector(x=1, y=2)
print(a.__dict__)
