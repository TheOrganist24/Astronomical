"""This module provides the dataclasses for celestials in astronomical."""

from dataclasses import dataclass

from astronomical.model.custom_types import (eccentricity, mass, radius,
                                             real_time)
from astronomical.service.logging import logger


@dataclass
class Body:
    """Base celestial body class.

    Attributes
    ----------
    name (str)          name of the celestial body
    mass (mass)         bodily mass
    radius (radius)     mean radius; assuming sphere
    """

    name: str
    mass: mass
    radius: radius

    def __post_init__(self) -> None:
        """Add TRACE logging to class."""
        logger.trace(f"CLASS: \"{self.__class__.__name__}\" instantiated.")


@dataclass
class OrbitalBody(Body):
    """Base orbital body class, extending Body.

    Attributes
    ----------
    semimajor_axis (radius)         "A" for parent
    eccentricity (eccentricity)     non-circularity of orbit
    orbital_obliquity (float)      axial tilt relative to orbit
    parent (Body)                   parent body; a star or planet
    """

    semimajor_axis: radius
    eccentricity: eccentricity
    orbital_obliquity: float
    parent: Body


@dataclass
class SpinningBody(Body):
    """Base spinning body class; extending Body.

    Attributes
    ----------
    sidereal_day (real_time)       time taken to complete an axial rotation
    """

    sidereal_day: real_time
