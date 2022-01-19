"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass


@dataclass
class Location:
    """Location on a body."""

    name: str
    longitude: float
    latitude: float
