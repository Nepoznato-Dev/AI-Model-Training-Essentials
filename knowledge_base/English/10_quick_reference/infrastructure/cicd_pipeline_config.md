<!--
---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.1"
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
# CI/CD Pipeline Configuration

Continuous Integration (CI) and Continuous Deployment (CD) pipelines automate the process of building, testing, and deploying software. This reference covers the configuration patterns for the most popular CI/CD platforms: GitHub Actions, GitLab CI, and general pipeline design principles.

---

## GitHub Actions

### Workflow Structure

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

### Common Triggers

| Trigger | Description |
|---------|-------------|
| `on: push` | On every push |
| `on: pull_request` | On PR open, update, reopen |
| `on: schedule` | Cron-based schedule |
| `on: workflow_dispatch` | Manual trigger |
| `on: release` | On release creation |
| `on: workflow_call` | Called by another workflow (reusable) |

### Key Features

| Feature | Description |
|---------|-------------|
| **Matrix strategy** | Run the same job with different configurations |
| **Secrets** | Encrypted environment variables (`${{ secrets.MY_SECRET }}`) |
| **Environments** | Deployment targets with protection rules |
| **Caching** | Cache dependencies between runs |
| **Artifacts** | Upload files from jobs (test reports, builds) |
| **Reusable workflows** | Share workflow logic across repositories |
| **Composite actions** | Combine multiple steps into one action |

### Matrix Strategy

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

### Pipeline Structure

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

### Key Keywords

| Keyword | Description |
|---------|-------------|
| `stages` | Define pipeline stages and their order |
| `stage` | Assign a job to a stage |
| `script` | Commands to execute |
| `before_script` | Commands run before main script |
| `after_script` | Commands run after main script (even on failure) |
| `only / except` | Control when jobs run (branches, tags) |
| `rules` | More flexible version of only/except |
| `variables` | Define CI/CD variables |
| `cache` | Cache files between pipeline runs |
| `artifacts` | Files to pass between jobs |
| `environment` | Deployment environment |
| `when` | Control job execution (on_success, on_failure, manual, always) |
| `needs` | Specify job dependencies (DAG mode) |
| `extends` | Inherit configuration from another job |
| `include` | Import external YAML files |

### Predefined Variables

| Variable | Description |
|----------|-------------|
| `$CI_COMMIT_SHA` | Current commit hash |
| `$CI_COMMIT_REF_NAME` | Branch or tag name |
| `$CI_PIPELINE_ID` | Pipeline ID |
| `$CI_JOB_ID` | Job ID |
| `$CI_PROJECT_DIR` | Full path to the project |
| `$CI_REGISTRY` | Container registry URL |
| `$CI_DEFAULT_BRANCH` | Default branch name |

---

## Pipeline Design Patterns

### Common Patterns

| Pattern | Description |
|---------|-------------|
| **Build once, deploy many** | Build artifact once; deploy same artifact to each environment |
| **Gate checks** | Manual approval before production deployment |
| **Feature flags** | Deploy to production but hide behind feature flag |
| **Canary deployment** | Deploy to small percentage; monitor; roll out |
| **Blue-green deployment** | Two identical environments; switch traffic |
| **Parallel testing** | Run test suites in parallel to reduce pipeline time |
| **Lint first** | Run linters before expensive tests; fail fast |
| **Cache dependencies** | Cache node_modules, pip, Maven to speed up builds |

### Pipeline Stages (Typical)

| Stage | Purpose |
|-------|---------|
| **Lint** | Code style and static analysis |
| **Build** | Compile; bundle; create artifacts |
| **Unit test** | Fast tests; no external dependencies |
| **Integration test** | Tests with databases; APIs; external services |
| **Security scan** | Dependency vulnerabilities; secret scanning; SAST |
| **Package** | Create Docker image; build release artifacts |
| **Deploy staging** | Deploy to staging environment |
| **E2E test** | Full system tests against staging |
| **Deploy production** | Deploy to production (manual or automatic) |
| **Smoke test** | Verify deployment is healthy |

---

## Caching Strategies

| Language / Tool | Cache Path | Example |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip` | `actions/cache` with key from `requirements.txt` hash |
| **Node.js (npm)** | `~/.npm` | `actions/setup-node` with built-in caching |
| **Java (Maven)** | `~/.m2/repository` | Cache with key from `pom.xml` hash |
| **Java (Gradle)** | `~/.gradle/caches` | Cache with key from `build.gradle` hash |
| **Go** | `~/go/pkg/mod` | Cache with key from `go.sum` hash |
| **Rust (Cargo)** | `~/.cargo/registry` | Cache with key from `Cargo.lock` hash |
| **Docker** | Docker layer caching | `docker/build-push-action` with cache-from |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Pipeline is slow** | Cache dependencies; parallelise jobs; use smaller base images |
| **Secrets not available** | Check secret name; verify environment scope; check fork PR restrictions |
| **Artifact too large** | Exclude unnecessary files; compress; use shorter retention |
| **Matrix too large** | Reduce combinations; use `include` / `exclude` |
| **Flaky tests** | Quarantine flaky tests; fix root cause; retry with `retry:` |
| **Permission denied** | Check token scopes; verify runner permissions |

---

## Summary

CI/CD pipelines automate building, testing, and deploying software. GitHub Actions uses YAML workflows triggered by repository events; GitLab CI uses stages and jobs with flexible rules. Key patterns include: build once deploy many; gate checks before production; lint first for fast feedback; cache dependencies to speed up builds; and parallelise tests. Pipeline stages typically progress from lint → build → test → security → package → deploy → smoke test. Caching strategies vary by language but follow the same principle: cache dependency directories keyed by lock file hashes. The goal is fast, reliable feedback on every change and safe, repeatable deployments to production.
