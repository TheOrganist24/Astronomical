"""This module calculates solar system mechanics."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Tuple

from ..model.celestials import Body
from ..model.custom_types import eccentricity, mass, radius, real_time
from ..model.location import Location
from ..model.physics import (altitude, declination, solar_hour_angle,
                             synodic_day)
from .mechanics import OrbittalMechanicsService, RotationalMechanicsService


@dataclass
class Star(Body):
    """Solar system structure; the primary object."""

    pass


@dataclass
class Planet(RotationalMechanicsService, OrbittalMechanicsService):
    """Solar system structure; an orbitting object."""

    parent: Star
    ref_march_equinox: datetime  # orbittal obliquity spring equinox
    ref_midnight: datetime  # any old midnight

    def _calculate_synodic_day(self) -> real_time:
        """Calculate synodic day from sidereal day and period."""
        sidereal_period: timedelta = \
            self._calculate_orbittal_period()
        year: float = sidereal_period.total_seconds()
        day: float = self.sidereal_day.total_seconds()

        syn_day: real_time = synodic_day(year, day)

        return syn_day


@dataclass
class Moon(RotationalMechanicsService, OrbittalMechanicsService):
    """Solar system structure; the orbitter of an orbitting object."""

    parent: Planet


@dataclass
class PlanetaryLocation(Location):
    """Location situated on a planet."""

    planet: Planet

    def _calculate_sun_times(self, instant: datetime = datetime.now()
                             ) -> Tuple[real_time, real_time]:
        """Calculate the sunrise.

        # if altitude >= 0 or time is after noon:
        #     iterate backwards to find sunrise
        # else:
        #     iterate forwards
        """
        # declare variables
        lat = self.latitude
        lon = self.longitude
        year: timedelta = self.planet._calculate_orbittal_period()
        sidereal_day: real_time = self.planet.sidereal_day
        syn_day: real_time = self.planet._calculate_synodic_day()
        start = ((((instant - self.planet.ref_midnight) // syn_day) * syn_day)
                 + self.planet.ref_midnight)

        current_min_altitude: float = 0.0
        improving: bool = False
        previously_was_improving: bool = False
        horizon_crossing: list = []

        for minute_elapsed in range(0, int(syn_day.total_seconds()/60)):
            calc_time = start + timedelta(minutes=minute_elapsed)

            # calculate variables
            time_since_march_equinox: timedelta = calc_time \
                - self.planet.ref_march_equinox
            ha = (solar_hour_angle(syn_day, timedelta(minutes=minute_elapsed))
                  - lon)
            dec = declination(self.planet.orbittal_obliquity,
                              sidereal_day,
                              time_since_march_equinox)

            calculated_altitude = abs(altitude(lat, dec, ha))

            if calculated_altitude < current_min_altitude:
                current_min_altitude = calculated_altitude
                improving = True
            else:
                improving = False
            if not improving and previously_was_improving:
                horizon_crossing.append(calc_time)
            if not improving and not previously_was_improving:
                current_min_altitude = calculated_altitude

            previously_was_improving = improving
        return horizon_crossing[0], horizon_crossing[1]


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
                                      microseconds=90053),
               ref_march_equinox=datetime(year=2021,
                                          month=3,
                                          day=20,
                                          hour=9,
                                          minute=37),
               ref_midnight=datetime(year=1970,
                                     month=1,
                                     day=1))
