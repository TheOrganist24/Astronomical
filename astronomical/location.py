"""Utilities related to location."""


class Location:
    """Location on the globe."""

    def __init__(self, name, longitude, latitude):
        """Define all instance attributes here."""
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.location = (longitude, latitude)

    def __repr__(self):
        """Procuce code to initialise this class."""
        return f"Location({self.name!r}, {self.longitude}, {self.latitude})"

    def __str__(self):
        """Generate summary of class with minimal inputs."""
        return f"Location \"{self.name}\": ({self.longitude}, {self.latitude})"
