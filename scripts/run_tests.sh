#!/bin/bash

# Exit on error
set -e

echo "Running tests for Cloud Ops MCP..."

# Activate virtual environment
source .venv/bin/activate || source venv/bin/activate

# Run tests with coverage
pytest --cov=app --cov=memory tests/ -v

echo "Tests completed!"
