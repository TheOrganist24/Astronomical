"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass
from .celestials import Planet


@dataclass
class Location:
    """Location on a body."""

    name: str
    longitude: float
    latitude: float


@dataclass
class PlanetaryLocation:
    """Location situated on a planet."""

    planet: Planet
