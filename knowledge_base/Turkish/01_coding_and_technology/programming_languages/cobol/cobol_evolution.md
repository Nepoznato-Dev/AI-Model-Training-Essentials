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
# COBOL — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| AKIŞ-MATİK | 1955 | Grace Hopper'ın iş dili öncüsü |
| COBOL-60 | 1959 | **İlk COBOL** (CODASYL komitesi) |
| COBOL-61 | 1961 | Rapor Yazarı,`PERFORM`iyileştirmeleri |
| COBOL-68 | 1968 | İlk ANSI standardı (X3.1-1968) |
| COBOL-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(anahtar), genellemeler |
| COBOL-85 | 1985 | **Yapılandırılmış programlama**: `END-IF`, `END-PERFORM`, kapsam sonlandırıcılar |
| COBOL 2002 | 2002 | **OOP**: sınıflar, yöntemler, kalıtım,`FUNCTION`|
| COBOL 2014 | 2014 | **XML**,`JSON`(kısmi),`BOOLEAN`türü |
| COBOL 2023 | 2023 | **Yerel JSON**, UTF-8,`LIST`koleksiyonları |
## Önemli Kilometre Taşları
### COBOL'un Doğuşu (1959)
- **1959**: CODASYL (Veri Sistemleri Dilleri Konferansı), COBOL'u oluşturur
- **Grace Hopper'ın etkisi**: "İş dili İngilizceye benzemeli"
- **Hedef**: Taşınabilir iş dili — herhangi bir bilgisayarda çalışır
- COBOL-60: İlk versiyon — dosya işleme, raporlar, aritmetik
### COBOL 68–74: Standardizasyon (1968–1974)
- **COBOL-68**: İlk ANSI standardı
- **COBOL-74**:`EVALUATE`(anahtar ifadesi), yapılandırılmış`IF`/`ELSE`
- COBOL dünya çapında baskın iş dili haline geliyor
### COBOL 85: Yapılandırılmış COBOL (1985)
- **Kapsam sonlandırıcılar**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(anahtar)
-`PERFORM`/`END-PERFORM`(satır içi döngüler)
-`SECTION`iyileştirmeleri
- Bu, çoğu COBOL kodunun yazıldığı sürümdür
### COBOL 2002: Nesneye Yönelik COBOL (2002)
- **Sınıflar ve yöntemler** —`CLASS-ID`,`METHOD-ID`
- **Miras** —`INHERITS`
- **Arayüzler** —`IMPLEMENTS`
-`FUNCTION`anahtar kelimesi
-`BOOLEAN`tipi (kısmi)
- İç içe programlar
### COBOL 2014–2023: Modern COBOL (2014 – günümüz)
- **2014**: XML desteği, kısmi JSON,`BOOLEAN`türü
- **2023**: **Yerel JSON** (PARSE JSON, GENERATE JSON), UTF-8,`LIST`koleksiyonları
- COBOL modern çağ için gelişmeye devam ediyor
## Söz Dizimi Gelişimi
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

## Özellik Gelişimi
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## Temel Tasarım İlkeleri
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## Y2K Hikayesi
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## Ekosistem Büyümesi
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
