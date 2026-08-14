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
# Python - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم پایتون را پوشش می‌دهد.
---

## مدیریت بسته
| ابزار | هدف | نصب |
|------|---------|---------|
| **پیپ** | نصب کننده بسته استاندارد | `pip install package`|
| **pipenv** | Dependency + virtual env manager | `pipenv install package`|
| **شعر** | بسته بندی مدرن و مدیریت وابستگی | `poetry add package`|
| **uv** | نصب کننده بسته مبتنی بر Rust | `uv pip install package`|
| **کوندا** | مدیر محیط بین زبانی | `conda install package`|
| **پی دی ام** | مدیر بسته سازگار با PEP | `pdm add package`|
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

## ساخت و توزیع
| ابزار | هدف |
|------|---------|
| **suptools** | سیستم ساخت سنتی |
| **دریچه** | مدیریت پروژه مدرن |
| **بال زدن** | انتشار ساده PyPI |
| **ماتورین** | Rust + Python (PyO3) می سازد |
| **cibuildwheel** | ساختمان چرخ کراس پلت فرم |
| **ساخت ** | PEP 517 build frontend |
```bash
python -m build               # build sdist + wheel
twine upload dist/*            # upload to PyPI
```

---

## تست
| چارچوب | مورد استفاده |
|-----------|----------|
| **pytest** | استاندارد صنعت، وسایل قدرتمند |
| **واحد تست** | داخلی، سبک xUnit |
| **فرضیه** | تست مبتنی بر اموال |
| **سم** | تست چند محیطی |
| **نوکس** | اتوماسیون تست انعطاف پذیر |
| **پوشش** | اندازه گیری پوشش کد |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **روف** | لینتر + فرمتر فوق سریع (جایگزین flake8، isort، black) |
| **سیاه** | فرمت کننده کد |
| **ایزورت** | جورکننده وارداتی |
| **mypy** | جستجوگر نوع استاتیک |
| **کپی رایت** | جستجوگر نوع مایکروسافت |
| **پیلینت** | لینتر جامع |
| **فلک8** | لنگر کلاسیک |
```bash
ruff check .                    # lint
ruff format .                   # format
mypy --strict src/              # type check
```

---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| ** کد VS ** | پسوند پایتون سبک و عالی |
| **PyCharm** | Python IDE با امکانات کامل |
| **ژوپیتر** | نوت بوک های تعاملی، علم داده |
| **اسپایدر** | IDE علمی شبیه به MATLAB |
| **Neovim** | مبتنی بر ترمینال با LSP |
---

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **جانگو** | تمام پشته | برنامه های وب سازمانی، پنل های مدیریت |
| **فلاسک** | میکرو فریمورک | API ها، برنامه های کوچک |
| **FastAPI** | API مدرن | APIهای با کارایی بالا، async |
| **گردباد** | همگام | WebSockets، طولانی نظرسنجی |
| **استارلت** | همگام | جعبه ابزار ASGI |
---

## علم داده و ML
| پکیج | هدف |
|---------|---------|
| **نومپی** | محاسبات عددی |
| **پاندا** | دستکاری داده ها |
| **matplotlib** | نقشه کشی |
| **scikit-learn** | ML کلاسیک |
| **pytorch** | یادگیری عمیق |
| **تنسورفلو** | یادگیری عمیق |
| **قطبی** | کتابخانه Fast DataFrame |
---

## استقرار
| روش | ابزار |
|--------|------|
| **ظروف** | داکر، پودمان |
| **سرور WSGI** | Gunicorn، uWSGI |
| **سرور ASGI** | Uvicorn, Hypercorn |
| **PaaS** | هروکو، راه آهن، رندر |
| **بدون سرور** | AWS Lambda، Google Cloud Functions |
| **مدیر فرآیند** | Supervisor, systemd |
---

## خلاصه
اکوسیستم پایتون وسیع و بالغ است. پشته مدرن عبارت است از: **uv/poetry** برای وابستگی ها، **pytest** برای آزمایش، **ruff** برای پرده زدن/قالب بندی، **mypy** برای بررسی نوع، **FastAPI** برای APIها و **Docker** برای استقرار. نقطه قوت اکوسیستم در علم داده (numpy، پانداها، pytorch) و توسعه وب (Django، FastAPI) است. فلسفه "باتری شامل" پایتون به این معنی است که اکثر وظایف دارای کتابخانه های مستند و به خوبی نگهداری می شوند.