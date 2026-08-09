---
# Metadata
title: "CI/CD Pipeline Configuration"
description: "GitHub Actions, GitLab CI, Jenkins, pipeline YAML patterns"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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

# การกำหนดค่าไปป์ไลน์ CI/CD
ไปป์ไลน์การบูรณาการอย่างต่อเนื่อง (CI) และการปรับใช้อย่างต่อเนื่อง (CD) ทำให้กระบวนการสร้าง การทดสอบ และการใช้งานซอฟต์แวร์เป็นไปโดยอัตโนมัติ ข้อมูลอ้างอิงนี้ครอบคลุมรูปแบบการกำหนดค่าสำหรับแพลตฟอร์ม CI/CD ที่ได้รับความนิยมสูงสุด: GitHub Actions, GitLab CI และหลักการออกแบบไปป์ไลน์ทั่วไป
---

## การดำเนินการ GitHub
### โครงสร้างขั้นตอนการทำงาน
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

### ทริกเกอร์ทั่วไป
| ทริกเกอร์ | คำอธิบาย |
|---------|-------------|
| `on: push`| ทุกครั้งที่กด |
| `on: pull_request`| บน PR เปิด อัปเดต เปิดใหม่ |
| `on: schedule`| กำหนดการตาม Cron |
| `on: workflow_dispatch`| ทริกเกอร์แบบแมนนวล |
| `on: release`| ในการสร้างการเปิดตัว |
| `on: workflow_call`| ถูกเรียกโดยเวิร์กโฟลว์อื่น (ใช้ซ้ำได้) |
### คุณสมบัติที่สำคัญ
| คุณสมบัติ | คำอธิบาย |
|---------|-------------|
| **กลยุทธ์เมทริกซ์** | รันงานเดียวกันโดยมีการกำหนดค่าต่างกัน |
| **ความลับ** | ตัวแปรสภาพแวดล้อมที่เข้ารหัส (`${{ secrets.MY_SECRET }}`) |
| **สภาพแวดล้อม** | เป้าหมายการปรับใช้ด้วยกฎการป้องกัน |
| **แคช** | การพึ่งพาแคชระหว่างการรัน |
| **สิ่งประดิษฐ์** | อัปโหลดไฟล์จากงาน (รายงานการทดสอบ บิลด์) |
| **ขั้นตอนการทำงานที่นำมาใช้ซ้ำได้** | แบ่งปันตรรกะเวิร์กโฟลว์ระหว่างที่เก็บ |
| **การกระทำแบบผสม** | รวมหลายขั้นตอนเป็นการกระทำเดียว |
### กลยุทธ์เมทริกซ์
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
### โครงสร้างท่อ
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

### คำหลักที่สำคัญ
| คำสำคัญ | คำอธิบาย |
|---------|-------------|
| `stages`| Define pipeline stages and their order |
| `stage`| Assign a job to a stage |
| `script`| คำสั่งที่จะดำเนินการ |
| `before_script`| Commands run before main script |
| `after_script`| คำสั่งทำงานหลังจากสคริปต์หลัก (แม้จะล้มเหลว) |
| `only / except`| Control when jobs run (branches, tags) |
| `rules`| More flexible version of only/except |
| `variables`| กำหนดตัวแปร CI/CD |
| `cache`| Cache files between pipeline runs |
| `artifacts`| Files to pass between jobs |
| `environment`| สภาพแวดล้อมการปรับใช้ |
| `when`| ควบคุมการปฏิบัติงาน (on_success, on_failure, manual, เสมอ) |
| `needs`| Specify job dependencies (DAG mode) |
| `extends`| Inherit configuration from another job |
| `include`| Import external YAML files |
### ตัวแปรที่กำหนดไว้ล่วงหน้า
| ตัวแปร | คำอธิบาย |
|----------|-------------|
| `$CI_COMMIT_SHA`| แฮชคอมมิตปัจจุบัน |
| `$CI_COMMIT_REF_NAME`| ชื่อสาขาหรือแท็ก |
| `$CI_PIPELINE_ID`| รหัสไปป์ไลน์ |
| `$CI_JOB_ID`| รหัสงาน |
| `$CI_PROJECT_DIR`| เส้นทางสู่โครงการแบบเต็ม |
| `$CI_REGISTRY`| URL รีจิสทรีของคอนเทนเนอร์ |
| `$CI_DEFAULT_BRANCH`| ชื่อสาขาเริ่มต้น |
---

