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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Configurazione della pipeline CI/CD
Le pipeline di integrazione continua (CI) e distribuzione continua (CD) automatizzano il processo di creazione, test e distribuzione del software. Questo riferimento copre i modelli di configurazione per le piattaforme CI/CD più popolari: GitHub Actions, GitLab CI e i principi generali di progettazione della pipeline.
---

## Azioni GitHub
### Struttura del flusso di lavoro
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

### Trigger comuni
| Trigger | Descrizione |
|---------|-----|
| `on: push`| Ad ogni spinta |
| `on: pull_request`| Su PR apri, aggiorna, riapri |
| `on: schedule`| Pianificazione basata su cron |
| `on: workflow_dispatch`| Trigger manuale |
| `on: release`| Alla creazione della versione |
| `on: workflow_call`| Chiamato da un altro flusso di lavoro (riutilizzabile) |
### Caratteristiche principali
| Caratteristica | Descrizione |
|---------|-----|
| **Strategia Matrix** | Esegui lo stesso lavoro con configurazioni diverse |
| **Segreti** | Variabili di ambiente crittografate (`${{ secrets.MY_SECRET }}`) |
| **Ambienti** | Obiettivi di distribuzione con regole di protezione |
| **Memorizzazione nella cache** | Dipendenze della cache tra le esecuzioni |
| **Manufatti** | Carica file da lavori (rapporti di test, build) |
| **Flussi di lavoro riutilizzabili** | Condividere la logica del flusso di lavoro tra repository |
| **Azioni composite** | Combina più passaggi in un'unica azione |
### Strategia della matrice
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

## CI GitLab
### Struttura della pipeline
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

### Parole chiave chiave
| Parola chiave | Descrizione |
|---------|-----|
| `stages`| Definire le fasi della pipeline e il loro ordine |
| `stage`| Assegnare un lavoro a una fase |
| `script`| Comandi da eseguire |
| `before_script`| I comandi vengono eseguiti prima dello script principale |
| `after_script`| I comandi vengono eseguiti dopo lo script principale (anche in caso di errore) |
| `only / except`| Controllare quando vengono eseguiti i lavori (rami, tag) |
| `rules`| Versione più flessibile di solo/eccetto |
| `variables`| Definire variabili CI/CD |
| `cache`| File di cache tra le esecuzioni della pipeline |
| `artifacts`| File da passare tra lavori |
| `environment`| Ambiente di distribuzione |
| `when`| Controllare l'esecuzione del lavoro (on_success, on_failure, manuale, sempre) |
| `needs`| Specificare le dipendenze del lavoro (modalità DAG) |
| `extends`| Eredita la configurazione da un altro lavoro |
| `include`| Importa file YAML esterni |
### Variabili predefinite
| Variabile | Descrizione |
|----------|-------------|
| `$CI_COMMIT_SHA`| Hash del commit corrente |
| `$CI_COMMIT_REF_NAME`| Nome del ramo o del tag |
| `$CI_PIPELINE_ID`| ID pipeline |
| `$CI_JOB_ID`| ID lavoro |
| `$CI_PROJECT_DIR`| Percorso completo del progetto |
| `$CI_REGISTRY`| URL del registro contenitori |
| `$CI_DEFAULT_BRANCH`| Nome ramo predefinito |
---

## Modelli di progettazione della pipeline
### Modelli comuni
| Modello | Descrizione |
|---------|-----|
| **Costruisci una volta, distribuiscine molti** | Costruisci l'artefatto una volta; distribuire lo stesso artefatto in ciascun ambiente |
| **Controlli cancello** | Approvazione manuale prima della distribuzione in produzione |
| **Flag funzionalità** | Distribuisci in produzione ma nascondi dietro il flag della funzionalità |
| **Distribuzione Canary** | Distribuire in piccola percentuale; monitorare; srotolare |
| **Distribuzione blu-verde** | Due ambienti identici; cambiare traffico |
| **Test paralleli** | Esegui suite di test in parallelo per ridurre i tempi di pipeline |
| **Prima la lanugine** | Eseguire linter prima di test costosi; fallire velocemente |
| **Dipendenze cache** | Memorizza nella cache node_modules, pip, Maven per accelerare le build |
### Fasi della pipeline (tipiche)
| Palcoscenico | Scopo |
|-------|---------|
| **Lanugine** | Stile del codice e analisi statica |
| **Costruisci** | Compilare; fascio; creare artefatti |
| **Test unitario** | Test veloci; nessuna dipendenza esterna |
| **Test di integrazione** | Test con database; API; servizi esterni |
| **Scansione di sicurezza** | Vulnerabilità delle dipendenze; scansione segreta; SAST |
| **Pacchetto** | Crea un'immagine Docker; creare artefatti di rilascio |
| **Distribuisci la gestione temporanea** | Distribuire nell'ambiente di staging |
| **Test E2E** | Test completi del sistema contro lo staging |
| **Distribuire la produzione** | Distribuire in produzione (manuale o automatica) |
| **Test del fumo** | Verificare che la distribuzione sia integra |
---

## Strategie di memorizzazione nella cache
| Lingua/Strumento | Percorso cache | Esempio |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`con chiave dall'hash`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`con memorizzazione nella cache integrata |
| **Java (Maven)** | `~/.m2/repository`| Cache con chiave dall'hash`pom.xml`|
| **Java (Gradle)** | `~/.gradle/caches`| Cache con chiave dall'hash`build.gradle`|
| **Vai** | `~/go/pkg/mod`| Cache con chiave dall'hash`go.sum`|
| **Ruggine (Carico)** | `~/.cargo/registry`| Cache con chiave dall'hash`Cargo.lock`|
| **Docker** | Caching del livello Docker | `docker/build-push-action`con cache da |
---

## Risoluzione dei problemi
| Problema | Soluzione |
|---------|----------|
| **La pipeline è lenta** | Dipendenze della cache; parallelizzare i lavori; utilizzare immagini di base più piccole |
| **Segreti non disponibili** | Controlla il nome segreto; verificare l'ambito dell'ambiente; controlla le restrizioni PR del fork |
| **Artefatto troppo grande** | Escludere file non necessari; comprimere; utilizzare una conservazione più breve |
| **Matrice troppo grande** | Ridurre le combinazioni; utilizzare`include`/`exclude`|
| **Test instabili** | Test instabili in quarantena; risolvere la causa principale; riprovare con`retry:`|
| **Autorizzazione negata** | Controllare gli ambiti dei token; verificare i permessi del corridore |
---

## Riepilogo
Le pipeline CI/CD automatizzano la creazione, il test e la distribuzione del software. GitHub Actions utilizza flussi di lavoro YAML attivati ​​da eventi del repository; GitLab CI utilizza fasi e lavori con regole flessibili. I modelli chiave includono: costruire una volta distribuirne molti; controlli ai cancelli prima della produzione; pelucchi prima per un feedback rapido; dipendenze della cache per accelerare le build; e parallelizzare i test. Le fasi della pipeline in genere procedono da lint → build → test → sicurezza → pacchetto → distribuzione → smoke test. Le strategie di memorizzazione nella cache variano in base alla lingua ma seguono lo stesso principio: directory di dipendenza della cache codificate dagli hash dei file di blocco. L'obiettivo è un feedback rapido e affidabile su ogni modifica e implementazioni sicure e ripetibili nella produzione.