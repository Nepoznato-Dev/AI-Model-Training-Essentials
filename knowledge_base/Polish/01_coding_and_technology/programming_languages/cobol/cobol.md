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
#COBOL
COBOL (Common Business-Oriented Language) to jeden z najstarszych wciąż używanych języków programowania, opracowany po raz pierwszy w 1959 roku. Został zaprojektowany do przetwarzania danych biznesowych — systemów finansowych, płacowych, bankowych, ubezpieczeniowych i aplikacji rządowych. Składnia języka COBOL przypominająca angielską miała być czytelna dla menedżerów biznesowych, a nie tylko programistów.
Pomimo swojego wieku COBOL przetwarza szacunkowo 30% wszystkich transakcji biznesowych na całym świecie. Największe banki, agencje rządowe (w tym amerykańska administracja zabezpieczenia społecznego) i firmy ubezpieczeniowe w dalszym ciągu polegają na systemach mainframe COBOL. Strach przed błędami Y2K w 1999 r. przywrócił język COBOL do świadomości społecznej, a język ten w dalszym ciągu obsługuje infrastrukturę krytyczną na całym świecie.
---

## Dlaczego COBOL ma znaczenie
- **Infrastruktura o znaczeniu krytycznym**: codziennie przetwarza transakcje o wartości bilionów dolarów w bankach i instytucjach rządowych.
- **Stabilność**: programy w języku COBOL napisane w latach 70. XX wieku nadal działają niezawodnie — potrzebne są minimalne zmiany.
- **Czytelność**: składnia przypominająca angielską sprawia, że ​​logika biznesowa jest zrozumiała dla osób niebędących programistami.
- **Arytmetyka dziesiętna**: Natywna obsługa precyzyjnych obliczeń finansowych (brak błędów zaokrągleń zmiennoprzecinkowych).
- **Przetwarzanie wsadowe**: Zaprojektowane do wydajnego przetwarzania dużych ilości rekordów.
- **Rynek pracy**: Poważny niedobór programistów COBOL powoduje wysoki popyt (i wysokie wynagrodzenia) na stanowiska konserwacyjne.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Rozszerzona składnia** | Wymaga wielu linii do prostych operacji | Zaakceptuj jako część projektu języka |
| **Nie nowoczesny** | Żadnych klas, żadnego programowania funkcjonalnego, ograniczone abstrakcje | Używać do konserwacji; budować nowe systemy w językach nowożytnych |
| **Zależność od komputera głównego** | Zwykle działa na komputerach mainframe IBM (drogie) | Używaj kompilatorów COBOL w systemach rozproszonych (GnuCOBOL) |
| **Spadek zatrudnienia** | Mniej programistów COBOL wchodzących na rynek | Wysoki popyt na tych, którzy to wiedzą; dobra nisza zawodowa |
| **Brak internetu/urządzenia mobilnego** | Nie można tworzyć nowoczesnych aplikacji | Użyj do przetwarzania wsadowego zaplecza; nowoczesne frontendy |
---

## Podstawy składni
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

### Przykład przetwarzania plików
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

## Zaawansowana składnia i wzorce
### Głębokie nurkowanie w dziale danych
Podział danych w języku COBOL jest najbardziej charakterystyczną cechą tego języka. Do definiowania struktur danych wykorzystuje hierarchiczny system numeracji (poziomy 01–88).
| Poziom | Cel | Przykład |
|-------|---------|--------|
| **01** | Element na poziomie rekordu (zmienna lub rekord najwyższego poziomu) | `01 WS-EMPLOYEE.`|
| **02–49** | Pozycje grupowe lub elementarne (podpola) | `05 EMP-NAME PIC X(30).`|
| **66** | Klauzula zmiany nazwy (alternatywny widok danych) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Samodzielny element podstawowy (bez elementów podrzędnych) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Nazwy warunków (flagi typu logicznego) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Oświadczenie COPY (zeszyty)
Zeszyty to mechanizm języka COBOL umożliwiający ponowne wykorzystanie kodu — podobny do`#include`w C. Są one przechowywane jako osobne elementy i wstawiane w czasie kompilacji.
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

### WYKONAJ wariacje
W języku COBOL dostępnych jest kilka odmian instrukcji PERFORM do programowania strukturalnego.
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

### Obsługa i kontrola ciągów
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

## Architektura i projektowanie systemów
### Cztery dywizje
Każdy program w języku COBOL jest podzielony na cztery sekcje, z których każda służy innemu celowi:
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

### Hierarchia programów
Systemy COBOL zazwyczaj korzystają z hierarchii wywołań z programem głównym, który wywołuje podprogramy.
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

### Typowa struktura katalogu projektu
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

