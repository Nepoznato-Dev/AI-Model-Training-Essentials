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

# Usanidi wa Bomba la CI/CD
Ujumuishaji Unaoendelea (CI) na Usambazaji Unaoendelea (CD) hurekebisha mchakato wa kujenga, kupima na kupeleka programu kiotomatiki. Rejeleo hili linajumuisha mifumo ya usanidi ya majukwaa maarufu zaidi ya CI/CD: Vitendo vya GitHub, GitLab CI, na kanuni za jumla za muundo wa bomba.
---

## Vitendo vya GitHub
### Muundo wa Mtiririko wa Kazi
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

### Vichochezi vya Kawaida
| Anzisha | Maelezo |
|---------|-------------|
| `on: push`| Kwa kila kushinikiza |
| `on: pull_request`| Kwenye PR fungua, sasisha, fungua upya |
| `on: schedule`| Ratiba inayotokana na Cron |
| `on: workflow_dispatch`| Kianzishaji cha mkono |
| `on: release`| Kwenye uundaji wa toleo |
| `on: workflow_call`| Imeitwa na mtiririko mwingine wa kazi (unaoweza kutumika tena) |
### Sifa Muhimu
| Kipengele | Maelezo |
|---------|-------------|
| **Mkakati wa Matrix** | Endesha kazi sawa na usanidi tofauti |
| **Siri** | Vigeu vya mazingira vilivyosimbwa kwa njia fiche (`${{ secrets.MY_SECRET }}`) |
| **Mazingira** | Malengo ya upelekaji na sheria za ulinzi |
| **Kuhifadhi** | Utegemezi wa akiba kati ya kukimbia |
| **Vitu vya Kubakia** | Pakia faili kutoka kwa kazi (ripoti za majaribio, miundo) |
| **Mitiririko ya kazi inayoweza kutumika tena** | Shiriki mantiki ya mtiririko wa kazi kwenye hazina |
| **Vitendo vya mchanganyiko** | Kuchanganya hatua nyingi katika hatua moja |
### Mbinu ya Matrix
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
### Muundo wa Bomba
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

### Maneno Muhimu
| Neno muhimu | Maelezo |
|---------|-------------|
| `stages`| Bainisha hatua za bomba na mpangilio wao |
| `stage`| Panga kazi kwa jukwaa |
| `script`| Amri za kutekeleza |
| `before_script`| Amri huendeshwa kabla ya hati kuu |
| `after_script`| Amri huendeshwa baada ya hati kuu (hata ikishindwa) |
| `only / except`| Dhibiti kazi zinapoendeshwa (matawi, vitambulisho) |
| `rules`| Toleo linalonyumbulika zaidi la pekee/isipokuwa |
| `variables`| Bainisha vigeu vya CI/CD |
| `cache`| Faili za akiba kati ya bomba huendesha |
| `artifacts`| Faili za kupitisha kati ya kazi |
| `environment`| Mazingira ya kupeleka |
| `when`| Dhibiti utekelezaji wa kazi (on_success, on_falure, manual, always) |
| `needs`| Bainisha tegemezi za kazi (Njia ya DAG) |
| `extends`| Kurithi usanidi kutoka kwa kazi nyingine |
| `include`| Leta faili za YAML za nje |
### Vigeu Vilivyoainishwa Awali
| Tofauti | Maelezo |
|----------|-------------|
| `$CI_COMMIT_SHA`| Heshi ya ahadi ya sasa |
| `$CI_COMMIT_REF_NAME`| Tawi au jina la lebo |
| `$CI_PIPELINE_ID`| Kitambulisho cha bomba |
| `$CI_JOB_ID`| Kitambulisho cha kazi |
| `$CI_PROJECT_DIR`| Njia kamili ya mradi |
| `$CI_REGISTRY`| URL ya kusajili kontena |
| `$CI_DEFAULT_BRANCH`| Jina chaguo-msingi la tawi |
---

