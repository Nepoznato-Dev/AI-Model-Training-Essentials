<!--
---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
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

-->
# CI/CD 管道配置
持续集成 (CI) 和持续部署 (CD) 管道可自动化构建、测试和部署软件的过程。本参考涵盖了最流行的 CI/CD 平台的配置模式：GitHub Actions、GitLab CI 和一般管道设计原则。
---

## GitHub 操作
### 工作流程结构
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

### 常见触发器
|触发|描述 |
|---------|-------------|
| `on: push`|每一次推动|
| `on: pull_request`|在 PR 上打开、更新、重新打开 |
| `on: schedule`|基于 Cron 的计划 |
| `on: workflow_dispatch`|手动触发|
| `on: release`|关于发布创建 |
| `on: workflow_call`|由另一个工作流程调用（可重用） |
### 主要特点
|特色 |描述 |
|---------|-------------|
| **矩阵策略** |使用不同的配置运行相同的作业 |
| **秘密** |加密的环境变量（`${{ secrets.MY_SECRET }}`）|
| **环境** |具有保护规则的部署目标|
| **缓存** |运行之间的缓存依赖关系 |
| **文物** |从作业上传文件（测试报告、构建）|
| **可重复使用的工作流程** |跨存储库共享工作流逻辑 |
| **复合动作** |将多个步骤合并为一个操作 |
### 矩阵策略
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
### 管道结构
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

### 关键关键词
|关键词 |描述 |
|---------|-------------|
| `stages`|定义管道阶段及其顺序 |
| `stage`|将作业分配给阶段 |
| `script`|要执行的命令 |
| `before_script`|命令在主脚本之前运行 |
| `after_script`|命令在主脚本之后运行（即使失败）|
| `only / except`|控制作业何时运行（分支、标签）|
| `rules`| only/ except | 更灵活的版本
| `variables`|定义 CI/CD 变量 |
| `cache`|在管道运行之间缓存文件 |
| `artifacts`|在作业之间传递的文件 |
| `environment`|部署环境|
| `when`|控制作业执行（on_success、on_failure、手动、始终）|
| `needs`|指定作业依赖关系（DAG 模式）|
| `extends`|从另一个作业继承配置 |
| `include`|导入外部 YAML 文件 |
### 预定义变量
|变量|描述 |
|----------|-------------|
| `$CI_COMMIT_SHA`|当前提交哈希 |
| `$CI_COMMIT_REF_NAME`|分支或标签名称|
| `$CI_PIPELINE_ID`|管道编号 |
| `$CI_JOB_ID`|职位编号 |
| `$CI_PROJECT_DIR`|项目的完整路径 |
| `$CI_REGISTRY`|容器注册表 URL |
| `$CI_DEFAULT_BRANCH`|默认分支名称 |
---

## 管道设计模式
### 常见模式
|图案|描述 |
|---------|-------------|
| **构建一次，部署多次** |构建一次工件；将相同的工件部署到每个环境|
| **登机口检查** |生产部署前手动审批 |
| **功能标志** |部署到生产环境但隐藏在功能标志后面 |
| **金丝雀部署** |部署到小比例；监视器;推出 |
| **蓝绿部署** |两个相同的环境；切换流量 |
| **并行测试** |并行运行测试套件以减少管道时间 |
| **首先清理** |在昂贵的测试之前运行 linter；快速失败|
| **缓存依赖** |缓存node_modules、pip、Maven 以加速构建 |
### 管道阶段（典型）
|舞台|目的|
|--------|---------|
| **棉绒** |代码风格和静态分析|
| **构建** |编译；捆;创造文物|
| **单元测试** |快速测试；没有外部依赖|
| **集成测试** |使用数据库进行测试；蜜蜂;外部服务|
| **安全扫描** |依赖漏洞；秘密扫描；先科科技|
| **套餐** |创建 Docker 镜像；构建发布工件|
| **部署暂存** |部署到暂存环境 |
| **端到端测试** |针对分期的完整系统测试|
| **部署生产** |部署到生产环境（手动或自动）|
| **冒烟测试** |验证部署是否正常 |
---

## 缓存策略
|语言/工具|缓存路径|示例|
|----------------|---------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`带有来自`requirements.txt`哈希的密钥 |
| **Node.js (npm)** | `~/.npm`|  带内置缓存的`actions/setup-node`|
| **Java (Maven)** | `~/.m2/repository`|使用`pom.xml`哈希中的密钥进行缓存 |
| **Java (Gradle)** | `~/.gradle/caches`|使用`build.gradle`哈希中的密钥进行缓存 |
| **去** | `~/go/pkg/mod`|使用`go.sum`哈希中的密钥进行缓存 |
| **生锈（货物）** | `~/.cargo/registry`|使用`Cargo.lock`哈希中的密钥进行缓存 |
| **码头工人** | Docker 层缓存 | `docker/build-push-action`带缓存来源 |
---

## 故障排除
|问题 |解决方案 |
|---------|----------|
| **管道速度缓慢** |缓存依赖；并行作业；使用较小的基础图像 |
| **秘密不可用** |检查秘密名称；验证环境范围；检查叉子 PR 限制 |
| **文物太大** |排除不必要的文件；压缩;使用较短的保留时间 |
| **矩阵太大** |减少组合；使用`include`/`exclude`|
| **片状测试** |检疫片状测试；修复根本原因；使用`retry:`重试 |
| **权限被拒绝** |检查令牌范围；验证跑步者权限 |
---

＃＃ 概括
CI/CD 管道可自动构建、测试和部署软件。 GitHub Actions 使用由存储库事件触发的 YAML 工作流程； GitLab CI 使用具有灵活规则的阶段和作业。关键模式包括：构建一次、部署多次；生产前进行门检查；首先进行 lint 以获得快速反馈；缓存依赖项以加快构建速度；并并行测试。管道阶段通常从 lint → 构建 → 测试 → 安全 → 打包 → 部署 → 冒烟测试进行。缓存策略因语言而异，但遵循相同的原则：缓存由锁定文件哈希键控的依赖目录。目标是对每次更改提供快速、可靠的反馈，并安全、可重复地部署到生产环境。