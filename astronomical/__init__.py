"""Library of utilities related to astronomical movements.

This module provides information about the sun, moon, seasons and tides
according to the user's current whereabouts and whenabouts.
"""

from .interfaces.sun import sun_times, SunTimes
from .interfaces.location import Location
from .model.location import (
    default_planetary_location
)

defaults = {
    "planetary_location": default_planetary_location
}

__version__ = "0.1.0"
