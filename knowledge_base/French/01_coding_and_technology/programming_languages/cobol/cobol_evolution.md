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
# COBOL — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| FLUX-MATIC | 1955 | Le précurseur du langage des affaires de Grace Hopper |
| COBOL-60 | 1959 | **Premier COBOL** (Comité CODASYL) |
| COBOL-61 | 1961 | Rédacteur de rapports, améliorations`PERFORM`|
| COBOL-68 | 1968 | Première norme ANSI (X3.1-1968) |
| COBOL-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(commutateur), généralisations |
| COBOL-85 | 1985 | **Programmation structurée** :`END-IF`,`END-PERFORM`, terminateurs de portée |
| COBOL 2002 | 2002 | **POO** : classes, méthodes, héritage,`FUNCTION`|
| COBOL 2014 | 2014 | **XML**,`JSON`(partiel), type`BOOLEAN`|
| COBOL 2023 | 2023 | **Collections JSON natif**, UTF-8,`LIST`|
## Étapes majeures
### La naissance de COBOL (1959)
- **1959** : CODASYL (Conférence sur les langages des systèmes de données) crée COBOL
- **Influence de Grace Hopper** : "Le langage des affaires devrait ressembler à l'anglais"
- **Objectif** : langage professionnel portable – fonctionne sur n'importe quel ordinateur
- COBOL-60 : Première version — gestion de fichiers, rapports, arithmétique
### COBOL 68-74 : Standardisation (1968-1974)
- **COBOL-68** : Première norme ANSI
- **COBOL-74** :`EVALUATE`(instruction switch), structuré`IF`/`ELSE`
- COBOL devient le langage commercial dominant dans le monde
### COBOL 85 : COBOL structuré (1985)
- **Terminateurs de portée** :`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(interrupteur)
-`PERFORM`/`END-PERFORM`(boucles en ligne)
- Améliorations `SECTION`
- Il s'agit de la version dans laquelle la plupart du code COBOL est écrit
### COBOL 2002 : COBOL orienté objet (2002)
- **Classes et méthodes** —`CLASS-ID`,`METHOD-ID`
- **Héritage** —`INHERITS`
- **Interfaces** —`IMPLEMENTS`
- Mot-clé `FUNCTION`
- Type`BOOLEAN`(partiel)
- Programmes imbriqués
### COBOL 2014-2023 : COBOL moderne (2014-présent)
- **2014** : support XML, JSON partiel, type `BOOLEAN`
- **2023** : **JSON natif** (PARSE JSON, GENERATE JSON), UTF-8, collections `LIST`
- COBOL continue d'évoluer pour l'ère moderne
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## Principes de conception clés
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## L'histoire de l'an 2000
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## Croissance de l'écosystème
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
