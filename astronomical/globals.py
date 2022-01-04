"""Utilities related to the heavenly spheres."""

from typing import Optional, Dict
from .physics import gravitational_force


class CelestialBody:
    """Base class for astronomical objects."""

    def __init__(self,
                 name: str,
                 mass: float,
                 daughters: Dict[str, "CelestialBody"] = {},
                 orbital_distance: Optional[float] = None
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

    def add_orbital_distance(self, orbital_distance: float) -> None:
        """Add orbital distance to parent."""
        self.orbital_distance = orbital_distance

    def add_daughters(self, daughter: "CelestialBody",
                      orbital_distance: float) -> None:
        """Add daugters to self."""
        daughter.add_orbital_distance(orbital_distance)
        self.daughters[daughter.name] = daughter
    
    def orbittal_force(self,
                       daughter: str) -> float:
        return gravitational_force(self.mass,
                                   self.daughters[daughter].mass,
                                   self.daughters[daughter].orbital_distance)


earth = CelestialBody("Earth", 5*10**24)
