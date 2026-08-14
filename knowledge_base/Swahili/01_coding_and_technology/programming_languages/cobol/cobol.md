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
COBOL (Lugha ya Kawaida inayolenga Biashara) ni mojawapo ya lugha kongwe zaidi za upangaji ambazo bado inatumika, iliyotengenezwa kwa mara ya kwanza mnamo 1959. Iliundwa kwa ajili ya usindikaji wa data ya biashara - mifumo ya kifedha, malipo, benki, bima, na maombi ya serikali. Sintaksia inayofanana na Kiingereza ya COBOL ilikusudiwa kusomeka na wasimamizi wa biashara, si watayarishaji programu pekee.
Licha ya umri wake, COBOL huchakata takriban 30% ya miamala yote ya biashara ulimwenguni. Benki kuu, mashirika ya serikali (ikiwa ni pamoja na Utawala wa Usalama wa Jamii wa Marekani), na makampuni ya bima bado yanategemea mifumo ya mfumo mkuu wa COBOL. Hofu ya mdudu wa Y2K mnamo 1999 ilileta COBOL katika ufahamu wa umma, na lugha inaendelea kutekeleza miundombinu muhimu ulimwenguni kote.
---

## Kwa nini COBOL Ni Muhimu
- **Miundombinu muhimu kwa biashara**: Huchakata matrilioni ya dola katika miamala kila siku kwenye benki na serikali.
- **Uthabiti**: Programu za COBOL zilizoandikwa miaka ya 1970 bado zinafanya kazi kwa uhakika leo - mabadiliko machache yanahitajika.
- **Usomaji**: Sintaksia inayofanana na Kiingereza hufanya mantiki ya biashara kueleweka kwa wasio watayarishaji programu.
- **Hesabu ya decimal**: Usaidizi wa asili kwa hesabu sahihi za kifedha (hakuna makosa ya kuzunguka kwa pointi zinazoelea).
- **Uchakataji wa kundi**: Imeundwa kwa ajili ya kuchakata rekodi nyingi kwa ufanisi.
- **Soko la nafasi za kazi**: Upungufu mkubwa wa wasanidi wa COBOL husababisha mahitaji makubwa (na mishahara mikubwa) kwa majukumu ya matengenezo.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Sintaksia ya kitenzi** | Inahitaji mistari mingi kwa shughuli rahisi | Kubali kama sehemu ya muundo wa lugha |
| **Si ya kisasa** | Hakuna madarasa, hakuna utendakazi wa programu, vifupisho vichache | Tumia kwa matengenezo; tengeneza mifumo mipya katika lugha za kisasa |
| **Utegemezi wa mfumo mkuu** | Kwa kawaida hutumika kwenye fremu kuu za IBM (ghali) | Tumia vikusanyaji vya COBOL kwenye mifumo iliyosambazwa (GnuCOBOL) |
| **Kupungua kwa nguvu kazi** | Watengenezaji wachache wa COBOL wanaoingia kwenye uwanja | Mahitaji makubwa kwa wale wanaoijua; kazi nzuri niche |
| **Hakuna mtandao/simu** | Haiwezi kuunda programu za kisasa | Tumia kwa usindikaji wa batch ya nyuma; mbele za kisasa |
---

## Misingi ya Sintaksia
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

### Mfano wa Kuchakata Faili
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

## Sintaksia na Miundo ya Kina
### Data Division Deep Dive
Mgawanyiko wa data wa COBOL ndio sifa bainifu zaidi ya lugha. Inatumia mfumo wa kuweka nambari wa daraja (viwango vya 01-88) kufafanua miundo ya data.
| Kiwango | Kusudi | Mfano |
|-------|--------------------|
| **01** | Kipengee cha kiwango cha rekodi (kigeu cha kiwango cha juu au rekodi) | `01 WS-EMPLOYEE.`|
| **02–49** | Kikundi au vitu vya msingi (sehemu ndogo) | `05 EMP-NAME PIC X(30).`|
| **66** | Badilisha jina la kifungu (mwonekano mbadala wa data) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Kipengee cha msingi cha kujitegemea (hakuna vipengee vidogo) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Majina ya masharti (bendera zinazofanana na boolean) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Taarifa ya NAKALA (Vitabu vya nakala)
Vitabu vya nakala ni utaratibu wa COBOL wa kutumia tena msimbo - sawa na`#include`katika C. Huhifadhiwa kama wanachama tofauti na kuingizwa kwa wakati wa mkusanyiko.
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

### FANYA Tofauti
COBOL hutoa ladha kadhaa za taarifa ya PERFORM kwa upangaji programu.
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

### Ushughulikiaji na Ukaguzi wa Kamba
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

## Usanifu na Usanifu wa Mfumo
### Divisheni Nne
Kila mpango wa COBOL umeundwa katika sehemu nne, kila moja ikitumikia kusudi tofauti:
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

### Hierarkia ya Programu
Mifumo ya COBOL kwa kawaida hutumia daraja la kupiga simu na programu kuu inayoita programu ndogo.
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

