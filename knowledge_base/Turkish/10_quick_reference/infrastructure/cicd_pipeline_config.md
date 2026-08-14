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
# CI/CD İşlem Hattı Yapılandırması
Sürekli Entegrasyon (CI) ve Sürekli Dağıtım (CD) işlem hatları, yazılım oluşturma, test etme ve dağıtma sürecini otomatikleştirir. Bu referans, en popüler CI/CD platformlarına yönelik yapılandırma modellerini kapsar: GitHub Eylemleri, GitLab CI ve genel işlem hattı tasarım ilkeleri.
---

## GitHub Eylemleri
### İş Akışı Yapısı
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

### Yaygın Tetikleyiciler
| Tetikleyici | Açıklama |
|-----------|------------|
| `on: push`| Her basışta |
| `on: pull_request`| PR'da açın, güncelleyin, yeniden açın |
| `on: schedule`| Cron tabanlı program |
| `on: workflow_dispatch`| Manuel tetik |
| `on: release`| Sürüm oluşturmada |
| `on: workflow_call`| Başka bir iş akışı tarafından çağrıldı (yeniden kullanılabilir) |
### Temel Özellikler
| Özellik | Açıklama |
|-----------|------------|
| **Matris stratejisi** | Aynı işi farklı konfigürasyonlarla çalıştırın |
| **Sırlar** | Şifrelenmiş ortam değişkenleri (`${{ secrets.MY_SECRET }}`) |
| **Ortamlar** | Koruma kurallarına sahip dağıtım hedefleri |
| **Önbelleğe alma** | Çalıştırmalar arasındaki önbellek bağımlılıkları |
| **Yapılar** | İşlerden dosya yükleyin (test raporları, derlemeler) |
| **Yeniden kullanılabilir iş akışları** | İş akışı mantığını veri havuzları arasında paylaşın |
| **Bileşik eylemler** | Birden çok adımı tek bir eylemde birleştirin |
### Matris Stratejisi
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
### Boru Hattı Yapısı
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

### Anahtar Anahtar Kelimeler
| Anahtar kelime | Açıklama |
|-----------|------------|
| `stages`| Boru hattı aşamalarını ve sıralarını tanımlayın |
| `stage`| Bir aşamaya iş atama |
| `script`| Yürütülecek komutlar |
| `before_script`| Komutlar ana komut dosyasından önce çalıştırılır |
| `after_script`| Komutlar ana komut dosyasından sonra çalıştırılır (başarısızlık durumunda bile) |
| `only / except`| İşlerin ne zaman çalıştırılacağını kontrol edin (dallar, etiketler) |
| `rules`| only/hariç'in daha esnek versiyonu |
| `variables`| CI/CD değişkenlerini tanımlayın |
| `cache`| İşlem hattı çalıştırmaları arasındaki dosyaları önbelleğe alın |
| `artifacts`| İşler arasında aktarılacak dosyalar |
| `environment`| Dağıtım ortamı |
| `when`| İşin yürütülmesini kontrol edin (başarılı olduğunda, başarısız olduğunda, manuel, her zaman) |
| `needs`| İş bağımlılıklarını belirtin (DAG modu) |
| `extends`| Yapılandırmayı başka bir işten devral |
| `include`| Harici YAML dosyalarını içe aktar |
### Önceden Tanımlanmış Değişkenler
| Değişken | Açıklama |
|----------|----------------|
| `$CI_COMMIT_SHA`| Mevcut taahhüt karması |
| `$CI_COMMIT_REF_NAME`| Şube veya etiket adı |
| `$CI_PIPELINE_ID`| Boru Hattı Kimliği |
| `$CI_JOB_ID`| İş Kimliği |
| `$CI_PROJECT_DIR`| Projenin tam yolu |
| `$CI_REGISTRY`| Kapsayıcı kayıt URL'si |
| `$CI_DEFAULT_BRANCH`| Varsayılan şube adı |
---

