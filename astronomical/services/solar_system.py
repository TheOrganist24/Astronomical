"""This module calculates solar system mechanics."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

from ..model.celestials import Body
from ..model.custom_types import angle, eccentricity, mass, radius, real_time
from ..model.location import Location
from ..model.physics import (altitude, declination, elevation,
                             equatorial_coordinates, solar_hour_angle,
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

    def calculate_sun_times(self, instant: datetime = datetime.now()
                            ) -> Tuple[datetime, datetime]:
        """Calculate the sunrise.

        For a given day, start at midnight and iterate through,
        minute-by-minute. Capture the changes in |altitute| when closest to 0
        which will correspond to sunrise and sunset (in that order).
        """
        # redeclare or caclculate variables with simpler names
        lat = self.latitude
        lon = self.longitude
        year: real_time = self.planet._calculate_orbittal_period()
        syn_day: real_time = self.planet._calculate_synodic_day()

        # setup variables to aid with iterating through the day
        start = ((((instant - self.planet.ref_midnight) // syn_day) * syn_day)
                 + self.planet.ref_midnight)
        current_min_altitude: float = 0.0
        improving: bool = False
        previously_was_improving: bool = False
        horizon_crossing: List[datetime] = []

        for minute_elapsed in range(0, int(syn_day.total_seconds()/60)):
            calc_time = start + timedelta(minutes=minute_elapsed)

            # calculate altitude arguments for this iteration
            time_since_march_equinox: timedelta = calc_time \
                - self.planet.ref_march_equinox
            ha = (solar_hour_angle(syn_day, timedelta(minutes=minute_elapsed))
                  - lon)
            dec = declination(self.planet.orbittal_obliquity,
                              year,
                              time_since_march_equinox)

            calculated_altitude = abs(altitude(lat, dec, ha))

            # detect whether there is an improvement in the altitude
            if calculated_altitude < current_min_altitude:
                current_min_altitude = calculated_altitude
                improving = True
            else:
                improving = False
            # detect minimum which indicates sunrise/set
            if not improving and previously_was_improving:
                horizon_crossing.append(calc_time)
            if not improving and not previously_was_improving:
                current_min_altitude = calculated_altitude

            previously_was_improving = improving

        sunrise, sunset = horizon_crossing[0], horizon_crossing[1]
        return sunrise, sunset

    def calculate_equatorial_coords(self, instant: datetime = datetime.now()
                                    ) -> Tuple[angle, angle]:
        """Calculate the right ascension and declination."""
        time_since_vernal_equinox: timedelta = instant \
            - self.planet.ref_march_equinox
        time_since_march_equinox: timedelta = instant \
            - self.planet.ref_march_equinox
        eqc = equatorial_coordinates(time_since_vernal_equinox,
                                     self.planet._calculate_synodic_day(),
                                     self.planet.orbittal_obliquity,
                                     self.planet._calculate_orbittal_period(),
                                     time_since_march_equinox)
        ra_calc, dec_calc = eqc
        ra: angle = angle(360 * (ra_calc / timedelta(hours=24)))
        dec = angle(dec_calc)
        return ra, dec

    def calculate_elevation(self, instant: datetime = datetime.now()
                            ) -> Tuple[angle, angle]:
        """Calculate the azimuth and altitude."""
        syn_day: real_time = self.planet._calculate_synodic_day()
        start = ((((instant - self.planet.ref_midnight) // syn_day) * syn_day)
                 + self.planet.ref_midnight)
        time_since_midnight = instant - start
        time_since_march_equinox: timedelta = instant \
            - self.planet.ref_march_equinox
        dec = declination(self.planet.orbittal_obliquity,
                          self.planet._calculate_orbittal_period(),
                          time_since_march_equinox)
        ha = solar_hour_angle(syn_day, time_since_midnight)

        az_calc, alt_calc = elevation(self.latitude, dec, ha)
        az: angle = angle(az_calc)
        alt: angle = angle(alt_calc)
        return az, alt


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
