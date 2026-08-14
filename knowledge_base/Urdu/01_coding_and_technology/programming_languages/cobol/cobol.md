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
# کوبول
COBOL (Common Business-Oriented Language) سب سے قدیم پروگرامنگ زبانوں میں سے ایک ہے جو اب بھی استعمال میں ہے، جو پہلی بار 1959 میں تیار کی گئی تھی۔ اسے کاروباری ڈیٹا پروسیسنگ — مالیاتی نظام، پے رول، بینکنگ، انشورنس، اور سرکاری ایپلی کیشنز کے لیے ڈیزائن کیا گیا تھا۔ COBOL کا انگریزی جیسا نحو صرف پروگرامرز ہی نہیں بلکہ بزنس مینیجرز کے پڑھنے کے قابل تھا۔
اپنی عمر کے باوجود، COBOL عالمی سطح پر تمام کاروباری لین دین کا تخمینہ 30% عمل کرتا ہے۔ بڑے بینک، سرکاری ایجنسیاں (بشمول یو ایس سوشل سیکیورٹی ایڈمنسٹریشن)، اور انشورنس کمپنیاں اب بھی COBOL مین فریم سسٹم پر انحصار کرتی ہیں۔ 1999 میں Y2K بگ ڈراؤ نے COBOL کو عوامی بیداری میں واپس لایا، اور یہ زبان دنیا بھر میں اہم بنیادی ڈھانچے کو چلا رہی ہے۔
---

## کوبول کیوں اہمیت رکھتا ہے۔
- **کاروباری اہم بنیادی ڈھانچہ**: بینکنگ اور حکومت میں روزانہ ٹریلین ڈالر کے لین دین پر کارروائی کرتا ہے۔
- **استحکام**: 1970 کی دہائی میں لکھے گئے COBOL پروگرام آج بھی قابل اعتماد طریقے سے چلتے ہیں - کم سے کم تبدیلیوں کی ضرورت ہے۔
- **پڑھنے کی اہلیت**: انگریزی جیسا نحو کاروباری منطق کو غیر پروگرامرز کے لیے قابل فہم بنا دیتا ہے۔
- **اعشاریہ ریاضی**: درست مالی حسابات کے لیے مقامی تعاون (کوئی فلوٹنگ پوائنٹ راؤنڈنگ غلطیاں نہیں)۔
- **بیچ پروسیسنگ**: ریکارڈز کی بڑی مقدار کو مؤثر طریقے سے پروسیس کرنے کے لیے ڈیزائن کیا گیا ہے۔
- **ملازمت کا بازار**: COBOL ڈویلپرز کی شدید کمی دیکھ بھال کے کرداروں کے لیے زیادہ مانگ (اور زیادہ تنخواہیں) پیدا کرتی ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **وربوز نحو** | سادہ آپریشنز کے لیے بہت سی لائنوں کی ضرورت ہے | زبان کے ڈیزائن کے حصے کے طور پر قبول کریں |
| **جدید نہیں** | کوئی کلاس نہیں، کوئی فنکشنل پروگرامنگ نہیں، محدود تجرید | دیکھ بھال کے لیے استعمال کریں؛ جدید زبانوں میں نئے نظام بنائیں |
| **مین فریم انحصار** | عام طور پر IBM مین فریمز پر چلتا ہے (مہنگا) | تقسیم شدہ نظاموں پر COBOL کمپائلرز استعمال کریں (GnuCOBOL) |
| **کم ہوتی افرادی قوت** | کم COBOL ڈویلپرز فیلڈ میں داخل ہو رہے ہیں | ان لوگوں کے لئے اعلی مطالبہ جو اسے جانتے ہیں؛ اچھا کیریئر طاق |
| **کوئی ویب/موبائل نہیں** | جدید ایپلی کیشنز نہیں بنا سکتے | پسدید بیچ پروسیسنگ کے لیے استعمال کریں؛ جدید فرنٹ اینڈ |
---

## نحوی بنیادی باتیں
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

### فائل پروسیسنگ کی مثال
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

