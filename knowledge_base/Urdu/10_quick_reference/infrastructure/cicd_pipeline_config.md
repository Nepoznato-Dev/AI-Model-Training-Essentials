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

# CI/CD پائپ لائن کنفیگریشن
مسلسل انٹیگریشن (CI) اور مسلسل تعیناتی (CD) پائپ لائنیں سافٹ ویئر کی تعمیر، جانچ اور تعیناتی کے عمل کو خودکار کرتی ہیں۔ یہ حوالہ مقبول ترین CI/CD پلیٹ فارمز کے کنفیگریشن پیٹرن کا احاطہ کرتا ہے: GitHub ایکشنز، GitLab CI، اور پائپ لائن ڈیزائن کے عمومی اصول۔
---

## گٹ ہب ایکشنز
### ورک فلو کا ڈھانچہ
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

### عام محرکات
| ٹرگر | تفصیل |
|---------|---------------|
| `on: push`| ہر دھکے پر |
| `on: pull_request`| PR کھولنے پر، اپ ڈیٹ کریں، دوبارہ کھولیں |
| `on: schedule`| کرون پر مبنی شیڈول |
| `on: workflow_dispatch`| دستی محرک |
| `on: release`| رہائی کی تخلیق پر |
| `on: workflow_call`| ایک اور ورک فلو (دوبارہ استعمال کے قابل) کے ذریعہ بلایا گیا |
### اہم خصوصیات
| فیچر | تفصیل |
|---------|---------------|
| **میٹرکس حکمت عملی** | ایک ہی کام کو مختلف کنفیگریشنز کے ساتھ چلائیں |
| **راز** | خفیہ کردہ ماحولیاتی متغیرات (`${{ secrets.MY_SECRET }}`) |
| **ماحول** | تحفظ کے قواعد کے ساتھ تعیناتی کے اہداف |
| **کیشنگ** | رنز کے درمیان کیشے کا انحصار |
| **نادرات** | ملازمتوں سے فائلیں اپ لوڈ کریں (ٹیسٹ رپورٹس، تعمیرات) |
| **دوبارہ قابل استعمال ورک فلوز** | تمام ذخیروں میں ورک فلو منطق کا اشتراک کریں |
| **جامع اعمال** | ایک عمل میں متعدد مراحل کو یکجا کریں |
### میٹرکس کی حکمت عملی
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

## گٹ لیب سی آئی
### پائپ لائن کا ڈھانچہ
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

### کلیدی مطلوبہ الفاظ
| کلیدی لفظ | تفصیل |
|---------|---------------|
| `stages`| پائپ لائن کے مراحل اور ان کی ترتیب کی وضاحت کریں |
| `stage`| ایک مرحلے پر ایک کام تفویض کریں |
| `script`| عمل کرنے کے احکامات |
| `before_script`| کمانڈز مین اسکرپٹ سے پہلے چلتی ہیں۔
| `after_script`| کمانڈز مین اسکرپٹ کے بعد چلتی ہیں (ناکامی پر بھی) |
| `only / except`| جب نوکریاں چلتی ہیں تو کنٹرول کریں (شاخیں، ٹیگز) |
| `rules`| صرف/سوائے | کا زیادہ لچکدار ورژن
| `variables`| CI/CD متغیرات کی وضاحت کریں |
| `cache`| پائپ لائن کے درمیان کیش فائلیں |
| `artifacts`| ملازمتوں کے درمیان منتقل ہونے والی فائلیں |
| `environment`| تعیناتی ماحول |
| `when`| کام پر عمل درآمد کو کنٹرول کریں (کامیابی پر، ناکامی پر، دستی، ہمیشہ) |
| `needs`| ملازمت کے انحصار کی وضاحت کریں (DAG موڈ) |
| `extends`| کسی اور کام سے وراثت کی ترتیب |
| `include`| بیرونی YAML فائلیں درآمد کریں۔
### پہلے سے طے شدہ متغیرات
| متغیر | تفصیل |
|------------|---------------|
| `$CI_COMMIT_SHA`| موجودہ کمٹ ہیش |
| `$CI_COMMIT_REF_NAME`| برانچ یا ٹیگ کا نام |
| `$CI_PIPELINE_ID`| پائپ لائن ID |
| `$CI_JOB_ID`| ملازمت کی شناخت |
| `$CI_PROJECT_DIR`| منصوبے کا مکمل راستہ |
| `$CI_REGISTRY`| کنٹینر رجسٹری URL |
| `$CI_DEFAULT_BRANCH`| پہلے سے طے شدہ برانچ کا نام |
---

