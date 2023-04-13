from __future__ import annotations
from datetime import datetime
from zoneinfo import ZoneInfo

"""Non-data descriptors"""

# We can change the behavior of the descriptor whether 
# it is accessed from a class or an instance.


class UTCTimeDescriptor:

    """Non-data descriptor"""

    def __get__(self, instance: any, owner: type) -> UTCTimeDescriptor | str:
        """
        Returns the descriptor instance if called from a class.
        Returns the current UTC datetime in ISO format if called
        from a class instance.
        """
        if instance is None:
            return self
        else:
            return datetime.now(tz= ZoneInfo("UTC")).isoformat()


class Logger:
    """A simple logger class"""

    current_time: UTCTimeDescriptor = UTCTimeDescriptor()


# Instantiating the Logger
logger = Logger()

"""Accessing the descriptor"""

# Expecting the descriptor's instance (called from the class)
print(f"{Logger.current_time = }")
# Logger.current_time = <__main__.UTCTimeDescriptor object at 0x7fc52f35e9a0>

# Expecting the time string (called from the class instance)
print(f"{logger.current_time = }")
# logger.current_time = '2021-09-09T03:36:43.399404+00:00'
