"""This module calculates sunrise etc."""

from datetime import datetime, timedelta

from astronomical.model.location import Requirements
from astronomical.model.solar_system import PlanetaryLocation


class Alarms:
    """Alarms object."""

    def __init__(self, requirements: Requirements,
                 location: PlanetaryLocation) -> None:
        """Initialise variables."""
        self.needs: Requirements = requirements
        self.locale: PlanetaryLocation = location
        self.wake: datetime = self._calculate_wake()
        self.sleep: datetime = self.wake + self.needs.sleep
        self.work: datetime = self.wake + self.needs.ablutions

    def _calculate_wake(self) -> datetime:
        """Calculate wake-up time."""
        # Add code here to calculate wake-up time
        return datetime.now()
