"""This module calculates solar system mechanics."""

from datetime import (
    timedelta
)
from ..model.celestials import (
    Star,
    Planet
)


class EarthService:
    """Do caclulations for earth."""

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
                   sidereal_period=timedelta(hours=23,
                                             minutes=56,
                                             seconds=4,
                                             microseconds=90053))
