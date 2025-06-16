#!/bin/bash

# Exit on error
set -e

echo "Setting up development environment for Cloud Ops MCP..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Set up pre-commit hooks
echo "Setting up pre-commit hooks..."
pip install pre-commit
pre-commit install

echo "Development environment setup complete!"
echo "To activate the virtual environment, run: source .venv/bin/activate"
echo "To start the server, run: python run.py"
