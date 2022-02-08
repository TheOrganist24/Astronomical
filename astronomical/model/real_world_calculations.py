"""This module calculates sunrise etc."""

import math
from datetime import date, datetime, time, timedelta
from typing import List, Tuple

from astronomical.model.custom_types import angle, real_time
from astronomical.model.physics import (altitude, declination, elevation,
                                        equatorial_coordinates,
                                        solar_hour_angle)
from astronomical.model.solar_system import PlanetaryLocation


class State:
    """Planetary Location State Object."""

    def __init__(self, instant: datetime, location: PlanetaryLocation) -> None:
        """Initialise variables."""
        self.instant: datetime = instant
        self.locale: PlanetaryLocation = location
        self.suntimes: Tuple[datetime, datetime] = self._calculate_sun_times()
        self.equatorial_coords: Tuple[angle, angle] =\
            self._calculate_equatorial_coords()
        self.elevation: Tuple[angle, angle] = self._calculate_elevation()

    def _calculate_sun_times(self, instant: datetime = datetime.now()
                             ) -> Tuple[datetime, datetime]:
        """Calculate the sunrise.

        For a given day, start at midnight and iterate through,
        minute-by-minute. Capture the changes in |altitute| when closest to 0
        which will correspond to sunrise and sunset (in that order).
        """
        # redeclare or calculate variables with simpler names
        lat = self.locale.latitude
        lon = self.locale.longitude
        year: real_time = self.locale.planet._calculate_orbittal_period()
        syn_day: real_time = self.locale.planet._calculate_synodic_day()

        # setup variables to aid with iterating through the day
        start = ((((instant - self.locale.planet.ref_midnight) // syn_day)
                  * syn_day)
                 + self.locale.planet.ref_midnight)
        current_min_altitude: float = 0.0
        improving: bool = False
        previously_was_improving: bool = False
        horizon_crossing: List[datetime] = []

        for minute_elapsed in range(0, int(syn_day.total_seconds()/60)):
            calc_time = start + timedelta(minutes=minute_elapsed)

            # calculate altitude arguments for this iteration
            time_since_march_equinox: timedelta = calc_time \
                - self.locale.planet.ref_march_equinox
            ha = (solar_hour_angle(syn_day, timedelta(minutes=minute_elapsed))
                  - lon)
            dec = declination(self.locale.planet.orbittal_obliquity,
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

    def _calculate_equatorial_coords(self, instant: datetime = datetime.now()
                                     ) -> Tuple[angle, angle]:
        """Calculate the right ascension and declination."""
        time_since_vernal_equinox: timedelta = instant \
            - self.locale.planet.ref_march_equinox
        time_since_march_equinox: timedelta = instant \
            - self.locale.planet.ref_march_equinox
        syn_day: real_time = self.locale.planet._calculate_synodic_day()
        o_period: real_time = self.locale.planet._calculate_orbittal_period()
        eqc = equatorial_coordinates(time_since_vernal_equinox,
                                     syn_day,
                                     self.locale.planet.orbittal_obliquity,
                                     o_period,
                                     time_since_march_equinox)
        ra_calc, dec_calc = eqc
        ra: angle = angle(360 * (ra_calc / timedelta(hours=24)))
        dec = angle(dec_calc)
        return ra, dec

    def _calculate_elevation(self, instant: datetime = datetime.now()
                             ) -> Tuple[angle, angle]:
        """Calculate the azimuth and altitude."""
        syn_day: real_time = self.locale.planet._calculate_synodic_day()
        start = ((((instant - self.locale.planet.ref_midnight) // syn_day)
                  * syn_day)
                 + self.locale.planet.ref_midnight)
        time_since_midnight = instant - start
        time_since_march_equinox: timedelta = instant \
            - self.locale.planet.ref_march_equinox
        dec = declination(self.locale.planet.orbittal_obliquity,
                          self.locale.planet._calculate_orbittal_period(),
                          time_since_march_equinox)
        ha = solar_hour_angle(syn_day, time_since_midnight)

        az_calc, alt_calc = elevation(self.locale.latitude, dec, ha)
        az: angle = angle(az_calc)
        alt: angle = angle(alt_calc)
        return az, alt


class Alarms:
    """Alarms object."""

    def __init__(self, duration: timedelta, latest: time, earliest: time,
                 ablutions: timedelta,
                 location: PlanetaryLocation) -> None:
        """Initialise variables."""
        self.duration = duration
        self.latest = latest
        self.earliest = earliest
        self.ablutions = ablutions
        self.locale: PlanetaryLocation = location

        now: datetime = datetime.now()
        tomorrow: date = (now + self.locale.planet.sidereal_day).date()
        year: real_time = self.locale.planet._calculate_orbittal_period()
        ref_vernal_equinox: datetime = self.locale.planet.ref_march_equinox
        latest_vernal_equinox: datetime = \
            self._calculate_latest_vernal_equinox(now, ref_vernal_equinox,
                                                  year)
        annual_progress =\
            self._calculate_annual_progress(now, year, latest_vernal_equinox)
        margin: timedelta = datetime.combine(tomorrow,
                                             self.latest) \
            - datetime.combine(tomorrow, self.earliest)
        final_wake_up: datetime = datetime.combine(tomorrow,
                                                   self.latest)
        standard_duration: timedelta = self.duration
        sleep_duration = self._calculate_sleep_time(annual_progress,
                                                    margin, standard_duration)

        self.wake: datetime = self._calculate_wake(annual_progress,
                                                   margin,
                                                   final_wake_up)
        self.sleep: datetime = self.wake - sleep_duration

        self.work: datetime = self.wake + self.ablutions

    def _calculate_latest_vernal_equinox(self, now: datetime,
                                         ref_vernal_equinox: datetime,
                                         year_length: timedelta) -> datetime:
        """Calculate latest vernal equinox."""
        years_since_ref: float = (now - ref_vernal_equinox).total_seconds() \
            // year_length.total_seconds()
        latest: datetime = ref_vernal_equinox + (years_since_ref * year_length)
        return latest

    def _calculate_annual_progress(self, now: datetime,
                                   year_length: timedelta,
                                   vernal_equinox: datetime) -> float:
        """Calculate annual progress: break this out."""
        midnight: datetime = datetime.combine(now, time()) \
            + timedelta(hours=24)
        annual_progress: float = (2 * math.pi) * ((midnight - vernal_equinox)
                                                  / year_length)
        return annual_progress

    def _calculate_sleep_time(self, annual_progress: float, margin: timedelta,
                              normal_length: timedelta):
        """Calculate sleep duration."""
        calc_length: timedelta = normal_length - (margin *
                                                  math.sin(annual_progress))
        return calc_length

    def _calculate_wake(self, annual_progress: float, margin: timedelta,
                        final_wake_up: datetime) -> datetime:
        """Calculate wake-up time."""
        offset: timedelta = ((margin * math.sin(annual_progress)) / 2) \
            + (margin / 2)
        alarm: datetime = final_wake_up - offset
        return alarm


class Time:
    """Object for calculating NAC time.

    NAC time is defined as one period of each day and night, where each period
    has exactly twelve hours. This leads to hours during each period being
    different lengths too each other; summer day hours are longer while summer
    night hours are shorter. Sunrise and sunset is defined as being 6am and
    6pm respectively.
    """

    def __init__(self, state: State,
                 std_time: datetime = datetime.now()) -> None:
        """Initialise object."""
        sunrise, sunset = state.suntimes
        day_length: timedelta = state.locale.planet.sidereal_day
        self.nac: datetime = \
            self._calculate_nac_time(std_time, sunrise, sunset, day_length)

    def _calculate_nac_time(self, std_time: datetime, sunrise: datetime,
                            sunset: datetime, sidereal_day: timedelta
                            ) -> datetime:
        """Calculate NAC time.

        NAC is the calculated time (NACs is NAC seconds)
        STD is the standard time (STDs is standard seconds)
        """
        midnight: datetime = datetime.combine(std_time.date(), time())
        nac_daylight: int = 43200
        nac_night: int = 43200
        std_daylight: int = int((sunset - sunrise).total_seconds())
        std_night: int = int(sidereal_day.total_seconds() - std_daylight)

        # Calculate day and night NACs/STDs
        day_NACpSTD: float = nac_daylight / std_daylight
        night_NACpSTD: float = nac_night / std_night

        # Calculate time based on day/night window
        if std_time < sunrise:
            s_since_midnight: float = (std_time - midnight).total_seconds()
            NACs_elapsed: int = int(night_NACpSTD * s_since_midnight)
            NACs: timedelta = timedelta(seconds=NACs_elapsed)
        elif std_time >= sunrise and std_time < sunset:
            s_since_sunrise: float = (std_time - sunrise).total_seconds()
            NACs_elapsed = int(day_NACpSTD * s_since_sunrise)
            NACs = timedelta(seconds=NACs_elapsed) + timedelta(seconds=21600)
        elif std_time >= sunset:
            s_since_sunset: float = (std_time - sunset).total_seconds()
            NACs_elapsed = int(night_NACpSTD * s_since_sunset)
            NACs = timedelta(seconds=NACs_elapsed) + timedelta(seconds=64800)

        NAC_time: datetime = midnight + NACs
        return NAC_time
