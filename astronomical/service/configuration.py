"""Service module for plumbing User Config and Defaults together."""

from datetime import datetime
from typing import Any, Dict

from astronomical.interface.configuration import UserDefaults
from astronomical.model.configuration import Defaults
from astronomical.service.logging import logger


class DefaultService(Defaults):
    """Default configuration service.

    Attributes
    ----------
    location (str)              name of the location
    longitude (float)           positional longitude
    latitude (float)            positional latitude
    locale (PlanetaryLocation)  localized location to a planet
    state (State)               time dependent PlanetaryLocation
    sleep (SleepRequirements)   sleeping pattern requirements

    Public Methods
    --------------
    None
    """

    def __init__(self, user_defaults: UserDefaults, instant: datetime) -> None:
        """Use UserDefaults to initialise, but default to parent defaults.

        Parameters
        ----------
        user_defaults (UserDefaults)    the user defined part (explicit)
        instant (datetime)              required for parent (explicit)

        Returns
        -------
        None
        """
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        default_data: Dict[str, Any] \
            = self._create_kwargs_for_parent(user_defaults, instant)
        super().__init__(**default_data)

    def _create_kwargs_for_parent(self, user_defaults, instant
                                  ) -> Dict[str, Any]:
        """Create keyword arguments dictionary for initialising parent.

        A dictionary of kwargs will allow for those unset to fall back to the
        default values as set in the parent; in this case, the Model's
        Defaults class.

        Parameters
        ----------
        user_defaults (UserDefaults)    the user defined part (explicit)
        instant (datetime)              required for parent (explicit)

        Returns
        -------
        default_data (Dictionary)       Data with only specified defaults
        """
        default_data: Dict[str, Any] = {}
        if user_defaults.loaded:
            default_data = user_defaults.config

            # Handle naming differences between Default class and user config
            if "name" in default_data:
                default_data["location"] = default_data["name"]
                default_data.pop("name")
            default_data["instant"] = instant
        return default_data
