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
