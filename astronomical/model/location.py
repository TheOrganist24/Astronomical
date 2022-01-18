"""This module provides the dataclasses for location in astronomical."""

from dataclasses import dataclass
from ..services.solar_system import (
    Planet,
    earth
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
