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
# COBOL
Ang COBOL (Common Business-Oriented Language) ay isa sa mga pinakalumang programming language na ginagamit pa, na unang binuo noong 1959. Idinisenyo ito para sa pagproseso ng data ng negosyo — mga financial system, payroll, banking, insurance, at mga aplikasyon ng gobyerno. Ang tulad-Ingles na syntax ng COBOL ay nilayon upang mabasa ng mga tagapamahala ng negosyo, hindi lamang ng mga programmer.
Sa kabila ng edad nito, pinoproseso ng COBOL ang tinatayang 30% ng lahat ng transaksyon sa negosyo sa buong mundo. Ang mga pangunahing bangko, ahensya ng gobyerno (kabilang ang US Social Security Administration), at mga kompanya ng seguro ay umaasa pa rin sa COBOL mainframe system. Ang Y2K bug scare noong 1999 ay nagdala ng COBOL sa kamalayan ng publiko, at ang wika ay patuloy na nagpapatakbo ng kritikal na imprastraktura sa buong mundo.
---

## Bakit Mahalaga ang COBOL
- **Imprastraktura na kritikal sa negosyo**: Nagpoproseso ng trilyong dolyar sa mga transaksyon araw-araw sa buong pagbabangko at pamahalaan.
- **Stability**: Ang mga programang COBOL na isinulat noong 1970s ay gumagana pa rin ng maaasahan ngayon — kaunting pagbabago ang kailangan.
- **Kakayahang mabasa**: Ang tulad-Ingles na syntax ay ginagawang nauunawaan ng mga hindi programmer ang lohika ng negosyo.
- **Decimal arithmetic**: Katutubong suporta para sa tumpak na mga kalkulasyon sa pananalapi (walang floating-point rounding error).
- **Batch processing**: Idinisenyo para sa pagproseso ng malalaking volume ng mga talaan nang mahusay.
- **Pamilihan ng trabaho**: Ang matinding kakulangan ng mga developer ng COBOL ay lumilikha ng mataas na demand (at mataas na suweldo) para sa mga tungkulin sa pagpapanatili.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Verbose syntax** | Nangangailangan ng maraming linya para sa mga simpleng operasyon | Tanggapin bilang bahagi ng disenyo ng wika |
| **Hindi makabago** | Walang mga klase, walang functional programming, limitadong abstraction | Gamitin para sa pagpapanatili; bumuo ng mga bagong sistema sa mga modernong wika |
| **Mainframe dependency** | Karaniwang tumatakbo sa mga mainframe ng IBM (mahal) | Gumamit ng COBOL compiler sa mga distributed system (GnuCOBOL) |
| **Bumababa ang workforce** | Mas kaunting mga developer ng COBOL na pumapasok sa field | Mataas na demand para sa mga nakakaalam nito; magandang career niche |
| **Walang web/mobile** | Hindi makabuo ng mga modernong application | Gamitin para sa backend batch processing; modernong frontend |
---

## Syntax Fundamentals
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

### Halimbawa ng Pagproseso ng File
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

## Advanced na Syntax at Mga Pattern
### Data Division Deep Dive
Ang paghahati ng data ng COBOL ay ang pinakanatatanging katangian ng wika. Gumagamit ito ng hierarchical numbering system (mga antas 01–88) upang tukuyin ang mga istruktura ng data.
| Antas | Layunin | Halimbawa |
|-------|---------|---------|
| **01** | Record-level na item (top-level variable o record) | `01 WS-EMPLOYEE.`|
| **02–49** | Grupo o elementarya na mga item (sub-field) | `05 EMP-NAME PIC X(30).`|
| **66** | Palitan ang pangalan ng sugnay (alternatibong view ng data) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Standalone elementary item (walang sub-item) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Mga pangalan ng kundisyon (mga flag na parang boolean) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Ang COPY Statement (Mga Copybook)
Ang mga copybook ay mekanismo ng COBOL para sa muling paggamit ng code — katulad ng`#include`sa C. Iniimbak ang mga ito bilang hiwalay na miyembro at inilalagay sa oras ng pag-compile.
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

### MAGAGAWA ng mga Pagkakaiba-iba
Nagbibigay ang COBOL ng ilang lasa ng PERFORM na pahayag para sa structured programming.
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

### Pangangasiwa at Inspeksyon ng String
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

## Arkitektura at Disenyo ng System
### Ang Apat na Dibisyon
Ang bawat programa ng COBOL ay nakabalangkas sa apat na dibisyon, bawat isa ay nagsisilbi sa isang natatanging layunin:
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

### Hierarchy ng Programa
Ang mga COBOL system ay karaniwang gumagamit ng calling hierarchy na may pangunahing program na tumatawag sa mga subprogram.
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

### Karaniwang Istraktura ng Direktoryo ng Proyekto
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

