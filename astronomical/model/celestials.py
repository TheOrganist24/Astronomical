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


@dataclass
class Star(Body):
    """Solar system structure; the primary object."""

    pass


@dataclass
class Planet(SpinningBody, OrbittalBody):
    """Solar system structure; an orbitting object."""

    parent: Star


@dataclass
class Moon(SpinningBody, OrbittalBody):
    """Solar system structure; the orbitter of an orbitting object."""

    parent: Planet


default_star = Star(name="The Sun",
                    mass=1.9885*10**30,
                    radius=696340000)
default_planet = Planet(name="Earth",
                        mass=5.9722*10**24,
                        radius=6371000,
                        semimajor_axis=149.598*10**9,
                        eccentricity=0.014710219,
                        orbittal_obliquity=23.44,
                        parent=default_star,
                        sidereal_period=timedelta(hours=23,
                                                  minutes=56,
                                                  seconds=4,
                                                  microseconds=90053))
