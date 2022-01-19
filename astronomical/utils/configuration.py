"""Utility module for setting configurations."""

import configparser
from os.path import expanduser, exists
from ..services.solar_system import (
    PlanetaryLocation,
    earth
)


class Defaults:
    """Default configurations."""

    def __init__(self):
        """Define all instance attributes here."""
        home_dir = expanduser("~")
        self.config_ini = f"{home_dir}/.astronomical"
        self.defaults = {
            "location": {
                "name": None,
                "latitude": None,
                "longitude": None
            }
        }

    def _check_for_user_defined_defaults(self):
        """Check that a user config exists."""
        if exists(self.config_ini):
            return True
        return False

    def _load_defaults(self):
        """Load user configurations.

        If parameters are missing leave blank.
        """
        config = configparser.ConfigParser()
        config.read(self.config_ini)

        for key, value in config["location"].items():
            if key in self.defaults["location"]:
                if key in ["latitude", "longitude"]:
                    self.defaults["location"][key] = float(value)
                else:
                    self.defaults["location"][key] = value

    def location(self):
        """Set user location.

        If entire configuration ismissing, set to London.
        """
        if self._check_for_user_defined_defaults():
            self._load_defaults()
        else:
            self.defaults["location"]["name"] = "London"
            self.defaults["location"]["longitude"] = 0.1276
            self.defaults["location"]["latitude"] = 51.5072
        locale = PlanetaryLocation(self.defaults["location"]["name"],
                                   self.defaults["location"]["longitude"],
                                   self.defaults["location"]["latitude"],
                                   planet=earth)
        return locale
