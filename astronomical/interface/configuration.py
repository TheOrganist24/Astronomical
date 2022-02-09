"""Interface module for handling user defined configuration."""

import configparser
from datetime import datetime, time, timedelta
from os.path import expanduser
from typing import Any, Dict, List, Optional

from astronomical.model.configuration import SleepRequirements
from astronomical.model.custom_types import (eccentricity, mass, radius,
                                             real_time)
from astronomical.model.solar_system import Planet, PlanetaryLocation, Star


class UserDefaults:
    """Class for handling user defaults set externally.

    Attributes
    ----------
    path (str)                  path to config
    loaded (bool)               the loaded state
    location (str)              name of the location
    longitude (float)           positional longitude
    latitude (float)            positional latitude
    locale (PlanetaryLocation)  localized location to a planet
    sleep (SleepRequirements)   sleeping pattern requirements

    Public Methods
    --------------
    None
    """

    def __init__(self, path: str = f"{expanduser('~')}/.astronomical"
                 ) -> None:
        """Ingest user variables.

        Parameters
        ----------
        path (str)      path to config ("~/.astronomical")

        Returns
        -------
        None
        """
        self.path = path
        self.loaded: bool = False

        config = self._load_config(path)
        self.location: str = config["name"]
        self.longitude: float = config["longitude"]
        self.latitude: float = config["latitude"]
        self.locale: Optional[PlanetaryLocation] = config["planet_location"]
        self.sleep: Optional[SleepRequirements] = config["sleep"]

    def _load_config(self, path: str) -> Dict[str, Any]:
        """Load config and return as dictionary.

        Parameters
        ----------
        path (str)          path to config (explicit)

        Returns
        -------
        data (Dictionary)   data with supplied configuration
        """
        self.loaded = True
        keys: List[str] = ["name", "longitude", "latitude", "planet_location",
                           "sleep"]
        data: Dict = dict.fromkeys(keys)

        config = configparser.ConfigParser()
        config.read(path)

        # if field not there then leave as None
        if "location" in config:
            try:
                for key, value in config["location"].items():
                    if key in ["latitude", "longitude"]:
                        data[key] = float(value)
                    else:
                        data[key] = str(value)
            except TypeError:
                self.loaded = False
                return data
        if "star" in config:
            star_data: Dict[str, Any] = {}
            try:
                star_data["name"] = config["star"]["name"]
                star_data["mass"] = mass(float(config["star"]["mass"]))
                star_data["radius"] = radius(float(config["star"]["radius"]))
                star: Star = Star(**star_data)
                if "planet" in config:
                    planet_data: Dict[str, Any] = {}  # type: ignore
                    planet_data["name"] = config["planet"]["name"]
                    planet_data["mass"] = mass(float(config["planet"]["mass"]))
                    planet_data["radius"] \
                        = radius(float(config["planet"]["radius"]))
                    planet_data["semimajor_axis"] \
                        = radius(float(config["planet"]["semimajor_axis"]))
                    planet_data["eccentricity"] \
                        = eccentricity(float(config["planet"]["eccentricity"]))
                    planet_data["orbital_obliquity"] \
                        = float(config["planet"]["orbital_obliquity"])
                    planet_data["sidereal_day"] \
                        = real_time(
                            seconds=float(config["planet"]["sidereal_day"]))
                    planet_data["ref_march_equinox"] \
                        = datetime.strptime(
                            config["planet"]["ref_march_equinox"],
                            "%Y-%m-%d %H:%M:%S")
                    planet_data["ref_midnight"]\
                        = datetime.strptime(
                            config["planet"]["ref_midnight"],
                            "%Y-%m-%d %H:%M:%S")
                    planet_data["parent"] = star
                    planet: Planet = Planet(**planet_data)
                    planet_location: PlanetaryLocation \
                        = PlanetaryLocation(name=data["name"],
                                            longitude=data["longitude"],
                                            latitude=data["latitude"],
                                            planet=planet)
                    data["planet_location"] = planet_location
            except TypeError as ex:
                print(ex)
                return data
        if "sleep" in config:
            sleep_data: Dict[str, Any] = {}  # type: ignore
            try:
                sleep_data["sleep"] = timedelta(
                    seconds=float(config["sleep"]["sleep"]))
                sleep_data["earliest_wake_up"] = datetime.strptime(
                    config["sleep"]["earliest_wake_up"], "%H:%M:%S").time()
                sleep_data["latest_wake_up"] = datetime.strptime(
                    config["sleep"]["latest_wake_up"], "%H:%M:%S").time()
                sleep_data["ablutions"] = timedelta(
                    seconds=float(config["sleep"]["ablutions"]))
                requirement: SleepRequirements \
                    = SleepRequirements(**sleep_data)
            except TypeError as ex:
                print(ex)
                return data
            data["sleep"] = requirement

        return data
