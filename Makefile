.PHONY: test clean clean-pyc clean-build help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

test: ## run pytest
	pytest

vup: ## install and initialize the vagrant box
	vagrant init ubuntu/xenial64
	vagrant up

vinstall: ## install all of the necessary packages for development - this only needs to be run once when first starting the vagrant box
	export LC_ALL=en_US.UTF-8;
	sudo apt-get update
	sudo apt-get install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib
	sudo pip3 install virtualenv
	sudo pip3 install -r requirements

clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +