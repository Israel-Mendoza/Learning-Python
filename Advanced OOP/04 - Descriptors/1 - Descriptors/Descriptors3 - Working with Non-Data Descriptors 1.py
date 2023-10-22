from __future__ import annotations
from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

"""Non-data descriptors"""

# We can change the behavior of the descriptor whether it is accessed from a class or an instance.


class UTCTimeDescriptor:

    """Non-data descriptor"""

    def __get__(self, instance: Any, owner: type) -> UTCTimeDescriptor | str:
        """
        Returns the descriptor instance if called from a class.
        Returns the current UTC datetime in ISO format if called
        from a class instance.
        """
        if instance is None:
            return self
        else:
            return datetime.now(tz= ZoneInfo("UTC")).isoformat()

    def __repr__(self) -> str:
        return f"UTCTimeDescriptor object @ {hex(id(self)).upper()}"


class Logger:
    """A simple logger class"""
    current_time: UTCTimeDescriptor = UTCTimeDescriptor()


# Instantiating the Logger
logger: Logger = Logger()

"""Accessing the descriptor"""

# Expecting the descriptor's instance (called from the class)
print(f"{Logger.current_time = }")
# Logger.current_time = UTCTimeDescriptor object @ 0X1029C1A60

# Expecting the time string (called from the class instance)
print(f"{logger.current_time = }")
# logger.current_time = '2023-10-22T06:06:19.879964+00:00'