### Muundo wa Kawaida wa Saraka ya Mradi
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### GnuCOBOL (Mkusanyaji wa Chanzo Huria wa COBOL)
GnuCOBOL (zamani OpenCOBOL) hukusanya COBOL hadi C na kisha kwa msimbo asili wa mashine, kuwezesha COBOL kufanya kazi kwenye Linux, Windows, na macOS.
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

### IBM Mainframe JCL (Lugha ya Kudhibiti Kazi)
Kwenye mifumo kuu ya IBM, programu za COBOL hutungwa na kutekelezwa kwa kutumia JCL.
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

### Marejeleo ya Chaguo za Mkusanyaji
| Chaguo | Maelezo | Mfano |
|--------|-------------|----------|
| `-free`| Chanzo cha umbizo lisilolipishwa (hakuna vizuizi vya safu wima) | `cobc -free prog.cbl`|
| `-fixed`| Umbizo lisilobadilika (safu wima 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Kiwango cha 2 cha uboreshaji | `cobc -O2 prog.cbl`|
| `-g`| Tengeneza maelezo ya utatuzi | `cobc -g prog.cbl`|
| `-std=cobol2014`| Tumia kiwango cha COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Jenga inayoweza kutekelezwa (sio tu kukusanya) | `cobc -x prog.cbl`|
| `-I`| Njia ya utafutaji ya kitabu cha nakala | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Washa maonyo yote | `cobc -Wall prog.cbl`|
---

## Majaribio na Utatuzi
### Mbinu za Kitatuzi cha COBOL
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

### Utatuzi wa GnuCOBOL na gdb
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

### Miundo ya Kawaida ya Utatuzi
| Tatizo | Dalili | Suluhisho |
|---------|---------------------|
| Data iliyopunguzwa | Mashamba yamekatwa | Angalia ukubwa wa kifungu cha PIC kinacholingana na mpangilio wa rekodi |
| Kufurika kwa nambari | Hesabu zisizo sahihi | Thibitisha PIC 9(n) ina tarakimu za kutosha |
| Hitilafu za hali ya faili | WS-FILE-STATUS sio '00' | Angalia majina ya faili za DD, njia, na ruhusa |
| Kitanzi kisicho na kikomo | FANYA MPAKA kamwe isitishe | Thibitisha utofauti wa kitanzi umebadilishwa ndani ya kitanzi |
| KUPIGA SIMU kufeli | KURUDISHA zisizo sifuri | Angalia mpango wa kupiga simu unaolingana na LINKAGE SECTION |
---

## Kuingiliana
### Taarifa ya SIMU - Programu Ndogo za Kupiga simu
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

### C Kuingiliana (GnuCOBOL)
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

### Muunganisho wa Hifadhidata (DB2/COBOL)
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

## Miundo ya Kubuni
### Mchoro wa 1: Uchakataji wa Bechi kwa Vipindi vya Udhibiti
Mchoro wa uvunjaji wa udhibiti ndio muundo msingi zaidi wa muundo wa COBOL - rekodi za usindikaji zilizopangwa kulingana na sehemu kuu na kutoa jumla ndogo.
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

### Mchoro wa 2: Badilisha/Uthibitishaji Muundo
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

### Mchoro wa 3: Utafutaji wa Jedwali (Safu ya Kumbukumbu)
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

## Utendaji na Uboreshaji
### Uboreshaji wa Faili ya I/O
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

### Uboreshaji wa Kuchakata Bechi
| Mbinu | Athari | Maelezo |
|-----------|--------|-------------|
| **Zuia I/O** | Juu | Tumia BLOCK CONTAINS ili kupunguza shughuli halisi za I/O |
| **Ufikiaji uliowekwa kwenye faharasa** | Juu | Tumia INDEXED ORGANIZATION kwa utafutaji wa ufikiaji bila mpangilio |
| **Panga/Unganisha** | Kati | Tumia kitenzi cha SORT kwa upangaji wa mkusanyiko mkubwa wa data |
| **Punguza ONYESHO** | Kati | DISPLAY ni polepole katika kundi; andika kwa faili badala yake |
| **COMP/COMP-3** | Kati | Sehemu jozi/zilizojaa ni haraka kuliko nambari ya DISPLAY |
| **Urekebishaji wa akiba** | Kati | Rekebisha saizi za bafa kwa uchakataji mfuatano wa faili |
---

## Usambazaji na Matumizi Halisi ya Ulimwenguni
### Usambazaji wa Mfumo Mkuu (IBM z/OS)
Programu za COBOL kwenye fremu kuu huwekwa kama moduli za upakiaji katika hifadhidata zilizogawanywa (PDS). JCL inadhibiti utungaji, kuunganisha, na utekelezaji.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Usambazaji Uliosambazwa (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Viwanda Halisi vya Ulimwengu Vinavyotumia COBOL
| Viwanda | Matumizi | Kiwango |
|----------|----------------|
| **Benki** | Usindikaji wa shughuli, usimamizi wa akaunti | Huchakata ~85% ya miamala ya ATM |
| **Bima** | Usimamizi wa sera, usindikaji wa madai | Bima wakuu huendesha huduma za nyuma za COBOL |
| **Serikali** | Usalama wa Jamii, usindikaji wa kodi, faida | SSA ya Marekani huchakata mabilioni ya rekodi |
| **Huduma za afya** | Rekodi za wagonjwa, mifumo ya malipo | Mifumo ya taarifa za hospitali za urithi |
| **Reja reja** | Usimamizi wa hesabu, sehemu za nyuma za mauzo | Wauzaji wakubwa na mifumo ya urithi |
| **Simu** | Mifumo ya bili, usindikaji wa rekodi za simu | Uchakataji wa rekodi ya maelezo ya simu |
---

## Wakati wa kutumia COBOL
| Hali | Kwa nini COBOL | Mbadala Bora |
|----------|----------|-------------------|
| Matengenezo ya mfumo mkuu | Codebase iliyopo | - |
| Usindikaji wa fedha wa kundi | Imethibitishwa, ya kuaminika, hesabu sahihi ya decimal | Java, Python kwa mifumo mipya |
| Mifumo ya urithi wa serikali | Codebase iliyopo | - |
| Kujifunza historia ya kompyuta | Kuelewa mageuzi ya programu | - |
| Maombi mapya ya biashara | Sio chaguo la kisasa | Java, C#, Python |
| Ukuzaji wa wavuti/simu | Haifai | JavaScript, Swift, Kotlin |
| Sayansi ya data / ML | Haifai | Chatu, R |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kwa nini COBOL bado inatumika katika benki baada ya miaka 60+?
**Jibu:** COBOL huchakata makadirio ya 70-80% ya miamala ya benki. Sababu:
- Codebases kubwa (mamilioni ya mistari) ambayo hufanya kazi kwa usahihi
- Kuegemea sana - mifumo hii imejaribiwa katika uzalishaji kwa miongo kadhaa
- Gharama na hatari ya uhamiaji inazidi gharama za matengenezo
- Kitenzi cha COBOL, sintaksia inayofanana na Kiingereza inajiandikisha
- Hesabu ya decimal iliyojumuishwa katika lugha (hakuna makosa ya kuzunguka kwa sehemu zinazoelea)
### Q2: COBOL hushughulikia vipi hesabu za desimali bila makosa ya sehemu zinazoelea?
**J:** COBOL ina aina za desimali asilia zilizo na usahihi usiobadilika:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` ni nukta ya desimali iliyodokezwa. COBOL kamwe haitumii sehemu ya kuelea ya binary kupata pesa.
### Q3: Muundo wa mpango wa COBOL ni upi?
**J:** Kila mpango wa COBOL una sehemu nne:
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

### Q4: Je, ninasomaje na kuchakata faili zinazofuatana katika COBOL?
**J:** COBOL inafaulu katika uchakataji wa faili:
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

### Q5: Ni zana gani zinapatikana kwa maendeleo ya kisasa ya COBOL?
**A:** GnuCOBOL (chanzo huria), IBM Enterprise COBOL, Micro Focus, na viendelezi vya Msimbo wa VS hutoa mazingira ya kisasa ya usanidi. Jenga kwa`cobc -x program.cob`.
---

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Kuzalisha Ripoti ya Mteja
**Hatua ya 1: Elewa Tatizo**
Soma rekodi za wateja, hesabu jumla, na utoe ripoti iliyoumbizwa.
**Hatua ya 2: Tambua Mbinu**
Tumia uwezo wa kushughulikia faili za COBOL na kuandika ripoti.
**Hatua ya 3: Tekeleza**```cobol
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

**Hatua ya 4: Thibitisha**
Kagua jumla dhidi ya data chanzo. Jaribu na kesi za makali (faili tupu, salio sifuri).
### Tatizo la 2: Uchakataji wa Bechi kwa Vipunguzo vya Kudhibiti
**Hatua ya 1: Elewa Tatizo**
Mchakato wa shughuli zilizopangwa kulingana na idara, jumla ndogo za uchapishaji.
**Hatua ya 2: Tambua Mbinu**
Tumia mantiki ya kukatika kwa udhibiti - tambua wakati kitufe cha kikundi kinabadilika.
**Hatua ya 3: Tekeleza**```cobol
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

**Hatua ya 4: Thibitisha**
Hakikisha kuwa jumla ya kikundi cha mwisho imechapishwa. Thibitisha jumla ya jumla ya jumla ya jumla ya jumla ya idara.
---

## Muhtasari
COBOL ni urithi wa miongo ya mapema ya kompyuta ambayo inasalia kutumika kwa sababu ubadilishaji hauwezekani kwa kiwango kikubwa. Mifumo ya benki na serikali duniani inategemea programu za COBOL ambazo zimeendeshwa kwa uhakika kwa miongo kadhaa. Ingawa COBOL isingechaguliwa kwa kawaida kwa mradi mpya leo, lugha inasalia kuwa muhimu kwa kudumisha miundombinu inayotumia fedha za kimataifa. Upungufu wa watengenezaji wa COBOL hufanya iwe niche yenye faida.