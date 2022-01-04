"""Utilities related to the heavenly spheres."""


class CelestialBody:
    """Base class for astronomical objects."""

    def __init__(self,
                 name: str,
                 mass: float) -> None:
        """Define all instance attributes here."""
        self.name = name
        self.mass = mass

    def __repr__(self) -> str:
        """Procuce code to initialise this class."""
        return f"CelestialBody({self.name!r}, {self.mass})"

    def __str__(self) -> str:
        """Generate summary of class with minimal inputs."""
        return f"CelestialBody \"{self.name.title()}\": ({self.mass:.2e}kg)"


earth = CelestialBody("Earth", 5*10**24)