## پائپ لائن ڈیزائن پیٹرن
### مشترکہ پیٹرن
| پیٹرن | تفصیل |
|---------|---------------|
| **ایک بار بنائیں، بہت سے تعینات کریں** | ایک بار آرٹفیکٹ بنائیں؛ ہر ماحول میں ایک ہی نمونے کی تعیناتی |
| **گیٹ چیک** | پیداوار کی تعیناتی سے پہلے دستی منظوری |
| **خصوصیت کے جھنڈے** | پروڈکشن میں تعینات کریں لیکن فیچر کے جھنڈے کے پیچھے چھپائیں |
| **کینری تعیناتی** | چھوٹے فیصد پر تعینات کریں؛ مانیٹر رول آؤٹ |
| **نیلے سبز کی تعیناتی** | دو ایک جیسے ماحول؛ ٹریفک کو تبدیل کریں |
| **متوازی جانچ** | پائپ لائن کا وقت کم کرنے کے لیے متوازی طور پر ٹیسٹ سویٹس چلائیں۔
| **لنٹ پہلے** | مہنگے ٹیسٹ سے پہلے لنٹر چلائیں؛ تیزی سے ناکام |
| **کیشے پر انحصار** | تعمیرات کو تیز کرنے کے لیے کیشے نوڈ_ماڈیولز، پائپ، ماون |
### پائپ لائن کے مراحل (عام)
| اسٹیج | مقصد |
|---------|---------|
| **لنٹ** ​​| کوڈ کا انداز اور جامد تجزیہ |
| **تعمیر** | مرتب کرنا بنڈل نمونے بنائیں |
| **یونٹ ٹیسٹ** | تیز ٹیسٹ؛ کوئی بیرونی انحصار نہیں |
| **انٹیگریشن ٹیسٹ** | ڈیٹا بیس کے ساتھ ٹیسٹ؛ APIs؛ بیرونی خدمات |
| **سیکیورٹی اسکین** | انحصار کے خطرات؛ خفیہ سکیننگ؛ SAST |
| **پیکیج** | ڈوکر امیج بنائیں؛ ریلیز کے نمونے بنائیں |
| **اسٹیجنگ تعینات کریں** | سٹیجنگ ماحول میں تعینات کریں |
| **E2E ٹیسٹ** | سٹیجنگ کے خلاف مکمل سسٹم ٹیسٹ |
| **پروڈکشن تعینات کریں** | پیداوار میں تعینات کریں (دستی یا خودکار) |
| ** دھواں ٹیسٹ** | تصدیق کریں کہ تعیناتی صحت مند ہے |
---

## کیشنگ کی حکمت عملی
| زبان / ٹول | کیشے کا راستہ | مثال |
|----------------|------------|---------|
| **ازگر (پائپ)** | `~/.cache/pip`| `actions/cache``requirements.txt` ہیش سے کلید کے ساتھ |
| **Node.js (npm)** | `~/.npm`|  بلٹ ان کیشنگ کے ساتھ`actions/setup-node`|
| **جاوا (ماون)** | `~/.m2/repository`|`pom.xml`ہیش سے کلید کے ساتھ کیش |
| **جاوا (گریڈل)** | `~/.gradle/caches`|`build.gradle`ہیش سے کلید کے ساتھ کیش |
| **جاؤ** | `~/go/pkg/mod`|`go.sum`ہیش سے کلید کے ساتھ کیش |
| **زنگ (کارگو)** | `~/.cargo/registry`|`Cargo.lock`ہیش سے کلید کے ساتھ کیشے |
| **ڈوکر** | ڈوکر پرت کیشنگ | `docker/build-push-action`کیشے سے |
---

## خرابی کا سراغ لگانا
| مسئلہ | حل |
|---------|------------|
| **پائپ لائن سست ہے** | کیشے پر انحصار؛ متوازی ملازمتیں؛ چھوٹی بنیادی تصاویر کا استعمال کریں |
| **راز دستیاب نہیں** | خفیہ نام چیک کریں؛ ماحولیاتی دائرہ کار کی تصدیق کریں؛ فورک PR پابندیوں کو چیک کریں |
| **آرٹیفیکٹ بہت بڑا** | غیر ضروری فائلوں کو خارج کریں؛ کمپریس مختصر برقرار رکھنے کا استعمال کریں |
| **میٹرکس بہت بڑا** | مجموعے کو کم کریں؛`include`/`exclude`| استعمال کریں۔
| **فلکی ٹیسٹ** | قرنطینہ فلکی ٹیسٹ؛ بنیادی وجہ کو درست کریں؛`retry:`کے ساتھ دوبارہ کوشش کریں۔
| **اجازت سے انکار** | ٹوکن اسکوپس چیک کریں؛ رنر کی اجازتوں کی تصدیق کریں |
---

## خلاصہ
CI/CD پائپ لائنیں خود کار طریقے سے تعمیر، جانچ، اور سافٹ ویئر کی تعیناتی کرتی ہیں۔ GitHub ایکشنز ریپوزٹری ایونٹس سے شروع ہونے والے YAML ورک فلوز کا استعمال کرتا ہے۔ GitLab CI لچکدار قواعد کے ساتھ مراحل اور ملازمتوں کا استعمال کرتا ہے۔ کلیدی نمونوں میں شامل ہیں: ایک بار بہت سے تعینات کریں؛ پیداوار سے پہلے گیٹ کی جانچ پڑتال؛ تیز رائے کے لئے پہلے لنٹ تعمیرات کو تیز کرنے کے لیے کیشے پر انحصار؛ اور متوازی ٹیسٹ۔ پائپ لائن کے مراحل عام طور پر لنٹ → بلڈ → ٹیسٹ → سیکیورٹی → پیکج → تعیناتی → دھواں ٹیسٹ سے آگے بڑھتے ہیں۔ کیشنگ کی حکمت عملی زبان کے لحاظ سے مختلف ہوتی ہیں لیکن ایک ہی اصول پر عمل کریں: کیش ڈیپینڈنسی ڈائریکٹریز کو لاک فائل ہیشز کے ذریعے کلید کیا جاتا ہے۔ مقصد ہر تبدیلی پر تیز، قابل اعتماد فیڈ بیک اور پروڈکشن میں محفوظ، دوبارہ قابل تعیناتی ہے۔