## اعلی درجے کی نحو اور نمونے۔
### ڈیٹا ڈویژن ڈیپ ڈائیو
COBOL کی ڈیٹا ڈویژن زبان کی سب سے مخصوص خصوصیت ہے۔ یہ اعداد و شمار کے ڈھانچے کی وضاحت کے لیے درجہ بندی کے نمبروں کے نظام (سطح 01–88) کا استعمال کرتا ہے۔
| سطح | مقصد | مثال |
|---------|---------|---------|
| **01** | ریکارڈ سطح کی آئٹم (اعلی سطحی متغیر یا ریکارڈ) | `01 WS-EMPLOYEE.`|
| **02–49** | گروپ یا ابتدائی اشیاء (ذیلی فیلڈز) | `05 EMP-NAME PIC X(30).`|
| **66** | شق کا نام تبدیل کریں (ڈیٹا کا متبادل نقطہ نظر) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | اسٹینڈ ایلیمنٹری آئٹم (کوئی ذیلی آئٹم نہیں) | `77 WS-COUNTER PIC 9(5).`|
| **88** | حالت کے نام (بولین نما جھنڈے) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### کاپی اسٹیٹمنٹ (کاپی بکس)
کاپی بکس کوڈ کو دوبارہ استعمال کرنے کے لیے COBOL کا طریقہ کار ہے — جو C میں`#include`کی طرح ہے۔ وہ الگ ممبرز کے طور پر محفوظ کی جاتی ہیں اور مرتب کرنے کے وقت داخل کی جاتی ہیں۔
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

### پرفارم تغیرات
COBOL ساختی پروگرامنگ کے لیے PERFORM سٹیٹمنٹ کے کئی ذائقے فراہم کرتا ہے۔
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

### سٹرنگ ہینڈلنگ اور معائنہ
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

## آرکیٹیکچر اور سسٹم ڈیزائن
### چار ڈویژنز
ہر COBOL پروگرام کو چار ڈویژنوں میں تشکیل دیا گیا ہے، ہر ایک کا ایک الگ مقصد ہے:
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

### پروگرام کا درجہ بندی
COBOL سسٹم عام طور پر ایک اہم پروگرام کے ساتھ کالنگ کے درجہ بندی کا استعمال کرتے ہیں جو ذیلی پروگراموں کو کال کرتا ہے۔
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

### عام پروجیکٹ ڈائرکٹری کا ڈھانچہ
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### GnuCOBOL (اوپن سورس COBOL کمپائلر)
GnuCOBOL (سابقہ ​​OpenCOBOL) COBOL کو C اور پھر مقامی مشین کوڈ میں مرتب کرتا ہے، COBOL کو Linux، Windows اور macOS پر چلانے کے قابل بناتا ہے۔
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

### IBM مین فریم JCL (جاب کنٹرول لینگویج)
IBM مین فریمز پر، COBOL پروگرام JCL کا استعمال کرتے ہوئے مرتب اور عمل میں لائے جاتے ہیں۔
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