## Boru Hattı Tasarım Modelleri
### Ortak Desenler
| Desen | Açıklama |
|-----------|------------|
| **Bir kez oluşturun, birçok kez dağıtın** | Eseri bir kez inşa edin; aynı yapıyı her ortama dağıtın |
| **Kapı kontrolleri** | Üretim dağıtımından önce manuel onay |
| **Özellik işaretleri** | Üretime dağıtın ancak özellik bayrağının arkasına saklanın |
| **Canary dağıtımı** | Küçük bir yüzdeye dağıtın; monitör; piyasaya sür |
| **Mavi-yeşil dağıtım** | İki özdeş ortam; trafiği değiştir |
| **Paralel test** | İşlem hattı süresini azaltmak için test paketlerini paralel olarak çalıştırın |
| **Önce tüysüz** | Pahalı testlerden önce linterleri çalıştırın; hızlı başarısız ol |
| **Önbellek bağımlılıkları** | Yapıları hızlandırmak için önbellek node_modules, pip, Maven |
### Boru Hattı Aşamaları (Tipik)
| Sahne | Amaç |
|----------|-----------|
| **Tiftik** | Kod stili ve statik analiz |
| **İnşa** | Derleyin; paket; eserler yaratın |
| **Birim testi** | Hızlı testler; dış bağımlılık yok |
| **Entegrasyon testi** | Veritabanlarıyla yapılan testler; API'ler; harici hizmetler |
| **Güvenlik taraması** | Bağımlılık güvenlik açıkları; gizli tarama; SAST |
| **Paket** | Docker görüntüsü oluşturun; derleme sürümü eserleri |
| **Hazırlamayı dağıtın** | Hazırlama ortamına dağıtma |
| **E2E testi** | Aşamalamaya karşı tam sistem testleri |
| **Üretimi dağıtın** | Üretime dağıtma (manuel veya otomatik) |
| **Duman testi** | Dağıtımın sağlıklı olduğunu doğrulayın |
---

## Önbelleğe Alma Stratejileri
| Dil / Araç | Önbellek Yolu | Örnek |
|----------------|-----------|-----------|
| **Python (pip)** | `~/.cache/pip`|  `actions/cache`,`requirements.txt`karmasından anahtarla |
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`yerleşik önbelleğe alma özelliğine sahip |
| **Java (Maven)** | `~/.m2/repository`|`pom.xml`karmasından anahtar içeren önbellek |
| **Java (Gradle)** | `~/.gradle/caches`|`build.gradle`karmasından anahtar içeren önbellek |
| **Git** | `~/go/pkg/mod`|`go.sum`karmasından anahtar içeren önbellek |
| **Pas (Kargo)** | `~/.cargo/registry`|`Cargo.lock`karmasından anahtar içeren önbellek |
| **Docker** | Docker katmanı önbelleğe alma | `docker/build-push-action`önbellekten |
---

## Sorun Giderme
| Sorun | Çözüm |
|-----------|----------|
| **Ardışık düzen yavaş** | Önbellek bağımlılıkları; işleri paralelleştirin; daha küçük temel görseller kullanın |
| **Gizli bilgiler mevcut değil** | Gizli adı kontrol edin; ortam kapsamını doğrulayın; çatal PR kısıtlamalarını kontrol edin |
| **Yapı çok büyük** | Gereksiz dosyaları hariç tutun; kompres; daha kısa saklama kullanın |
| **Matris çok büyük** | Kombinasyonları azaltın;`include`/`exclude`kullanın |
| **Kesintili testler** | Karantina lapa lapa testleri; temel nedeni düzeltin;`retry:`ile yeniden deneyin |
| **İzin reddedildi** | Belirteç kapsamlarını kontrol edin; koşucu izinlerini doğrulayın |
---

## Özet
CI/CD işlem hatları, yazılım oluşturmayı, test etmeyi ve dağıtmayı otomatikleştirir. GitHub Actions, depo olayları tarafından tetiklenen YAML iş akışlarını kullanır; GitLab CI, esnek kurallara sahip aşamaları ve işleri kullanır. Temel kalıplar şunları içerir: bir kez oluşturun, birçok kez dağıtın; üretim öncesi kapı kontrolleri; hızlı geri bildirim için önce tiftik; derlemeleri hızlandırmak için önbellek bağımlılıkları; ve testleri paralelleştirin. Boru hattı aşamaları genellikle tüy bırakma → oluştur → test → güvenlik → paket → dağıtma → duman testinden ilerler. Önbelleğe alma stratejileri dile göre değişir ancak aynı prensibi izler: kilit dosyası karmalarıyla anahtarlanan önbellek bağımlılık dizinleri. Hedef, her değişiklikte hızlı, güvenilir geri bildirim ve üretimde güvenli, tekrarlanabilir dağıtımlardır.