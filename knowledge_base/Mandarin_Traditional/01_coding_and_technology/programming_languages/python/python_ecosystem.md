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
# Python — 生態系統與工具指南
本指南涵蓋了 Python 生態系統中的基本工具、框架和基礎架構。
---

## 套件管理
|工具|目的|安裝 |
|------|---------|---------|
| **點** |標準包安裝程式 |`pip install package`|
| **pipenv** |依賴+虛擬環境管理器|`pipenv install package`|
| **詩歌** |現代包裝與依賴管理|`poetry add package`|
| **紫外線** |基於 Rust 的快速軟體包安裝程式 |`uv pip install package`|
| **康達** |跨語言環境管理器 |`conda install package`|
| **pdm** |符合 PEP 的套件管理器 |`pdm add package`|
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

## 建置和分發
|工具|目的|
|------|---------|
| **設定工具** |傳統建置系統 |
| **孵化** |現代專案管理|
| **掠過** |簡單的 PyPI 發布 |
| **成熟** | Rust + Python (PyO3) 建置 |
| **cibuildwheel** |跨平台輪子建構 |
| **建構** | PEP 517 建構前端 |
```bash
python -m build               # build sdist + wheel
twine upload dist/*            # upload to PyPI
```

---

## 測試
|框架|使用案例|
|------------|----------|
| **pytest** |業界標準，強大夾具|
| **單元測試** |內置，xUnit 風格 |
| **假設** |基於屬性的測試 |
| **毒性** |多環境測試|
| **諾克斯** |靈活的測試自動化|
| **覆蓋範圍** |代碼覆蓋率測量|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **皺褶** |超快速 linter + 格式化程式（取代 flake8、isort、black）|
| **黑色** |程式碼格式化程式|
| **分類** |進口分類機|
| **mypy** |靜態類型檢查器 |
| **版權** |微軟的類型檢查器 |
| **pylint** |全面的短絨 |
| **片8** |經典短絨 |
```bash
ruff check .                    # lint
ruff format .                   # format
mypy --strict src/              # type check
```

---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS 程式碼** |輕量級、優秀的Python擴充|
| **PyCharm** |功能齊全的Python IDE |
| **Jupyter** |互動筆記本，資料科學|
| **間諜** |類似 MATLAB 的科學 IDE |
| **Neovim** |基於終端的LSP |
---

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **姜戈** |全栈|企业网络应用程序、管理面板 |
| **烧瓶** |微框架| API、小型应用程序 |
| **快速API** |现代 API |高性能异步 API |
| **龙卷风** |异步 | WebSockets，长轮询 |
| **星光** |异步 | ASGI工具包|
---

## 資料科學與機器學習
|套餐 |目的|
|---------|---------|
| **numpy** |數值計算|
| **熊貓** |資料處理 |
| **matplotlib** |繪圖 |
| **scikit-learn** |經典機器學習 |
| **pytorch** |深度學習 |
| **張量流** |深度學習 |
| **極地** |快速 DataFrame 庫 |
---

## 部署
|方法|工具|
|--------|------|
| **容器** | Docker、Podman |
| **WSGI 伺服器** | Gunicorn，uWSGI |
| **ASGI 伺服器** | Uvicorn、Hypercorn |
| **PaaS** | Heroku、鐵路、渲染 |
| **無伺服器** | AWS Lambda、Google雲端函數 |
| **流程管理器** | systemd 主管 |
---

＃＃ 概括
Python的生態系龐大且成熟。現代堆疊是：**uv/poetry** 用於依賴項，**pytest** 用於測試，**ruff** 用於 linting/formatting，**mypy** 用於類型檢查，**FastAPI** 用於 API，**Docker** 用於部署。此生態系統的優勢在於資料科學（numpy、pandas、pytorch）和 Web 開發（Django、FastAPI）。 Python 的「自備電池」概念意味著大多數任務都有維護良好、記錄在案的程式庫。