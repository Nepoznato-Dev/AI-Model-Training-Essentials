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
# Configuration du pipeline CI/CD
Les pipelines d'intégration continue (CI) et de déploiement continu (CD) automatisent le processus de création, de test et de déploiement de logiciels. Cette référence couvre les modèles de configuration pour les plateformes CI/CD les plus populaires : GitHub Actions, GitLab CI et les principes généraux de conception de pipeline.
---

## Actions GitHub
### Structure du flux de travail
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

### Déclencheurs courants
| Déclencheur | Descriptif |
|---------|-------------|
| `on: push`| À chaque poussée |
| `on: pull_request`| Sur PR ouvrir, mettre à jour, rouvrir |
| `on: schedule`| Planification basée sur Cron |
| `on: workflow_dispatch`| Déclenchement manuel |
| `on: release`| Lors de la création de la version |
| `on: workflow_call`| Appelé par un autre workflow (réutilisable) |
### Principales fonctionnalités
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Stratégie matricielle** | Exécutez le même travail avec différentes configurations |
| **Secrets** | Variables d'environnement chiffrées (`${{ secrets.MY_SECRET }}`) |
| **Environnements** | Cibles de déploiement avec règles de protection |
| **Mise en cache** | Dépendances du cache entre les exécutions |
| **Artefacts** | Télécharger des fichiers à partir de tâches (rapports de test, builds) |
| **Flux de travail réutilisables** | Partager la logique du workflow entre les référentiels |
| **Actions composites** | Combinez plusieurs étapes en une seule action |
### Stratégie matricielle
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

## GitLabCI
### Structure des pipelines
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

### Mots-clés clés
| Mot clé | Descriptif |
|---------|-------------|
| `stages`| Définir les étapes du pipeline et leur ordre |
| `stage`| Attribuer une tâche à une étape |
| `script`| Commandes à exécuter |
| `before_script`| Commandes exécutées avant le script principal |
| `after_script`| Commandes exécutées après le script principal (même en cas d'échec) |
| `only / except`| Contrôler le moment où les tâches sont exécutées (branches, balises) |
| `rules`| Version plus flexible de seulement/sauf |
| `variables`| Définir les variables CI/CD |
| `cache`| Mettre en cache les fichiers entre les exécutions du pipeline |
| `artifacts`| Fichiers à transmettre entre les tâches |
| `environment`| Environnement de déploiement |
| `when`| Contrôler l'exécution des tâches (on_success, on_failure, manuel, toujours) |
| `needs`| Spécifier les dépendances du travail (mode DAG) |
| `extends`| Hériter de la configuration d'un autre travail |
| `include`| Importer des fichiers YAML externes |
### Variables prédéfinies
| Variables | Descriptif |
|--------------|-------------|
| `$CI_COMMIT_SHA`| Hachage de validation actuel |
| `$CI_COMMIT_REF_NAME`| Nom de la branche ou de l'étiquette |
| `$CI_PIPELINE_ID`| ID du pipeline |
| `$CI_JOB_ID`| Identifiant du travail |
| `$CI_PROJECT_DIR`| Chemin complet vers le projet |
| `$CI_REGISTRY`| URL du registre de conteneurs |
| `$CI_DEFAULT_BRANCH`| Nom de branche par défaut |
---

## Modèles de conception de pipelines
### Modèles courants
| Modèle | Descriptif |
|---------|-------------|
| **Construisez une fois, déployez plusieurs** | Construisez l'artefact une fois ; déployer le même artefact dans chaque environnement |
| **Contrôles aux portes** | Approbation manuelle avant le déploiement en production |
| **Drapeaux de fonctionnalité** | Déployer en production mais se cacher derrière l'indicateur de fonctionnalité |
| **Déploiement Canary** | Déployer sur un petit pourcentage ; moniteur; déployer |
| **Déploiement bleu-vert** | Deux environnements identiques ; changer de trafic |
| **Tests parallèles** | Exécutez des suites de tests en parallèle pour réduire le temps de pipeline |
| **Les peluches en premier** | Exécutez des linters avant des tests coûteux ; échouer rapidement |
| **Dépendances du cache** | Cachez node_modules, pip, Maven pour accélérer les builds |
### Étapes du pipeline (typique)
| Scène | Objectif |
|-------|--------------|
| **Charpie** | Style de code et analyse statique |
| **Construire** | Compiler; paquet; créer des artefacts |
| **Test unitaire** | Tests rapides ; pas de dépendances externes |
| **Test d'intégration** | Tests avec des bases de données ; Apis; prestations externes |
| **Analyse de sécurité** | Vulnérabilités de dépendance ; analyse secrète ; SAST |
| **Forfait** | Créer une image Docker ; construire des artefacts de version |
| **Déployer la préparation** | Déployer dans un environnement de test |
| **Test E2E** | Tests complets du système par rapport à la mise en scène |
| **Déployer la production** | Déployer en production (manuel ou automatique) |
| **Test de fumée** | Vérifier que le déploiement est sain |
---

## Stratégies de mise en cache
| Langage / Outil | Chemin du cache | Exemple |
|----------------|-----------|---------|
| **Python (pépin)** | `~/.cache/pip`| `actions/cache`avec clé du hachage`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`avec mise en cache intégrée |
| **Java (Maven)** | `~/.m2/repository`| Cache avec clé du hachage`pom.xml`|
| **Java (Gradle)** | `~/.gradle/caches`| Cache avec clé du hachage`build.gradle`|
| **Allez** | `~/go/pkg/mod`| Cache avec clé du hachage`go.sum`|
| **Rouille (Cargo)** | `~/.cargo/registry`| Cache avec clé du hachage`Cargo.lock`|
| **Docker** | Mise en cache de la couche Docker | `docker/build-push-action`avec cache-from |
---

## Dépannage
| Problème | Solutions |
|---------|----------|
| **Le pipeline est lent** | Dépendances du cache ; paralléliser les tâches ; utiliser des images de base plus petites |
| **Secrets non disponibles** | Vérifiez le nom secret ; vérifier la portée de l'environnement ; vérifier les restrictions de relations publiques du fourchette |
| **Artefact trop grand** | Excluez les fichiers inutiles ; compresse; utiliser une rétention plus courte |
| **Matrice trop grande** | Réduisez les combinaisons ; utiliser`include`/`exclude`|
| **Tests feuilletés** | Tests floconneux de quarantaine ; corriger la cause première ; réessayez avec`retry:`|
| **Autorisation refusée** | Vérifiez les portées des jetons ; vérifier les autorisations des coureurs |
---

## Résumé
Les pipelines CI/CD automatisent la création, les tests et le déploiement de logiciels. GitHub Actions utilise des workflows YAML déclenchés par les événements du référentiel ; GitLab CI utilise des étapes et des tâches avec des règles flexibles. Les modèles clés incluent : construire une fois, déployer plusieurs ; contrôles aux portes avant la production ; peluchez en premier pour un retour rapide ; dépendances de cache pour accélérer les builds ; et paralléliser les tests. Les étapes du pipeline progressent généralement de lint → build → test → sécurité → package → déploiement → smoke test. Les stratégies de mise en cache varient selon la langue mais suivent le même principe : mettre en cache les répertoires de dépendances codés par des hachages de fichiers de verrouillage. L’objectif est d’obtenir un retour rapide et fiable sur chaque modification et des déploiements sûrs et reproductibles en production.