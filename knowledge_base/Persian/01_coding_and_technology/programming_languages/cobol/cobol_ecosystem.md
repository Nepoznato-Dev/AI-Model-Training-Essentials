<!--
---
# Metadata
title: "COBOL — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the COBOL ecosystem including compilers, tools, and modernization."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [cobol, ecosystem, tooling, compilers, mainframe, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "11 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# COBOL - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، کامپایلرها و زیرساخت های ضروری در اکوسیستم COBOL را پوشش می دهد.
---

## کامپایلرها و پیاده سازی ها
| کامپایلر | نوع | یادداشت ها |
|----------|------|-------|
| **GnuCOBOL (OpenCOBOL)** | منبع باز | پرکاربردترین کامپایلر رایگان |
| **IBM Enterprise COBOL** | تجاری | استاندارد مین فریم z/OS |
| **میکرو فوکوس COBOL** | تجاری | شرکت COBOL |
| **فوجیتسو COBOL** | تجاری | یونیکس COBOL |
| **ACUCOBOL-GT** | تجاری | اکنون میکرو فوکوس |
| **COBOL-IT** | تجاری | مبتنی بر GnuCOBOL |
```bash
cobc --version              # GnuCOBOL version
cobc -x -o app program.cob  # compile to executable
cobc -m -o lib.so module.cob  # compile to shared library
cobc -free program.cob      # free-format source
```

---

## ساخت سیستم
| ابزار | هدف |
|------|---------|
| **ساخت ** | سازهای کلاسیک |
| **کامپایلر GnuCOBOL** | گردآوری مستقیم |
| **Maven (افزونه cobol)** | سازمانی می سازد |
| **JCL** | کنترل کار اصلی |
| **CMake** | کراس پلتفرم (با پشتیبانی COBOL) |
```makefile
# Makefile for COBOL project
COBOL = cobc
FLAGS = -free -O2 -Wall

SRCS = $(wildcard src/*.cob)
OBJS = $(SRCS:.cob=.o)

all: myapp

myapp: $(OBJS)
	$(COBOL) -x -o $@ $^

%.o: %.cob
	$(COBOL) $(FLAGS) -c $<

clean:
	rm -f $(OBJS) myapp
```

---

## پایگاه داده و سیستم های تراکنش
| فناوری | هدف |
|------------|---------|
| **Db2** | پایگاه داده اصلی آی بی ام |
| **VSAM** | روش دسترسی به فضای ذخیره سازی مجازی |
| **CICS** | پردازش تراکنش |
| **IMS** | سیستم مدیریت اطلاعات |
| **SQL** | دسترسی به پایگاه داده استاندارد |
| **GnuCOBOL + SQLite** | پایگاه داده تعبیه شده |
```cobol
       *> SQL example in COBOL
       EXEC SQL
           SELECT NAME, SALARY
           INTO :WS-NAME, :WS-SALARY
           FROM EMPLOYEES
           WHERE EMP_ID = :WS-EMP-ID
       END-EXEC.
       
       IF SQLCODE = 0
           DISPLAY "Name: " WS-NAME
           DISPLAY "Salary: " WS-SALARY
       ELSE
           DISPLAY "Error: " SQLCODE
       END-IF.
```

---

## تست
| چارچوب | هدف |
|-----------|---------|
| **CobolUnit** | تست واحد (میکرو فوکوس) |
| **تست GnuCOBOL** | تست پایه |
| **ابزار تست z/OS** | تست IBM |
| **اسکریپت های سفارشی** | تست مبتنی بر پوسته |
```cobol
       *> Simple test in COBOL
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-ADD.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A    PIC 9(3) VALUE 5.
       01 WS-B    PIC 9(3) VALUE 3.
       01 WS-RESULT PIC 9(3).
       
       PROCEDURE DIVISION.
           COMPUTE WS-RESULT = WS-A + WS-B
           
           IF WS-RESULT = 8
               DISPLAY "PASS: 5 + 3 = 8"
           ELSE
               DISPLAY "FAIL: Expected 8, got " WS-RESULT
           END-IF
           
           STOP RUN.
```

---

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **OpenCobolCE** | تحلیل کد |
| **تحلیل کدهای IBM** | تجزیه و تحلیل z/OS |
| **SonarCOBOL** | افزونه SonarQube |
| **لیترهای سفارشی** | چک های مبتنی بر Regex |
---

## ابزار مدرنیزاسیون
| ابزار | هدف |
|------|---------|
| **میکرو فوکوس تصویری COBOL** | IDE مدرن |
| **GnuCOBOL** | نوسازی متن باز |
| **عصر آبی AWS** | بازسازی خودکار |
| **نوسازی اپلیکیشن IBM z/OS** | نوسازی مین فریم |
| **AST COBOL** | تحلیل کد |
| **OpenLegacy** | فعال سازی API |
---

## کتابخانه ها و الگوهای کلیدی
| الگو | هدف |
|---------|---------|
| **کپی کتاب** | قطعه کد قابل استفاده مجدد |
| **تماس ** | تماس های برنامه به برنامه |
| **کپی** | شامل کد خارجی |
| **EXEC SQL** | SQL تعبیه شده |
| **EXEC CICS** | دستورات تراکنش CICS |
| **مرتب سازی ** | مرتب سازی فایل |
| **STRING/UNSTRING** | دستکاری رشته |
| **بازرسی** | معاینه رشته |
| **اجرا ** | اجرای حلقه / پاراگراف |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **میکرو فوکوس تصویری COBOL** | IDE سازمانی |
| ** کد VS + COBOL** | ویرایش مدرن |
| **IBM Z Open Editor** | توسعه z/OS |
| **SPF/ISPF** | ویرایشگر اصلی |
| **GnuCOBOL + هر ویرایشگر** | منبع باز |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **z/OS** | پردازنده مرکزی آی بی ام |
| **سرور میکرو فوکوس** | COBOL توزیع شده |
| **GnuCOBOL** | لینوکس/یونیکس/ویندوز |
| **داکر** | ظروف (GnuCOBOL) |
| **CICS** | پردازش تراکنش |
| **دسته** | پردازش دسته ای |
---

## خلاصه
اکوسیستم COBOL تحت سلطه رایانه های بزرگ و سازمانی است. زنجیره ابزار استاندارد عبارتند از: **IBM Enterprise COBOL** در z/OS (مین فریم) یا **GnuCOBOL** (متن باز، کراس پلتفرم)، **Db2** و **VSAM** برای داده، **CICS** برای تراکنش ها، و ابزارهای **Micro Focus** برای مدرن سازی. COBOL تقریباً 70٪ از تراکنش‌های تجاری جهان را پردازش می‌کند - بانک‌ها، بیمه‌ها، دولت و مراقبت‌های بهداشتی هنوز به شدت به COBOL متکی هستند. اکوسیستم برای حفظ سیستم های قدیمی و مدرن سازی برنامه های اصلی ضروری است. GnuCOBOL یک مسیر آزاد و منبع باز برای توسعه و مهاجرت COBOL فراهم می کند.