# environment
SHELL=/bin/bash
EXECUTE=poetry run

# code
PACKAGE=astronomical

# file groups
LINT_GROUP=$(PACKAGE)
TEST_GROUP=tests/.

# targets
## standard
all:

install:

uninstall:

clean:

info:

check: lint test

## less standard
dev-environment:
	cp pre-commit .git/hooks/
	poetry install
lint:
	pycodestyle $(LINT_GROUP)
	pydocstyle $(LINT_GROUP)
	mypy $(LINT_GROUP)

test:
	$(EXECUTE) python3 -m pytest $(TEST_GROUP)

build:
	poetry build

## custom
pre-commit: check
