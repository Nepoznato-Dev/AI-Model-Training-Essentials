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
COBOL (زبان تجاری متداول) یکی از قدیمی ترین زبان های برنامه نویسی است که هنوز مورد استفاده قرار می گیرد، اولین بار در سال 1959 توسعه یافت. این زبان برای پردازش داده های تجاری - سیستم های مالی، حقوق و دستمزد، بانکداری، بیمه و برنامه های دولتی طراحی شده است. دستور زبان انگلیسی COBOL برای مدیران تجاری و نه فقط برنامه نویسان قابل خواندن بود.
COBOL علیرغم قدمتش، تقریباً 30 درصد از کل معاملات تجاری در سطح جهان را پردازش می کند. بانک‌های بزرگ، سازمان‌های دولتی (از جمله اداره تامین اجتماعی ایالات متحده) و شرکت‌های بیمه همچنان به سیستم‌های اصلی COBOL متکی هستند. ترس از اشکال Y2K در سال 1999 COBOL را به آگاهی عمومی بازگرداند و این زبان همچنان زیرساخت های حیاتی را در سراسر جهان اجرا می کند.
---

## چرا COBOL مهم است
- **زیرساخت های حیاتی تجاری**: تریلیون ها دلار تراکنش روزانه در بانک ها و دولت را پردازش می کند.
- **پایداری**: برنامه های COBOL که در دهه 1970 نوشته شده بودند، امروزه هنوز به طور قابل اعتماد اجرا می شوند - حداقل تغییرات مورد نیاز است.
- **خوانایی**: نحوی شبیه به انگلیسی، منطق تجاری را برای غیر برنامه نویسان قابل درک می کند.
- ** محاسبات اعشاری **: پشتیبانی بومی برای محاسبات مالی دقیق (بدون خطاهای گرد کردن ممیز شناور).
- ** پردازش دسته ای **: طراحی شده برای پردازش حجم زیادی از رکوردها به طور موثر.
- **بازار کار**: کمبود شدید توسعه دهندگان COBOL باعث ایجاد تقاضای بالا (و حقوق بالا) برای نقش های تعمیر و نگهداری می شود.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| ** نحو پرمخاطب ** | برای عملیات ساده به خطوط زیادی نیاز دارد | پذیرش به عنوان بخشی از طراحی زبان |
| **مدرن نیست** | بدون کلاس، بدون برنامه نویسی تابعی، انتزاعات محدود | استفاده برای نگهداری؛ ساخت سیستم های جدید به زبان های مدرن |
| **وابستگی به Mainframe** | به طور معمول بر روی پردازنده های مرکزی IBM اجرا می شود (گران قیمت) | استفاده از کامپایلرهای COBOL در سیستم های توزیع شده (GnuCOBOL) |
| **کاهش نیروی کار** | تعداد کمتری از توسعه دهندگان COBOL وارد این حوزه می شوند | تقاضای بالا برای کسانی که آن را می شناسند؛ موقعیت شغلی خوب |
| **بدون وب/موبایل** | نمی توان برنامه های مدرن ساخت | استفاده برای پردازش دسته ای باطن. پیشانی مدرن |
---

## اصول نحو
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

### مثال پردازش فایل
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

## نحو و الگوهای پیشرفته
### Division Division Deep Dive
تقسیم داده COBOL متمایزترین ویژگی این زبان است. از یک سیستم شماره گذاری سلسله مراتبی (سطوح 01-88) برای تعریف ساختارهای داده استفاده می کند.
| سطح | هدف | مثال |
|-------|---------|---------|
| **01** | آیتم سطح رکورد (متغیر سطح بالا یا رکورد) | `01 WS-EMPLOYEE.`|
| **02–49** | اقلام گروهی یا ابتدایی (فیلدهای فرعی) | `05 EMP-NAME PIC X(30).`|
| **66** | تغییر نام بند (نمای جایگزین داده ها) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | آیتم ابتدایی مستقل (بدون موارد فرعی) | `77 WS-COUNTER PIC 9(5).`|
| **88** | نام شرایط (پرچم های بولی مانند) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### بیانیه کپی (کتاب های کپی)
کتاب‌های کپی مکانیزم COBOL برای استفاده مجدد از کد هستند - شبیه به`#include`در C. آنها به عنوان اعضای جداگانه ذخیره می‌شوند و در زمان کامپایل درج می‌شوند.
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

### PERFORM Variations
COBOL چندین طعم از عبارت PERFORM را برای برنامه نویسی ساخت یافته ارائه می دهد.
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

### کنترل و بازرسی رشته
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

## معماری و طراحی سیستم
### چهار بخش
هر برنامه COBOL به چهار بخش ساختار یافته است که هر یک هدف مشخصی را انجام می دهند:
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

### سلسله مراتب برنامه
سیستم های COBOL معمولاً از یک سلسله مراتب فراخوانی با یک برنامه اصلی استفاده می کنند که برنامه های فرعی را فراخوانی می کند.
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

