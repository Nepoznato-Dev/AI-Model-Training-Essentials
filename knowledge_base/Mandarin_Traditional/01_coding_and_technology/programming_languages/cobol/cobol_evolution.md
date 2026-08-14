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
# COBOL — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|流動自動控制 | 1955 | Grace Hopper 的商業語言先驅 |
| COBOL-60 | 1959 | **第一個 COBOL**（CODASYL 委員會）|
| COBOL-61 | 1961 |報告編寫器，`PERFORM` 改進 |
| COBOL-68 | 1968 |第一個 ANSI 標準 (X3.1-1968) |
| COBOL-74 | COBOL-74 1974 |`IF`/`ELSE`、`EVALUATE`（開關），概括 |
| COBOL-85 | 1985 | **結構化程式設計**：`END-IF`、`END-PERFORM`、範圍終止符 |
| COBOL 2002 | 2002 | **OOP**：類別、方法、繼承、`FUNCTION` |
| COBOL 2014 | 2014年| **XML**、`JSON`（部分）、`BOOLEAN` 型別 |
| COBOL 2023 | 2023 | **原生 JSON**、UTF-8、`LIST` 集合 |
## 主要里程碑
### COBOL 的誕生 (1959)
- **1959**：CODASYL（資料系統語言會議）建立 COBOL
- **格蕾絲霍珀的影響**：“商務語言應該看起來像英語”
- **目標**：可移植的商業語言 - 在任何電腦上運行
- COBOL-60：第一個版本 — 文件處理、報告、算術
### COBOL 68–74：標準化 (1968–1974)
- **COBOL-68**：第一個 ANSI 標準
- **COBOL-74**：`EVALUATE`（switch 語句），結構化`IF`/ `ELSE`
- COBOL 成為全球主導商業語言
### COBOL 85：結構化 COBOL (1985)
- **範圍終止符**：`END-IF`、`END-PERFORM`、 `END-READ`
-`EVALUATE`/ `WHEN`（開關）
-`PERFORM`/ `END-PERFORM`（內聯循環）
-`SECTION`改進
- 這是大多數 COBOL 程式碼編寫的版本
### COBOL 2002：物件導向的 COBOL (2002)
- **類別與方法** —`CLASS-ID`、 `METHOD-ID`
- **繼承** — `INHERITS`
- **介面** — `IMPLEMENTS`
-`FUNCTION`關鍵字
- `BOOLEAN`型（部分）
- 嵌套程序
### COBOL 2014–2023：現代 COBOL（2014 年至今）
- **2014**：XML 支持，部分 JSON，`BOOLEAN` 類型
- **2023**：**原生 JSON**（解析 JSON、生成 JSON）、UTF-8、`LIST` 集合
- COBOL 不斷發展以適應現代時代
## 語法演變
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

## 功能演變
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## 關鍵設計原則
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## 千年蟲故事
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## 生態系成長
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
