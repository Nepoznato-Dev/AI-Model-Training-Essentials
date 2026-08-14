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

# پیکربندی خط لوله CI/CD
خطوط لوله یکپارچه سازی مداوم (CI) و استقرار مستمر (CD) فرآیند ساخت، آزمایش و استقرار نرم افزار را خودکار می کنند. این مرجع الگوهای پیکربندی محبوب‌ترین پلتفرم‌های CI/CD را پوشش می‌دهد: GitHub Actions، GitLab CI، و اصول کلی طراحی خط لوله.
---

## اقدامات GitHub
### ساختار گردش کار
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

### محرک های رایج
| ماشه | توضیحات |
|---------|-------------|
| `on: push`| در هر فشار |
| `on: pull_request`| در روابط عمومی باز، به روز رسانی، بازگشایی |
| `on: schedule`| جدول زمانی مبتنی بر کرون |
| `on: workflow_dispatch`| ماشه دستی |
| `on: release`| هنگام انتشار |
| `on: workflow_call`| فراخوانی شده توسط گردش کار دیگری (قابل استفاده مجدد) |
### ویژگی های کلیدی
| ویژگی | توضیحات |
|---------|-------------|
| **استراتژی ماتریسی** | همان کار را با تنظیمات مختلف اجرا کنید |
| **رازها** | متغیرهای محیط رمزگذاری شده (`${{ secrets.MY_SECRET }}`) |
| **محیط ها** | اهداف استقرار با قوانین حفاظتی |
| **در حافظه پنهان** | وابستگی های کش بین اجراها |
| **مصنوعات** | آپلود فایل ها از مشاغل (گزارش های تست، ساخت) |
| **جریان کاری قابل استفاده مجدد** | به اشتراک گذاری منطق گردش کار در مخازن |
| **اقدامات مرکب** | ترکیب چند مرحله در یک عمل |
### استراتژی ماتریسی
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
### ساختار خط لوله
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

### کلمات کلیدی
| کلمه کلیدی | توضیحات |
|---------|-------------|
| `stages`| تعریف مراحل خط لوله و ترتیب آنها |
| `stage`| واگذاری کار به مرحله |
| `script`| دستورات برای اجرا |
| `before_script`| دستورات قبل از اسکریپت اصلی اجرا می شوند |
| `after_script`| دستورات بعد از اسکریپت اصلی اجرا می شوند (حتی در صورت شکست) |
| `only / except`| کنترل زمان اجرای مشاغل (شاخه ها، برچسب ها) |
| `rules`| نسخه انعطاف پذیرتر فقط/به جز |
| `variables`| تعریف متغیرهای CI/CD |
| `cache`| فایل های کش بین اجرای خط لوله |
| `artifacts`| فایل هایی برای ارسال بین کارها |
| `environment`| محیط استقرار |
| `when`| کنترل اجرای کار (روی_موفقیت، روی_شکست، دستی، همیشه) |
| `needs`| تعیین وابستگی های شغلی (حالت DAG) |
| `extends`| به ارث بردن پیکربندی از یک کار دیگر |
| `include`| وارد کردن فایل های YAML خارجی |
### متغیرهای از پیش تعریف شده
| متغیر | توضیحات |
|----------|-------------|
| `$CI_COMMIT_SHA`| هش commit فعلی |
| `$CI_COMMIT_REF_NAME`| نام شعبه یا برچسب |
| `$CI_PIPELINE_ID`| شناسه خط لوله |
| `$CI_JOB_ID`| شناسه شغلی |
| `$CI_PROJECT_DIR`| مسیر کامل پروژه |
| `$CI_REGISTRY`| آدرس رجیستری کانتینر |
| `$CI_DEFAULT_BRANCH`| نام شعبه پیش فرض |
---

