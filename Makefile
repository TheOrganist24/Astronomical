# environment
SHELL=/bin/bash
EXECUTE=poetry run

# code
PACKAGE=astronomical

# file groups
LINT_GROUP=$(PACKAGE)
TEST_GROUP=tests/test_*.py tests/*/test_*.py

# targets
## standard
all:

install:

uninstall:

clean:

info:

check: format lint test

## less standard
dev-environment:
	cp pre-commit .git/hooks/
	poetry install
format:
	$(EXECUTE) isort $(LINT_GROUP)
lint:
	$(EXECUTE) pycodestyle $(LINT_GROUP)
	$(EXECUTE) pydocstyle $(LINT_GROUP)
	$(EXECUTE) mypy $(LINT_GROUP)

test:
	$(EXECUTE) python3 -m unittest $(TEST_GROUP)

coverage:
	$(EXECUTE) pytest --cov=$(PACKAGE) $(TEST_GROUP)

build:
	poetry build

## custom
pre-commit: lint
