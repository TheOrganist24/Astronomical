"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass

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
