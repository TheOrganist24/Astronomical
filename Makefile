# environment
SHELL=/bin/bash

# code
PACKAGE=astronomical
SCRIPT=bin/astronomical

# file groups
LINT_GROUP=$(PACKAGE) $(SCRIPT)
TEST_GROUP=tests/.

pre-commit: lint test

lint:
	pycodestyle $(LINT_GROUP)
	pydocstyle $(LINT_GROUP)
	mypy $(LINT_GROUP)

test:
	poetry run python3 -m pytest $(TEST_GROUP)
