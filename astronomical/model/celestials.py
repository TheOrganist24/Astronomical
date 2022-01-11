"""This module provides the dataclasses for celestials in astronomical."""

from dataclasses import dataclass


@dataclass
class Body:
    """Base celestial body class."""

    name: str
    mass: float


@dataclass
class OrbitalBody(Body):
    """Base orbittal body class, extends Body()."""

    semimajor_axis: float
    eccentricity: float
    parent: Body
