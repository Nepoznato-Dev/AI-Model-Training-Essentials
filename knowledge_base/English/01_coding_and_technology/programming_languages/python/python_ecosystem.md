<!--
---
# Metadata
title: "Python — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Python ecosystem including package managers, build tools, testing frameworks, linters, IDEs, and deployment options."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [python, ecosystem, tooling, package-manager, pip, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Python — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Python ecosystem.

---

## Package Management

| Tool | Purpose | Install |
|------|---------|---------|
| **pip** | Standard package installer | `pip install package` |
| **pipenv** | Dependency + virtual env manager | `pipenv install package` |
| **poetry** | Modern packaging and dependency management | `poetry add package` |
| **uv** | Fast Rust-based package installer | `uv pip install package` |
| **conda** | Cross-language environment manager | `conda install package` |
| **pdm** | PEP-compliant package manager | `pdm add package` |

```bash
# Virtual environments
python -m venv .venv          # built-in
source .venv/bin/activate     # Linux/Mac
.venv\Scripts\activate        # Windows

# Poetry workflow
poetry init                   # create pyproject.toml
poetry install                # install dependencies
poetry run python main.py     # run in virtual env
```

---

## Build & Distribution

| Tool | Purpose |
|------|---------|
| **setuptools** | Traditional build system |
| **hatch** | Modern project management |
| **flit** | Simple PyPI publishing |
| **maturin** | Rust + Python (PyO3) builds |
| **cibuildwheel** | Cross-platform wheel building |
| **build** | PEP 517 build frontend |

```bash
python -m build               # build sdist + wheel
twine upload dist/*            # upload to PyPI
```

---

## Testing

| Framework | Use Case |
|-----------|----------|
| **pytest** | Industry standard, powerful fixtures |
| **unittest** | Built-in, xUnit style |
| **hypothesis** | Property-based testing |
| **tox** | Multi-environment testing |
| **nox** | Flexible test automation |
| **coverage** | Code coverage measurement |

```python
# pytest example
import pytest

def test_addition():
    assert 1 + 1 == 2

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"

# Parametrized tests
@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(x, y, expected):
    assert x + y == expected
```

```bash
pytest                          # run all tests
pytest -v                       # verbose
pytest --cov=src --cov-report=html  # with coverage
pytest -x                       # stop on first failure
```

---

## Code Quality

| Tool | Purpose |
|------|---------|
| **ruff** | Ultra-fast linter + formatter (replaces flake8, isort, black) |
| **black** | Code formatter |
| **isort** | Import sorter |
| **mypy** | Static type checker |
| **pyright** | Microsoft's type checker |
| **pylint** | Comprehensive linter |
| **flake8** | Classic linter |

```bash
ruff check .                    # lint
ruff format .                   # format
mypy --strict src/              # type check
```

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code** | Lightweight, excellent Python extension |
| **PyCharm** | Full-featured Python IDE |
| **Jupyter** | Interactive notebooks, data science |
| **Spyder** | MATLAB-like scientific IDE |
| **Neovim** | Terminal-based with LSP |

---

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **Django** | Full-stack | Enterprise web apps, admin panels |
| **Flask** | Micro-framework | APIs, small apps |
| **FastAPI** | Modern API | High-performance APIs, async |
| **Tornado** | Async | WebSockets, long-polling |
| **Starlette** | Async | ASGI toolkit |

---

## Data Science & ML

| Package | Purpose |
|---------|---------|
| **numpy** | Numerical computing |
| **pandas** | Data manipulation |
| **matplotlib** | Plotting |
| **scikit-learn** | Classical ML |
| **pytorch** | Deep learning |
| **tensorflow** | Deep learning |
| **polars** | Fast DataFrame library |

---

## Deployment

| Method | Tool |
|--------|------|
| **Containers** | Docker, Podman |
| **WSGI Server** | Gunicorn, uWSGI |
| **ASGI Server** | Uvicorn, Hypercorn |
| **PaaS** | Heroku, Railway, Render |
| **Serverless** | AWS Lambda, Google Cloud Functions |
| **Process Manager** | Supervisor, systemd |

---

## Summary

Python's ecosystem is vast and mature. The modern stack is: **uv/poetry** for dependencies, **pytest** for testing, **ruff** for linting/formatting, **mypy** for type checking, **FastAPI** for APIs, and **Docker** for deployment. The ecosystem's strength is in data science (numpy, pandas, pytorch) and web development (Django, FastAPI). Python's "batteries included" philosophy means most tasks have well-maintained, documented libraries.
