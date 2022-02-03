"""Library of utilities related to astronomical movements.

This module provides information about the sun, moon, seasons and tides
according to the user's current whereabouts and whenabouts.
"""

import os
import sys

from .utils.logging import logger, setup_logging

setup_logging()

__version__ = "0.3.0"
