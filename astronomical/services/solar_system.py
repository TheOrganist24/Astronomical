"""This module calculates solar system mechanics."""

from dataclasses import dataclass
from datetime import timedelta

from ..model.celestials import Body
from ..model.custom_types import eccentricity, mass, radius, real_time
from ..model.location import Location
from .mechanics import OrbittalMechanicsService, RotationalMechanicsService


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
           mass=mass(1.9885*10**30),
           radius=radius(696340000))

earth = Planet(name="Earth",
               mass=mass(5.9722*10**24),
               radius=radius(6371000),
               semimajor_axis=radius(149.598*10**9),
               eccentricity=eccentricity(0.014710219),
               orbittal_obliquity=23.44,
               parent=sun,
               sidereal_day=real_time(hours=23,
                                      minutes=56,
                                      seconds=4,
                                      microseconds=90053))
