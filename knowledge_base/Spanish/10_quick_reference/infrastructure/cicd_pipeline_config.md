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
# Configuración de canalización CI/CD
Los canales de integración continua (CI) e implementación continua (CD) automatizan el proceso de creación, prueba e implementación de software. Esta referencia cubre los patrones de configuración para las plataformas CI/CD más populares: GitHub Actions, GitLab CI y principios generales de diseño de canalizaciones.
---

## Acciones de GitHub
### Estructura del flujo de trabajo
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

### Desencadenantes comunes
| Gatillo | Descripción |
|---------|-------------|
| `on: push`| En cada empujón |
| `on: pull_request`| En PR abrir, actualizar, reabrir |
| `on: schedule`| Programación basada en cron |
| `on: workflow_dispatch`| Gatillo manual |
| `on: release`| Sobre la creación del lanzamiento |
| `on: workflow_call`| Llamado por otro flujo de trabajo (reutilizable) |
### Características clave
| Característica | Descripción |
|---------|-------------|
| **Estrategia matricial** | Ejecute el mismo trabajo con diferentes configuraciones |
| **Secretos** | Variables de entorno cifradas (`${{ secrets.MY_SECRET }}`) |
| **Ambientes** | Objetivos de implementación con reglas de protección |
| **Almacenamiento en caché** | Dependencias de caché entre ejecuciones |
| **Artefactos** | Cargar archivos desde trabajos (informes de prueba, compilaciones) |
| **Flujos de trabajo reutilizables** | Compartir la lógica del flujo de trabajo entre repositorios |
| **Acciones compuestas** | Combine varios pasos en una sola acción |
### Estrategia matricial
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
### Estructura de la tubería
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

### Palabras clave clave
| Palabra clave | Descripción |
|---------|-------------|
| `stages`| Definir las etapas del pipeline y su orden |
| `stage`| Asignar un trabajo a una etapa |
| `script`| Comandos a ejecutar |
| `before_script`| Los comandos se ejecutan antes del script principal |
| `after_script`| Los comandos se ejecutan después del script principal (incluso en caso de error) |
| `only / except`| Controlar cuándo se ejecutan los trabajos (ramas, etiquetas) |
| `rules`| Versión más flexible de sólo/excepto |
| `variables`| Definir variables CI/CD |
| `cache`| Archivos de caché entre ejecuciones de canalización |
| `artifacts`| Archivos para pasar entre trabajos |
| `environment`| Entorno de implementación |
| `when`| Controlar la ejecución del trabajo (on_success, on_failure, manual, siempre) |
| `needs`| Especificar dependencias del trabajo (modo DAG) |
| `extends`| Heredar configuración de otro trabajo |
| `include`| Importar archivos YAML externos |
### Variables predefinidas
| Variables | Descripción |
|----------|-------------|
| `$CI_COMMIT_SHA`| Hash de confirmación actual |
| `$CI_COMMIT_REF_NAME`| Nombre de rama o etiqueta |
| `$CI_PIPELINE_ID`| ID de tubería |
| `$CI_JOB_ID`| ID de trabajo |
| `$CI_PROJECT_DIR`| Ruta completa al proyecto |
| `$CI_REGISTRY`| URL de registro de contenedor |
| `$CI_DEFAULT_BRANCH`| Nombre de sucursal predeterminado |
---

## Patrones de diseño de tuberías
### Patrones comunes
| Patrón | Descripción |
|---------|-------------|
| **Construya una vez, implemente muchas** | Construye el artefacto una vez; implementar el mismo artefacto en cada entorno |
| **Revisiones de puerta** | Aprobación manual antes del despliegue en producción |
| **Marcas de características** | Implementar en producción pero esconderse detrás del indicador de función |
| **Implementación en Canarias** | Implementar a un pequeño porcentaje; monitor; desplegar |
| **Implementación azul-verde** | Dos ambientes idénticos; cambiar el tráfico |
| **Pruebas paralelas** | Ejecute conjuntos de pruebas en paralelo para reducir el tiempo de canalización |
| **Pelusa primero** | Ejecute linters antes de pruebas costosas; fallar rápido |
| **Dependencias de caché** | Caché node_modules, pip, Maven para acelerar las compilaciones |
### Etapas de canalización (típicas)
| Etapa | Propósito |
|-------|---------|
| **Pelusa** | Estilo de código y análisis estático |
| **Construir** | Compilar; manojo; crear artefactos |
| **Prueba unitaria** | Pruebas rápidas; sin dependencias externas |
| **Prueba de integración** | Pruebas con bases de datos; API; servicios externos |
| **Escaneo de seguridad** | Vulnerabilidades de dependencia; escaneo secreto; SAST |
| **Paquete** | Crear imagen de Docker; construir artefactos de lanzamiento |
| **Implementar preparación** | Implementar en el entorno de ensayo |
| **Prueba E2E** | Pruebas completas del sistema contra puesta en escena |
| **Implementar producción** | Implementar en producción (manual o automático) |
| **Prueba de humo** | Verificar que la implementación esté en buen estado |
---

## Estrategias de almacenamiento en caché
| Idioma / Herramienta | Ruta de caché | Ejemplo |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`con clave del hash`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`con almacenamiento en caché integrado |
| **Java (Maven)** | `~/.m2/repository`| Caché con clave del hash`pom.xml`|
| **Java (Gradle)** | `~/.gradle/caches`| Caché con clave del hash`build.gradle`|
| **Ir** | `~/go/pkg/mod`| Caché con clave del hash`go.sum`|
| **Óxido (Carga)** | `~/.cargo/registry`| Caché con clave del hash`Cargo.lock`|
| **Acoplador** | Almacenamiento en caché de la capa acoplable | `docker/build-push-action`con caché desde |
---

## Solución de problemas
| Problema | Solución |
|---------|----------|
| **La tubería es lenta** | Dependencias de caché; paralelizar puestos de trabajo; utilizar imágenes base más pequeñas |
| **Secretos no disponibles** | Verifique el nombre secreto; verificar el alcance del entorno; comprobar las restricciones de relaciones públicas de la bifurcación |
| **Artefacto demasiado grande** | Excluir archivos innecesarios; comprimir; utilizar una retención más corta |
| **Matriz demasiado grande** | Reducir combinaciones; utilizar`include`/`exclude`|
| **Pruebas inestables** | Poner en cuarentena pruebas escamosas; solucionar la causa raíz; reintentar con`retry:`|
| **Permiso denegado** | Verifique los alcances de los tokens; verificar los permisos del corredor |
---

## Resumen
Los canales de CI/CD automatizan la creación, prueba e implementación de software. GitHub Actions utiliza flujos de trabajo YAML activados por eventos del repositorio; GitLab CI utiliza etapas y trabajos con reglas flexibles. Los patrones clave incluyen: construir una vez, implementar muchas; controles de puerta antes de la producción; pelusa primero para una respuesta rápida; dependencias de caché para acelerar las compilaciones; y pruebas de paralelización. Las etapas de la canalización generalmente avanzan desde pelusa → compilación → prueba → seguridad → paquete → implementación → prueba de humo. Las estrategias de almacenamiento en caché varían según el idioma, pero siguen el mismo principio: directorios de dependencia de caché codificados por hashes de archivos de bloqueo. El objetivo es una retroalimentación rápida y confiable sobre cada cambio y implementaciones seguras y repetibles en producción.