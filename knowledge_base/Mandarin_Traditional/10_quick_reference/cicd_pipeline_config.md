---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cicd, pipeline, config, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# CI/CD 管道配置
持續整合 (CI) 和持續部署 (CD) 管道可自動化建置、測試和部署軟體的流程。本參考涵蓋了最受歡迎的 CI/CD 平台的配置模式：GitHub Actions、GitLab CI 和一般管道設計原則。
---

## GitHub 操作
### 工作流程結構
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up language
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build
        run: python setup.py build
```

### 常見觸發器
|觸發|描述 |
|---------|-------------|
|`on: push`|每一次推動|
|`on: pull_request`|在 PR 上開啟、更新、重新開啟 |
|`on: schedule`|基於 Cron 的計劃 |
|`on: workflow_dispatch`|手動觸發|
|`on: release`|關於發布創建 |
|`on: workflow_call`|由另一個工作流程呼叫（可重複使用） |
### 主要特點
|特色 |描述 |
|---------|-------------|
| **矩陣策略** |使用不同的配置執行相同的作業 |
| **秘密** |加密的環境變數（`${{ secrets.MY_SECRET }}`）|
| **環境** |具有保護規則的部署目標|
| **快取** |運行之間的快取依賴關係 |
| **文物** |從作業上傳文件（測試報告、建置）|
| **可重複使用的工作流程** |跨儲存庫共用工作流程邏輯 |
| **複合動作** |將多個步驟合併為一個操作 |
### 矩陣策略
```yaml
jobs:
  test:
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

---

## GitLab CI
### 管道結構
```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run myapp:$CI_COMMIT_SHA pytest

deploy:
  stage: deploy
  script:
    - deploy.sh $CI_COMMIT_SHA
  only:
    - main
  when: manual
```

### 關鍵關鍵字
|關鍵字 |說明 |
|---------|-------------|
|`stages`|定義管道階段及其順序 |
|`stage`|將作業指派給階段 |
|`script`|要執行的命令 |
|`before_script`|指令在主腳本之前執行 |
|`after_script`|命令在主腳本之後運行（即使失敗）|
|`only / except`|控製作業何時運行（分支、標籤）|
|`rules`| only/ except | 更靈活的版本
|`variables`|定義 CI/CD 變數 |
|`cache`|在管道運行之間快取檔案 |
|`artifacts`|在作業之間傳遞的文件 |
|`environment`|部署環境|
|`when`|控製作業執行（on_success、on_failure、手動、始終）|
|`needs`|指定作業依賴關係（DAG 模式）|
|`extends`|從另一個作業繼承配置 |
|`include`|導入外部 YAML 檔案 |
### 預定義變數
|變數|描述 |
|----------|-------------|
|`$CI_COMMIT_SHA`|目前提交哈希 |
|`$CI_COMMIT_REF_NAME`|分支或標籤名稱|
|`$CI_PIPELINE_ID`|管路編號 |
|`$CI_JOB_ID`|職位編號 |
|`$CI_PROJECT_DIR`|專案的完整路徑 |
|`$CI_REGISTRY`|容器註冊表 URL |
|`$CI_DEFAULT_BRANCH`|預設分支名稱 |
---

## 管道設計模式
### 常見模式
|圖案|描述 |
|---------|-------------|
| **建置一次，部署多次** |建置一次工件；將相同的工件部署到每個環境|
| **登機口檢查** |生產部署前手動審核 |
| **功能標誌** |部署到生產環境但隱藏在功能標誌後面 |
| **金絲雀部署** |部署到小比例；監視器;推出 |
| **藍綠部署** |兩個相同的環境；切換流量 |
| **並行測試** |並行運行測試套件以減少管道時間 |
| **首先清理** |在昂貴的測試之前運行 linter；快速失敗|
| **快取依賴** |快取node_modules、pip、Maven 以加速建置 |
### 管道階段（典型）
|舞台|目的|
|--------|---------|
| **棉絨** |程式碼風格與靜態分析|
| **建構** |編譯；捆;創造文物|
| **單元測試** |快速測試；沒有外部依賴|
| **整合測試** |使用資料庫進行測試；蜜蜂;外部服務|
| **安全掃描** |依賴漏洞；秘密掃描；先科科技|
| **套餐** |建立 Docker 映像；建置發布工件|
| **部署暫存** |部署到暫存環境 |
| **端對端測試** |針對分期的完整系統測試|
| **部署生產** |部署到生產環境（手動或自動）|
| **冒煙測試** |驗證部署是否正常 |
---

## 快取策略
|語言/工具|快取路徑|範例|
|----------------|---------|---------|
| **Python (pip)** |`~/.cache/pip`|`actions/cache`帶有來自`requirements.txt`雜湊的金鑰 |
| **Node.js (npm)** |`~/.npm`| 內建快取的`actions/setup-node`|
| **Java (Maven)** |`~/.m2/repository`|使用`pom.xml`雜湊中的金鑰進行快取 |
| **Java (Gradle)** |`~/.gradle/caches`|使用`build.gradle`雜湊中的金鑰進行快取 |
| **去** |`~/go/pkg/mod`|使用`go.sum`雜湊中的金鑰進行快取 |
| **生鏽（貨物）** |`~/.cargo/registry`|使用`Cargo.lock`哈希中的金鑰進行快取 |
| **碼頭工人** | Docker 層快取 |`docker/build-push-action`帶快取來源 |
---

## 故障排除
|問題 |解決方案 |
|---------|----------|
| **管道速度緩慢** |快取依賴；並行作業；使用較小的基礎圖像 |
| **秘密不可用** |檢查秘密名稱；驗證環境範圍；檢查叉子 PR 限制 |
| **文物太大** |排除不必要的文件；壓縮;使用較短的保留時間 |
| **矩陣太大** |減少組合；使用`include`/`exclude`|
| **片狀測試** |檢疫片狀測試；修復根本原因；使用`retry:`重試 |
| **權限被拒絕** |檢查令牌範圍；驗證跑步者權限 |
---

＃＃ 概括
CI/CD 管道可自動建置、測試和部署軟體。 GitHub Actions 使用由儲存庫事件觸發的 YAML 工作流程； GitLab CI 使用具有彈性規則的階段和作業。關鍵模式包括：建置一次、部署多次；生產前進行門檢查；先進行 lint 以獲得快速回饋；快取相依性以加快建置速度；並並行測試。管道階段通常從 lint → 建置 → 測試 → 安全性 → 打包 → 部署 → 冒煙測試進行。快取策略因語言而異，但遵循相同的原則：快取由鎖定檔案雜湊鍵控的依賴目錄。目標是對每次更改提供快速、可靠的回饋，以及安全、可重複的生產部署。