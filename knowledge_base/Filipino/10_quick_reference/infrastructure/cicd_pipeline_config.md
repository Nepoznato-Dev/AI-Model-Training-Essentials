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
# CI/CD Pipeline Configuration
Kino-automate ng mga pipeline ng Continuous Integration (CI) at Continuous Deployment (CD) ang proseso ng pagbuo, pagsubok, at pag-deploy ng software. Sinasaklaw ng reference na ito ang mga pattern ng configuration para sa pinakasikat na CI/CD platform: GitHub Actions, GitLab CI, at pangkalahatang mga prinsipyo ng disenyo ng pipeline.
---

## Mga Pagkilos sa GitHub
### Istraktura ng Daloy ng Trabaho
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

### Mga Karaniwang Trigger
| Trigger | Paglalarawan |
|---------|-------------|
| `on: push`| Sa bawat tulak |
| `on: pull_request`| Sa PR bukas, i-update, muling buksan |
| `on: schedule`| Cron-based na iskedyul |
| `on: workflow_dispatch`| Manu-manong trigger |
| `on: release`| Sa paggawa ng release |
| `on: workflow_call`| Tinatawag ng isa pang daloy ng trabaho (magagamit muli) |
### Mga Pangunahing Tampok
| Tampok | Paglalarawan |
|---------|-------------|
| **Diskarte sa matrix** | Patakbuhin ang parehong trabaho na may iba't ibang mga configuration |
| **Mga Lihim** | Mga naka-encrypt na variable ng kapaligiran (`${{ secrets.MY_SECRET }}`) |
| **Mga Kapaligiran** | Mga target sa deployment na may mga panuntunan sa proteksyon |
| **Pag-cache** | Mga dependency ng cache sa pagitan ng mga pagtakbo |
| **Mga artifact** | Mag-upload ng mga file mula sa mga trabaho (mga ulat sa pagsubok, mga build) |
| **Muling magamit na daloy ng trabaho** | Ibahagi ang lohika ng daloy ng trabaho sa mga repositoryo |
| **Mga pinagsama-samang pagkilos** | Pagsamahin ang maraming hakbang sa isang aksyon |
### Diskarte sa Matrix
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
### Istraktura ng Pipeline
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

### Mga Keyword
| Keyword | Paglalarawan |
|---------|-------------|
| `stages`| Tukuyin ang mga yugto ng pipeline at ang kanilang pagkakasunud-sunod |
| `stage`| Magtalaga ng trabaho sa isang yugto |
| `script`| Mga utos na isagawa |
| `before_script`| Ang mga utos ay tumatakbo bago ang pangunahing script |
| `after_script`| Ang mga utos ay tumatakbo pagkatapos ng pangunahing script (kahit sa pagkabigo) |
| `only / except`| Kontrolin kapag tumatakbo ang mga trabaho (mga sangay, mga tag) |
| `rules`| Mas nababaluktot na bersyon ng lamang/maliban sa |
| `variables`| Tukuyin ang mga variable ng CI/CD |
| `cache`| Cache file sa pagitan ng pipeline runs |
| `artifacts`| Mga file na ipapasa sa pagitan ng mga trabaho |
| `environment`| Deployment environment |
| `when`| Kontrolin ang pagpapatupad ng trabaho (on_success, on_failure, manual, palaging) |
| `needs`| Tukuyin ang mga dependency sa trabaho (DAG mode) |
| `extends`| Magmana ng configuration mula sa ibang trabaho |
| `include`| Mag-import ng mga panlabas na YAML file |
### Mga Paunang Natukoy na Variable
| Variable | Paglalarawan |
|----------|-------------|
| `$CI_COMMIT_SHA`| Kasalukuyang commit hash |
| `$CI_COMMIT_REF_NAME`| Pangalan ng sangay o tag |
| `$CI_PIPELINE_ID`| Pipeline ID |
| `$CI_JOB_ID`| ID ng Trabaho |
| `$CI_PROJECT_DIR`| Buong landas sa proyekto |
| `$CI_REGISTRY`| URL ng pagpapatala ng container |
| `$CI_DEFAULT_BRANCH`| Default na pangalan ng sangay |
---

