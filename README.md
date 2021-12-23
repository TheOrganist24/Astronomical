![TheOrganist24 Code](https://hosted.courtman.me.uk/img/logos/theorganist24_banner_code.png "TheOrganist24 Code")

# Astronomical
> Library of utilities related to astronomical movements

## Get Started
```
git clone git@gitlab.com:TheOrganist24/astronomical.git
cd astronomical
poetry install
poetry run python3 example.py
```

## Components
### The Daily Hours
See [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4720388/) which seems to suggest that natural sleep cycles are determined by temperature and sunrise times.  A rough summary for our purposes is that there is a sleep variation of ~1 hour between summer and winter (based around the soltices as maxima and minima) and that sleep length ranges from ~7-9 hours.  Additionally awakening time seems to be most directly correlated to sunrise and thus dictates the settling down to sleep time.

This component assumes a get up time closest to sunrise (within an optional varience), and an optionally defined sleep duration and varience.

![Sleep Flow](img/sleep_flow.png "Sleep Flow")

This component provides the following:
```
sunrise, sunset = astronomical.sun.sun_times(location)
sleep_duration = astronomical.sleep.duration(requirements, location)  # to be implemented
bedtime, morning_alarm = astronomical.sleep.alarms(requirements, location)  # to be implemented
```


## Development
### Lint and Test
Code should be compliant with PEPs 8, 256, 484, and 526.
```
for LINTER in "pydocstyle" "pycodestyle" "mypy"
do 
  echo Running $LINTER
  $LINTER astronomical && echo -e " -> \e[32mpassed\e[0m" || echo -e " -> \e[31mfailed\e[0m"
done
```

To test:
```
poetry run python3 -m pytest tests/.
```
