SHELL  := /bin/bash
SOURCE := $(shell pwd)

help: ## display this help text
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

setup: ## installs or upgrade pipenv at current user home
	pip install --upgrade --user pipenv

init: ## creates the virtual environment inside the project, then installs all dependencies
	PIPENV_VERBOSITY=-1 PIPENV_VENV_IN_PROJECT=1 pipenv install

dev: ## starts the application using the python interpreter in the virtual environment
	.venv/bin/python src/main.py

start: ## starts the application using the system python interpreter
	python src/main.py
