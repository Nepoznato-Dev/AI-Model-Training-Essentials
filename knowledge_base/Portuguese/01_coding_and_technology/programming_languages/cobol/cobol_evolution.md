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

# COBOL — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| FLOW-MATIC | 1955 | Precursor da linguagem empresarial de Grace Hopper |
| COBOL-60 | 1959 | **Primeiro COBOL** (comitê CODASYL) |
| COBOL-61 | 1961 | Report Writer, melhorias em`PERFORM`|
| COBOL-68 | 1968 | Primeiro padrão ANSI (X3.1-1968) |
| COBOL-74 | 1974 | `IF`/`ELSE`,`EVALUATE`(switch), generalizações |
| COBOL-85 | 1985 | **Programação estruturada**:`END-IF`,`END-PERFORM`, terminadores de escopo |
| COBOL2002 | 2002 | **OOP**: classes, métodos, herança,`FUNCTION`|
| COBOL2014 | 2014 | **XML**,`JSON`(parcial), tipo`BOOLEAN`|
| COBOL 2023 | 2023 | **Coleções JSON nativas**, UTF-8,`LIST`|
## Marcos importantes
### O Nascimento do COBOL (1959)
- **1959**: CODASYL (Conferência sobre Linguagens de Sistemas de Dados) cria COBOL
- **Influência de Grace Hopper**: "A linguagem empresarial deve ser parecida com o inglês"
- **Objetivo**: Linguagem comercial portátil — roda em qualquer computador
- COBOL-60: Primeira versão — manipulação de arquivos, relatórios, aritmética
### COBOL 68–74: Padronização (1968–1974)
- **COBOL-68**: Primeiro padrão ANSI
- **COBOL-74**:`EVALUATE`(instrução switch), estruturado `IF`/`ELSE` 
- COBOL se torna a linguagem comercial dominante em todo o mundo
### COBOL 85: COBOL estruturado (1985)
- **Terminadores de escopo**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(interruptor)
-`PERFORM`/`END-PERFORM`(loops em linha)
- Melhorias `SECTION`
- Esta é a versão na qual a maior parte do código COBOL é escrita
### COBOL 2002: COBOL Orientado a Objetos (2002)
- **Classes e métodos** —`CLASS-ID`,`METHOD-ID`
- **Herança** —`INHERITS`
- **Interfaces** —`IMPLEMENTS`
- Palavra-chave `FUNCTION`
- Tipo`BOOLEAN`(parcial)
- Programas aninhados
### COBOL 2014–2023: COBOL moderno (2014–presente)
- **2014**: suporte XML, JSON parcial, tipo `BOOLEAN`
- **2023**: **JSON nativo** (PARSE JSON, GENERATE JSON), coleções UTF-8, `LIST`
- COBOL continua a evoluir para a era moderna
## Evolução da Sintaxe
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

## Evolução de recursos
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## Princípios-chave de design
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## A história do ano 2000
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## Crescimento do Ecossistema
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
