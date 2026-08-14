---
# Metadata
title: "COBOL"
description: "Comprehensive reference for the COBOL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# COBOL
COBOL (Common Business-Oriented Language) ist eine der ältesten noch verwendeten Programmiersprachen und wurde erstmals 1959 entwickelt. Sie wurde für die Verarbeitung von Geschäftsdaten entwickelt – Finanzsysteme, Gehaltsabrechnung, Banken, Versicherungen und Regierungsanwendungen. Die englischähnliche Syntax von COBOL sollte für Unternehmensmanager und nicht nur für Programmierer lesbar sein.
Trotz seines Alters verarbeitet COBOL schätzungsweise 30 % aller Geschäftstransaktionen weltweit. Große Banken, Regierungsbehörden (einschließlich der US-amerikanischen Sozialversicherungsbehörde) und Versicherungsunternehmen verlassen sich immer noch auf COBOL-Mainframe-Systeme. Die Y2K-Bug-Angst im Jahr 1999 brachte COBOL wieder ins öffentliche Bewusstsein, und die Sprache betreibt weiterhin weltweit kritische Infrastrukturen.
---

## Warum COBOL wichtig ist
- **Geschäftskritische Infrastruktur**: Verarbeitet täglich Billionen von Dollar an Transaktionen im Banken- und Regierungsbereich.
- **Stabilität**: COBOL-Programme, die in den 1970er Jahren geschrieben wurden, laufen auch heute noch zuverlässig – nur minimale Änderungen erforderlich.
- **Lesbarkeit**: Eine englischähnliche Syntax macht die Geschäftslogik auch für Nicht-Programmierer verständlich.
- **Dezimalarithmetik**: Native Unterstützung für präzise Finanzberechnungen (keine Gleitkomma-Rundungsfehler).
- **Stapelverarbeitung**: Entwickelt für die effiziente Verarbeitung großer Datensatzmengen.
- **Arbeitsmarkt**: Der starke Mangel an COBOL-Entwicklern führt zu einer hohen Nachfrage (und hohen Gehältern) nach Wartungsrollen.
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Ausführliche Syntax** | Erfordert viele Zeilen für einfache Operationen | Als Teil des Sprachdesigns akzeptieren |
| **Nicht modern** | Keine Klassen, keine funktionale Programmierung, begrenzte Abstraktionen | Zur Wartung verwenden; Erstellen Sie neue Systeme in modernen Sprachen |
| **Mainframe-Abhängigkeit** | Läuft normalerweise auf IBM-Mainframes (teuer) | Verwenden Sie COBOL-Compiler auf verteilten Systemen (GnuCOBOL) |
| **Rückgang der Belegschaft** | Weniger COBOL-Entwickler betreten das Feld | Hohe Nachfrage für diejenigen, die es wissen; gute Karrierenische |
| **Kein Web/Mobilgerät** | Moderne Anwendungen können nicht erstellt werden | Verwendung für die Backend-Stapelverarbeitung; moderne Frontends |
---

## Syntax-Grundlagen
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

### Beispiel für die Dateiverarbeitung
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

## Erweiterte Syntax und Muster
### Deep Dive zur Datenabteilung
Die Datenaufteilung von COBOL ist das markanteste Merkmal der Sprache. Es verwendet ein hierarchisches Nummerierungssystem (Ebenen 01–88), um Datenstrukturen zu definieren.
| Ebene | Zweck | Beispiel |
|-------|---------|---------|
| **01** | Element auf Datensatzebene (Variable oder Datensatz der obersten Ebene) | `01 WS-EMPLOYEE.`|
| **02–49** | Gruppen- oder Elementarelemente (Unterfelder) | `05 EMP-NAME PIC X(30).`|
| **66** | Umbenennungsklausel (alternative Datenansicht) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Eigenständiges Elementarelement (keine Unterelemente) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Bedingungsnamen (boolesche Flags) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Die COPY-Anweisung (Copybooks)
Copybooks sind COBOLs Mechanismus zur Wiederverwendung von Code – ähnlich wie`#include`in C. Sie werden als separate Mitglieder gespeichert und zur Kompilierungszeit eingefügt.
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

### PERFORM-Variationen
COBOL bietet verschiedene Varianten der PERFORM-Anweisung für die strukturierte Programmierung.
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

### Saitenhandhabung und -inspektion
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

## Architektur und Systemdesign
### Die vier Divisionen
Jedes COBOL-Programm ist in vier Abteilungen gegliedert, die jeweils einem bestimmten Zweck dienen:
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

### Programmhierarchie
COBOL-Systeme verwenden typischerweise eine Aufrufhierarchie mit einem Hauptprogramm, das Unterprogramme aufruft.
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

### Typische Projektverzeichnisstruktur
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

## Projektkonfiguration und Build-System
### GnuCOBOL (Open-Source-COBOL-Compiler)
GnuCOBOL (ehemals OpenCOBOL) kompiliert COBOL in C und dann in nativen Maschinencode, sodass COBOL unter Linux, Windows und macOS ausgeführt werden kann.
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

### IBM Mainframe JCL (Job Control Language)
Auf IBM-Mainframes werden COBOL-Programme mit JCL kompiliert und ausgeführt.
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

