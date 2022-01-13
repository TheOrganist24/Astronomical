# environment
SHELL=/bin/bash
EXECUTE=poetry run

# code
PACKAGE=astronomical
SCRIPT=bin/astronomical

# file groups
LINT_GROUP=$(PACKAGE) $(SCRIPT)
TEST_GROUP=tests/.

# targets
## standard
all:

install:

uninstall:

clean:

info:

check: lint test

## particulars
lint:
	pycodestyle $(LINT_GROUP)
	pydocstyle $(LINT_GROUP)
	mypy $(LINT_GROUP)

test:
	$(EXECUTE) python3 -m pytest $(TEST_GROUP)

pre-commit: check
