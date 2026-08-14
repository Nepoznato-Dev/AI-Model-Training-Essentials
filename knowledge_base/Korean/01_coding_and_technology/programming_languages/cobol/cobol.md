<!--
---
# Metadata
title: "COBOL"
description: "Comprehensive reference for the COBOL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cobol, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "34 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# 코볼
COBOL(Common Business-Oriented Language)은 1959년에 처음 개발되어 현재까지 사용되는 가장 오래된 프로그래밍 언어 중 하나입니다. 이는 금융 시스템, 급여, 금융, 보험 및 정부 애플리케이션과 같은 비즈니스 데이터 처리용으로 설계되었습니다. COBOL의 영어와 유사한 구문은 프로그래머뿐만 아니라 비즈니스 관리자도 읽을 수 있도록 고안되었습니다.
오랜 역사에도 불구하고 COBOL은 전 세계 모든 비즈니스 거래의 약 30%를 처리합니다. 주요 은행, 정부 기관(미국 사회 보장국 포함) 및 보험 회사는 여전히 COBOL 메인프레임 시스템에 의존하고 있습니다. 1999년 Y2K 버그 공포로 인해 COBOL이 다시 대중의 인지도를 얻었으며 이 언어는 전 세계적으로 계속해서 중요한 인프라를 실행하고 있습니다.
---

## COBOL이 중요한 이유
- **비즈니스에 중요한 인프라**: 은행과 정부 전반에 걸쳐 매일 수조 달러에 달하는 거래를 처리합니다.
- **안정성**: 1970년대에 작성된 COBOL 프로그램은 오늘날에도 여전히 안정적으로 실행되며 최소한의 변경만 필요합니다.
- **가독성**: 영어와 유사한 구문을 통해 프로그래머가 아닌 사람도 비즈니스 논리를 이해할 수 있습니다.
- **소수점 산술**: 정확한 재무 계산을 기본적으로 지원합니다(부동 소수점 반올림 오류 없음).
- **일괄 처리**: 대용량 기록을 효율적으로 처리하도록 설계되었습니다.
- **고용 시장**: COBOL 개발자의 심각한 부족으로 인해 유지 관리 역할에 대한 수요가 높아지고 급여도 높아집니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **자세한 구문** | 간단한 작업을 위해 많은 라인이 필요함 | 언어 설계의 일부로 수락 |
| **현대적이지 않음** | 클래스 없음, 함수형 프로그래밍 없음, 제한된 추상화 | 유지 관리에 사용합니다. 현대 언어로 새로운 시스템 구축 |
| **메인프레임 종속성** | 일반적으로 IBM 메인프레임에서 실행됨(비싼) | 분산 시스템에서 COBOL 컴파일러 사용(GnuCOBOL) |
| **인력감소** | 현장에 진입하는 COBOL 개발자 감소 | 그것을 아는 사람들에 대한 수요가 높습니다. 좋은 직업 틈새 시장 |
| **웹/모바일 없음** | 최신 애플리케이션을 구축할 수 없음 | 백엔드 일괄 처리에 사용합니다. 현대적인 프런트엔드 |
---

## 구문 기본 사항
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME        PIC A(20) VALUE 'Alice'.
       01 WS-AGE         PIC 99 VALUE 30.
       01 WS-SCORE       PIC 9V99 VALUE 9.50.
       01 WS-GREETING    PIC X(50).
       
       PROCEDURE DIVISION.
           STRING 'Hello, ' DELIMITED BY SIZE
                  WS-NAME DELIMITED BY SIZE
                  '!' DELIMITED BY SIZE
                  INTO WS-GREETING
           END-STRING
           
           DISPLAY WS-GREETING
           DISPLAY 'Age: ' WS-AGE
           DISPLAY 'Score: ' WS-SCORE
           
           STOP RUN.
```

### 파일 처리 예시
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROCESS-CUSTOMERS.
       
       DATA DIVISION.
       FILE SECTION.
       FD  CUSTOMER-FILE.
       01  CUSTOMER-RECORD.
           05 CUST-ID        PIC 9(6).
           05 CUST-NAME      PIC X(30).
           05 CUST-BALANCE   PIC 9(7)V99.
       
       WORKING-STORAGE SECTION.
       01  WS-EOF            PIC X VALUE 'N'.
       
       PROCEDURE DIVISION.
           OPEN INPUT CUSTOMER-FILE
           
           PERFORM UNTIL WS-EOF = 'Y'
               READ CUSTOMER-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END
                       IF CUST-BALANCE > 1000.00
                           DISPLAY CUST-ID ' ' CUST-NAME 
                               ' Balance: ' CUST-BALANCE
                       END-IF
               END-READ
           END-PERFORM
           
           CLOSE CUSTOMER-FILE
           STOP RUN.
```

