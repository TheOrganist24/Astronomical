"""Library of utilities related to astronomical movements.

This module provides information about the sun, moon, seasons and tides
according to the user's current whereabouts and whenabouts.
"""

import os
import sys
from loguru import logger
from .interfaces.sun import sun_times
from .interfaces.location import Location
from .model.location import (
    default_planetary_location
)
from .interfaces import cli_arguments
defaults = {
    "planetary_location": default_planetary_location
}

__version__ = "0.1.0"

# setup logging
log_levels = [
    "DEBUG",  # only for diagnosis
    "INFO",  # things are working as expected
    "WARNING",  # nothing is broken, just something unexpected happened
    "ERROR",  # something has broken
    "CRITICAL"  # everything is on fire
]
logger.remove()
logger.add("example.log", level="INFO")
log_level = os.getenv("LOG_LEVEL")
if not log_level:
    logger.add(sys.stdout, level="ERROR")
elif log_level in (log_levels):
    logger.add(sys.stdout, level=log_level)
else:
    logger.add(sys.stdout, level="DEBUG")
    logger.warning(f"LOGGING: Mistyped environment variable;\n"
                   f"\ttry one of {log_levels}\n"
                   f"\teg. `export LOG_LEVEL=DEBUG`.\n"
                   f"\tLog level will be set to \"DEBUG\".")
