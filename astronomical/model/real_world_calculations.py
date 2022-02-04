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
        margin: timedelta = datetime.combine(tomorrow,
                                             self.needs.latest_wake_up) \
            - datetime.combine(tomorrow, self.needs.earliest_wake_up)
        final_wake_up: datetime = datetime.combine(tomorrow,
                                                   self.needs.latest_wake_up)

        self.wake: datetime = self._calculate_wake(now, year,
                                                   latest_vernal_equinox,
                                                   margin,
                                                   final_wake_up)
        self.sleep: datetime = self.wake - self.needs.sleep
        self.work: datetime = self.wake + self.needs.ablutions

    def _calculate_latest_vernal_equinox(self, now: datetime,
                                         ref_vernal_equinox: datetime,
                                         year_length: timedelta) -> datetime:
        """Calculate latest vernal equinox."""
        years_since_ref: float = (now - ref_vernal_equinox).total_seconds() \
            // year_length.total_seconds()
        latest: datetime = ref_vernal_equinox + (years_since_ref * year_length)
        return latest

    def _calculate_wake(self, now: datetime, year_length: timedelta,
                        vernal_equinox: datetime, margin: timedelta,
                        final_wake_up: datetime) -> datetime:
        """Calculate wake-up time."""
        midnight: datetime = datetime.combine(now, time()) \
            + timedelta(hours=24)
        annual_progress: float = (2 * math.pi) * ((midnight - vernal_equinox)
                                                  / year_length)
        offset: timedelta = ((margin * math.sin(annual_progress)) / 2) \
            + (margin / 2)
        alarm: datetime = final_wake_up - offset
        return alarm
