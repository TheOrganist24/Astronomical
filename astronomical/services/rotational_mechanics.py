"""This module calculates the rotational mechanics."""

from datetime import timedelta
from ..model.celestials import (
    OrbittalBody
)
from .physics import (
    gravitational_force,
    law_of_periods
)


class OrbittalMechanicsService:
    """Execute orbittal calculations."""

    def calculate_gravitational_force(self,
                                      orbitting_body: OrbittalBody) -> float:
        """Apply Universal Law of Gravitation.

        Returns force (N).
        """
        return gravitational_force(orbitting_body.mass,
                                   orbitting_body.parent.mass,
                                   orbitting_body.semimajor_axis)

    def calculate_orbittal_period(self,
                                  orbitting_body: OrbittalBody) -> timedelta:
        """Apply Kepler's Law of Periods to specific daughter.

        Returns period (timedelta).
        """
        return law_of_periods(orbitting_body.mass,
                              orbitting_body.parent.mass,
                              orbitting_body.semimajor_axis)
