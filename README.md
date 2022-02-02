![TheOrganist24 Code](https://hosted.courtman.me.uk/img/logos/theorganist24_banner_code.png "TheOrganist24 Code")

# Astronomical
> Library of utilities related to astronomical movements

This module provides information about the sun, moon, seasons and tides according to the user's current whereabouts and whenabouts.


## Get Started
To install run from inside the directory:
```bash
make dev-environment
make install
astronomical --version
```


### Set a Default Location
You can setup an optional location, if you don't it'll default to London.

```
# ~/.astronomical

[location]
name = "London"
longitude = 0.1276
latitude = 51.5072
```


## Design Notes
![Full Design](img/full_design.png "Full Design")


### Logging Strategy
Logging should be woven throughout the application. Log levels supported here are DEBUG, INFO, WARNING, ERROR, and CRITICAL.
* **DEBUG**:
  * Class instantiations - only done at the most base classes in the model layer to denote the usage of any class
  * Base function invokations - only done on core functions found in the model layer to denote the usage of it
  * Service class method returns - done in the service layer to highlight the outputs of serivce class methods
  * Command line tool argument - done in the package script to show which option is being used
* **INFO**:
  * Interface class instantiations - highlight the beginning of a happy path for a particular option
  * Interface class method returns - to confirm the end of the happy path for a given option
* **WARNING**:
  * Any time there is a "try/except" structure
* **ERROR**:
  * Base functions - capture any unhandled exceptions in the model class
  * Non-trivial service methods - any method in the service layer that does more than just call a base function


## Development
### Setting up Environment
```bash
git clone git@gitlab.com:TheOrganist24/astronomical.git
cd astronomical
make dev-environment
export LOG_LEVEL=INFO  # Optional; supports DEBUG, INFO, WARNING, ERROR, CRITICAL
poetry run astronomical --help
```


### Lint and Test
Code should be compliant with PEPs 8, 256, 484, and 526.
```bash
make check  # calls `make lint; make test`
```
