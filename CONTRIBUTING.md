# Contributing to CloudOps-MCP

Thank you for considering contributing to CloudOps-MCP! This document provides guidelines and steps for contributing to this open source project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

When reporting bugs, please include:

- A clear, descriptive title
- Steps to reproduce the bug
- Expected behavior vs. actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots if applicable

Please use the GitHub Issues tracker with the "bug" label.

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- A clear description of the enhancement
- Rationale for the enhancement
- Possible implementation approach if you have one

Please use the GitHub Issues tracker with the "enhancement" label.

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add or update tests as needed
5. Update documentation as needed
6. Run tests: `pytest`
7. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cloudops-mcp.git
   cd cloudops-mcp
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Coding Standards

- Follow PEP 8 for Python code
- Write clear, descriptive commit messages
- Document functions, classes, and modules
- Add unit tests for new features

## Testing

Run the test suite:
```bash
pytest
```

For coverage report:
```bash
pytest --cov=app tests/
```

## Documentation

- Update documentation for any changes to API or functionality
- Document new features with examples
- Keep the README up to date

## Review Process

1. All pull requests require review from at least one maintainer
2. CI checks must pass
3. Changes must be well-tested and documented

Thank you for improving CloudOps-MCP!
