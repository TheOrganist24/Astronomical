"""This module provides the dataclasses for celestials in astronomical."""

from dataclasses import dataclass
from datetime import (
    timedelta
)


@dataclass
class Body:
    """Base celestial body class."""

    name: str
    mass: float
    radius: float


@dataclass
class OrbittalBody(Body):
    """Base orbittal body class, extends Body()."""

    semimajor_axis: float
    eccentricity: float
    orbittal_obliquity: float
    parent: Body


@dataclass
class SpinningBody(Body):
    """Base spinning body class; extends Body()."""

    sidereal_period: timedelta
