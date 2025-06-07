# Contributing to media-calc

Thank you for your interest in contributing to media-calc! This document provides guidelines and steps for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/your-username/media-calc.git
```
3. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -e .
```

## Development Process

1. Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes
3. Write or update tests
4. Run tests
5. Update documentation if needed
6. Submit a pull request

## Code Style

- Follow PEP 8 guidelines
- Add docstrings to new functions
- Include type hints where possible
- Write clear commit messages

## Running Tests

```bash
python -m unittest discover
```

## Questions?

Feel free to open an issue with any questions or concerns.
