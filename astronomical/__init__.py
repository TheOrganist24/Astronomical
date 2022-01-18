"""Library of utilities related to astronomical movements.

This module provides information about the sun, moon, seasons and tides
according to the user's current whereabouts and whenabouts.
"""

import os
import sys
from .logging import logger, setup_logging
from .interfaces.sun import sun_times
from .interfaces.location import Location
from .model.location import (
    default_planetary_location
)
from .interfaces import cli_arguments
defaults = {
    "planetary_location": default_planetary_location
}

setup_logging()
__version__ = "0.1.0"