## الگوهای طراحی خط لوله
### الگوهای رایج
| الگو | توضیحات |
|---------|-------------|
| **یک بار بسازید، بسیاری را مستقر کنید** | یک بار مصنوع بسازید. استقرار آرتیفکت مشابه در هر محیط |
| **چک دروازه** | تایید دستی قبل از استقرار تولید |
| **پرچم های ویژگی** | مستقر در تولید اما پشت پرچم ویژگی پنهان شوید |
| **استقرار قناری** | استقرار به درصد کمی؛ نظارت؛ رول کردن |
| **استقرار سبز-آبی** | دو محیط یکسان؛ سوئیچ ترافیک |
| **تست موازی** | اجرای مجموعه های آزمایشی به صورت موازی برای کاهش زمان خط لوله |
| **اول لینت** | قبل از آزمایش های گران قیمت، لینترها را اجرا کنید. شکست سریع |
| **وابستگی های کش** | Cache node_modules، pip، Maven برای افزایش سرعت ساخت |
### مراحل خط لوله (معمولی)
| مرحله | هدف |
|-------|---------|
| **لینت** | سبک کد و تحلیل استاتیک |
| **ساخت ** | کامپایل؛ بسته نرم افزاری ایجاد مصنوعات |
| **آزمون واحد** | تست های سریع؛ بدون وابستگی خارجی |
| **آزمون ادغام** | تست با پایگاه داده؛ API ها خدمات خارجی |
| **اسکن امنیتی** | آسیب پذیری های وابستگی؛ اسکن مخفی؛ SAST |
| **بسته** | ایجاد تصویر داکر؛ آرتیفکت های انتشار ساخت |
| **استقرار صحنه سازی** | استقرار در محیط صحنه |
| **تست E2E** | تست های کامل سیستم در برابر مرحله بندی |
| **استقرار تولید** | استقرار به تولید (دستی یا اتوماتیک) |
| **تست دود** | بررسی سالم بودن استقرار |
---

## استراتژی های ذخیره سازی
| زبان / ابزار | مسیر کش | مثال |
|----------------|-----------|---------|
| **پایتون (پیپ)** | `~/.cache/pip`| `actions/cache`با کلید از هش`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`با کش داخلی |
| **جاوا (Maven)** | `~/.m2/repository`| حافظه پنهان با کلید از هش`pom.xml`|
| **جاوا (گرادل)** | `~/.gradle/caches`| حافظه پنهان با کلید از هش`build.gradle`|
| **برو** | `~/go/pkg/mod`| حافظه پنهان با کلید از هش`go.sum`|
| **زنگ (محموله)** | `~/.cargo/registry`| حافظه پنهان با کلید از هش`Cargo.lock`|
| **داکر** | ذخیره سازی لایه داکر | `docker/build-push-action`با کش-از |
---

## عیب یابی
| مشکل | راه حل |
|---------|----------|
| **خط لوله کند است** | وابستگی های کش؛ مشاغل موازی؛ استفاده از تصاویر پایه کوچکتر |
| **اسرار در دسترس نیست** | نام مخفی را بررسی کنید. بررسی محدوده محیطی؛ بررسی محدودیت های روابط عمومی چنگال |
| **مصنوع خیلی بزرگ** | حذف فایل های غیر ضروری؛ فشرده سازی؛ استفاده از نگهداری کوتاهتر |
| **ماتریس خیلی بزرگ** | کاهش ترکیبات؛ استفاده از`include`/`exclude`|
| **تست های پوسته پوسته** | تست های پوسته پوسته قرنطینه؛ رفع علت اصلی؛ با`retry:`دوباره امتحان کنید |
| **اجازه رد شد** | محدوده نشانه را بررسی کنید. تایید مجوزهای دونده |
---

## خلاصه
خطوط لوله CI/CD ساخت، آزمایش و استقرار نرم افزار را خودکار می کند. GitHub Actions از گردش‌های کاری YAML استفاده می‌کند که توسط رویدادهای مخزن ایجاد می‌شوند. GitLab CI از مراحل و کارهایی با قوانین انعطاف پذیر استفاده می کند. الگوهای کلیدی عبارتند از: ساخت یک بار استقرار بسیاری. بررسی دروازه قبل از تولید؛ پرز اول برای بازخورد سریع. وابستگی های کش برای افزایش سرعت ساخت. و تست های موازی مراحل خط لوله معمولاً از پرز → ساخت → تست → امنیت → بسته → استقرار → تست دود پیشرفت می کنند. استراتژی‌های کش بسته به زبان متفاوت هستند، اما از یک اصل پیروی می‌کنند: دایرکتوری‌های وابستگی کش که توسط هش‌های فایل قفل کلید می‌شوند. هدف، بازخورد سریع و قابل اعتماد در مورد هر تغییر و استقرار ایمن و قابل تکرار در تولید است.