![TheOrganist24 Code](https://hosted.courtman.me.uk/img/logos/theorganist24_banner_code.png "TheOrganist24 Code")

# Astronomical
> Library of utilities related to astronomical movements

This module provides information about the sun, moon, seasons and tides according to the user's current whereabouts and whenabouts.


## Get Started
Once installed run:
```bash
astronomical --help
```

### Set a Default Location
```
# .astronomical.ini

[location]
name = "London"
longitude = 0.1276
latitude = 51.5072
```

## Development
### Setting up Environment
```bash
git clone git@gitlab.com:TheOrganist24/astronomical.git
cd astronomical
make dev-environment
export LOG_LEVEL=ERROR  # Optional; supports DEBUG, INFO, WARNING, ERROR, CRITICAL
poetry run python3 example.py
```

### Lint and Test
Code should be compliant with PEPs 8, 256, 484, and 526.
```bash
make lint
make test
```
