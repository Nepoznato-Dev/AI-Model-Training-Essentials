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
# CI/CD-Pipeline-Konfiguration
Continuous Integration (CI)- und Continuous Deployment (CD)-Pipelines automatisieren den Prozess des Erstellens, Testens und Bereitstellens von Software. Diese Referenz behandelt die Konfigurationsmuster für die gängigsten CI/CD-Plattformen: GitHub Actions, GitLab CI und allgemeine Pipeline-Designprinzipien.
---

## GitHub-Aktionen
### Workflow-Struktur
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

### Häufige Auslöser
| Auslöser | Beschreibung |
|---------|-------------|
| `on: push`| Bei jedem Stoß |
| `on: pull_request`| Auf PR öffnen, aktualisieren, erneut öffnen |
| `on: schedule`| Cron-basierter Zeitplan |
| `on: workflow_dispatch`| Manueller Auslöser |
| `on: release`| Bei der Release-Erstellung |
| `on: workflow_call`| Von einem anderen Workflow aufgerufen (wiederverwendbar) |
### Hauptmerkmale
| Funktion | Beschreibung |
|---------|-------------|
| **Matrixstrategie** | Führen Sie denselben Job mit unterschiedlichen Konfigurationen aus |
| **Geheimnisse** | Verschlüsselte Umgebungsvariablen (`${{ secrets.MY_SECRET }}`) |
| **Umgebungen** | Bereitstellungsziele mit Schutzregeln |
| **Caching** | Cache-Abhängigkeiten zwischen Läufen |
| **Artefakte** | Dateien von Jobs hochladen (Testberichte, Builds) |
| **Wiederverwendbare Workflows** | Workflow-Logik über Repositorys hinweg teilen |
| **Zusammengesetzte Aktionen** | Kombinieren Sie mehrere Schritte zu einer Aktion |
### Matrix-Strategie
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
### Pipeline-Struktur
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

### Schlüsselwörter
| Schlüsselwort | Beschreibung |
|---------|-------------|
| `stages`| Definieren Sie Pipeline-Stufen und deren Reihenfolge |
| `stage`| Weisen Sie einen Job einer Phase zu |
| `script`| Auszuführende Befehle |
| `before_script`| Befehle werden vor dem Hauptskript | ausgeführt
| `after_script`| Befehle werden nach dem Hauptskript ausgeführt (auch bei einem Fehler) |
| `only / except`| Steuern Sie, wann Jobs ausgeführt werden (Zweige, Tags) |
| `rules`| Flexiblere Version von only/exclusive |
| `variables`| CI/CD-Variablen definieren |
| `cache`| Dateien zwischen Pipeline-Ausführungen zwischenspeichern |
| `artifacts`| Zwischen Jobs zu übergebende Dateien |
| `environment`| Bereitstellungsumgebung |
| `when`| Jobausführung steuern (on_success, on_failure, manuell, immer) |
| `needs`| Jobabhängigkeiten angeben (DAG-Modus) |
| `extends`| Konfiguration von einem anderen Job übernehmen |
| `include`| Externe YAML-Dateien importieren |
### Vordefinierte Variablen
| Variable | Beschreibung |
|----------|-------------|
| `$CI_COMMIT_SHA`| Aktueller Commit-Hash |
| `$CI_COMMIT_REF_NAME`| Zweig- oder Tagname |
| `$CI_PIPELINE_ID`| Pipeline-ID |
| `$CI_JOB_ID`| Job-ID |
| `$CI_PROJECT_DIR`| Vollständiger Pfad zum Projekt |
| `$CI_REGISTRY`| URL der Containerregistrierung |
| `$CI_DEFAULT_BRANCH`| Standardzweigname |
---

