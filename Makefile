# Makefile

# Virtual environment name
VENV := venv

# Python interpreter to use
PYTHON := $(VENV)/bin/python

# Pip command
PIP := $(VENV)/bin/pip

# Output directory for generated files
OUTPUT_DIR := output

# Main script file
MAIN_SCRIPT := scripts/main.py

# Default target when 'make' is run without arguments
.PHONY: all
all: run

# Target to create virtual environment
.PHONY: venv
venv:
	python3 -m venv $(VENV)
	@echo "Created virtual environment $(VENV)"

# Target to install dependencies
.PHONY: install
install: venv requirements.txt
	$(PIP) install -r requirements.txt
	@echo "Installed dependencies"

# Target to run the main project script
.PHONY: run
run: venv install
	@echo "Running the main project script..."
	$(PYTHON) $(MAIN_SCRIPT)
	@echo "Main project script execution completed"

# Clean up generated files
.PHONY: clean
clean:
	rm -rf $(VENV) $(OUTPUT_DIR) map_advanced.html
	@echo "Cleaned up generated files"

# Help target to display available targets
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  make venv        - Create virtual environment"
	@echo "  make install     - Install dependencies"
	@echo "  make run         - Run the main project script"
	@echo "  make clean       - Clean up generated files"
	@echo "  make help        - Display this help message"
