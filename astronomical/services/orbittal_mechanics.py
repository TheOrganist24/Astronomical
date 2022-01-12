"""This module calculates the orbittal mechanics."""

from datetime import timedelta
from ..model.celestials import (
    OrbittalBody,
    SpinningBody
)
from .physics import (
    angular_velocity
)


class RotationalMechanicsService:
    """Execute orbittal calculations."""

    def calculate_axial_velocity(self, spinning_body: SpinningBody) -> float:
        """Convert sidereal period to axial velocity.

        Returns angular velocity (degrees/s).
        """
        return angular_velocity(spinning_body.sidereal_period)
