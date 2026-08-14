---
# Metadata
title: "COBOL — Version History & Evolution"
description: "Comprehensive version history and evolution of COBOL from 1959 to modern COBOL."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cobol, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# COBOL — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| فلوماتيك | 1955 | مقدمة لغة الأعمال الخاصة بجريس هوبر |
| كوبول-60 | 1959 | **الكوبول الأول** (لجنة الكوداسيل) |
| كوبول-61 | 1961 | كاتب التقارير، تحسينات`PERFORM`|
| كوبول-68 | 1968 | معيار ANSI الأول (X3.1-1968) |
| كوبول-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(التبديل) التعميمات |
| كوبول-85 | 1985 | **البرمجة المنظمة**: `END-IF`، `END-PERFORM`، أجهزة إنهاء النطاق |
| كوبول 2002 | 2002 | **OOP**: الفئات، الأساليب، الميراث،`FUNCTION`|
| كوبول 2014 | 2014 | **XML**،`JSON`(جزئي)، النوع`BOOLEAN`|
| كوبول 2023 | 2023 | **مجموعات JSON الأصلية** وUTF-8 و`LIST` |
## المعالم الرئيسية
### ميلاد كوبول (1959)
- **1959**: أنشأ CODASYL (مؤتمر لغات أنظمة البيانات) لغة COBOL
- **تأثير غريس هوبر**: "لغة الأعمال يجب أن تبدو مثل اللغة الإنجليزية"
- **الهدف**: لغة أعمال محمولة — تعمل على أي جهاز كمبيوتر
- COBOL-60: الإصدار الأول — معالجة الملفات والتقارير والحساب
### كوبول 68-74: التقييس (1968-1974)
- **كوبول-68**: معيار ANSI الأول
- **COBOL-74**:`EVALUATE`(بيان التبديل)، منظم`IF`/`ELSE`
- أصبحت لغة COBOL لغة الأعمال المهيمنة في جميع أنحاء العالم
### كوبول 85: كوبول منظم (1985)
- **حدود النطاق**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(التبديل)
-`PERFORM`/`END-PERFORM`(الحلقات المضمنة)
- تحسينات `SECTION`
- هذا هو الإصدار الذي تمت كتابة معظم أكواد COBOL فيه
### كوبول 2002: كوبول كائني التوجه (2002)
- **الفئات والأساليب** —`CLASS-ID`,`METHOD-ID`
- **الميراث** —`INHERITS`
- **الواجهات** —`IMPLEMENTS`
- الكلمة الرئيسية `FUNCTION`
- نوع`BOOLEAN`(جزئي)
- البرامج المتداخلة
### كوبول 2014-2023: كوبول الحديثة (2014 إلى الوقت الحاضر)
- **2014**: دعم XML، نوع JSON الجزئي، `BOOLEAN`
- **2023**: **JSON الأصلي** (PARSE JSON، GENERATE JSON)، UTF-8، مجموعات `LIST`
- تواصل كوبول التطور للعصر الحديث
## تطور بناء الجملة
```cobol
      * COBOL-68: Basic file processing
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 EMPLOYEE-RECORD.
          05 EMP-NAME      PIC X(30).
          05 EMP-SALARY    PIC 9(7)V99.
       PROCEDURE DIVISION.
           OPEN INPUT EMPLOYEE-FILE.
           READ EMPLOYEE-FILE
               AT END MOVE 'YES' TO END-OF-FILE.
           CLOSE EMPLOYEE-FILE.
           STOP RUN.

      * COBOL-85: Structured programming
       IF SALARY > 50000
           DISPLAY 'High earner: ' EMP-NAME
           ADD 1 TO HIGH-EARNER-COUNT
       ELSE
           DISPLAY 'Standard: ' EMP-NAME
       END-IF

       PERFORM VARYING I FROM 1 BY 1 UNTIL I > 100
           COMPUTE TOTAL = TOTAL + AMOUNT(I)
       END-PERFORM

       EVALUATE DEPT-CODE
           WHEN 'ENG'
               MOVE 'Engineering' TO DEPT-NAME
           WHEN 'MKT'
               MOVE 'Marketing' TO DEPT-NAME
           WHEN OTHER
               MOVE 'Unknown' TO DEPT-NAME
       END-EVALUATE

      * COBOL 2002: Object-oriented
       CLASS-ID. BankAccount.
       WORKING-STORAGE SECTION.
       01 BALANCE PIC 9(10)V99.

       METHOD-ID. DEPOSIT.
       PROCEDURE DIVISION USING AMOUNT AS PIC 9(10)V99.
           ADD AMOUNT TO BALANCE
       END METHOD.

       METHOD-ID. GET-BALANCE.
       PROCEDURE DIVISION RETURNING BALANCE.
       END METHOD.

      * COBOL 2023: JSON support
       IDENTIFICATION DIVISION.
       PROGRAM-ID. JSON-EXAMPLE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 JSON-STRING PIC X(1000).
       01 PARSED-DATA.
          05 NAME PIC X(50).
          05 AGE  PIC 99.
       PROCEDURE DIVISION.
           MOVE '{"name":"Alice","age":30}' TO JSON-STRING
           PARSE JSON-STRING INTO PARSED-DATA
           DISPLAY "Name: " NAME " Age: " AGE
```

## تطور الميزة
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## مبادئ التصميم الرئيسية
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## قصة Y2K
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## نمو النظام البيئي
```
1959: COBOL created by CODASYL committee
1968: First ANSI standard
1970s: COBOL dominates business computing worldwide
1985: COBOL-85 — structured programming
2000: Y2K — COBOL's finest hour
2002: COBOL 2002 — OOP
2014: COBOL 2014 — XML
2023: COBOL 2023 — native JSON
2025: COBOL still processes:
       - 95% of ATM transactions
       - 80% of in-person financial transactions
       - Government systems (tax, social security)
       Estimated 200+ billion lines of COBOL still running
       IBM Z mainframes run COBOL at massive scale
```
