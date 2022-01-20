"""This module calculates solar system mechanics."""

from dataclasses import dataclass
from datetime import (
    timedelta
)
from ..model.celestials import (
    Body
)
from ..model.location import (
    Location
)
from .mechanics import (
    RotationalMechanicsService,
    OrbittalMechanicsService
)


@dataclass
class Star(Body):
    """Solar system structure; the primary object."""

    pass


@dataclass
class Planet(RotationalMechanicsService, OrbittalMechanicsService):
    """Solar system structure; an orbitting object."""

    parent: Star


@dataclass
class Moon(RotationalMechanicsService, OrbittalMechanicsService):
    """Solar system structure; the orbitter of an orbitting object."""

    parent: Planet


@dataclass
class PlanetaryLocation(Location):
    """Location situated on a planet."""

    planet: Planet


sun = Star(name="The Sun",
           mass=1.9885*10**30,
           radius=696340000)

earth = Planet(name="Earth",
               mass=5.9722*10**24,
               radius=6371000,
               semimajor_axis=149.598*10**9,
               eccentricity=0.014710219,
               orbittal_obliquity=23.44,
               parent=sun,
               sidereal_day=timedelta(hours=23,
                                      minutes=56,
                                      seconds=4,
                                      microseconds=90053))
