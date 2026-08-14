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
# COBOL - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| FLUJO-MATIC | 1955 | El precursor del lenguaje empresarial de Grace Hopper |
| COBOL-60 | 1959 | **Primer COBOL** (comité CODASYL) |
| COBOL-61 | 1961 | Redactor de informes, mejoras`PERFORM`|
| COBOL-68 | 1968 | Primer estándar ANSI (X3.1-1968) |
| COBOL-74 | 1974 | `IF`/ `ELSE`,`EVALUATE`(interruptor), generalizaciones |
| COBOL-85 | 1985 | **Programación estructurada**: `END-IF`, `END-PERFORM`, terminadores de alcance |
| COBOL 2002 | 2002 | **OOP**: clases, métodos, herencia,`FUNCTION`|
| COBOL 2014 | 2014 | **XML**, tipo`JSON`(parcial),`BOOLEAN`|
| COBOL 2023 | 2023 | **Colecciones JSON nativas**, UTF-8,`LIST`|
## Hitos importantes
### El nacimiento de COBOL (1959)
- **1959**: CODASYL (Conferencia sobre Lenguajes de Sistemas de Datos) crea COBOL
- **Influencia de Grace Hopper**: "El lenguaje comercial debería parecerse al inglés"
- **Objetivo**: lenguaje empresarial portátil: se ejecuta en cualquier computadora
- COBOL-60: Primera versión: manejo de archivos, informes, aritmética
### COBOL 68–74: Estandarización (1968–1974)
- **COBOL-68**: Primer estándar ANSI
- **COBOL-74**:`EVALUATE`(sentencia de cambio), estructurado`IF`/`ELSE`
- COBOL se convierte en el lenguaje empresarial dominante en todo el mundo.
### COBOL 85: COBOL estructurado (1985)
- **Terminadores de alcance**: `END-IF`, `END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(interruptor)
-`PERFORM`/`END-PERFORM`(bucles en línea)
- Mejoras `SECTION`
- Esta es la versión en la que está escrito la mayor parte del código COBOL.
### COBOL 2002: COBOL orientado a objetos (2002)
- **Clases y métodos** — `CLASS-ID`,`METHOD-ID`
- **Herencia** —`INHERITS`
- **Interfaces** —`IMPLEMENTS`
- Palabra clave `FUNCTION`
- Tipo`BOOLEAN`(parcial)
- Programas anidados
### COBOL 2014-2023: COBOL moderno (2014-presente)
- **2014**: compatibilidad con XML, JSON parcial, tipo `BOOLEAN`
- **2023**: **JSON nativo** (PARSE JSON, GENERATE JSON), colecciones UTF-8, `LIST`
- COBOL continúa evolucionando para la era moderna
## Evolución de la sintaxis
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

## Evolución de funciones
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## Principios clave de diseño
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## La historia del año 2000
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## Crecimiento del ecosistema
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