---

## 고급 구문 및 패턴
### 데이터 분할 심층 분석
COBOL의 데이터 분할은 언어의 가장 독특한 특징입니다. 계층적 번호 지정 시스템(레벨 01-88)을 사용하여 데이터 구조를 정의합니다.
| 레벨 | 목적 | 예 |
|-------|---------|---------|
| **01** | 레코드 수준 항목(최상위 변수 또는 레코드) | `01 WS-EMPLOYEE.`|
| **02–49** | 그룹 또는 기본 항목(하위 필드) | `05 EMP-NAME PIC X(30).`|
| **66** | Rename 절(데이터의 대체 보기) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | 독립형 기본 항목(하위 항목 없음) | `77 WS-COUNTER PIC 9(5).`|
| **88** | 조건 이름(부울 유사 플래그) | `88 WS-IS-SENIOR VALUE 'Y'.`|
```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       * Hierarchical data structure
       01  WS-EMPLOYEE.
           05  EMP-ID            PIC 9(6).
           05  EMP-NAME.
               10  EMP-FIRST     PIC X(15).
               10  EMP-LAST      PIC X(20).
           05  EMP-SALARY        PIC 9(7)V99.
           05  EMP-HIRE-DATE.
               10  EMP-YEAR      PIC 9(4).
               10  EMP-MONTH     PIC 9(2).
               10  EMP-DAY       PIC 9(2).
           05  EMP-STATUS        PIC X.
               88  EMP-ACTIVE    VALUE 'A'.
               88  EMP-INACTIVE  VALUE 'I'.
               88  EMP-ON-LEAVE  VALUE 'L'.
       
       * Packed decimal for precise financial calculations
       01  WS-TRANSACTION.
           05  TR-AMOUNT         PIC S9(9)V99 COMP-3.
           05  TR-TYPE           PIC XX.
               88  TR-DEBIT      VALUE 'DB'.
               88  TR-CREDIT     VALUE 'CR'.
       
       * Usage types
       01  WS-CALC-FIELD         COMP-2.      * Double precision float
       01  WS-BINARY-FIELD       COMP.         * Binary integer
       01  WS-INDEX-FIELD        POINTER.      * Memory address
```

### COPY 문(카피북)
카피북은 코드 재사용을 위한 COBOL의 메커니즘입니다. C의 `#include`와 유사합니다. 카피북은 별도의 멤버로 저장되고 컴파일 타임에 삽입됩니다.
```cobol
       * In the main program — copy in common data definitions
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL-MAIN.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       * Copy in standard record layouts
       COPY EMPLOYEE-RECORD.
       COPY PAYROLL-CALC.
       COPY ERROR-HANDLER.
       
       PROCEDURE DIVISION.
           PERFORM 100-INITIALIZE
           PERFORM 200-PROCESS-EMPLOYEES
           PERFORM 900-CLEANUP
           STOP RUN.
```

```cobol
       * EMPLOYEE-RECORD copybook (stored as EMPLOYEE.cpy)
       01  WS-EMPLOYEE-RECORD.
           05  EMP-ID            PIC 9(6).
           05  EMP-NAME          PIC X(30).
           05  EMP-DEPT          PIC X(4).
           05  EMP-SALARY        PIC 9(7)V99.
           05  EMP-HOURS-WORKED  PIC 9(3).
```

### 변형 수행
COBOL은 구조적 프로그래밍을 위한 여러 가지 PERFORM 문을 제공합니다.
```cobol
       PROCEDURE DIVISION.
       
       * Simple paragraph call (like a function call)
           PERFORM 100-CALCULATE-TAX
       
       * PERFORM with inline code (like a block)
           PERFORM
               DISPLAY 'Processing...'
               ADD 1 TO WS-COUNTER
           END-PERFORM
       
       * PERFORM N TIMES (counted loop)
           PERFORM 200-PROCESS-RECORD 100 TIMES
       
       * PERFORM VARYING (for loop equivalent)
           PERFORM 300-PROCESS-EMPLOYEE
               VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-EMPLOYEE-COUNT
       
       * PERFORM UNTIL (while loop equivalent)
           PERFORM UNTIL WS-EOF = 'Y'
               READ INPUT-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END PERFORM 400-HANDLE-RECORD
               END-READ
           END-PERFORM
       
       * PERFORM THRU (executes a range of paragraphs)
           PERFORM 100-START THRU 100-END
       
       100-CALCULATE-TAX.
           COMPUTE WS-TAX = WS-SALARY * 0.22
           .
       
       200-PROCESS-RECORD.
           DISPLAY 'Processing record' WS-COUNTER
           .
```