## Konfiguracja projektu i budowanie systemu
### GnuCOBOL (kompilator języka COBOL o otwartym kodzie źródłowym)
GnuCOBOL (dawniej OpenCOBOL) kompiluje język COBOL do języka C, a następnie do natywnego kodu maszynowego, umożliwiając działanie języka COBOL w systemach Linux, Windows i macOS.
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

### IBM Mainframe JCL (język kontroli zadań)
Na komputerach mainframe IBM programy w języku COBOL są kompilowane i wykonywane przy użyciu języka JCL.
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

### Informacje o opcjach kompilatora
| Opcja | Opis | Przykład |
|------------|------------|--------|
| `-free`| Źródło w dowolnym formacie (bez ograniczeń dotyczących kolumn) | `cobc -free prog.cbl`|
| `-fixed`| Stały format (tradycyjne kolumny 1–80) | `cobc -fixed prog.cbl`|
| `-O2`| Poziom optymalizacji 2 | `cobc -O2 prog.cbl`|
| `-g`| Generuj informacje debugowania | `cobc -g prog.cbl`|
| `-std=cobol2014`| Użyj standardu COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Zbuduj plik wykonywalny (nie tylko skompiluj) | `cobc -x prog.cbl`|
| `-I`| Ścieżka wyszukiwania zeszytu | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Włącz wszystkie ostrzeżenia | `cobc -Wall prog.cbl`|
---

## Testowanie i debugowanie
### Techniki debugowania języka COBOL
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

### Debugowanie GnuCOBOL za pomocą gdb
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

### Typowe wzorce debugowania
| Problem | Objaw | Rozwiązanie |
|--------|---------|---------|
| Obcięte dane | Pola odcięte | Sprawdź, czy rozmiary klauzuli PIC odpowiadają układowi rekordu |
| Przepełnienie numeryczne | Błędne obliczenia | Sprawdź, czy PIC 9(n) ma wystarczającą liczbę cyfr |
| Błędy statusu pliku | STATUS-PLIKU WS nie '00' | Sprawdź nazwy plików DD, ścieżki i uprawnienia |
| Nieskończona pętla | PERFORM aż nigdy się nie kończy | Sprawdź, czy zmienna pętli została zmodyfikowana wewnątrz pętli |
| Niepowodzenie połączeń | ZWRACANIE niezerowe | Sprawdź SEKCJA POŁĄCZENIA odpowiada programowi wywołującemu |
---

## Interoperacyjność
### Instrukcja CALL — wywoływanie podprogramów
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

### Interoperacyjność C (GnuCOBOL)
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

### Łączność z bazą danych (DB2/COBOL)
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

## Wzorce projektowe
### Wzorzec 1: Przetwarzanie wsadowe z przerwami w kontroli
Wzorzec przerwania kontroli jest najbardziej podstawowym wzorcem projektowym języka COBOL — przetwarzanie rekordów pogrupowanych według pól kluczowych i tworzenie sum częściowych.
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

### Wzorzec 2: Wzorzec edycji/weryfikacji
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

### Wzorzec 3: Przeszukiwanie tabeli (tablica w pamięci)
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

## Wydajność i optymalizacja
### Optymalizacja we/wy pliku
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

### Optymalizacja przetwarzania wsadowego
| Technika | Wpływ | Opis |
|---------------|--------|------------|
| **Blokuj wejścia/wyjścia** | Wysoki | Użyj BLOK ZAWIERA, aby ograniczyć fizyczne operacje we/wy |
| **Dostęp indeksowany** | Wysoki | Użyj INDEKSOWANEJ ORGANIZACJI do wyszukiwań o dostępie swobodnym |
| **Sortuj/Scal** | Średni | Użyj czasownika SORT, aby uporządkować duży zbiór danych |
| **Minimalizuj WYŚWIETLANIE** | Średni | WYŚWIETLANIE jest powolne w partii; zamiast tego zapisuj do plików |
| **KOMP/KOMP-3** | Średni | Pola binarne/spakowane są szybsze niż numeryczne DISPLAY |
| **Strojenie bufora** | Średni | Dostosuj rozmiary buforów do sekwencyjnego przetwarzania plików |
---