## Pipeline-Entwurfsmuster
### Gemeinsame Muster
| Muster | Beschreibung |
|---------|-------------|
| **Einmal erstellen, viele bereitstellen** | Artefakt einmal bauen; Stellen Sie dasselbe Artefakt in jeder Umgebung bereit |
| **Torkontrollen** | Manuelle Genehmigung vor der Produktionsbereitstellung |
| **Feature-Flags** | In der Produktion bereitstellen, aber hinter dem Feature-Flag verstecken |
| **Canary-Bereitstellung** | Bereitstellung auf einen kleinen Prozentsatz; Monitor; ausrollen |
| **Blau-grüne Bereitstellung** | Zwei identische Umgebungen; Verkehr wechseln |
| **Paralleles Testen** | Führen Sie Testsuiten parallel aus, um die Pipeline-Zeit zu verkürzen |
| **Zuerst fusseln** | Führen Sie Linters vor teuren Tests durch; schnell scheitern |
| **Cache-Abhängigkeiten** | Node_modules, pip, Maven zwischenspeichern, um Builds zu beschleunigen |
### Pipeline-Stufen (typisch)
| Bühne | Zweck |
|-------|---------|
| **Fussel** | Codestil und statische Analyse |
| **Bauen** | Kompilieren; bündeln; Artefakte erstellen |
| **Einheitentest** | Schnelle Tests; keine externen Abhängigkeiten |
| **Integrationstest** | Tests mit Datenbanken; APIs; externe Dienstleistungen |
| **Sicherheitsscan** | Abhängigkeitsschwachstellen; geheimes Scannen; SAST |
| **Paket** | Docker-Image erstellen; Build-Release-Artefakte |
| **Staging bereitstellen** | In der Staging-Umgebung bereitstellen |
| **E2E-Test** | Vollständige Systemtests gegen Staging |
| **Produktion bereitstellen** | Bereitstellung in der Produktion (manuell oder automatisch) |
| **Rauchtest** | Sicherstellen, dass die Bereitstellung fehlerfrei ist |
---

## Caching-Strategien
| Sprache / Werkzeug | Cache-Pfad | Beispiel |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`mit Schlüssel aus`requirements.txt`Hash |
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`mit integriertem Caching |
| **Java (Maven)** | `~/.m2/repository`| Cache mit Schlüssel vom `pom.xml`-Hash |
| **Java (Gradle)** | `~/.gradle/caches`| Cache mit Schlüssel vom `build.gradle`-Hash |
| **Los** | `~/go/pkg/mod`| Cache mit Schlüssel vom `go.sum`-Hash |
| **Rost (Fracht)** | `~/.cargo/registry`| Cache mit Schlüssel vom `Cargo.lock`-Hash |
| **Docker** | Docker-Layer-Caching | `docker/build-push-action`mit Cache-von |
---

## Fehlerbehebung
| Problem | Lösung |
|---------|----------|
| **Pipeline ist langsam** | Cache-Abhängigkeiten; Jobs parallelisieren; Verwenden Sie kleinere Basisbilder |
| **Geheimnisse nicht verfügbar** | Überprüfen Sie den geheimen Namen. Überprüfen Sie den Umgebungsbereich. Überprüfen Sie die PR-Einschränkungen für die Gabel |
| **Artefakt zu groß** | Schließen Sie unnötige Dateien aus; Kompresse; Verwenden Sie eine kürzere Aufbewahrungszeit |
| **Matrix zu groß** | Kombinationen reduzieren; verwenden Sie`include`/`exclude`|
| **Flockentests** | Quarantäne-Flockentests; Grundursache beheben; Versuchen Sie es erneut mit`retry:`|
| **Erlaubnis verweigert** | Überprüfen Sie den Token-Bereich. Läuferberechtigungen überprüfen |
---

## Zusammenfassung
CI/CD-Pipelines automatisieren das Erstellen, Testen und Bereitstellen von Software. GitHub Actions verwendet YAML-Workflows, die durch Repository-Ereignisse ausgelöst werden; GitLab CI verwendet Phasen und Jobs mit flexiblen Regeln. Zu den wichtigsten Mustern gehören: Einmal erstellen, viele bereitstellen; Gate-Checks vor der Produktion; Flusen zuerst für schnelles Feedback; Cache-Abhängigkeiten, um Builds zu beschleunigen; und Tests parallelisieren. Die Pipeline-Stufen verlaufen typischerweise von Lint → Build → Test → Sicherheit → Paket → Bereitstellung → Rauchtest. Caching-Strategien variieren je nach Sprache, folgen aber demselben Prinzip: Abhängigkeitsverzeichnisse werden zwischengespeichert, die durch Sperrdatei-Hashes verschlüsselt sind. Das Ziel ist schnelles, zuverlässiges Feedback zu jeder Änderung und sichere, wiederholbare Bereitstellungen in der Produktion.