## Project Configuration at Build System
### GnuCOBOL (Open-Source COBOL Compiler)
Kino-compile ng GnuCOBOL (dating OpenCOBOL) ang COBOL sa C at pagkatapos ay sa native machine code, na nagpapagana sa COBOL na tumakbo sa Linux, Windows, at macOS.
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

### IBM Mainframe JCL (Wika ng Kontrol ng Trabaho)
Sa mga mainframe ng IBM, ang mga programa ng COBOL ay pinagsama-sama at isinasagawa gamit ang JCL.
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

### Compiler Options Reference
| Pagpipilian | Paglalarawan | Halimbawa |
|--------|--------------|---------|
| `-free`| Free-format source (walang mga paghihigpit sa column) | `cobc -free prog.cbl`|
| `-fixed`| Fixed-format (tradisyunal na column 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Antas ng pag-optimize 2 | `cobc -O2 prog.cbl`|
| `-g`| Bumuo ng impormasyon sa pag-debug | `cobc -g prog.cbl`|
| `-std=cobol2014`| Gamitin ang pamantayan ng COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Bumuo ng executable (hindi lang mag-compile) | `cobc -x prog.cbl`|
| `-I`| Path ng paghahanap sa copybook | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Paganahin ang lahat ng babala | `cobc -Wall prog.cbl`|
---

## Pagsubok at Pag-debug
### COBOL Debugger Techniques
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

### GnuCOBOL Debugging gamit ang gdb
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

### Mga Karaniwang Pattern ng Pag-debug
| Problema | Sintomas | Solusyon |
|---------|---------|----------|
| Pinutol na data | Naputol ang mga patlang | Suriin ang mga sukat ng sugnay ng PIC na tumutugma sa layout ng talaan |
| Numeric overflow | Mga maling kalkulasyon | I-verify na may sapat na digit ang PIC 9(n) |
| Mga error sa katayuan ng file | WS-FILE-STATUS hindi '00' | Suriin ang mga pangalan ng file DD, mga landas, at mga pahintulot |
| Walang katapusang loop | MAGGANAP HANGGANG hindi kailanman magwawakas | I-verify na ang variable ng loop ay binago sa loob ng loop |
| mga pagkabigo sa TAWAG | BUMALIK na hindi zero | Suriin ang LINKAGE SECTION na tumutugma sa programa ng pagtawag |
---

## Interoperability
### Pahayag ng TAWAG — Pagtawag sa mga Subprogram
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

### C Interoperability (GnuCOBOL)
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

### Pagkakakonekta sa Database (DB2/COBOL)
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

## Mga Pattern ng Disenyo
### Pattern 1: Batch Processing na may Control Break
Ang pattern ng control break ay ang pinakapangunahing pattern ng disenyo ng COBOL — pagpoproseso ng mga talaan na nakapangkat ayon sa isang pangunahing field at gumagawa ng mga subtotal.
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

### Pattern 2: Pattern ng Pag-edit/Pagpapatunay
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

### Pattern 3: Table Lookup (In-Memory Array)
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

## Pagganap at Pag-optimize
### Pag-optimize ng I/O ng File
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

### Batch Processing Optimization
| Teknik | Epekto | Paglalarawan |
|-----------|--------|-------------|
| **Harangan ang I/O** | Mataas | Gamitin ang BLOCK CONTAINS upang bawasan ang mga pisikal na operasyon ng I/O |
| **Naka-index na access** | Mataas | Gumamit ng INDEXED ORGANIZATION para sa random-access lookup |
| **Pagbukud-bukurin/Pagsamahin** | Katamtaman | Gumamit ng SORT verb para sa malalaking pag-order ng dataset |
| **I-minimize ang DISPLAY** | Katamtaman | Ang DISPLAY ay mabagal sa batch; sumulat sa mga file sa halip |
| **COMP/COMP-3** | Katamtaman | Ang binary/packed na mga field ay mas mabilis kaysa sa DISPLAY numeric |
| **Pag-tune ng buffer** | Katamtaman | I-tune ang mga laki ng buffer para sa sequential file processing |
---

## Deployment at Real-World na Paggamit
### Mainframe Deployment (IBM z/OS)
Ang mga programa ng COBOL sa mga mainframe ay naka-deploy bilang mga module ng pag-load sa mga naka-partition na dataset (PDS). Kinokontrol ng JCL ang compilation, linking, at execution.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Naipamahagi na Deployment (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Mga Real-World na Industriya na Gumagamit ng COBOL
| Industriya | Paggamit | Iskala |
|----------|-------|-------|
| **Pagbabangko** | Pagproseso ng transaksyon, pamamahala ng account | Mga proseso ~85% ng mga transaksyon sa ATM |
| **Seguro** | Pangangasiwa ng patakaran, pagproseso ng mga claim | Ang mga pangunahing tagaseguro ay nagpapatakbo ng mga backend ng COBOL |
| **Pamahalaan** | Social Security, pagproseso ng buwis, mga benepisyo | Pinoproseso ng US SSA ang bilyun-bilyong talaan |
| **Pangangalaga sa kalusugan** | Mga talaan ng pasyente, mga sistema ng pagsingil | Legacy na mga sistema ng impormasyon sa ospital |
| **Tingi** | Pamamahala ng imbentaryo, mga backend ng point-of-sale | Mga malalaking retailer na may mga legacy system |
| **Telecom** | Mga sistema ng pagsingil, pagpoproseso ng record ng tawag | Pagproseso ng rekord ng detalye ng tawag |
---

## Kailan Gamitin ang COBOL
| Sitwasyon | Bakit COBOL | Mas mahusay na Alternatibo |
|----------|----------|-------------------|
| Pagpapanatili ng mainframe | Umiiral na codebase | — |
| Batch pinansiyal na pagproseso | Napatunayan, maaasahan, tumpak na decimal math | Java, Python para sa mga bagong system |
| Mga legacy system ng pamahalaan | Umiiral na codebase | — |
| Pag-aaral ng kasaysayan ng computing | Pag-unawa sa ebolusyon ng programming | — |
| Mga bagong aplikasyon sa negosyo | Hindi ang modernong pagpipilian | Java, C#, Python |
| Web/mobile development | Hindi angkop | JavaScript, Swift, Kotlin |
| Data science / ML | Hindi angkop | Python, R |
---

## Synthetic na Q&A
### Q1: Bakit ginagamit pa rin ang COBOL sa pagbabangko pagkatapos ng 60+ na taon?
**A:** Pinoproseso ng COBOL ang tinatayang 70-80% ng mga transaksyon sa pagbabangko. Ang mga dahilan:
- Napakalaking codebase (milyong linya) na gumagana nang tama
- Napakahusay na pagiging maaasahan — ang mga sistemang ito ay nasubok sa produksyon sa loob ng mga dekada
- Ang gastos at panganib ng paglipat ay mas malaki kaysa sa mga gastos sa pagpapanatili
- Ang verbose ng COBOL, tulad ng English na syntax ay self-documenting
- Decimal arithmetic na binuo sa wika (walang floating-point rounding errors)
### Q2: Paano pinangangasiwaan ng COBOL ang decimal arithmetic nang walang mga floating-point error?
**A:** Ang COBOL ay may mga katutubong uri ng decimal na may nakapirming katumpakan:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

Ang`V`ay isang ipinahiwatig na decimal point. Ang COBOL ay hindi kailanman gumagamit ng binary floating-point para sa pera.
### Q3: Ano ang istruktura ng isang COBOL program?
**A:** Ang bawat programa ng COBOL ay may apat na dibisyon:
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

### Q4: Paano ko babasahin at ipoproseso ang mga sunud-sunod na file sa COBOL?
**A:** Napakahusay ng COBOL sa pagproseso ng file:
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

### Q5: Anong mga tool ang magagamit para sa modernong pag-develop ng COBOL?
**A:** Ang mga extension ng GnuCOBOL (open source), IBM Enterprise COBOL, Micro Focus, at VS Code ay nagbibigay ng mga modernong development environment. Bumuo gamit ang`cobc -x program.cob`.
---

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Pagbuo ng Ulat ng Customer
**Hakbang 1: Unawain ang Problema**
Basahin ang mga tala ng customer, kalkulahin ang mga kabuuan, at bumuo ng isang naka-format na ulat.
**Hakbang 2: Tukuyin ang Diskarte**
Gamitin ang paghawak ng file ng COBOL at mga kakayahan sa pagsulat ng ulat.
**Hakbang 3: Ipatupad**```cobol
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

**Hakbang 4: I-verify**
Cross-check ang mga kabuuan laban sa source data. Subukan gamit ang mga edge case (walang laman na file, zero na balanse).
### Problema 2: Batch Processing na may Control Break
**Hakbang 1: Unawain ang Problema**
Iproseso ang mga transaksyon na nakapangkat ayon sa departamento, pag-print ng mga subtotal.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng control break logic — tuklasin kapag nagbago ang key ng grupo.
**Hakbang 3: Ipatupad**```cobol
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

**Hakbang 4: I-verify**
Suriin na ang kabuuan ng huling pangkat ay naka-print. I-verify na ang grand total ay katumbas ng kabuuan ng mga kabuuan ng departamento.
---

## Buod
Ang COBOL ay isang legacy ng mga unang dekada ng computing na nananatiling aktibong ginagamit dahil ang pagpapalit ay hindi magagawa sa sukat. Ang mga sistema ng pagbabangko at gobyerno sa mundo ay umaasa sa mga programa ng COBOL na maaasahang tumatakbo sa loob ng mga dekada. Bagama't karaniwang hindi pipiliin ang COBOL para sa isang bagong proyekto ngayon, nananatiling mahalaga ang wika para sa pagpapanatili ng imprastraktura na sumusuporta sa pandaigdigang pananalapi. Ang kakulangan ng mga developer ng COBOL ay ginagawa itong isang kapaki-pakinabang na angkop na lugar.