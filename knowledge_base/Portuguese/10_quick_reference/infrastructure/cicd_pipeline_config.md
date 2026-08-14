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
# Configuração do pipeline CI/CD
Os pipelines de integração contínua (CI) e implantação contínua (CD) automatizam o processo de construção, teste e implantação de software. Esta referência aborda os padrões de configuração para as plataformas CI/CD mais populares: GitHub Actions, GitLab CI e princípios gerais de design de pipeline.
---

## Ações do GitHub
### Estrutura do fluxo de trabalho
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

### Gatilhos Comuns
| Gatilho | Descrição |
|--------|-------------|
| `on: push`| A cada impulso |
| `on: pull_request`| No PR abrir, atualizar, reabrir |
| `on: schedule`| Agenda baseada em Cron |
| `on: workflow_dispatch`| Gatilho manual |
| `on: release`| Na criação do lançamento |
| `on: workflow_call`| Chamado por outro fluxo de trabalho (reutilizável) |
### Principais recursos
| Recurso | Descrição |
|--------|-------------|
| **Estratégia matricial** | Execute o mesmo trabalho com configurações diferentes |
| **Segredos** | Variáveis ​​de ambiente criptografadas (`${{ secrets.MY_SECRET }}`) |
| **Ambientes** | Alvos de implantação com regras de proteção |
| **Cache** | Dependências de cache entre execuções |
| **Artefatos** | Carregar arquivos de trabalhos (relatórios de teste, compilações) |
| **Fluxos de trabalho reutilizáveis** | Compartilhe lógica de fluxo de trabalho entre repositórios |
| **Ações compostas** | Combine várias etapas em uma ação |
### Estratégia Matricial
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

## CI do GitLab
### Estrutura do pipeline
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

### Palavras-chave principais
| Palavra-chave | Descrição |
|--------|-------------|
| `stages`| Definir etapas do pipeline e sua ordem |
| `stage`| Atribuir um trabalho a um estágio |
| `script`| Comandos para executar |
| `before_script`| Comandos executados antes do script principal |
| `after_script`| Os comandos são executados após o script principal (mesmo em caso de falha) |
| `only / except`| Controlar quando os jobs são executados (ramificações, tags) |
| `rules`| Versão mais flexível de only/except |
| `variables`| Definir variáveis ​​CI/CD |
| `cache`| Arquivos de cache entre execuções de pipeline |
| `artifacts`| Arquivos para passar entre jobs |
| `environment`| Ambiente de implantação |
| `when`| Controlar a execução do trabalho (on_success, on_failure, manual, sempre) |
| `needs`| Especifique dependências de trabalho (modo DAG) |
| `extends`| Herdar configuração de outro trabalho |
| `include`| Importar arquivos YAML externos |
### Variáveis ​​predefinidas
| Variável | Descrição |
|----------|------------|
| `$CI_COMMIT_SHA`| Hash de commit atual |
| `$CI_COMMIT_REF_NAME`| Nome da filial ou tag |
| `$CI_PIPELINE_ID`| ID do pipeline |
| `$CI_JOB_ID`| ID do trabalho |
| `$CI_PROJECT_DIR`| Caminho completo para o projeto |
| `$CI_REGISTRY`| URL de registro de contêiner |
| `$CI_DEFAULT_BRANCH`| Nome da filial padrão |
---

## Padrões de projeto de pipeline
### Padrões Comuns
| Padrão | Descrição |
|--------|-------------|
| **Crie uma vez, implante muitas** | Construa o artefato uma vez; implantar o mesmo artefato em cada ambiente |
| **Verificações de portão** | Aprovação manual antes da implantação em produção |
| **Sinalizadores de recursos** | Implante na produção, mas esconda-se atrás do sinalizador de recurso |
| **Implantação canário** | Implantar em uma pequena porcentagem; monitor; lançar |
| **Implantação azul-verde** | Dois ambientes idênticos; mudar o tráfego |
| **Testes paralelos** | Execute suítes de testes em paralelo para reduzir o tempo do pipeline |
| **Lint primeiro** | Execute linters antes de testes caros; falhar rapidamente |
| **Dependências de cache** | Cache node_modules, pip, Maven para acelerar compilações |
### Estágios do pipeline (típico)
| Palco | Finalidade |
|-------|---------|
| **Lint** | Estilo de código e análise estática |
| **Construir** | Compilar; pacote; criar artefatos |
| **Teste de unidade** | Testes rápidos; sem dependências externas |
| **Teste de integração** | Testes com bancos de dados; APIs; serviços externos |
| **Verificação de segurança** | Vulnerabilidades de dependência; digitalização secreta; SAST |
| **Pacote** | Criar imagem Docker; construir artefatos de liberação |
| **Implantar preparação** | Implantar no ambiente de teste |
| **Teste E2E** | Testes completos do sistema em relação ao teste |
| **Implantar produção** | Implantar em produção (manual ou automático) |
| **Teste de fumaça** | Verifique se a implantação está íntegra |
---

## Estratégias de cache
| Linguagem / Ferramenta | Caminho do cache | Exemplo |
|----------------|-----------|---------|
| **Python (pip)** | `~/.cache/pip`| `actions/cache`com chave do hash`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`com cache integrado |
| **Java (Maven)** | `~/.m2/repository`| Cache com chave do hash`pom.xml`|
| **Java (Gradle)** | `~/.gradle/caches`| Cache com chave do hash`build.gradle`|
| **Vá** | `~/go/pkg/mod`| Cache com chave do hash`go.sum`|
| **Ferrugem (Carga)** | `~/.cargo/registry`| Cache com chave do hash`Cargo.lock`|
| **Docker** | Cache da camada Docker | `docker/build-push-action`com cache de |
---

## Solução de problemas
| Problema | Solução |
|--------|----------|
| **O pipeline está lento** | Dependências de cache; paralelizar trabalhos; use imagens de base menores |
| **Segredos não disponíveis** | Verifique o nome secreto; verificar o escopo do ambiente; verifique as restrições de relações públicas do fork |
| **Artefato muito grande** | Exclua arquivos desnecessários; compressa; use retenção mais curta |
| **Matriz muito grande** | Reduza combinações; usar`include`/`exclude`|
| **Testes instáveis** | Testes escamosos de quarentena; corrigir a causa raiz; tente novamente com`retry:`|
| **Permissão negada** | Verifique os escopos do token; verifique as permissões do executor |
---

## Resumo
Os pipelines de CI/CD automatizam a construção, o teste e a implantação de software. GitHub Actions usa fluxos de trabalho YAML acionados por eventos de repositório; O GitLab CI usa estágios e jobs com regras flexíveis. Os principais padrões incluem: construir uma vez, implantar muitos; verificações de portão antes da produção; lint primeiro para feedback rápido; dependências de cache para acelerar compilações; e paralelizar testes. Os estágios do pipeline normalmente progridem de lint → build → test → security → package → deploy → smoke test. As estratégias de cache variam de acordo com o idioma, mas seguem o mesmo princípio: armazenar em cache diretórios de dependência codificados por hashes de arquivo de bloqueio. O objetivo é obter feedback rápido e confiável sobre cada alteração e implantações seguras e repetíveis na produção.