### Compiler-Optionen-Referenz
| Option | Beschreibung | Beispiel |
|--------|-------------|---------|
| `-free`| Freiformatige Quelle (keine Spaltenbeschränkungen) | `cobc -free prog.cbl`|
| `-fixed`| Festes Format (traditionelle Spalten 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Optimierungsstufe 2 | `cobc -O2 prog.cbl`|
| `-g`| Debug-Informationen generieren | `cobc -g prog.cbl`|
| `-std=cobol2014`| Verwenden Sie den COBOL 2014-Standard | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Ausführbare Datei erstellen (nicht nur kompilieren) | `cobc -x prog.cbl`|
| `-I`| Copybook-Suchpfad | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Alle Warnungen aktivieren | `cobc -Wall prog.cbl`|
---

## Testen und Debuggen
### COBOL-Debugger-Techniken
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

### GnuCOBOL-Debugging mit GDB
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

### Gängige Debugging-Muster
| Problem | Symptom | Lösung |
|---------|---------|----------|
| Gekürzte Daten | Abgeschnittene Felder | Überprüfen Sie, ob die PIC-Klauselgrößen mit dem Datensatzlayout übereinstimmen |
| Numerischer Überlauf | Falsche Berechnungen | Stellen Sie sicher, dass PIC 9(n) über genügend Ziffern verfügt |
| Dateistatusfehler | WS-FILE-STATUS nicht '00' | Datei-DD-Namen, Pfade und Berechtigungen prüfen |
| Endlosschleife | PERFORM UNTIL endet nie | Überprüfen Sie, ob die Schleifenvariable innerhalb der Schleife | geändert wurde
| CALL-Fehler | RETURNING ungleich Null | Überprüfen Sie, ob LINKAGE SECTION mit dem aufrufenden Programm | übereinstimmt
---

## Interoperabilität
### CALL-Anweisung – Aufrufen von Unterprogrammen
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

### C-Interoperabilität (GnuCOBOL)
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

### Datenbankkonnektivität (DB2/COBOL)
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

## Designmuster
### Muster 1: Stapelverarbeitung mit Kontrollunterbrechungen
Das Kontrollunterbrechungsmuster ist das grundlegendste COBOL-Entwurfsmuster – es verarbeitet Datensätze, die nach einem Schlüsselfeld gruppiert sind, und erstellt Zwischensummen.
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

### Muster 2: Bearbeitungs-/Validierungsmuster
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

### Muster 3: Tabellensuche (In-Memory-Array)
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

## Leistung und Optimierung
### Datei-I/O-Optimierung
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

### Optimierung der Stapelverarbeitung
| Technik | Auswirkungen | Beschreibung |
|-----------|--------|-------------|
| **Block-E/A** | Hoch | Verwenden Sie BLOCK CONTAINS, um physische E/A-Vorgänge zu reduzieren |
| **Indizierter Zugriff** | Hoch | Verwenden Sie INDEXED ORGANIZATION für Suchvorgänge mit wahlfreiem Zugriff |
| **Sortieren/Zusammenführen** | Mittel | Verwenden Sie das SORT-Verb für die Reihenfolge großer Datensätze |
| **ANZEIGE minimieren** | Mittel | DISPLAY ist im Batch langsam; stattdessen in Dateien schreiben |
| **COMP/COMP-3** | Mittel | Binäre/gepackte Felder sind schneller als DISPLAY numeric |
| **Pufferoptimierung** | Mittel | Puffergrößen für sequentielle Dateiverarbeitung optimieren |
---

## Bereitstellung und reale Nutzung
### Mainframe-Bereitstellung (IBM z/OS)
COBOL-Programme auf Mainframes werden als Lademodule in partitionierten Datensätzen (PDS) bereitgestellt. JCL steuert die Kompilierung, Verknüpfung und Ausführung.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Verteilte Bereitstellung (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Reale Branchen mit COBOL
| Industrie | Verwendung | Maßstab |
|----------|-------|-------|
| **Bankwesen** | Transaktionsabwicklung, Kontoverwaltung | Verarbeitet ca. 85 % der Geldautomatentransaktionen |
| **Versicherung** | Policenverwaltung, Schadensbearbeitung | Große Versicherer betreiben COBOL-Backends |
| **Regierung** | Sozialversicherung, Steuerabwicklung, Sozialleistungen | US SSA verarbeitet Milliarden von Datensätzen |
| **Gesundheitswesen** | Patientenakten, Abrechnungssysteme | Ältere Krankenhausinformationssysteme |
| **Einzelhandel** | Bestandsverwaltung, Point-of-Sale-Backends | Große Einzelhändler mit Altsystemen |
| **Telekommunikation** | Abrechnungssysteme, Anrufdatenverarbeitung | Verarbeitung von Anrufdetaildatensätzen |
---

## Wann sollte COBOL verwendet werden?
| Szenario | Warum COBOL | Bessere Alternative |
|----------|----------|-----|
| Mainframe-Wartung | Vorhandene Codebasis | — |
| Batch-Finanzverarbeitung | Bewährte, zuverlässige und präzise Dezimalberechnung | Java, Python für neue Systeme |
| Legacy-Systeme der Regierung | Vorhandene Codebasis | — |
| Computergeschichte lernen | Die Entwicklung der Programmierung verstehen | — |
| Neue Geschäftsanwendungen | Nicht die moderne Wahl | Java, C#, Python |
| Web-/mobile Entwicklung | Nicht geeignet | JavaScript, Swift, Kotlin |
| Datenwissenschaft / ML | Nicht geeignet | Python, R |
---

## Zusammenfassung
COBOL ist ein Erbe der frühen Jahrzehnte des Computerwesens, das aktiv genutzt wird, weil ein Ersatz in großem Maßstab nicht machbar ist. Die Banken- und Regierungssysteme der Welt sind auf COBOL-Programme angewiesen, die seit Jahrzehnten zuverlässig laufen. Obwohl COBOL heute typischerweise nicht für ein neues Projekt gewählt würde, bleibt die Sprache wichtig für die Aufrechterhaltung der Infrastruktur, die die globalen Finanzen unterstützt. Der Mangel an COBOL-Entwicklern macht es zu einer lukrativen Nische.