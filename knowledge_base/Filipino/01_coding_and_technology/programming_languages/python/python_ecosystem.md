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
# Python — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, frameworks, at imprastraktura sa Python ecosystem.
---

## Pamamahala ng Package
| Tool | Layunin | I-install |
|------|---------|---------|
| **pip** | Karaniwang package installer | `pip install package`|
| **pipenv** | Dependency + virtual env manager | `pipenv install package`|
| **tula** | Modernong packaging at pamamahala ng dependency | `poetry add package`|
| **uv** | Mabilis na Rust-based na package installer | `uv pip install package`|
| **conda** | Cross-language environment manager | `conda install package`|
| **pdm** | Tagapamahala ng package na sumusunod sa PEP | `pdm add package`|
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

## Bumuo at Pamamahagi
| Tool | Layunin |
|------|---------|
| **setuptools** | Tradisyunal na build system |
| **pisa** | Pamamahala ng modernong proyekto |
| **lumipad** | Simpleng PyPI publishing |
| **maturin** | Ang Rust + Python (PyO3) ay bumubuo ng |
| **cibuildwheel** | Cross-platform wheel building |
| **build** | PEP 517 build frontend |
```bash
python -m build               # build sdist + wheel
twine upload dist/*            # upload to PyPI
```

---

## Pagsubok
| Balangkas | Use Case |
|-----------|----------|
| **pytest** | Standard sa industriya, makapangyarihang mga fixture |
| **unittest** | Built-in, estilo ng xUnit |
| **hypothesis** | Pagsubok na nakabatay sa ari-arian |
| **lason** | Multi-environment testing |
| **nox** | Flexible na pag-aautomat ng pagsubok |
| **saklaw** | Pagsukat ng saklaw ng code |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **ruff** | Napakabilis na linter + formatter (pinapalitan ang flake8, isort, black) |
| **itim** | Taga-format ng code |
| **sort** | Import sorter |
| **mypy** | Static type checker |
| **pyright** | Uri ng checker ng Microsoft |
| **pylint** | Comprehensive linter |
| **flake8** | Klasikong linter |
```bash
ruff check .                    # lint
ruff format .                   # format
mypy --strict src/              # type check
```

---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code** | Magaan, mahusay na extension ng Python |
| **PyCharm** | Full-feature na Python IDE |
| **Jupyter** | Mga interactive na notebook, data science |
| **Spyder** | MATLAB-like scientific IDE |
| **Neovim** | Nakabatay sa terminal sa LSP |
---

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Django** | Full-stack | Enterprise web app, admin panel |
| **Flask** | Micro-framework | Mga API, maliliit na app |
| **FastAPI** | Makabagong API | Mga high-performance na API, async |
| **Buhawi** | Async | WebSockets, mahabang botohan |
| **Starlette** | Async | ASGI toolkit |
---

## Data Science at ML
| Package | Layunin |
|---------|---------|
| **numpy** | Numerical computing |
| **pandas** | Pagmamanipula ng data |
| **matplotlib** | Pag-plot |
| **scikit-learn** | Klasikong ML |
| **pytorch** | Malalim na pagkatuto |
| **tensorflow** | Malalim na pagkatuto |
| **polar** | Mabilis na DataFrame library |
---

## Deployment
| Paraan | Tool |
|--------|------|
| **Mga lalagyan** | Docker, Podman |
| **WSGI Server** | Gunicorn, uWSGI |
| **ASGI Server** | Uvicorn, Hypercorn |
| **PaaS** | Heroku, Riles, Render |
| **Walang Server** | AWS Lambda, Google Cloud Functions |
| **Process Manager** | Superbisor, systemd |
---

## Buod
Malawak at mature ang ekosistema ng Python. Ang modernong stack ay: **uv/poetry** para sa mga dependency, **pytest** para sa pagsubok, **ruff** para sa linting/formatting, **mypy** para sa type checking, **FastAPI** para sa mga API, at **Docker** para sa deployment. Ang lakas ng ecosystem ay nasa data science (numpy, pandas, pytorch) at web development (Django, FastAPI). Ang pilosopiya ng "kabilang ang mga baterya" ng Python ay nangangahulugang karamihan sa mga gawain ay may maayos at nakadokumentong mga aklatan.