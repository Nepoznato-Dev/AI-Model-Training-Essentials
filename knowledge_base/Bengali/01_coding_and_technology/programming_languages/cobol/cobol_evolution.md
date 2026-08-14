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
# COBOL — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| ফ্লো-ম্যাটিক | 1955 | গ্রেস হপারের ব্যবসায়িক ভাষার অগ্রদূত |
| COBOL-60 | 1959 | **প্রথম COBOL** (CODASYL কমিটি) |
| COBOL-61 | 1961 | রিপোর্ট লেখক,`PERFORM`উন্নতি |
| COBOL-68 | 1968 | প্রথম ANSI মান (X3.1-1968) |
| COBOL-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(সুইচ), সাধারণীকরণ |
| COBOL-85 | 1985 | **স্ট্রাকচার্ড প্রোগ্রামিং**:`END-IF`,`END-PERFORM`, স্কোপ টার্মিনেটর |
| COBOL 2002 | 2002 | **OOP**: ক্লাস, পদ্ধতি, উত্তরাধিকার,`FUNCTION`|
| COBOL 2014 | 2014 | **XML**,`JSON`(আংশিক),`BOOLEAN`প্রকার |
| COBOL 2023 | 2023 | **নেটিভ JSON**, UTF-8,`LIST`সংগ্রহ |
## প্রধান মাইলফলক
### কোবলের জন্ম (1959)
- **1959**: CODASYL (ডেটা সিস্টেম ল্যাঙ্গুয়েজে কনফারেন্স) COBOL তৈরি করে
- **গ্রেস হপারের প্রভাব**: "ব্যবসায়ের ভাষা ইংরেজির মতো হওয়া উচিত"
- **লক্ষ্য**: পোর্টেবল ব্যবসায়িক ভাষা — যেকোনো কম্পিউটারে চলে
- COBOL-60: প্রথম সংস্করণ — ফাইল হ্যান্ডলিং, রিপোর্ট, পাটিগণিত
### COBOL 68-74: স্ট্যান্ডার্ডাইজেশন (1968-1974)
- **COBOL-68**: প্রথম ANSI মান
- **COBOL-74**:`EVALUATE`(সুইচ স্টেটমেন্ট), কাঠামোবদ্ধ`IF`/`ELSE`
- COBOL বিশ্বব্যাপী প্রভাবশালী ব্যবসায়িক ভাষা হয়ে উঠেছে
### COBOL 85: স্ট্রাকচার্ড COBOL (1985)
- **স্কোপ টার্মিনেটর**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(সুইচ)
-`PERFORM`/`END-PERFORM`(ইনলাইন লুপ)
-`SECTION`উন্নতি
- এটি এমন সংস্করণ যা সর্বাধিক COBOL কোড লেখা আছে
### COBOL 2002: অবজেক্ট-ওরিয়েন্টেড COBOL (2002)
- **ক্লাস এবং পদ্ধতি** —`CLASS-ID`,`METHOD-ID`
- **উত্তরাধিকার** —`INHERITS`
- **ইন্টারফেস** —`IMPLEMENTS`
-`FUNCTION`কীওয়ার্ড
-`BOOLEAN`প্রকার (আংশিক)
- নেস্টেড প্রোগ্রাম
### COBOL 2014-2023: আধুনিক COBOL (2014-বর্তমান)
- **2014**: XML সমর্থন, আংশিক JSON,`BOOLEAN`প্রকার
- **2023**: **নেটিভ JSON** (পার্স JSON, জেনারেট JSON), UTF-8,`LIST`সংগ্রহ
- COBOL আধুনিক যুগের জন্য বিকশিত হতে থাকে
## সিনট্যাক্স বিবর্তন
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

## বৈশিষ্ট্য বিবর্তন
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## মূল ডিজাইনের নীতি
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## Y2K গল্প
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## ইকোসিস্টেম বৃদ্ধি
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
