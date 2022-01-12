"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass
from .celestials import (
    Planet,
    default_planet as earth
)


@dataclass
class Location:
    """Location on a body."""

    name: str
    longitude: float
    latitude: float


@dataclass
class PlanetaryLocation(Location):
    """Location situated on a planet."""

    planet: Planet


default_location = Location("London", 0.1276, 51.5072)
default_planetary_location = PlanetaryLocation("London",
                                               0.1276,
                                               51.5072,
                                               earth)
