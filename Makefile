# Check make version.
MAKE_MIN_VERSION := 3.82
MAKE_OK := $(filter $(MAKE_MIN_VERSION),$(firstword $(sort $(MAKE_VERSION) $(MAKE_MIN_VERSION))))
ifeq ($(MAKE_OK),)
	$(error Make version required $(MAKE_MIN_VERSION)+, current version: $(MAKE_VERSION))
endif

# Versions.
POETRY_VERSION = 1.7.1
PYTHON = python3.11
PIP_VERSION = 24.3.1
SETUPTOOLS_VERSION = 75.6.0
WHEEL_VERSION = 0.45.1

# Paths.
PROJECT_PATH = $(CURDIR)
BE_PATH = $(PROJECT_PATH)/backend
FE_PATH = $(PROJECT_PATH)/frontend

export VIRTUAL_ENV ?= $(PROJECT_PATH)/.venv_$(PYTHON)
VIRTUAL_ENV_POETRY = $(PROJECT_PATH)/.venv_poetry

# Bin.
VENV_ACTIVATE = $(VIRTUAL_ENV)/bin/activate
VENV_POETRY_ACTIVATE = $(VIRTUAL_ENV_POETRY)/bin/activate

# Other.
SHELL = /bin/bash  # Using bash as default shell
CHECK_PYTHON = $(shell which $(PYTHON))

export PATH := $(VIRTUAL_ENV)/bin:$(PATH)
export PYTHONPATH = $(BE_PATH)

all: help

## ------------------------------------------------ SETUP --------------------------------------------------------------

$(VENV_ACTIVATE):
	# Check if correct python is installed.
ifeq ($(CHECK_PYTHON), )
	$(error $(PYTHON) was not found but needed to continue. Please install $(PYTHON))
endif
	$(PYTHON) -m venv $(VIRTUAL_ENV)
	pip install pip==$(PIP_VERSION) setuptools==$(SETUPTOOLS_VERSION) wheel==$(WHEEL_VERSION)

$(VENV_POETRY_ACTIVATE):
	$(PYTHON) -m venv $(VIRTUAL_ENV_POETRY)
	$(VIRTUAL_ENV_POETRY)/bin/pip install pip==$(PIP_VERSION) setuptools==$(SETUPTOOLS_VERSION) wheel==$(WHEEL_VERSION)

# @Setup Install poetry.
poetry: $(VENV_POETRY_ACTIVATE)
	$(VIRTUAL_ENV_POETRY)/bin/pip install poetry==$(POETRY_VERSION)
	ln -f -s $(realpath $(VIRTUAL_ENV_POETRY))/bin/poetry $(VIRTUAL_ENV)/bin/poetry

## @Setup Prepare environment for develop autotests.
install: $(VENV_ACTIVATE) poetry
	# Check user uid
ifeq ($(UID),0)
	$(error Can not run this command as root user)
endif

	poetry -C $(BE_PATH) install --no-root

## ------------------------------------------------ APP ----------------------------------------------------------------

## @App Start the environment.
start: stop
	docker-compose build --pull  && \
	docker-compose up

## @App Stop the environment.
stop:
	docker-compose kill   && \
	docker-compose down --volumes

## @App SSH to backend container.
in:
	docker exec -it week-eat-planner-backend-1 bash

## @App Connect to database.
db_shell:
	PGPASSWORD=wep psql -h localhost -U wep -d wep

## ------------------------------------------------ TESTS --------------------------------------------------------------

## @Checks Run linters.
lint: $(VENV_ACTIVATE)
	black --config $(BE_PATH)/pyproject.toml --check --diff --color $(BE_PATH)
	pylint --rcfile $(BE_PATH)/pyproject.toml $(BE_PATH) --output-format=colorized
	mypy --config-file $(BE_PATH)/pyproject.toml $(BE_PATH)

## @Checks Run code formatter.
style: $(VENV_ACTIVATE)
	black --config $(BE_PATH)/pyproject.toml $(BE_PATH)

## @Tests Run be unittests.
be_test: $(VENV_ACTIVATE)
	pytest $(BE_PATH)/tests
	coverage report --fail-under=100

## @Tests Run fe unittests.
fe_test:
	# TODO: add tests

HELP_TARGET_MAX_CHAR_NUM = 20

.PHONY:
help:
	@echo Usage:
	@echo '  make <target>'
	@echo '  make <target> <VAR>=<value>'
	@echo ''
	@awk '/^[a-zA-Z\-\_0-9\/]+:/ \
		{ \
			helpMessage = match(lastLine, /^## (.*)/); \
			if (helpMessage) { \
				helpCommand = substr($$1, 0, index($$1, ":")-1); \
				helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
				helpGroup = match(helpMessage, /^@([^ ]*)/); \
				if (helpGroup) { \
					helpGroup = substr(helpMessage, RSTART + 1, index(helpMessage, " ")-2); \
					helpMessage = substr(helpMessage, index(helpMessage, " ")+1); \
				} \
				printf "%s|  %-$(HELP_TARGET_MAX_CHAR_NUM)s %s\n", \
					helpGroup, helpCommand, helpMessage; \
			} \
		} \
		{ lastLine = $$0 }' \
		$(MAKEFILE_LIST) \
	| sort -t'|' -sk1,1 -k2,2 \
	| awk -F '|' ' \
			{ \
			cat = $$1; \
			if (cat != lastCat || lastCat == "") { \
				if ( cat == "0" ) { \
					print "Targets: " \
				} else { \
					gsub("_", " ", cat); \
					printf "\%s:\n", cat; \
				} \
			} \
			print $$2 \
		} \
		{ lastCat = $$1 }'
