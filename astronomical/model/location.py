"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass
from ..utils.logging import (
    log_base_class
)


@dataclass
class Location:
    """Location on a body."""

    name: str
    longitude: float
    latitude: float

    def __post_init__(self):
        """Add DEBUG logging to classes."""
        log_base_class(self.__class__.__name__)