### 문자열 처리 및 검사
```cobol
       WORKING-STORAGE SECTION.
       01  WS-SOURCE         PIC X(50) VALUE 'Hello World'.
       01  WS-TARGET         PIC X(50).
       01  WS-COUNT          PIC 9(3).
       
       PROCEDURE DIVISION.
       * INSPECT — count occurrences
           INSPECT WS-SOURCE TALLYING WS-COUNT
               FOR ALL 'o'
           DISPLAY 'Count of o: ' WS-COUNT
       
       * INSPECT — replace characters
           INSPECT WS-SOURCE REPLACING ALL 'o' BY '0'
           DISPLAY WS-SOURCE
       
       * STRING — concatenate
           STRING 'Mr. ' DELIMITED BY SIZE
                  WS-LAST-NAME DELIMITED BY SPACE
                  ', ' DELIMITED BY SIZE
                  WS-FIRST-NAME DELIMITED BY SPACE
                  INTO WS-FULL-NAME
           END-STRING
       
       * UNSTRING — split a string
           UNSTRING WS-FULL-NAME
               DELIMITED BY ',' OR SPACE
               INTO WS-PART1 WS-PART2 WS-PART3
           END-UNSTRING
       
       * REFERENCE MODIFICATION — substring
           MOVE WS-SOURCE(1:5) TO WS-TARGET
           DISPLAY WS-TARGET
```

---

## 아키텍처 및 시스템 설계
### 4개 부문
모든 COBOL 프로그램은 4개 부문으로 구성되어 있으며 각 부문은 고유한 목적을 수행합니다.
```
┌─────────────────────────────────────────────────┐
│ IDENTIFICATION DIVISION                          │
│   Program metadata (name, author, date, etc.)    │
├─────────────────────────────────────────────────┤
│ ENVIRONMENT DIVISION                             │
│   Hardware/software configuration                │
│   CONFIGURATION SECTION (computer, compiler)     │
│   INPUT-OUTPUT SECTION (file definitions)        │
├─────────────────────────────────────────────────┤
│ DATA DIVISION                                    │
│   FILE SECTION (file record layouts)             │
│   WORKING-STORAGE SECTION (variables)            │
│   LOCAL-STORAGE SECTION (procedure-local vars)   │
│   LINKAGE SECTION (parameters passed in)         │
├─────────────────────────────────────────────────┤
│ PROCEDURE DIVISION                               │
│   All business logic and control flow            │
│   Organized into paragraphs and sections         │
└─────────────────────────────────────────────────┘
```

### 프로그램 계층
COBOL 시스템은 일반적으로 서브프로그램을 호출하는 기본 프로그램과 함께 호출 계층 구조를 사용합니다.
```
MAINPGM (entry point)
├── INITPGM    (initialization, open files)
├── READPGM    (read input records)
├── CALCPGM    (business logic calculations)
├── WRITEPGM   (write output records)
└── CLEANPGM   (close files, cleanup)
```

```cobol
       * Main program calling subprograms
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAINPGM.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE ASSIGN TO EMPLFILE
               FILE STATUS IS WS-FILE-STATUS.
       
       DATA DIVISION.
       FILE SECTION.
       FD  EMPLOYEE-FILE.
       01  EMP-RECORD          PIC X(200).
       
       WORKING-STORAGE SECTION.
       01  WS-FILE-STATUS      PIC XX.
       01  WS-EOF              PIC X VALUE 'N'.
       01  WS-RETURN-CODE      PIC 9(4).
       
       PROCEDURE DIVISION.
       000-MAIN.
           PERFORM 100-INITIALIZE
           PERFORM 200-PROCESS
               UNTIL WS-EOF = 'Y'
           PERFORM 900-CLEANUP
           GOBACK.
       
       100-INITIALIZE.
           OPEN INPUT EMPLOYEE-FILE
           IF WS-FILE-STATUS NOT = '00'
               DISPLAY 'ERROR OPENING FILE: ' WS-FILE-STATUS
               MOVE 'Y' TO WS-EOF
           END-IF.
       
       200-PROCESS.
           READ EMPLOYEE-FILE
               AT END MOVE 'Y' TO WS-EOF
               NOT AT END
                   CALL 'CALCPGM' USING EMP-RECORD
                       RETURNING WS-RETURN-CODE
                   IF WS-RETURN-CODE = 0
                       CALL 'WRITEPGM' USING EMP-RECORD
                   END-IF
           END-READ.
       
       900-CLEANUP.
           CLOSE EMPLOYEE-FILE.
```

