"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass
from datetime import time, timedelta

from ..service.logging import logger


@dataclass
class Location:
    """Location on a body."""

    name: str
    longitude: float
    latitude: float

    def __post_init__(self):
        """Add DEBUG logging to classes."""
        logger.debug(f"CLASS: \"{self.__class__.__name__}\" instantiated.")


@dataclass
class Requirements:
    """Sleep requirements."""

    sleep: timedelta = timedelta(hours=8)
    latest_wake_up: time = time(hour=7)
    earliest_wake_up: time = time(hour=6)
    ablutions: timedelta = timedelta(hours=1)

    def __post_init__(self):
        """Add DEBUG logging to classes."""
        logger.debug(f"CLASS: \"{self.__class__.__name__}\" instantiated.")
