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
# পাইথন — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি পাইথন ইকোসিস্টেমের প্রয়োজনীয় টুল, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য | ইনস্টল করুন |
|------|---------|---------|
| **পিপ** | স্ট্যান্ডার্ড প্যাকেজ ইনস্টলার | `pip install package`|
| **পিপেনভ** | নির্ভরতা + ভার্চুয়াল এনভি ম্যানেজার | `pipenv install package`|
| **কবিতা** | আধুনিক প্যাকেজিং এবং নির্ভরতা ব্যবস্থাপনা | `poetry add package`|
| **uv** | দ্রুত মরিচা-ভিত্তিক প্যাকেজ ইনস্টলার | `uv pip install package`|
| **কন্ডা** | ক্রস-ভাষা পরিবেশ ব্যবস্থাপক | `conda install package`|
| **পিডিএম** | PEP-সম্মত প্যাকেজ ম্যানেজার | `pdm add package`|
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

## নির্মাণ ও বিতরণ
| টুল | উদ্দেশ্য |
|------|---------|
| **সেটআপ টুল** | ঐতিহ্যগত বিল্ড সিস্টেম |
| **হ্যাচ** | আধুনিক প্রকল্প ব্যবস্থাপনা |
| **ফ্লিট** | সাধারণ PyPI প্রকাশনা |
| **ম্যাচুরিন** | মরিচা + পাইথন (PyO3) তৈরি করে |
| **সিবিল্ডহুইল** | ক্রস-প্ল্যাটফর্ম হুইল বিল্ডিং |
| **নির্মাণ** | PEP 517 বিল্ড ফ্রন্টএন্ড |
```bash
python -m build               # build sdist + wheel
twine upload dist/*            # upload to PyPI
```

---

## পরীক্ষা
| ফ্রেমওয়ার্ক | কেস ব্যবহার করুন |
|------------|----------|
| **pytest** | শিল্প মান, শক্তিশালী ফিক্সচার |
| **একক* | অন্তর্নির্মিত, xUnit শৈলী |
| **অনুমান** | সম্পত্তি ভিত্তিক পরীক্ষা |
| **টক্স** | মাল্টি-এনভায়রনমেন্ট টেস্টিং |
| **nox** | নমনীয় পরীক্ষা অটোমেশন |
| **কভারেজ** | কোড কভারেজ পরিমাপ |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **রাফ** | আল্ট্রা-ফাস্ট লিন্টার + ফরম্যাটার (ফ্লেক8, আইসোর্ট, কালো প্রতিস্থাপন করে) |
| **কালো** | কোড ফরম্যাটার |
| **বিভাজন** | আমদানি বাছাইকারী |
| **mypy** | স্ট্যাটিক টাইপ পরীক্ষক |
| **পাইরাইট** | মাইক্রোসফটের টাইপ চেকার |
| **পিলিন্ট** | ব্যাপক লিন্টার |
| **ফ্লেক৮** | ক্লাসিক লিন্টার |
```bash
ruff check .                    # lint
ruff format .                   # format
mypy --strict src/              # type check
```

---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **VS কোড** | লাইটওয়েট, চমৎকার পাইথন এক্সটেনশন |
| **PyCharm** | সম্পূর্ণ বৈশিষ্ট্যযুক্ত পাইথন IDE |
| **বৃহস্পতি** | ইন্টারেক্টিভ নোটবুক, ডেটা সায়েন্স |
| **স্পাইডার** | MATLAB-এর মতো বৈজ্ঞানিক IDE |
| **নিওভিম** | LSP সহ টার্মিনাল-ভিত্তিক |
---

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **জ্যাঙ্গো** | ফুল-স্ট্যাক | এন্টারপ্রাইজ ওয়েব অ্যাপস, অ্যাডমিন প্যানেল |
| **ফ্লাস্ক** | মাইক্রো-ফ্রেমওয়ার্ক | APIs, ছোট অ্যাপস |
| **ফাস্টএপিআই** | আধুনিক API | উচ্চ-কর্মক্ষমতা API, async |
| **টর্নেডো** | অ্যাসিঙ্ক | WebSockets, দীর্ঘ ভোটগ্রহণ |
| **স্টারলেট** | অ্যাসিঙ্ক | ASGI টুলকিট |
---

## ডেটা সায়েন্স এবং এমএল
| প্যাকেজ | উদ্দেশ্য |
|---------|---------|
| **নম্বি** | সংখ্যাসূচক কম্পিউটিং |
| **পান্ডা** | ডেটা ম্যানিপুলেশন |
| **matplotlib** | চক্রান্ত |
| **স্কিট-লার্ন** | ক্লাসিক্যাল এমএল |
| **পিটর্চ** | গভীর শিক্ষা |
| **টেনসরফ্লো** | গভীর শিক্ষা |
| **পোলার** | দ্রুত ডেটাফ্রেম লাইব্রেরি |
---

## স্থাপনা
| পদ্ধতি | টুল |
|---------|------|
| **ধারক** | ডকার, পডম্যান |
| **WSGI সার্ভার** | Gunicorn, uWSGI |
| **ASGI সার্ভার** | Uvicorn, Hypercorn |
| **পাস** | হেরোকু, রেলওয়ে, রেন্ডার |
| **সার্ভারহীন** | AWS Lambda, Google ক্লাউড ফাংশন |
| **প্রসেস ম্যানেজার** | সুপারভাইজার, সিস্টেমড |
---

## সারাংশ
পাইথনের ইকোসিস্টেম বিশাল এবং পরিপক্ক। আধুনিক স্ট্যাক হল: নির্ভরতার জন্য **uv/poetry**, পরীক্ষার জন্য **pytest**, linting/formatting এর জন্য **ruff**, টাইপ চেকিংয়ের জন্য **mypy**, API-এর জন্য **FastAPI** এবং স্থাপনার জন্য **Docker**। ইকোসিস্টেমের শক্তি হল ডেটা সায়েন্স (নাম্পি, পান্ডাস, পাইটর্চ) এবং ওয়েব ডেভেলপমেন্ট (জ্যাঙ্গো, ফাস্টএপিআই)। পাইথনের "ব্যাটারি অন্তর্ভুক্ত" দর্শনের অর্থ হল বেশিরভাগ কাজেরই ভালভাবে রক্ষণাবেক্ষণ করা, নথিভুক্ত লাইব্রেরি রয়েছে।