## Wdrożenie i użytkowanie w świecie rzeczywistym
### Wdrożenie na komputerze mainframe (IBM z/OS)
Programy w języku COBOL na komputerach mainframe są wdrażane jako moduły ładujące w partycjonowanych zbiorach danych (PDS). JCL kontroluje kompilację, łączenie i wykonywanie.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Wdrożenie rozproszone (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Rzeczywiste branże korzystające z języka COBOL
| Przemysł | Użycie | Skala |
|---------|-------|-------|
| **Bankowość** | Przetwarzanie transakcji, zarządzanie kontem | Przetwarza ~85% transakcji bankomatowych |
| **Ubezpieczenie** | Administracja polisami, rozpatrywanie roszczeń | Główni ubezpieczyciele obsługują backendy COBOL |
| **Rząd** | Ubezpieczenie społeczne, przetwarzanie podatków, świadczenia | US SSA przetwarza miliardy rekordów |
| **Opieka zdrowotna** | Dokumentacja pacjentów, systemy bilingowe | Starsze szpitalne systemy informacyjne |
| **Handel detaliczny** | Zarządzanie zapasami, backendy punktów sprzedaży | Duzi sprzedawcy detaliczni ze starszymi systemami |
| **Telekomunikacja** | Systemy bilingowe, przetwarzanie nagrań rozmów | Przetwarzanie rekordu szczegółów połączenia |
---

## Kiedy używać języka COBOL
| Scenariusz | Dlaczego COBOL | Lepsza alternatywa |
|---------|----------|--------------------------------|
| Konserwacja komputera mainframe | Istniejąca baza kodu | — |
| Masowe przetwarzanie finansowe | Sprawdzona, niezawodna i precyzyjna matematyka dziesiętna | Java, Python dla nowych systemów |
| Stare systemy rządowe | Istniejąca baza kodu | — |
| Nauka historii informatyki | Zrozumienie ewolucji programowania | — |
| Nowe aplikacje biznesowe | Nie nowoczesny wybór | Java, C#, Python |
| Tworzenie stron internetowych/mobilnych | Nie nadaje się | JavaScript, Swift, Kotlin |
| Nauka o danych / ML | Nie nadaje się | Python, R |
---

## Syntetyczne pytania i odpowiedzi
### P1: Dlaczego po ponad 60 latach język COBOL jest nadal używany w bankowości?
**O:** COBOL przetwarza szacunkowo 70–80% transakcji bankowych. Powody:
- Ogromne bazy kodu (miliony linii), które działają poprawnie
- Wyjątkowa niezawodność — systemy te są testowane w produkcji od dziesięcioleci
- Koszt i ryzyko migracji przewyższają koszty utrzymania
- Pełna, przypominająca angielską składnię języka COBOL jest samodokumentująca
- Arytmetyka dziesiętna wbudowana w język (brak błędów zaokrąglania zmiennoprzecinkowego)
### P2: Jak język COBOL obsługuje arytmetykę dziesiętną bez błędów zmiennoprzecinkowych?
**A:** COBOL ma natywne typy dziesiętne ze stałą precyzją:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` jest domyślnym punktem dziesiętnym. COBOL nigdy nie używa binarnych liczb zmiennoprzecinkowych do wyrażania pieniędzy.
### P3: Jaka jest struktura programu w języku COBOL?
**A:** Każdy program COBOL ma cztery działy:
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

### P4: Jak czytać i przetwarzać pliki sekwencyjne w języku COBOL?
**A:** COBOL przoduje w przetwarzaniu plików:
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

### P5: Jakie narzędzia są dostępne do nowoczesnego programowania w języku COBOL?
**A:** Rozszerzenia GnuCOBOL (open source), IBM Enterprise COBOL, Micro Focus i VS Code zapewniają nowoczesne środowiska programistyczne. Kompiluj za pomocą`cobc -x program.cob`.
---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Generowanie raportu klienta
**Krok 1: Zrozum problem**
Odczytuj zapisy klientów, obliczaj sumy i generuj sformatowany raport.
**Krok 2: Zidentyfikuj podejście**
Wykorzystaj możliwości obsługi plików i pisania raportów w języku COBOL.
**Krok 3: Wdróż**```cobol
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

**Krok 4: Zweryfikuj**
Sprawdź sumy krzyżowo z danymi źródłowymi. Testuj z przypadkami Edge (pusty plik, salda zerowe).
### Problem 2: Przetwarzanie wsadowe z przerwami w sterowaniu
**Krok 1: Zrozum problem**
Przetwarzaj transakcje pogrupowane według działów, drukując sumy częściowe.
**Krok 2: Zidentyfikuj podejście**
Użyj logiki przerwania kontroli — wykryj zmianę klucza grupy.
**Krok 3: Wdróż**```cobol
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

**Krok 4: Zweryfikuj**
Sprawdź, czy wydrukowana została suma ostatniej grupy. Sprawdź, czy suma całkowita jest równa sumie sum działów.
---

## Streszczenie
Język COBOL to dziedzictwo pierwszych dziesięcioleci informatyki, które pozostaje w aktywnym użyciu, ponieważ wymiana nie jest możliwa na dużą skalę. Światowe systemy bankowe i rządowe zależą od programów w języku COBOL, które działają niezawodnie od dziesięcioleci. Chociaż język COBOL nie byłby obecnie wybierany do nowego projektu, język ten pozostaje ważny dla utrzymania infrastruktury obsługującej globalne finanse. Niedobór programistów COBOL sprawia, że ​​jest to lukratywna nisza.