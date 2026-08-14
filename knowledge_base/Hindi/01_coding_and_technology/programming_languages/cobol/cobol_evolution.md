---
# Metadata
title: "COBOL — Version History & Evolution"
description: "Comprehensive version history and evolution of COBOL from 1959 to modern COBOL."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# COBOL - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| फ्लो-मैटिक | 1955 | ग्रेस हॉपर की व्यावसायिक भाषा अग्रदूत |
| कोबोल-60 | 1959 | **पहला कोबोल** (CODASYL समिति) |
| कोबोल-61 | 1961 | रिपोर्ट लेखक,`PERFORM`सुधार |
| कोबोल-68 | 1968 | पहला ANSI मानक (X3.1-1968) |
| कोबोल-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(स्विच), सामान्यीकरण |
| कोबोल-85 | 1985 | **संरचित प्रोग्रामिंग**:`END-IF`,`END-PERFORM`, स्कोप टर्मिनेटर |
| कोबोल 2002 | 2002 | **OOP**: कक्षाएं, विधियां, वंशानुक्रम,`FUNCTION`|
| कोबोल 2014 | 2014 | **XML**,`JSON`(आंशिक),`BOOLEAN`प्रकार |
| कोबोल 2023 | 2023 | **मूल JSON**, UTF-8,`LIST`संग्रह |
## प्रमुख मील के पत्थर
### कोबोल का जन्म (1959)
- **1959**: CODASYL (डेटा सिस्टम भाषाओं पर सम्मेलन) COBOL बनाता है
- **ग्रेस हॉपर का प्रभाव**: "व्यावसायिक भाषा अंग्रेजी की तरह दिखनी चाहिए"
- **लक्ष्य**: पोर्टेबल व्यावसायिक भाषा - किसी भी कंप्यूटर पर चलती है
- COBOL-60: पहला संस्करण - फ़ाइल प्रबंधन, रिपोर्ट, अंकगणित
### COBOL 68-74: मानकीकरण (1968-1974)
- **COBOL-68**: पहला ANSI मानक
- **COBOL-74**:`EVALUATE`(स्विच स्टेटमेंट), संरचित`IF`/`ELSE`
- COBOL दुनिया भर में प्रमुख व्यावसायिक भाषा बन गई है
### कोबोल 85: संरचित कोबोल (1985)
- **स्कोप टर्मिनेटर**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(स्विच)
-`PERFORM`/`END-PERFORM`(इनलाइन लूप)
-`SECTION`सुधार
- यह वह संस्करण है जिसमें अधिकांश COBOL कोड लिखा जाता है
### COBOL 2002: ऑब्जेक्ट-ओरिएंटेड COBOL (2002)
- **कक्षाएँ और विधियाँ** —`CLASS-ID`,`METHOD-ID`
- **विरासत** —`INHERITS`
- **इंटरफ़ेस** -`IMPLEMENTS`
-`FUNCTION`कीवर्ड
-`BOOLEAN`प्रकार (आंशिक)
- नेस्टेड प्रोग्राम
### COBOL 2014-2023: आधुनिक COBOL (2014-वर्तमान)
- **2014**: XML समर्थन, आंशिक JSON,`BOOLEAN`प्रकार
- **2023**: **नेटिव JSON** (पार्स JSON, जनरेट JSON), UTF-8,`LIST`संग्रह
- आधुनिक युग में COBOL का विकास जारी है
## सिंटेक्स इवोल्यूशन
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

## फ़ीचर इवोल्यूशन
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## Y2K कहानी
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## पारिस्थितिकी तंत्र का विकास
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
