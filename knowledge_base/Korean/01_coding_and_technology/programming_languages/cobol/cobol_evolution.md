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

# COBOL — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 흐름매틱 | 1955 | Grace Hopper의 비즈니스 언어 선구자 |
| 코볼-60 | 1959 | **첫 번째 COBOL** (CODASYL 위원회) |
| 코볼-61 | 1961 | 보고서 작성기,`PERFORM`개선 |
| 코볼-68 | 1968 | 최초의 ANSI 표준(X3.1-1968) |
| 코볼-74 | 1974년 | `IF`/`ELSE`, `EVALUATE`(스위치), 일반화 |
| 코볼-85 | 1985 | **구조적 프로그래밍**:`END-IF`,`END-PERFORM`, 범위 종결자 |
| 코볼 2002 | 2002 | **OOP**: 클래스, 메서드, 상속,`FUNCTION`|
| 코볼 2014 | 2014 | **XML**, `JSON`(부분),`BOOLEAN`유형 |
| 코볼 2023 | 2023년 | **네이티브 JSON**, UTF-8,`LIST`컬렉션 |
## 주요 이정표
### 코볼의 탄생(1959)
- **1959**: CODASYL(데이터 시스템 언어 회의)이 COBOL을 생성합니다.
- **그레이스 호퍼의 영향**: "비즈니스 언어는 영어처럼 보여야 합니다"
- **목표**: 이식 가능한 비즈니스 언어 — 모든 컴퓨터에서 실행
- COBOL-60: 첫 번째 버전 — 파일 처리, 보고서, 산술
### COBOL 68–74: 표준화(1968–1974)
- **COBOL-68**: 최초의 ANSI 표준
- **COBOL-74**: `EVALUATE`(스위치 문), 구조화된`IF`/`ELSE`
- COBOL은 전 세계적으로 지배적인 비즈니스 언어가 됩니다.
### COBOL 85: 구조화된 COBOL(1985)
- **범위 종결자**:`END-IF`,`END-PERFORM`,`END-READ`
-`EVALUATE`/`WHEN`(스위치)
-`PERFORM`/ `END-PERFORM`(인라인 루프)
-`SECTION`개선
- 대부분의 COBOL 코드가 작성된 버전입니다.
### COBOL 2002: 객체 지향 COBOL(2002)
- **클래스 및 메서드** —`CLASS-ID`,`METHOD-ID`
- **상속** —`INHERITS`
- **인터페이스** —`IMPLEMENTS`
-`FUNCTION`키워드
- `BOOLEAN`형(일부)
- 중첩된 프로그램
### COBOL 2014-2023: 모던 COBOL(2014-현재)
- **2014**: XML 지원, 부분 JSON,`BOOLEAN`유형
- **2023**: **네이티브 JSON**(PARSE JSON, GENERATE JSON), UTF-8,`LIST`컬렉션
- COBOL은 현대에도 계속해서 진화하고 있습니다.
## 구문 진화
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

## 기능 진화
```
COBOL-60:  File processing, arithmetic, reports
COBOL-68:  First standard, structured data
COBOL-74:  EVALUATE, IF/ELSE, generalizations
COBOL-85:  Scope terminators, inline PERFORM, structured programming
COBOL 2002: OOP (classes, methods, inheritance), FUNCTION
COBOL 2014: XML, BOOLEAN, partial JSON
COBOL 2023: Native JSON, UTF-8, LIST collections
```

## 주요 디자인 원칙
```
1. "Business-oriented" — designed for data processing
2. "English-like" — readable by non-programmers
3. "Portable" — runs on any mainframe, any platform
4. "Record-oriented" — file and database processing
5. "Backward compatible" — 60-year-old programs still run
6. "Verbose but clear" — self-documenting code
```

## Y2K 스토리
```
1999: COBOL programs used 2-digit years (PIC 99)
      "19" assumed — would roll over to "1900" in 2000
      Massive global effort to fix billions of lines of COBOL
2000: Y2K fix — largely successful (thanks to COBOL programmers)
      COBOL proves its maintainability — code written in 1960s
      could be understood and modified in 1999
```

## 생태계 성장
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
