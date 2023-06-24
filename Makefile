.DEFAULT_GOAL := help
.PHONY: help clean install calendar calendar-config next-months-calendar test

VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python3
PIP := $(VENV_DIR)/bin/pip3

help:
	@echo "Usage:"
	@echo "  make help                      Display this help message"
	@echo "  make clean                     Remove generated files"
	@echo "  make install                   Install project dependencies"
	@echo "  make next-months-calendar      Generate a calendar HTML file for the upcoming month in the current year"
	@echo "  make calendar-config           Generate a holiday-config.json file. See the README.md in ./generate-holiday-config for more"
	@echo "  make install-calendar-config   Install dependencies for ./generate-holiday-config"
	@echo "  make test                      Run unit tests"

clean:
	rm -f *-Calendar.html
	rm -rf __pycache__
	rm -rf .pytest_cache

install:
	$(PIP) install -r requirements.txt

calendar:
	$(PYTHON) generate_calendar.py

next-months-calendar:
	$(PYTHON) generate_calendar.py

calendar-config:
	cd ./generate-holiday-config && npm run generate-config && cp holiday-config.json ../config

install-calendar-config:
	cd ./generate-holiday-config && npm install

test:
	$(PYTHON) -m unittest discover -s tests
