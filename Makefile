# environment
SHELL=/bin/bash
EXECUTE=poetry run
VERSION=$$(cat VERSION)

# code
PACKAGE=astronomical

# file groups
LINT_GROUP=$(PACKAGE)
TEST_GROUP=tests/test_*.py tests/*/test_*.py
CLEAN_GROUP=$(PACKAGE) tests/
DELETE_GROUP=$(dist .pytest_cache .mypy_cache)

# targets
## standard
all: build

install:
	python3 -m pip install ./dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl

uninstall:
	python3 -m pip uninstall $(PACKAGE)

clean:
	rm -rf $(DELETE_GROUP)
	pyclean $(CLEAN_GROUP)

info:

check: format lint test

## less standard
dev:
	cp pre-commit .git/hooks/
	poetry install

pre-commit: lint

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

fresh: clean dev
	poetry update