### 일반적인 프로젝트 디렉터리 구조
```
cobol-project/
├── src/
│   ├── mainpgm.cbl           * Main entry program
│   ├── calcpgm.cbl           * Calculation subprogram
│   ├── readpgm.cbl           * File reading subprogram
│   └── writepgm.cbl          * Output subprogram
├── copybooks/
│   ├── employee.cpy          * Employee record layout
│   ├── payroll-calc.cpy      * Payroll calculation copybook
│   └── error-handler.cpy     * Error handling copybook
├── jcl/
│   ├── compile.jcl           * Compilation JCL
│   └── run.jcl               * Execution JCL
├── data/
│   ├── input/                * Input data files
│   └── output/               * Output data files
├── Makefile                  * GnuCOBOL build (distributed)
└── README.md
```

---

## 프로젝트 구성 및 빌드 시스템
### GnuCOBOL(오픈 소스 COBOL 컴파일러)
GnuCOBOL(이전의 OpenCOBOL)은 COBOL을 C로 컴파일한 다음 기본 기계어 코드로 컴파일하여 COBOL을 Linux, Windows 및 macOS에서 실행할 수 있도록 합니다.
```makefile
# Makefile for GnuCOBOL project
COBC     = cobc
COBFLAGS = -free -O2 -std=cobol2014
LDFLAGS  = -L./lib

SRCDIR   = src
CPYDIR   = copybooks
OBJDIR   = obj

SRCS     = $(wildcard $(SRCDIR)/*.cbl)
OBJS     = $(SRCS:$(SRCDIR)/%.cbl=$(OBJDIR)/%.o)
TARGET   = payroll

all: $(TARGET)

$(OBJDIR)/%.o: $(SRCDIR)/%.cbl
	$(COBC) $(COBFLAGS) -I $(CPYDIR) -c $< -o $@

$(TARGET): $(OBJS)
	$(COBC) -x $(COBFLAGS) $(OBJS) $(LDFLAGS) -o $(TARGET)

clean:
	rm -f $(OBJDIR)/*.o $(OBJDIR)/*.c $(TARGET)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
```

### IBM 메인프레임 JCL(작업 제어 언어)
IBM 메인프레임에서 COBOL 프로그램은 JCL을 사용하여 컴파일되고 실행됩니다.
```jcl
//COMPILE  JOB (ACCT),'COMPILE COBOL',
//             CLASS=A,MSGCLASS=X
//*
//COBOL    EXEC IGYWCG,
//             COBOL.SYSCBL='MYPROJ.SRC.COBOL(MAINPGM)',
//             COBOL.SYSCP='MYPROJ.SRC.CPY'
//*
//LINK     EXEC IGYWLK,
//             LKED.SYSLMOD='MYPROJ.LOAD(MAINPGM)'
//*
//RUN      EXEC PGM=MAINPGM
//STEPLIB  DD DSN=MYPROJ.LOAD,DISP=SHR
//EMPLFILE DD DSN=MYPROJ.DATA.EMPLOYEE,DISP=SHR
//OUTFILE  DD DSN=MYPROJ.DATA.OUTPUT,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,(10,5))
//SYSOUT   DD SYSOUT=*
```

