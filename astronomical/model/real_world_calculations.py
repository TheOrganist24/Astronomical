"""This module calculates sunrise etc."""

import math
from datetime import date, datetime, time, timedelta

from astronomical.model.custom_types import real_time
from astronomical.model.location import Requirements
from astronomical.model.solar_system import PlanetaryLocation


class Alarms:
    """Alarms object."""

    def __init__(self, requirements: Requirements,
                 location: PlanetaryLocation) -> None:
        """Initialise variables."""
        self.needs: Requirements = requirements
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
                                             self.needs.latest_wake_up) \
            - datetime.combine(tomorrow, self.needs.earliest_wake_up)
        final_wake_up: datetime = datetime.combine(tomorrow,
                                                   self.needs.latest_wake_up)
        standard_duration: timedelta = self.needs.sleep
        sleep_duration = self._calculate_sleep_time(annual_progress,
                                                    margin, standard_duration)

        self.wake: datetime = self._calculate_wake(annual_progress,
                                                   margin,
                                                   final_wake_up)
        self.sleep: datetime = self.wake - sleep_duration

        self.work: datetime = self.wake + self.needs.ablutions

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

    def __init__(self, location: PlanetaryLocation,
                 std_time: datetime = datetime.now()) -> None:
        """Initialise object."""
        sunrise, sunset = location.calculate_sun_times()
        day_length: timedelta = location.planet.sidereal_day
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
