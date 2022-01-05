"""Utilities related to the heavenly spheres."""

from typing import Optional, Dict
from .physics import gravitational_force, law_of_periods


class CelestialBody:
    """Base class for astronomical objects."""

    def __init__(self,
                 name: str,
                 mass: float,
                 daughters: Dict[str, "CelestialBody"] = {},
                 semimajor_axis: Optional[float] = None
                 ) -> None:
        """Define all instance attributes here."""
        self.name = name
        self.mass = mass
        self.daughters = daughters

    def __repr__(self) -> str:
        """Procuce code to initialise this class."""
        return f"CelestialBody({self.name!r}, {self.mass})"

    def __str__(self) -> str:
        """Generate summary of class with minimal inputs."""
        return f"CelestialBody \"{self.name.title()}\": ({self.mass:.2e}kg)"

    def add_semimajor_axis(self, semimajor_axis: float) -> None:
        """Add orbital distance to parent."""
        self.semimajor_axis = semimajor_axis

    def add_daughters(self, daughter: "CelestialBody",
                      semimajor_axis: float) -> None:
        """Add daugters to self."""
        daughter.add_semimajor_axis(semimajor_axis)
        self.daughters[daughter.name] = daughter

    def orbittal_force(self, daughter: str) -> float:
        """Apply Universal Law of Gravitation to specific daughter."""
        return gravitational_force(self.mass,
                                   self.daughters[daughter].mass,
                                   self.daughters[daughter].semimajor_axis)

    def orbittal_period(self, daughter: str) -> float:
        """Apply Kepler's Law of Periods to specific daughter."""
        return law_of_periods(self.mass,
                              self.daughters[daughter].mass,
                              self.daughters[daughter].semimajor_axis)


earth = CelestialBody("Earth", 5.9722*10**24)
