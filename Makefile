.PHONY: setup run test lint clean build docs help

help:
	@echo "Available commands:"
	@echo "  setup  - Set up development environment"
	@echo "  run    - Run the application"
	@echo "  test   - Run tests"
	@echo "  lint   - Run linting checks"
	@echo "  clean  - Clean build artifacts"
	@echo "  build  - Build the package"
	@echo "  docs   - Build documentation"

setup:
	@scripts/setup_dev.sh

run:
	@python run.py

test:
	@scripts/run_tests.sh

lint:
	@pre-commit run --all-files

clean:
	@rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage htmlcov/
	@find . -type d -name __pycache__ -exec rm -rf {} +

build:
	@pip install -e .

docs:
	@echo "Documentation build not yet implemented"