### 컴파일러 옵션 참조
| 옵션 | 설명 | 예 |
|---------|-------------|---------|
| `-free`| 자유 형식 소스(열 제한 없음) | `cobc -free prog.cbl`|
| `-fixed`| 고정 형식(기존 열 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| 최적화 수준 2 | `cobc -O2 prog.cbl`|
| `-g`| 디버그 정보 생성 | `cobc -g prog.cbl`|
| `-std=cobol2014`| COBOL 2014 표준 사용 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| 실행 파일 빌드(컴파일뿐만 아니라) | `cobc -x prog.cbl`|
| `-I`| 카피북 검색 경로 | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| 모든 경고 활성화 | `cobc -Wall prog.cbl`|
---

## 테스트 및 디버깅
### COBOL 디버거 기술
```cobol
       * Debugging with DISPLAY statements
       PROCEDURE DIVISION.
       000-MAIN.
           DISPLAY '=== DEBUG: Program started ==='
           
           MOVE 1000 TO WS-SALARY
           DISPLAY 'DEBUG: Salary = ' WS-SALARY
           
           PERFORM 100-CALCULATE
           
           DISPLAY 'DEBUG: Tax = ' WS-TAX
           DISPLAY 'DEBUG: Net = ' WS-NET-PAY
           DISPLAY '=== DEBUG: Program complete ==='
           STOP RUN.
       
       * Using EVALUATE for conditional debugging
       100-CALCULATE.
           COMPUTE WS-TAX = WS-SALARY * 0.22
           COMPUTE WS-NET-PAY = WS-SALARY - WS-TAX
           
           * Conditional debug output
           IF WS-DEBUG-FLAG = 'Y'
               DISPLAY 'DEBUG: Tax rate applied: 22%'
               DISPLAY 'DEBUG: Gross=' WS-SALARY 
                       ' Tax=' WS-TAX ' Net=' WS-NET-PAY
           END-IF.
```

### gdb를 사용한 GnuCOBOL 디버깅
```bash
# Compile with debug symbols
cobc -free -g -o payroll src/mainpgm.cbl

# Debug with GDB
gdb ./payroll
```

```gdb
# GDB commands useful for COBOL debugging
(gdb) break MAINPGM             # Break at paragraph
(gdb) break calcpgm.cbl:42      # Break at source line
(gdb) print ws_salary           # Print COBOL variable
(gdb) display ws-employee-record # Auto-display on each step
(gdb) step                       # Step into CALL
(gdb) next                       # Step over
```

### 일반적인 디버깅 패턴
| 문제 | 증상 | 솔루션 |
|---------|---------|----------|
| 잘린 데이터 | 필드가 끊어졌습니다 | PIC 절 크기가 레코드 레이아웃과 일치하는지 확인 |
| 숫자 오버플로 | 잘못된 계산 | PIC 9(n)에 충분한 자릿수가 있는지 확인 |
| 파일 상태 오류 | WS-FILE-STATUS가 '00'이 아님 | 파일 DD 이름, 경로 및 권한 확인 |
| 무한 루프 | 종료되지 않을 때까지 수행 | 루프 변수가 루프 내에서 수정되었는지 확인 |
| 통화 실패 | 0이 아닌 값 반환 | LINKAGE SECTION이 호출 프로그램과 일치하는지 확인 |
---

## 상호 운용성
### CALL 문 — 서브프로그램 호출
```cobol
       * Dynamic CALL — program resolved at runtime
       WORKING-STORAGE SECTION.
       01  WS-PROGRAM-NAME   PIC X(8) VALUE 'TAXCALC'.
       01  WS-SALARY         PIC 9(7)V99 VALUE 75000.00.
       01  WS-TAX            PIC 9(7)V99.
       01  WS-RETURN-CODE    PIC 9(4).
       
       PROCEDURE DIVISION.
           CALL WS-PROGRAM-NAME
               USING WS-SALARY
                     WS-TAX
               RETURNING WS-RETURN-CODE
           END-CALL
           
           IF WS-RETURN-CODE = 0
               DISPLAY 'Tax: ' WS-TAX
           ELSE
               DISPLAY 'Error: ' WS-RETURN-CODE
           END-IF
```

### C 상호 운용성(GnuCOBOL)
```cobol
       * Calling a C function from COBOL via GnuCOBOL
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALL-C-FUNC.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-RESULT   PIC 9(9).
       
       PROCEDURE DIVISION.
           * Call C's strlen() function
           CALL "strlen" USING
               BY REFERENCE "Hello World"
               RETURNING WS-RESULT
           END-CALL
           DISPLAY "Length: " WS-RESULT
           STOP RUN.
```

### 데이터베이스 연결(DB2/COBOL)
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DB2-QUERY.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       EXEC SQL INCLUDE SQLCA END-EXEC.
       
       01  WS-EMPLOYEE.
           05  WS-EMP-ID     PIC 9(6).
           05  WS-EMP-NAME   PIC X(30).
           05  WS-EMP-SAL    PIC 9(7)V99.
       
       01  WS-SQL-STMT       PIC X(200).
       
       PROCEDURE DIVISION.
       * Embedded SQL — single row fetch
           EXEC SQL
               SELECT EMP_ID, EMP_NAME, EMP_SALARY
               INTO :WS-EMP-ID, :WS-EMP-NAME, :WS-EMP-SAL
               FROM EMPLOYEE
               WHERE EMP_ID = 1001
           END-EXEC
           
           IF SQLCODE = 0
               DISPLAY 'Found: ' WS-EMP-NAME ' Salary: ' WS-EMP-SAL
           ELSE
               DISPLAY 'SQL Error: ' SQLCODE
           END-IF
           
       * Embedded SQL — cursor for multiple rows
           EXEC SQL
               DECLARE EMP-CUR CURSOR FOR
               SELECT EMP_ID, EMP_NAME, EMP_SALARY
               FROM EMPLOYEE
               WHERE EMP_SALARY > 50000
               ORDER BY EMP_NAME
           END-EXEC
           
           EXEC SQL OPEN EMP-CUR END-EXEC
           
           PERFORM UNTIL SQLCODE NOT = 0
               EXEC SQL
                   FETCH EMP-CUR
                   INTO :WS-EMP-ID, :WS-EMP-NAME, :WS-EMP-SAL
               END-EXEC
               IF SQLCODE = 0
                   DISPLAY WS-EMP-ID ' ' WS-EMP-NAME
                       ' ' WS-EMP-SAL
               END-IF
           END-PERFORM
           
           EXEC SQL CLOSE EMP-CUR END-EXEC
           STOP RUN.
```

---

## 디자인 패턴
### 패턴 1: 제어 중단을 사용한 일괄 처리
컨트롤 중단 패턴은 가장 기본적인 COBOL 디자인 패턴으로, 주요 필드별로 그룹화된 레코드를 처리하고 소계를 생성합니다.
```cobol
       PROCEDURE DIVISION.
       000-MAIN.
           OPEN INPUT ORDER-FILE
           PERFORM 100-READ-ORDER
           PERFORM 200-PROCESS-ORDERS
               UNTIL WS-EOF = 'Y'
           CLOSE ORDER-FILE
           STOP RUN.
       
       100-READ-ORDER.
           READ ORDER-FILE
               AT END MOVE 'Y' TO WS-EOF
           END-READ.
       
       200-PROCESS-ORDERS.
           MOVE DEPT-CODE TO WS-PREV-DEPT
           MOVE ZERO TO WS-DEPT-TOTAL
           
           PERFORM UNTIL WS-EOF = 'Y'
               OR DEPT-CODE NOT = WS-PREV-DEPT
               
               IF DEPT-CODE NOT = WS-PREV-DEPT
                   PERFORM 300-PRINT-DEPT-SUBTOTAL
                   MOVE ZERO TO WS-DEPT-TOTAL
                   MOVE DEPT-CODE TO WS-PREV-DEPT
               END-IF
               
               ADD ORDER-AMOUNT TO WS-DEPT-TOTAL
               PERFORM 400-PRINT-ORDER-LINE
               PERFORM 100-READ-ORDER
           END-PERFORM
           
           PERFORM 300-PRINT-DEPT-SUBTOTAL.
       
       300-PRINT-DEPT-SUBTOTAL.
           DISPLAY 'Department: ' WS-PREV-DEPT
                   ' Total: ' WS-DEPT-TOTAL.
       
       400-PRINT-ORDER-LINE.
           DISPLAY '  Order: ' ORDER-ID
                   ' Amount: ' ORDER-AMOUNT.
```

### 패턴 2: 편집/검증 패턴
```cobol
       500-VALIDATE-RECORD.
           MOVE ZERO TO WS-ERROR-COUNT
           
           * Validate customer ID (must be 6 digits)
           IF CUST-ID IS NOT NUMERIC
               DISPLAY 'ERROR: Invalid Customer ID: ' CUST-ID
               ADD 1 TO WS-ERROR-COUNT
           END-IF
           
           * Validate amount (must be positive)
           IF ORDER-AMOUNT <= 0
               DISPLAY 'ERROR: Negative amount: ' ORDER-AMOUNT
               ADD 1 TO WS-ERROR-COUNT
           END-IF
           
           * Validate date fields
           IF ORDER-DATE NOT NUMERIC
               DISPLAY 'ERROR: Invalid date format'
               ADD 1 TO WS-ERROR-COUNT
           END-IF
           
           IF WS-ERROR-COUNT = 0
               MOVE 'Y' TO WS-RECORD-VALID
           ELSE
               MOVE 'N' TO WS-RECORD-VALID
           END-IF.
```

### 패턴 3: 테이블 조회(메모리 내 배열)
```cobol
       WORKING-STORAGE SECTION.
       01  WS-TAX-TABLE.
           05  WS-TAX-RATE OCCURS 5 TIMES.
               10  TR-BRACKET    PIC 9(7).
               10  TR-RATE       PIC V999.
       
       01  WS-INDEX              PIC 9 VALUE 1.
       01  WS-TAX-AMOUNT         PIC 9(7)V99.
       
       PROCEDURE DIVISION.
       * Initialize tax brackets
           MOVE 10000 TO TR-BRACKET(1)
           MOVE 0.100 TO TR-RATE(1)
           MOVE 25000 TO TR-BRACKET(2)
           MOVE 0.150 TO TR-RATE(2)
           MOVE 50000 TO TR-BRACKET(3)
           MOVE 0.220 TO TR-RATE(3)
           MOVE 100000 TO TR-BRACKET(4)
           MOVE 0.240 TO TR-RATE(4)
           MOVE 9999999 TO TR-BRACKET(5)
           MOVE 0.320 TO TR-RATE(5)
       
       * Lookup tax rate
       600-CALCULATE-TAX.
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > 5
               OR WS-SALARY <= TR-BRACKET(WS-INDEX)
               CONTINUE
           END-PERFORM
           
           COMPUTE WS-TAX-AMOUNT =
               WS-SALARY * TR-RATE(WS-INDEX).
```

---

## 성능 및 최적화
### 파일 I/O 최적화
```cobol
       * BAD: Reading one record at a time with no buffering
           PERFORM UNTIL WS-EOF = 'Y'
               READ CUSTOMER-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END PERFORM PROCESS-RECORD
               END-READ
           END-PERFORM
       
       * GOOD: Using BLOCK CONTAINS for buffered I/O
       * In the DATA DIVISION:
       FD  CUSTOMER-FILE
           BLOCK CONTAINS 0 RECORDS
           RECORDING MODE IS F.
       01  CUSTOMER-RECORD PIC X(200).
       
       * GOOD: Using indexed files for random access
       FD  INDEXED-CUSTOMER.
       01  CUST-RECORD.
           05  CUST-KEY      PIC 9(6).
           05  CUST-DATA     PIC X(194).
       
       * In ENVIRONMENT DIVISION:
       SELECT INDEXED-CUSTOMER ASSIGN TO CUSTFILE
           ORGANIZATION IS INDEXED
           ACCESS MODE IS DYNAMIC
           RECORD KEY IS CUST-KEY
           FILE STATUS IS WS-FILE-STATUS.
       
       * Random access read
           MOVE 1234 TO CUST-KEY
           READ INDEXED-CUSTOMER
               INVALID KEY DISPLAY 'Not found'
           END-READ
```

### 일괄 처리 최적화
| 기술 | 영향 | 설명 |
|------------|---------|-------------|
| **블록 I/O** | 높음 | BLOCK CONTAINS를 사용하여 물리적 I/O 작업 감소 |
| **색인화된 액세스** | 높음 | 무작위 액세스 조회를 위해 INDEXED ORGANIZATION 사용 |
| **정렬/병합** | 중간 | 대규모 데이터 세트 정렬에 SORT 동사 사용 |
| **디스플레이 최소화** | 중간 | DISPLAY는 일괄적으로 느립니다. 대신 파일에 쓰기 |
| **COMP/COMP-3** | 중간 | 바이너리/팩형 필드는 DISPLAY 숫자보다 빠릅니다. |
| **버퍼 튜닝** | 중간 | 순차 파일 처리를 위한 버퍼 크기 조정 |
---

## 배포 및 실제 사용
### 메인프레임 배포(IBM z/OS)
메인프레임의 COBOL 프로그램은 분할된 데이터세트(PDS)에 로드 모듈로 배포됩니다. JCL은 컴파일, 링크 및 실행을 제어합니다.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### 분산 배포(GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### COBOL을 사용하는 실제 산업
| 산업 | 사용법 | 규모 |
|----------|-------|-------|
| **뱅킹** | 거래처리, 계좌관리 | ATM 거래의 ~85% 처리 |
| **보험** | 정책관리, 청구처리 | 주요 보험사에서 COBOL 백엔드 실행 |
| **정부** | 사회 보장, 세금 처리, 혜택 | US SSA는 수십억 개의 기록을 처리합니다 |
| **헬스케어** | 환자 기록, 청구 시스템 | 기존 병원 정보 시스템 |
| **소매** | 재고 관리, POS 백엔드 | 레거시 시스템을 갖춘 대규모 소매업체 |
| **통신** | 빌링 시스템, 통화 기록 처리 | 통화내역 기록처리 |
---

## COBOL을 사용해야 하는 경우
| 시나리오 | 왜 코볼인가 | 더 나은 대안 |
|----------|----------|------|
| 메인프레임 유지 관리 | 기존 코드베이스 | — |
| 일괄 금융처리 | 입증되고 신뢰할 수 있으며 정확한 십진수 수학 | 새로운 시스템을 위한 Java, Python |
| 정부 레거시 시스템 | 기존 코드베이스 | — |
| 컴퓨팅 역사 학습 | 프로그래밍의 진화 이해 | — |
| 새로운 비즈니스 애플리케이션 | 현대적인 선택이 아닙니다 | 자바, C#, 파이썬 |
| 웹/모바일 개발 | 적합하지 않음 | 자바스크립트, 스위프트, 코틀린 |
| 데이터 과학 / ML | 적합하지 않음 | 파이썬, R |
---

## 종합 Q&A
### Q1: 왜 COBOL이 60년이 지난 지금도 은행 업무에 사용됩니까?
**답변:** COBOL은 은행 거래의 약 70~80%를 처리합니다. 이유:
- 올바르게 작동하는 대규모 코드베이스(수백만 줄)
- 극도의 신뢰성 - 이 시스템은 수십 년 동안 생산 테스트를 거쳤습니다.
- 마이그레이션 비용과 위험이 유지 관리 비용보다 큽니다.
- COBOL의 장황하고 영어와 유사한 구문은 자체 문서화됩니다.
- 언어에 내장된 소수점 연산(부동 소수점 반올림 오류 없음)
### Q2: COBOL은 부동 소수점 오류 없이 십진수 산술을 어떻게 처리합니까?
**A:** COBOL에는 고정된 정밀도의 기본 십진수 유형이 있습니다.
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V`는 암시적 소수점입니다. COBOL은 절대로 이진 부동 소수점을 돈으로 사용하지 않습니다.
### Q3: COBOL 프로그램의 구조는 무엇입니까?
**답:** 모든 COBOL 프로그램에는 4개 부문이 있습니다.
```cobol
       IDENTIFICATION DIVISION.
           PROGRAM-ID. HELLO.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
           WORKING-STORAGE SECTION.
       PROCEDURE DIVISION.
           DISPLAY "Hello, World!".
           STOP RUN.
```

### Q4: COBOL에서 순차 파일을 어떻게 읽고 처리합니까?
**답:** COBOL은 파일 처리에 탁월합니다.
```cobol
       SELECT CUST-FILE ASSIGN TO 'customers.dat'
           ORGANIZATION IS LINE SEQUENTIAL.

       FD CUST-FILE.
       01 CUST-RECORD.
           05 CUST-NAME    PIC X(30).
           05 CUST-BALANCE PIC 9(7)V99.

       PROCEDURE DIVISION.
           OPEN INPUT CUST-FILE
           PERFORM UNTIL EOF
               READ CUST-FILE
                   AT END MOVE 'YES' TO EOF
                   NOT AT END
                       ADD CUST-BALANCE TO GRAND-TOTAL
               END-READ
           END-PERFORM
           CLOSE CUST-FILE.
```

### Q5: 최신 COBOL 개발에 사용할 수 있는 도구는 무엇입니까?
**A:** GnuCOBOL(오픈 소스), IBM Enterprise COBOL, Micro Focus 및 VS Code 확장은 최신 개발 환경을 제공합니다.`cobc -x program.cob`로 빌드하세요.
---

## 사고 사슬 문제 해결
### 문제 1: 고객 보고서 생성
**1단계: 문제 이해**
고객 기록을 읽고, 총계를 계산하고, 형식화된 보고서를 생성하세요.
**2단계: 접근 방식 파악**
COBOL의 파일 처리 및 보고서 작성 기능을 사용하세요.
**3단계: 구현**```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CUSTREPORT.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  EOF-FLAG        PIC X VALUE 'N'.
       01  GRAND-TOTAL     PIC 9(9)V99 VALUE 0.
       01  CUST-COUNT      PIC 9(5) VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM READ-LOOP
               UNTIL EOF-FLAG = 'Y'
           DISPLAY "Total Customers: " CUST-COUNT
           DISPLAY "Grand Total: " GRAND-TOTAL
           STOP RUN.

       READ-LOOP.
           READ CUST-FILE
               AT END MOVE 'Y' TO EOF-FLAG
               NOT AT END
                   ADD 1 TO CUST-COUNT
                   ADD CUST-BALANCE TO GRAND-TOTAL
                   IF CUST-BALANCE > 10000
                       DISPLAY "High Balance: " CUST-NAME
                           " $" CUST-BALANCE
                   END-IF
           END-READ.
```

**4단계: 확인**
소스 데이터와 비교하여 총계를 교차 확인합니다. 극단적인 경우(빈 파일, 잔액 0)로 테스트합니다.
### 문제 2: 제어 중단을 사용한 일괄 처리
**1단계: 문제 이해**
부서별로 거래를 그룹화하여 소계를 인쇄합니다.
**2단계: 접근 방식 파악**
제어 중단 논리 사용 - 그룹 키가 변경되는 시기를 감지합니다.
**3단계: 구현**```cobol
       PROCESS-TRANSACTIONS.
           MOVE SPACES TO PREV-DEPT
           PERFORM READ-RECORD
           PERFORM UNTIL EOF-FLAG = 'Y'
               IF DEPT NOT = PREV-DEPT
                   PERFORM PRINT-DEPT-TOTAL
                   MOVE DEPT TO PREV-DEPT
                   MOVE 0 TO DEPT-TOTAL
               END-IF
               ADD AMOUNT TO DEPT-TOTAL
               ADD AMOUNT TO GRAND-TOTAL
               PERFORM READ-RECORD
           END-PERFORM
           PERFORM PRINT-DEPT-TOTAL.
```

**4단계: 확인**
마지막 그룹의 합계가 인쇄되는지 확인하세요. 총합계가 부서 총계의 합과 같은지 확인합니다.
---

## 요약
COBOL은 대규모 교체가 불가능하기 때문에 활발하게 사용되고 있는 컴퓨팅 초기 수십 년의 유산입니다. 세계의 은행 및 정부 시스템은 수십 년 동안 안정적으로 운영되어 온 COBOL 프로그램에 의존합니다. 오늘날 새로운 프로젝트에 COBOL이 일반적으로 선택되지는 않지만, 글로벌 금융을 지원하는 인프라를 유지 관리하는 데 언어는 여전히 중요합니다. COBOL 개발자의 부족으로 인해 수익성이 좋은 틈새 시장이 되었습니다.