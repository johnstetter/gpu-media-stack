# Contributing to Proxmox MCP Server

First off, thank you for considering contributing to Proxmox MCP Server! 

## Development Process

1. Fork the repository
2. Clone your fork
3. Create a new branch from `main`
4. Make your changes
5. Run the tests
6. Push to your fork
7. Submit a merge request

## Setting up Development Environment

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install development dependencies:
```bash
pip install pytest black flake8 mypy
```

## Running Tests

```bash
pytest tests/
```

## Code Style

We use:
- Black for code formatting
- Flake8 for style guide enforcement
- MyPy for type checking

Before submitting:
```bash
black src/ tests/
flake8 src/ tests/
mypy src/
```

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- feat: A new feature
- fix: A bug fix
- docs: Documentation changes
- style: Code style changes (formatting, etc)
- refactor: Code changes that neither fix bugs nor add features
- test: Adding or modifying tests
- chore: Changes to build process or auxiliary tools

## Making a Release

1. Update CHANGELOG.md
2. Update version in pyproject.toml
3. Create a git tag
4. Push tag to GitLab

## Questions?

Feel free to open an issue for any questions or concerns.