### ساختار دایرکتوری پروژه معمولی
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

## پیکربندی پروژه و سیستم ساخت
### GnuCOBOL (کامپایلر COBOL منبع باز)
GnuCOBOL (قبلاً OpenCOBOL) COBOL را به C و سپس به کد ماشین بومی کامپایل می‌کند و COBOL را قادر می‌سازد روی لینوکس، ویندوز و macOS اجرا شود.
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

### IBM Mainframe JCL (زبان کنترل شغل)
در رایانه های اصلی IBM، برنامه های COBOL با استفاده از JCL کامپایل و اجرا می شوند.
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

### مرجع گزینه های کامپایلر
| گزینه | توضیحات | مثال |
|--------|------------|---------|
| `-free`| منبع فرمت آزاد (بدون محدودیت ستونی) | `cobc -free prog.cbl`|
| `-fixed`| فرمت ثابت (ستون های سنتی 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| بهینه سازی سطح 2 | `cobc -O2 prog.cbl`|
| `-g`| ایجاد اطلاعات اشکال زدایی | `cobc -g prog.cbl`|
| `-std=cobol2014`| استفاده از استاندارد COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| ساخت فایل اجرایی (نه فقط کامپایل) | `cobc -x prog.cbl`|
| `-I`| مسیر جستجوی کتاب کپی | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| فعال کردن همه هشدارها | `cobc -Wall prog.cbl`|
---

## تست و اشکال زدایی
### تکنیک های دیباگر COBOL
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

### GnuCOBOL اشکال زدایی با gdb
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

### الگوهای رایج اشکال زدایی
| مشکل | علامت | راه حل |
|---------|---------|----------|
| داده های کوتاه شده | زمین های قطع شده | بررسی اندازه های PIC بند مطابق با طرح رکورد |
| سرریز عددی | محاسبات اشتباه | بررسی کنید که PIC 9(n) دارای ارقام کافی باشد |
| خطاهای وضعیت فایل | WS-FILE-STATUS '00' نیست | نام، مسیرها و مجوزهای فایل DD |
| حلقه بی نهایت | اجرا کنید تا هرگز خاتمه نیابد | بررسی متغیر حلقه در داخل حلقه |
| خرابی تماس | بازگشت غیر صفر | بررسی LINKAGE SECTION مطابق با برنامه تماس |
---

## قابلیت همکاری
### بیانیه تماس - فراخوانی برنامه های فرعی
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

### C قابلیت همکاری (GnuCOBOL)
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

### اتصال به پایگاه داده (DB2/COBOL)
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

## الگوهای طراحی
### الگوی 1: پردازش دسته ای با شکست های کنترل
الگوی شکست کنترل اساسی‌ترین الگوی طراحی COBOL است - پردازش رکوردها توسط یک فیلد کلیدی و تولید جمع‌های فرعی.
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

### الگوی 2: الگوی ویرایش/ اعتبارسنجی
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

### الگوی 3: جستجوی جدول (آرایه در حافظه)
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

## عملکرد و بهینه سازی
### بهینه سازی ورودی/خروجی فایل
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

### بهینه سازی پردازش دسته ای
| تکنیک | تاثیر | توضیحات |
|-----------|--------|-------------|
| **بلاک ورودی/خروجی** | بالا | از BLOCK CONTAINS برای کاهش عملیات I/O فیزیکی استفاده کنید |
| **دسترسی نمایه شده** | بالا | از ORGANIZATION INDEXED برای جستجوهای با دسترسی تصادفی |
| **مرتب سازی/ادغام** | متوسط ​​| استفاده از فعل SORT برای مرتب سازی مجموعه داده های بزرگ |
| **به حداقل رساندن DISPLAY** | متوسط ​​| DISPLAY در دسته کند است. به جای فایل ها بنویسید |
| **COMP/COMP-3** | متوسط ​​| فیلدهای باینری/مجموعه سریعتر از DISPLAY عددی |
| **تنظیم بافر** | متوسط ​​| تنظیم اندازه بافر برای پردازش متوالی فایل |
---

## استقرار و استفاده در دنیای واقعی
### استقرار Mainframe (IBM z/OS)
برنامه های COBOL بر روی پردازنده های مرکزی به عنوان ماژول های بار در مجموعه داده های پارتیشن بندی شده (PDS) مستقر می شوند. JCL کامپایل، پیوند و اجرا را کنترل می کند.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### استقرار توزیع شده (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### صنایع دنیای واقعی با استفاده از COBOL
| صنعت | استفاده | مقیاس |
|----------|-------|-------|
| **بانکداری** | پردازش تراکنش، مدیریت حساب | 85% از تراکنش های خودپرداز را پردازش می کند |
| **بیمه** | مدیریت خط مشی، پردازش ادعاها | بیمه گران بزرگ پشتیبان COBOL |
| **دولت** | تامین اجتماعی، پردازش مالیات، مزایا | SSA ایالات متحده میلیاردها رکورد را پردازش می کند |
| **بهداشت** | سوابق بیمار، سیستم های صورتحساب | سیستم های اطلاعات بیمارستان میراث |
| **خرده فروشی** | مدیریت موجودی، باطن های نقطه فروش | خرده فروشان بزرگ با سیستم های قدیمی |
| ** مخابرات ** | سیستم های صورتحساب، پردازش رکورد تماس | پردازش رکورد جزئیات تماس |
---

## چه زمانی از COBOL استفاده کنیم
| سناریو | چرا COBOL | جایگزین بهتر |
|----------|---------|-------------------|
| تعمیر و نگهداری اصلی | پایگاه کد موجود | — |
| پردازش مالی دسته ای | ریاضی اعشاری ثابت، قابل اعتماد و دقیق | جاوا، پایتون برای سیستم های جدید |
| سیستم های میراث دولتی | پایگاه کد موجود | — |
| یادگیری تاریخچه محاسبات | درک تکامل برنامه نویسی | — |
| برنامه های کاربردی کسب و کار جدید | نه انتخاب مدرن | جاوا، سی شارپ، پایتون |
| توسعه وب/موبایل | مناسب نیست | جاوا اسکریپت، سوئیفت، کاتلین |
| علم داده / ML | مناسب نیست | پایتون، R |
---

## پرسش و پاسخ مصنوعی
### Q1: چرا COBOL هنوز بعد از 60 سال در بانکداری استفاده می شود؟
**الف:** COBOL حدود 70 تا 80 درصد از تراکنش های بانکی را پردازش می کند. دلایل:
- پایگاه های کد عظیم (میلیون ها خط) که به درستی کار می کنند
- قابلیت اطمینان فوق العاده - این سیستم ها برای دهه ها در تولید آزمایش شده اند
- هزینه و خطر مهاجرت بیشتر از هزینه های نگهداری است
- نحو پرمخاطب و انگلیسی COBOL خود مستندسازی است
- حساب اعشاری ساخته شده در زبان (بدون خطا در گرد کردن ممیز شناور)
### Q2: COBOL چگونه محاسبات اعشاری را بدون خطاهای ممیز شناور مدیریت می کند؟
**A:** COBOL دارای انواع اعشاری بومی با دقت ثابت است:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` یک نقطه اعشاری ضمنی است. COBOL هرگز از ممیز شناور باینری برای پول استفاده نمی کند.
### Q3: ساختار برنامه COBOL چیست؟
**A:** هر برنامه COBOL دارای چهار بخش است:
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

### Q4: چگونه فایل های متوالی را در COBOL بخوانم و پردازش کنم؟
**A:** COBOL در پردازش فایل برتری دارد:
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

### Q5: چه ابزارهایی برای توسعه COBOL مدرن موجود است؟
**A:** GnuCOBOL (متن باز)، IBM Enterprise COBOL، Micro Focus، و افزونه های VS Code محیط های توسعه مدرن را ارائه می دهند. ساخت با `cobc -x program.cob`.
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: ایجاد گزارش مشتری
**مرحله 1: مشکل را درک کنید**
سوابق مشتری را بخوانید، مجموع ها را محاسبه کنید و یک گزارش فرمت شده ایجاد کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از قابلیت های مدیریت فایل و گزارش نویسی COBOL استفاده کنید.
**مرحله 3: پیاده سازی **```cobol
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

**مرحله 4: تایید **
مجموع ها را با داده های منبع بررسی کنید. تست با موارد لبه (فایل خالی، تعادل صفر).
### مشکل 2: پردازش دسته ای با کنترل خرابی
**مرحله 1: مشکل را درک کنید**
پردازش تراکنش‌ها بر اساس گروه‌بندی، چاپ جمع‌های فرعی.
**مرحله 2: رویکرد را شناسایی کنید**
از منطق شکست کنترل استفاده کنید — تشخیص دهید که چه زمانی کلید گروه تغییر می کند.
**مرحله 3: پیاده سازی **```cobol
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

**مرحله 4: تایید **
بررسی کنید که کل آخرین گروه چاپ شده باشد. بررسی کنید که کل کل برابر است با مجموع مجموع دپارتمان.
---

## خلاصه
COBOL میراث دهه های اولیه محاسبات است که همچنان در حال استفاده فعال است زیرا جایگزینی در مقیاس امکان پذیر نیست. سیستم‌های بانکی و دولتی جهان به برنامه‌های COBOL وابسته هستند که دهه‌ها به طور قابل اعتماد اجرا شده‌اند. در حالی که COBOL معمولاً امروزه برای یک پروژه جدید انتخاب نمی شود، این زبان برای حفظ زیرساختی که از مالی جهانی پشتیبانی می کند، مهم است. کمبود توسعه دهندگان COBOL آن را به یک جایگاه پردرآمد تبدیل می کند.