## รูปแบบการออกแบบท่อ
### รูปแบบทั่วไป
| รูปแบบ | คำอธิบาย |
|---------|-------------|
| **สร้างครั้งเดียวใช้งานได้หลายรายการ** | สร้างสิ่งประดิษฐ์หนึ่งครั้ง ปรับใช้สิ่งประดิษฐ์เดียวกันกับแต่ละสภาพแวดล้อม |
| **ตรวจประตู** | การอนุมัติด้วยตนเองก่อนการปรับใช้การผลิต |
| **ธงคุณลักษณะ** | ปรับใช้กับการใช้งานจริงแต่ซ่อนอยู่หลังแฟล็กคุณลักษณะ |
| **การติดตั้ง Canary** | ปรับใช้เป็นเปอร์เซ็นต์เล็กน้อย เฝ้าสังเกต; เปิดตัว |
| **การปรับใช้สีน้ำเงิน-เขียว** | สองสภาพแวดล้อมที่เหมือนกัน สลับการรับส่งข้อมูล |
| **การทดสอบแบบขนาน** | รันชุดทดสอบพร้อมกันเพื่อลดเวลาไปป์ไลน์ |
| **ผ้าสำลีก่อน** | เรียกใช้ linters ก่อนการทดสอบที่มีราคาแพง ล้มเหลวอย่างรวดเร็ว |
| **การพึ่งพาแคช** | แคช node_modules, pip, Maven เพื่อเพิ่มความเร็วในการสร้าง |
### ขั้นตอนไปป์ไลน์ (ทั่วไป)
| เวที | วัตถุประสงค์ |
|-------|---------|
| **ผ้าสำลี** | รูปแบบโค้ดและการวิเคราะห์แบบคงที่ |
| **สร้าง** | รวบรวม; กำ; สร้างสิ่งประดิษฐ์ |
| **การทดสอบหน่วย** | การทดสอบอย่างรวดเร็ว ไม่มีการพึ่งพาภายนอก |
| **การทดสอบบูรณาการ** | ทดสอบกับฐานข้อมูล API; บริการภายนอก |
| **สแกนความปลอดภัย** | ช่องโหว่ในการพึ่งพา การสแกนความลับ ศอท. |
| **แพ็คเกจ** | สร้างอิมเมจนักเทียบท่า สร้างสิ่งประดิษฐ์ที่วางจำหน่าย |
| **ปรับใช้การจัดเตรียม** | ปรับใช้กับสภาพแวดล้อมการแสดงละคร |
| **การทดสอบ E2E** | การทดสอบระบบเต็มรูปแบบเทียบกับการจัดเตรียม |
| **ปรับใช้การผลิต** | ปรับใช้กับการใช้งานจริง (ด้วยตนเองหรืออัตโนมัติ) |
| **ทดสอบควัน** | ตรวจสอบว่าการปรับใช้มีประสิทธิภาพดี |
---

## กลยุทธ์การแคช
| ภาษา / เครื่องมือ | เส้นทางแคช | ตัวอย่าง |
|----------------|-----------|---------|
| **หลาม (pip)** | `~/.cache/pip`| `actions/cache`พร้อมคีย์จากแฮช`requirements.txt`|
| **Node.js (npm)** | `~/.npm`| `actions/setup-node`พร้อมแคชในตัว |
| **ชวา (มาเวน)** | `~/.m2/repository`| แคชพร้อมคีย์จาก`pom.xml`hash |
| **ชวา (เกรเดิล)** | `~/.gradle/caches`| แคชพร้อมคีย์จาก`build.gradle`hash |
| **ไป** | `~/go/pkg/mod`| แคชพร้อมคีย์จาก`go.sum`hash |
| **สนิม (สินค้า)** | `~/.cargo/registry`| แคชพร้อมคีย์จาก`Cargo.lock`hash |
| **นักเทียบท่า** | การแคชเลเยอร์นักเทียบท่า | `docker/build-push-action`พร้อมแคชจาก |
---

## การแก้ไขปัญหา
| ปัญหา | โซลูชั่น |
|---------|----------|
| **ท่อช้า** | การพึ่งพาแคช งานคู่ขนาน; ใช้ภาพฐานที่เล็กกว่า |
| **ไม่มีความลับ** | ตรวจสอบชื่อลับ ตรวจสอบขอบเขตสภาพแวดล้อม ตรวจสอบข้อจำกัดการประชาสัมพันธ์ทางแยก |
| **สิ่งประดิษฐ์ใหญ่เกินไป** | ยกเว้นไฟล์ที่ไม่จำเป็น บีบอัด; ใช้การเก็บรักษาที่สั้นลง |
| **เมทริกซ์ใหญ่เกินไป** | ลดการรวมกัน ใช้`include`/`exclude`|
| **การทดสอบที่ไม่สม่ำเสมอ** | การทดสอบที่ไม่สม่ำเสมอ แก้ไขสาเหตุที่แท้จริง ลองอีกครั้งด้วย`retry:`|
| **การอนุญาตถูกปฏิเสธ** | ตรวจสอบขอบเขตโทเค็น ตรวจสอบสิทธิ์นักวิ่ง |
---

## สรุป
ไปป์ไลน์ CI/CD สร้าง ทดสอบ และปรับใช้ซอฟต์แวร์โดยอัตโนมัติ GitHub Actions ใช้เวิร์กโฟลว์ YAML ที่ถูกกระตุ้นโดยเหตุการณ์ของพื้นที่เก็บข้อมูล GitLab CI ใช้ขั้นตอนและงานด้วยกฎที่ยืดหยุ่น รูปแบบที่สำคัญได้แก่: สร้างครั้งเดียวปรับใช้หลายรายการ; การตรวจสอบประตูก่อนการผลิต ผ้าสำลีก่อนเพื่อการตอบรับที่รวดเร็ว การพึ่งพาแคชเพื่อเพิ่มความเร็วในการสร้าง และการทดสอบแบบขนาน โดยทั่วไปขั้นตอนไปป์ไลน์จะดำเนินไปจาก lint → build → test → security → package → ใช้งาน → ทดสอบควัน กลยุทธ์การแคชจะแตกต่างกันไปในแต่ละภาษา แต่ใช้หลักการเดียวกัน: ไดเร็กทอรีการพึ่งพาแคชที่คีย์โดยแฮชไฟล์ล็อค เป้าหมายคือการตอบรับที่รวดเร็วและเชื่อถือได้ในทุกการเปลี่ยนแปลงและการปรับใช้การผลิตที่ปลอดภัยและทำซ้ำได้