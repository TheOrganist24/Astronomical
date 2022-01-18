"""Command line script."""


import argparse
import sys
from loguru import logger
import astronomical
from .interfaces.cli_arguments import (
    Sun,
    Alarms,
    Time
)
from .model.location import default_planetary_location


def main():
    """Provide options for script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show the version and exit",
                        action="store_true")
    parser.add_argument("-s", "--sun", help=Sun.__doc__.lower()[:-1],
                        action="store_true")
    parser.add_argument("-t", "--time", help=Time.__doc__.lower()[:-1],
                        action="store_true")
    parser.add_argument("-a", "--alarms", help=Alarms.__doc__.lower()[:-1],
                        action="store_true")
    args = parser.parse_args()

    if args.version:
        print(astronomical.__version__)
        sys.exit(0)
    elif args.sun:
        sun = Sun(location=default_planetary_location)
        print(sun)
    elif args.time:
        time = Time()
        print(time)
    elif args.alarms:
        alarms = Alarms()
        print(alarms)
