"""Command line script."""


import argparse
import sys
from datetime import datetime

from loguru import logger

import astronomical
from astronomical.interface.configuration import UserDefaults
from astronomical.model.real_world_calculations import Alarms, Time
from astronomical.service.configuration import DefaultService
from astronomical.service.requirements import (AlarmsService, SunService,
                                               TimeService)


def main():
    """Provide options for script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show the version and exit",
                        action="store_true")
    parser.add_argument("-s", "--sun", help=SunService.__doc__.lower()[:-1],
                        action="store_true")
    parser.add_argument("-t", "--time", help=TimeService.__doc__.lower()[:-1],
                        action="store_true")
    parser.add_argument("-a", "--alarms",
                        help=AlarmsService.__doc__.lower()[:-1],
                        action="store_true")
    args = parser.parse_args()

    # supply config
    instant: datetime = datetime.now()
    defaults = DefaultService(UserDefaults(), instant)

    # parse main function arguments
    if args.version:
        print(astronomical.__version__)
        sys.exit(0)
    elif args.sun:
        logger.debug(f"CLI OPTION: \"sun\" invoked.")
        sun = SunService(defaults.state)
        print(sun)
    elif args.time:
        logger.debug(f"CLI OPTION: \"time\" invoked.")
        time = TimeService(Time(defaults.state, instant))
        print(time)
    elif args.alarms:
        logger.debug(f"CLI OPTION: \"alarms\" invoked.")
        alarms = AlarmsService(
            Alarms(defaults.sleep.sleep,
                   defaults.sleep.earliest_wake_up,
                   defaults.sleep.latest_wake_up,
                   defaults.sleep.ablutions,
                   defaults.state.locale))
        print(alarms)