## Miundo ya Usanifu wa Bomba
### Miundo ya Kawaida
| Muundo | Maelezo |
|---------|-------------|
| **Jenga mara moja, peleka nyingi** | Jenga mabaki mara moja; peleka vizalia vya programu sawa kwa kila mazingira |
| **Ukaguzi wa lango** | Idhini ya mwongozo kabla ya kusambaza uzalishaji |
| **Bendera za kipengele** | Sambaza hadi toleo la umma lakini ufiche nyuma ya kipengele cha bendera |
| **Usambazaji wa Canary** | Tumia kwa asilimia ndogo; kufuatilia; sambaza |
| **Bluu-kijani kupelekwa** | Mazingira mawili yanayofanana; badilisha trafiki |
| **Jaribio sambamba** | Endesha vyumba vya majaribio sambamba ili kupunguza muda wa bomba |
| **Weka kwanza** | Run linters kabla ya vipimo vya gharama kubwa; kushindwa haraka |
| **Vitegemezi vya akiba** | Cache nodi_modules, pip, Maven kuharakisha hujenga |
### Hatua za Bomba (Kawaida)
| Jukwaa | Kusudi |
|-------|----------|
| **Kitambaa** | Mtindo wa kanuni na uchanganuzi tuli |
| **Jenga** | Kukusanya; kifungu; unda vizalia |
| **Jaribio la kitengo** | Vipimo vya haraka; hakuna tegemezi za nje |
| **Jaribio la ujumuishaji** | Uchunguzi na hifadhidata; API; huduma za nje |
| **Uchanganuzi wa usalama** | Udhaifu wa utegemezi; skanning ya siri; SAST |
| **Kifurushi** | Unda picha ya Docker; tengeneza mabaki ya kutolewa |
| **Weka jukwaa** | Sambaza kwa mazingira ya jukwaa |
| **Mtihani wa E2E** | Majaribio kamili ya mfumo dhidi ya hatua |
| **Weka utayarishaji** | Sambaza kwa uzalishaji (mwongozo au otomatiki) |
| **Mtihani wa moshi** | Thibitisha upelekaji ni mzuri |
---

## Mikakati ya Uhifadhi
| Lugha/Zana | Njia ya Akiba | Mfano |
|---------------------------------------|
| **Chatu (bomba)** | `~/.cache/pip`| `actions/cache`yenye ufunguo kutoka`requirements.txt`heshi |
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`iliyo na kache iliyojengewa ndani |
| **Java (Maven)** | `~/.m2/repository`| Akiba yenye ufunguo kutoka`pom.xml`heshi |
| **Java (Gradle)** | `~/.gradle/caches`| Akiba yenye ufunguo kutoka`build.gradle`heshi |
| **Nenda** | `~/go/pkg/mod`| Akiba yenye ufunguo kutoka`go.sum`heshi |
| **Kutu (Mzigo)** | `~/.cargo/registry`| Akiba yenye ufunguo kutoka`Cargo.lock`heshi |
| **Docker** | Uhifadhi wa safu ya kizimbani | `docker/build-push-action`pamoja na akiba-kutoka |
---

## Utatuzi wa matatizo
| Tatizo | Suluhisho |
|---------|----------|
| **Bomba ni polepole** | utegemezi wa kache; kazi sambamba; tumia picha ndogo za msingi |
| **Siri hazipatikani** | Angalia jina la siri; thibitisha upeo wa mazingira; angalia vikwazo vya PR vya uma |
| **Vizalia vya programu ni kubwa mno** | Ondoa faili zisizo za lazima; compress; tumia uhifadhi mfupi |
| **Matrix ni kubwa mno** | Kupunguza mchanganyiko; tumia`include`/`exclude`|
| **Vipimo hafifu** | karantini vipimo flaky; kurekebisha sababu ya mizizi; jaribu tena ukitumia`retry:`|
| **Ruhusa imekataliwa** | Angalia upeo wa ishara; thibitisha ruhusa za wakimbiaji |
---

## Muhtasari
Mabomba ya CI/CD yanabadilisha ujenzi, majaribio na kupeleka programu kiotomatiki. Vitendo vya GitHub hutumia mtiririko wa kazi wa YAML unaosababishwa na matukio ya hazina; GitLab CI hutumia hatua na kazi zilizo na sheria rahisi. Mifumo muhimu ni pamoja na: jenga mara moja peleka nyingi; ukaguzi wa lango kabla ya uzalishaji; lint kwanza kwa maoni ya haraka; utegemezi wa cache ili kuharakisha hujenga; na kusawazisha vipimo. Hatua za bomba kwa kawaida huendelea kutoka lint → kujenga → mtihani → usalama → kifurushi → peleka → mtihani wa moshi. Mikakati ya kuweka akiba hutofautiana kulingana na lugha lakini hufuata kanuni sawa: saraka za utegemezi wa kache zilizowekwa na heshi za kufuli. Lengo ni maoni ya haraka, ya kuaminika kwa kila mabadiliko na uwekaji salama, unaorudiwa kwa uzalishaji.