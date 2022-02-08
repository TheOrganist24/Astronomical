"""Utility module for setting configurations."""

from datetime import datetime

from astronomical.interface.configuration import UserDefaults
from astronomical.model.configuration import Defaults


class DefaultService(Defaults):
    """Default configuration."""

    def __init__(self, user_defaults: UserDefaults, instant: datetime) -> None:
        """Initialise variables."""
        if user_defaults.loaded:
            location = user_defaults.location
            longitude = user_defaults.longitude
            latitude = user_defaults.latitude
            if user_defaults.locale is not None:
                planet = user_defaults.locale
                super().__init__(location=location, longitude=longitude,
                                 latitude=latitude,
                                 planet=planet,  # type: ignore
                                 instant=instant)
            else:
                super().__init__(location=location, longitude=longitude,
                                 latitude=latitude, instant=instant)
