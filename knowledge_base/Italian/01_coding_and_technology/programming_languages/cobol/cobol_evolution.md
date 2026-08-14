<!--
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

-->
# COBOL: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| FLOW-MATIC | 1955 | Precursore del linguaggio commerciale di Grace Hopper |
| COBOL-60 | 1959 | **Primo COBOL** (comitato CODASYL) |
| COBOL-61 | 1961 | Report Writer, miglioramenti`PERFORM`|
| COBOL-68 | 1968 | Primo standard ANSI (X3.1-1968) |
| COBOL-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(switch), generalizzazioni |
| COBOL-85 | 1985 | **Programmazione strutturata**:`END-IF`,`END-PERFORM`, terminatori di ambito |
| COBOL2002 | 2002| **OOP**: classi, metodi, ereditarietà,`FUNCTION`|
| COBOL2014 | 2014| **XML**,`JSON`(parziale), tipo`BOOLEAN`|
| COBOL2023 | 2023 | **Raccolte JSON native**, UTF-8,`LIST`|
## Traguardi importanti
### La nascita di COBOL (1959)
- **1959**: CODASYL (Conferenza sui linguaggi dei sistemi di dati) crea COBOL
- **L'influenza di Grace Hopper**: "Il linguaggio commerciale dovrebbe assomigliare all'inglese"
- **Obiettivo**: linguaggio aziendale portatile: funziona su qualsiasi computer
- COBOL-60: prima versione: gestione di file, rapporti, aritmetica
### COBOL 68–74: Standardizzazione (1968–1974)
- **COBOL-68**: Primo standard ANSI
- **COBOL-74**:`EVALUATE`(istruzione switch), strutturato`IF`/`ELSE`
- Il COBOL diventa il linguaggio commerciale dominante in tutto il mondo
### COBOL 85: COBOL strutturato (1985)
- **Terminatori dell'ambito**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(interruttore)
-`PERFORM`/`END-PERFORM`(loop in linea)
- Miglioramenti `SECTION`
- Questa è la versione in cui è scritta la maggior parte del codice COBOL
### COBOL 2002: COBOL orientato agli oggetti (2002)
- **Classi e metodi** —`CLASS-ID`,`METHOD-ID`
- **Eredità** —`INHERITS`
- **Interfacce** —`IMPLEMENTS`
- Parola chiave `FUNCTION`
- Tipo`BOOLEAN`(parziale)
- Programmi nidificati
### COBOL 2014–2023: COBOL moderno (2014–presente)
- **2014**: supporto XML, JSON parziale, tipo `BOOLEAN`
- **2023**: **JSON nativo** (PARSE JSON, GENERATE JSON), raccolte UTF-8, `LIST`
- COBOL continua ad evolversi per l'era moderna
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## Principi chiave di progettazione
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## La storia dell'anno 2000
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## Crescita dell'ecosistema
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
