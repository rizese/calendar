.DEFAULT_GOAL := help
.PHONY: help clean lint test

PYTHON := python3
PIP := pip3
VENV_DIR := .venv

help:
	@echo "Usage:"
	@echo "  make help          			Display this help message"
	@echo "  make clean         			Remove generated files"
	@echo "  make install       			Install project dependencies"
	@echo "  make current_calendar		Generate a calendar HTML file for the current month and year"

clean:
	rm -f *-Calendar.html
	rm -rf __pycache__
	rm -rf .pytest_cache

install:
	$(PIP) install -r requirements.txt

calendar:
	$(PYTHON) generate_calendar.py

calendar-config:
	cd ./generate-holiday-config && npm run generate-config && cp holiday-config.json ../

.PHONY: calendar-config


initialize-generate-config:
	cd ./generate-holiday-config && npm install

