"""This module provides the dataclasses for celestials in astronomical."""

from dataclasses import dataclass
from datetime import (
    timedelta
)
from ..utils.logging import (
    logger
)
from ..model.custom_types import (
    mass,
    radius,
    eccentricity
)


@dataclass
class Body:
    """Base celestial body class."""

    name: str
    mass: mass
    radius: radius

    def __post_init__(self):
        """Add DEBUG logging to classes."""
        logger.debug(f"CLASS: \"{self.__class__.__name__}\" instantiated.")


@dataclass
class OrbittalBody(Body):
    """Base orbittal body class, extends Body()."""

    semimajor_axis: radius
    eccentricity: eccentricity
    orbittal_obliquity: float
    parent: Body


@dataclass
class SpinningBody(Body):
    """Base spinning body class; extends Body()."""

    sidereal_day: timedelta
