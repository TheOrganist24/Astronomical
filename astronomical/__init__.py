"""Library of utilities related to astronomical movements.

This module provides information about the sun, moon, seasons and tides
according to the user's current whereabouts and whenabouts.
"""

from .interfaces.sun import sun_times
from .interfaces.location import Location


home = Location("Ivybridge", -3.9413, 50.3921)

__version__ = "0.1.0"
sunrise, sunset = sun_times(home)