## Mga Pattern ng Disenyo ng Pipeline
### Mga Karaniwang Pattern
| Pattern | Paglalarawan |
|---------|-------------|
| **Bumuo nang isang beses, mag-deploy ng marami** | Bumuo ng artifact nang isang beses; i-deploy ang parehong artifact sa bawat kapaligiran |
| **Mga tseke ng gate** | Manu-manong pag-apruba bago ang pag-deploy ng produksyon |
| **Mga tampok na flag** | I-deploy sa produksyon ngunit itago sa likod ng feature flag |
| **Pag-deploy ng Canary** | I-deploy sa maliit na porsyento; subaybayan; ilabas |
| **Asul-berdeng deployment** | Dalawang magkatulad na kapaligiran; lumipat ng trapiko |
| **Parallel testing** | Magpatakbo ng mga test suite nang magkatulad upang mabawasan ang oras ng pipeline |
| **Lint muna** | Magpatakbo ng mga linter bago ang mga mamahaling pagsubok; mabilis mabigo |
| **Mga dependency sa cache** | Cache node_modules, pip, Maven para mapabilis ang mga build |
### Mga Yugto ng Pipeline (Karaniwang)
| Yugto | Layunin |
|-------|---------|
| **Lint** | Estilo ng code at static na pagsusuri |
| **Build** | Compile; bundle; lumikha ng mga artifact |
| **Pagsusulit sa unit** | Mabilis na mga pagsubok; walang mga panlabas na dependencies |
| **Pagsusulit sa pagsasama** | Mga pagsubok na may mga database; Mga API; panlabas na serbisyo |
| **Pag-scan sa seguridad** | Mga kahinaan sa dependency; lihim na pag-scan; SAST |
| **Package** | Lumikha ng imahe ng Docker; bumuo ng release artifacts |
| **I-deploy ang pagtatanghal ng dula** | I-deploy sa kapaligiran ng pagtatanghal ng dula |
| **E2E test** | Mga kumpletong pagsubok sa system laban sa pagtatanghal ng dula |
| **I-deploy ang produksyon** | I-deploy sa produksyon (manual o awtomatiko) |
| **Smoke test** | I-verify na maayos ang deployment |
---

## Mga Istratehiya sa Pag-cache
| Wika / Tool | Path ng Cache | Halimbawa |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`na may susi mula sa`requirements.txt`hash |
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`na may built-in na caching |
| **Java (Maven)** | `~/.m2/repository`| Cache na may key mula sa`pom.xml`hash |
| **Java (Gradle)** | `~/.gradle/caches`| Cache na may key mula sa`build.gradle`hash |
| **Pumunta** | `~/go/pkg/mod`| Cache na may key mula sa`go.sum`hash |
| **Kalawang (Cargo)** | `~/.cargo/registry`| Cache na may key mula sa`Cargo.lock`hash |
| **Docker** | Pag-cache ng layer ng Docker | `docker/build-push-action`na may cache-mula sa |
---

## Pag-troubleshoot
| Problema | Solusyon |
|---------|----------|
| **Mabagal ang pipeline** | Mga dependency ng cache; parallelise trabaho; gumamit ng mas maliliit na batayang larawan |
| **Hindi magagamit ang mga lihim** | Suriin ang lihim na pangalan; i-verify ang saklaw ng kapaligiran; suriin ang mga paghihigpit sa PR |
| **Masyadong malaki ang artifact** | Ibukod ang mga hindi kinakailangang file; i-compress; gumamit ng mas maikling pagpapanatili |
| **Matrix masyadong malaki** | Bawasan ang mga kumbinasyon; gamitin ang`include`/`exclude`|
| **Mga patumpik-tumpik na pagsubok** | Quarantine flaky tests; ayusin ang sanhi ng ugat; subukang muli gamit ang`retry:`|
| **Tinanggihan ang pahintulot** | Suriin ang mga saklaw ng token; i-verify ang mga pahintulot ng runner |
---

## Buod
Ang mga pipeline ng CI/CD ay nag-automate ng pagbuo, pagsubok, at pag-deploy ng software. Gumagamit ang GitHub Actions ng mga workflow ng YAML na na-trigger ng mga kaganapan sa repository; Gumagamit ang GitLab CI ng mga yugto at trabaho na may mga flexible na panuntunan. Kabilang sa mga pangunahing pattern ang: bumuo sa sandaling i-deploy ang marami; mga pagsusuri sa gate bago ang produksyon; lint muna para sa mabilis na feedback; cache dependencies upang mapabilis ang mga build; at parallelise na mga pagsubok. Ang mga yugto ng pipeline ay karaniwang umuunlad mula sa lint → build → test → security → package → deploy → smoke test. Ang mga diskarte sa pag-cache ay nag-iiba ayon sa wika ngunit sumusunod sa parehong prinsipyo: mga direktoryo ng dependency ng cache na na-key ng mga lock file na hashes. Ang layunin ay mabilis, maaasahang feedback sa bawat pagbabago at ligtas, nauulit na pag-deploy sa produksyon.