### کمپائلر آپشنز کا حوالہ
| اختیار | تفصیل | مثال |
|---------|------------|---------|
| `-free`| فری فارمیٹ سورس (کالم کی کوئی پابندی نہیں) | `cobc -free prog.cbl`|
| `-fixed`| فکسڈ فارمیٹ (روایتی کالم 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| اصلاح کی سطح 2 | `cobc -O2 prog.cbl`|
| `-g`| ڈیبگ معلومات بنائیں | `cobc -g prog.cbl`|
| `-std=cobol2014`| COBOL 2014 معیاری استعمال کریں | `cobc -std=cobol2014 prog.cbl`|
| `-x`| قابل عمل بنائیں (صرف مرتب نہیں) | `cobc -x prog.cbl`|
| `-I`| کاپی بک تلاش کا راستہ | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| تمام انتباہات کو فعال کریں | `cobc -Wall prog.cbl`|
---

## ٹیسٹنگ اور ڈیبگنگ
### COBOL ڈیبگر تکنیک
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

### جی ڈی بی کے ساتھ GnuCOBOL ڈیبگنگ
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

### عام ڈیبگنگ پیٹرنز
| مسئلہ | علامت | حل |
|---------|---------|---------|
| چھوٹا ڈیٹا | کھیتوں کو کاٹ دیا | چیک کریں PIC شق سائز ریکارڈ ترتیب سے میچ |
| عددی اوور فلو | غلط حساب | تصدیق کریں کہ PIC 9(n) میں کافی ہندسے ہیں۔
| فائل کی حیثیت کی خرابیاں | WS-FILE-STATUS '00' نہیں | فائل کے ڈی ڈی کے نام، راستے اور اجازتیں چیک کریں۔
| لامحدود لوپ | پرفارم کریں جب تک کہ کبھی ختم نہ ہو | لوپ کے متغیر کی تصدیق کریں لوپ کے اندر ترمیم کی گئی ہے |
| کال کی ناکامیاں | غیر صفر واپسی | چیک کریں LINKAGE SECTION کالنگ پروگرام سے میل کھاتا ہے |
---

## انٹرآپریبلٹی
### کال اسٹیٹمنٹ - کالنگ سب پروگرامز
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

### C انٹرآپریبلٹی (GnuCOBOL)
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

### ڈیٹا بیس کنیکٹیویٹی (DB2/COBOL)
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

## ڈیزائن پیٹرن
### پیٹرن 1: کنٹرول بریکس کے ساتھ بیچ پروسیسنگ
کنٹرول بریک پیٹرن سب سے بنیادی COBOL ڈیزائن پیٹرن ہے — پروسیسنگ ریکارڈز کو کلیدی فیلڈ کے ذریعے گروپ کیا جاتا ہے اور ذیلی ٹوٹل تیار کرتا ہے۔
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

### پیٹرن 2: ترمیم/توثیق پیٹرن
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

### پیٹرن 3: ٹیبل تلاش (ان-میموری ارے)
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

## کارکردگی اور اصلاح
### فائل I/O آپٹیمائزیشن
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

### بیچ پروسیسنگ آپٹیمائزیشن
| تکنیک | اثر | تفصیل |
|------------|---------|------------|
| **بلاک I/O** | ہائی | جسمانی I/O آپریشنز کو کم کرنے کے لیے BLOCK CONTAINS استعمال کریں۔
| **انڈیکسڈ رسائی** | ہائی | بے ترتیب رسائی کی تلاش کے لیے INDEXED ORGANIZATION استعمال کریں۔
| **چھانٹیں/ضم کریں** | میڈیم | بڑے ڈیٹا سیٹ کی ترتیب کے لیے SORT فعل استعمال کریں۔
| **ڈسپلے کو کم سے کم کریں** | میڈیم | بیچ میں ڈسپلے سست ہے؛ اس کے بجائے فائلوں پر لکھیں |
| **COMP/COMP-3** | میڈیم | بائنری/پیکڈ فیلڈز DISPLAY عددی | سے زیادہ تیز ہیں۔
| **بفر ٹیوننگ** | میڈیم | ترتیب وار فائل پروسیسنگ کے لیے بفر سائز ٹیون کریں |
---

## تعیناتی اور حقیقی دنیا کا استعمال
### مین فریم کی تعیناتی (IBM z/OS)
مین فریمز پر COBOL پروگراموں کو تقسیم شدہ ڈیٹاسیٹس (PDS) میں لوڈ ماڈیول کے طور پر تعینات کیا جاتا ہے۔ JCL تالیف، لنکنگ، اور عملدرآمد کو کنٹرول کرتا ہے۔
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### تقسیم شدہ تعیناتی (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### COBOL استعمال کرنے والی حقیقی دنیا کی صنعتیں۔
| صنعت | استعمال | پیمانہ |
|------------|-------|-------|
| **بینکنگ** | ٹرانزیکشن پروسیسنگ، اکاؤنٹ مینجمنٹ | ATM ٹرانزیکشنز کا ~85% عمل |
| **انشورنس** | پالیسی ایڈمنسٹریشن، کلیمز پروسیسنگ | بڑے بیمہ کنندگان COBOL بیک اینڈز چلاتے ہیں |
| **حکومت** | سوشل سیکورٹی، ٹیکس پروسیسنگ، فوائد | US SSA اربوں ریکارڈ پر کارروائی کرتا ہے |
| **صحت کی دیکھ بھال** | مریض کا ریکارڈ، بلنگ سسٹم | میراثی ہسپتال انفارمیشن سسٹم |
| **خوردہ** | انوینٹری مینجمنٹ، پوائنٹ آف سیل بیک اینڈز | میراثی نظام کے ساتھ بڑے خوردہ فروش |
| **ٹیلی کام** | بلنگ سسٹم، کال ریکارڈ پروسیسنگ | کال ڈیٹیل ریکارڈ پروسیسنگ |
---

## COBOL کب استعمال کریں۔
| منظر نامہ | کیوں COBOL | بہتر متبادل |
|------------|------------|-------------------|
| مین فریم کی دیکھ بھال | موجودہ کوڈبیس | - |
| بیچ مالیاتی پروسیسنگ | ثابت، قابل اعتماد، عین مطابق اعشاریہ ریاضی | جاوا، نئے سسٹمز کے لیے ازگر |
| حکومتی میراثی نظام | موجودہ کوڈبیس | - |
| کمپیوٹنگ کی تاریخ سیکھنا | پروگرامنگ کے ارتقاء کو سمجھنا | - |
| نئی کاروباری ایپلی کیشنز | جدید انتخاب نہیں | Java, C#, Python |
| ویب/موبائل کی ترقی | مناسب نہیں | JavaScript, Swift, Kotlin |
| ڈیٹا سائنس / ایم ایل | مناسب نہیں | ازگر، آر |
---

## مصنوعی سوال و جواب
### Q1: COBOL کو 60+ سال بعد بھی بینکنگ میں کیوں استعمال کیا جاتا ہے؟
**A:** COBOL تقریباً 70-80% بینکنگ ٹرانزیکشنز پر کارروائی کرتا ہے۔ وجوہات:
- بڑے پیمانے پر کوڈ بیس (لاکھوں لائنیں) جو صحیح طریقے سے کام کرتے ہیں۔
- انتہائی قابل اعتماد - ان نظاموں کو کئی دہائیوں سے پیداوار میں آزمایا گیا ہے۔
- نقل مکانی کی لاگت اور خطرہ دیکھ بھال کے اخراجات سے زیادہ ہے۔
- COBOL کا وربوز، انگریزی جیسا نحو خود دستاویزی ہے۔
- زبان میں بنایا گیا اعشاریہ ریاضی (کوئی فلوٹنگ پوائنٹ راؤنڈنگ غلطیاں نہیں)
### Q2: COBOL فلوٹنگ پوائنٹ کی غلطیوں کے بغیر اعشاریہ ریاضی کو کیسے ہینڈل کرتا ہے؟
**A:** COBOL میں مقررہ درستگی کے ساتھ مقامی اعشاریہ قسمیں ہیں:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` ایک مضمر اعشاریہ ہے۔ COBOL کبھی بھی پیسے کے لیے بائنری فلوٹنگ پوائنٹ کا استعمال نہیں کرتا ہے۔
### Q3: COBOL پروگرام کی ساخت کیا ہے؟
**A:** ہر COBOL پروگرام کے چار ڈویژن ہوتے ہیں:
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

### Q4: میں COBOL میں ترتیب وار فائلوں کو کیسے پڑھ اور پروسیس کروں؟
**A:** فائل پروسیسنگ میں COBOL ایکسل کرتا ہے:
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

### Q5: جدید COBOL کی ترقی کے لیے کون سے ٹولز دستیاب ہیں؟
**A:** GnuCOBOL (اوپن سورس)، IBM Enterprise COBOL، مائیکرو فوکس، اور VS کوڈ ایکسٹینشنز جدید ترقی کے ماحول فراہم کرتے ہیں۔`cobc -x program.cob`کے ساتھ بنائیں۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: کسٹمر رپورٹ تیار کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
گاہک کے ریکارڈ پڑھیں، ٹوٹل کا حساب لگائیں، اور فارمیٹ شدہ رپورٹ بنائیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
COBOL کی فائل ہینڈلنگ اور رپورٹ لکھنے کی صلاحیتوں کا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```cobol
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

**مرحلہ 4: تصدیق کریں**
سورس ڈیٹا کے خلاف کراس چیک ٹوٹل۔ ایج کیسز کے ساتھ ٹیسٹ کریں (خالی فائل، صفر بیلنس)۔
### مسئلہ 2: کنٹرول بریکس کے ساتھ بیچ پروسیسنگ
**مرحلہ 1: مسئلہ کو سمجھیں**
عمل کے لین دین کو محکمہ کے لحاظ سے گروپ کیا گیا، پرنٹنگ ذیلی ٹوٹل۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
کنٹرول بریک منطق کا استعمال کریں - گروپ کی کلید تبدیل ہونے پر پتہ لگائیں۔
**مرحلہ 3: نافذ کریں**```cobol
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

**مرحلہ 4: تصدیق کریں**
چیک کریں کہ آخری گروپ کا کل پرنٹ کیا گیا ہے۔ توثیق کریں گرینڈ ٹوٹل ڈپارٹمنٹ کے ٹوٹل کے برابر ہے۔
---

## خلاصہ
COBOL کمپیوٹنگ کی ابتدائی دہائیوں کی میراث ہے جو فعال استعمال میں رہتی ہے کیونکہ پیمانے پر متبادل ممکن نہیں ہے۔ دنیا کے بینکنگ اور حکومتی نظام کا انحصار COBOL پروگراموں پر ہے جو کئی دہائیوں سے قابل اعتماد طریقے سے چل رہے ہیں۔ اگرچہ COBOL کو آج عام طور پر کسی نئے پروجیکٹ کے لیے منتخب نہیں کیا جائے گا، لیکن یہ زبان بنیادی ڈھانچے کو برقرار رکھنے کے لیے اہم ہے جو عالمی مالیات کو سپورٹ کرتا ہے۔ COBOL ڈویلپرز کی کمی اسے ایک منافع بخش مقام بناتی ہے۔