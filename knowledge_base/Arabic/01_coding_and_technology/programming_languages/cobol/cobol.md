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

# كوبول
تعد لغة COBOL (اللغة الشائعة الموجهة للأعمال) واحدة من أقدم لغات البرمجة التي لا تزال قيد الاستخدام، وقد تم تطويرها لأول مرة في عام 1959. وقد تم تصميمها لمعالجة بيانات الأعمال - الأنظمة المالية وكشوف المرتبات والخدمات المصرفية والتأمين والتطبيقات الحكومية. كان المقصود من لغة COBOL الشبيهة باللغة الإنجليزية أن تكون قابلة للقراءة من قبل مديري الأعمال، وليس فقط المبرمجين.
على الرغم من عمرها، تقوم COBOL بمعالجة ما يقدر بنحو 30٪ من جميع المعاملات التجارية على مستوى العالم. لا تزال البنوك الكبرى والوكالات الحكومية (بما في ذلك إدارة الضمان الاجتماعي الأمريكية) وشركات التأمين تعتمد على أنظمة الحاسب المركزي COBOL. أدى الذعر من خلل Y2K في عام 1999 إلى عودة لغة COBOL إلى الوعي العام، وتستمر اللغة في تشغيل البنية التحتية الحيوية في جميع أنحاء العالم.
---

## لماذا يهم كوبول
- **البنية التحتية الحيوية للأعمال**: تعالج معاملات بقيمة تريليونات الدولارات يوميًا عبر الخدمات المصرفية والحكومية.
- **الاستقرار**: لا تزال برامج COBOL المكتوبة في السبعينيات تعمل بشكل موثوق حتى اليوم — ولا يلزم إجراء سوى الحد الأدنى من التغييرات.
- **سهولة القراءة**: بناء الجملة المشابه للغة الإنجليزية يجعل منطق الأعمال مفهومًا لغير المبرمجين.
- **الحساب العشري**: دعم أصلي للحسابات المالية الدقيقة (بدون أخطاء تقريب بالفاصلة العائمة).
- **معالجة الدفعات**: مصممة لمعالجة كميات كبيرة من السجلات بكفاءة.
- **سوق العمل**: يؤدي النقص الحاد في مطوري COBOL إلى زيادة الطلب (ورواتب عالية) على أدوار الصيانة.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** بناء الجملة المطول ** | يتطلب العديد من الخطوط لعمليات بسيطة | قبول كجزء من تصميم اللغة |
| **ليست حديثة** | لا توجد فئات، ولا برمجة وظيفية، وتجريدات محدودة | استخدام للصيانة. بناء أنظمة جديدة باللغات الحديثة |
| ** تبعية الحاسوب المركزي ** | يعمل عادةً على حاسبات IBM المركزية (باهظة الثمن) | استخدم مترجمات COBOL على الأنظمة الموزعة (GnuCOBOL) |
| **انخفاض القوى العاملة** | عدد أقل من مطوري COBOL يدخلون المجال | ارتفاع الطلب لمن يعرفه؛ مكانة مهنية جيدة |
| **لا يوجد ويب/جوال** | لا يمكن بناء التطبيقات الحديثة | تستخدم لمعالجة الدفعات الخلفية. الواجهات الحديثة |
---

## أساسيات بناء الجملة
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

### مثال لمعالجة الملفات
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

## بناء الجملة والأنماط المتقدمة
### نظرة عميقة على قسم البيانات
يعد تقسيم البيانات في COBOL هو السمة الأكثر تميزًا للغة. ويستخدم نظام ترقيم هرمي (المستويات من 01 إلى 88) لتحديد هياكل البيانات.
| المستوى | الغرض | مثال |
|-------|---------|---------|
| **01** | عنصر مستوى السجل (متغير أو سجل المستوى الأعلى) | `01 WS-EMPLOYEE.`|
| **02–49** | عناصر المجموعة أو الأولية (حقول فرعية) | `05 EMP-NAME PIC X(30).`|
| **66** | إعادة تسمية الجملة (عرض بديل للبيانات) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | عنصر أساسي مستقل (بدون عناصر فرعية) | `77 WS-COUNTER PIC 9(5).`|
| **88** | أسماء الشروط (علامات تشبه المنطق) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### بيان النسخ (دفاتر النسخ)
دفاتر النسخ هي آلية COBOL لإعادة استخدام التعليمات البرمجية - تشبه`#include`في لغة C. ويتم تخزينها كأعضاء منفصلين وإدراجها في وقت الترجمة.
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

### أداء الاختلافات
يوفر COBOL العديد من نكهات بيان الأداء للبرمجة المنظمة.
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

### التعامل مع السلسلة وفحصها
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

## الهندسة المعمارية وتصميم النظام
### الأقسام الأربعة
يتم تنظيم كل برنامج COBOL إلى أربعة أقسام، يخدم كل منها غرضًا مميزًا:
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

### التسلسل الهرمي للبرنامج
تستخدم أنظمة COBOL عادةً تسلسل هرمي للاتصال مع برنامج رئيسي يستدعي البرامج الفرعية.
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

### هيكل دليل المشروع النموذجي
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

## تكوين المشروع ونظام البناء
### GnuCOBOL (مترجم COBOL مفتوح المصدر)
يقوم GnuCOBOL (المعروف سابقًا باسم OpenCOBOL) بتجميع COBOL إلى لغة C ثم إلى رمز الجهاز الأصلي، مما يتيح تشغيل COBOL على Linux وWindows وmacOS.
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

### IBM Mainframe JCL (لغة التحكم في المهام)
في حاسبات IBM المركزية، يتم تجميع برامج COBOL وتنفيذها باستخدام JCL.
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

### مرجع خيارات المترجم
| الخيار | الوصف | مثال |
|--------|-----------|---------|
| `-free`| مصدر ذو تنسيق حر (بدون قيود على الأعمدة) | `cobc -free prog.cbl`|
| `-fixed`| التنسيق الثابت (الأعمدة التقليدية 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| مستوى التحسين 2 | `cobc -O2 prog.cbl`|
| `-g`| إنشاء معلومات التصحيح | `cobc -g prog.cbl`|
| `-std=cobol2014`| استخدم معيار COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| بناء قابل للتنفيذ (وليس فقط تجميع) | `cobc -x prog.cbl`|
| `-I`| مسار البحث في الدفتر | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| تمكين كافة التحذيرات | `cobc -Wall prog.cbl`|
---

## الاختبار والتصحيح
### تقنيات مصحح أخطاء كوبول
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

### تصحيح أخطاء GnuCOBOL باستخدام gdb
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

### أنماط التصحيح الشائعة
| مشكلة | العَرَض | الحل |
|---------|--------|----------|
| البيانات المقتطعة | الحقول مقطوعة | تحقق من تطابق أحجام جملة PIC مع تخطيط السجل |
| التجاوز الرقمي | حسابات خاطئة | تحقق من أن PIC 9(n) يحتوي على أرقام كافية |
| أخطاء حالة الملف | WS-FILE-STATUS ليس "00" | تحقق من أسماء ملفات DD ومساراتها وأذوناتها |
| حلقة لا نهائية | الأداء حتى لا ينتهي أبدًا | تحقق من تعديل متغير الحلقة داخل الحلقة |
| فشل الاتصال | عودة غير الصفر | تحقق من تطابق قسم LINKAGE مع برنامج الاتصال |
---

## إمكانية التشغيل البيني
### بيان الاتصال — استدعاء البرامج الفرعية
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

### إمكانية التشغيل البيني C (GnuCOBOL)
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

### الاتصال بقاعدة البيانات (DB2/COBOL)
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

## أنماط التصميم
### النموذج 1: معالجة الدُفعات مع فواصل التحكم
يعد نمط فواصل التحكم هو نمط تصميم COBOL الأكثر أهمية - وهو معالجة السجلات المجمعة حسب حقل رئيسي وإنتاج الإجماليات الفرعية.
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

### النموذج 2: نمط التحرير/التحقق
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

### النموذج 3: البحث في الجدول (مصفوفة داخل الذاكرة)
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

## الأداء والتحسين
### تحسين إدخال/إخراج الملفات
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

### تحسين معالجة الدفعات
| تقنية | التأثير | الوصف |
|-----------|-------|-------------|
| ** كتلة الإدخال / الإخراج ** | عالية | استخدم BLOCK CONTAINS لتقليل عمليات الإدخال/الإخراج الفعلية |
| ** الوصول المفهرس ** | عالية | استخدم INDEXED ORGANIZATION لعمليات البحث ذات الوصول العشوائي |
| **فرز/دمج** | متوسطة | استخدم الفعل SORT لطلب مجموعات البيانات الكبيرة |
| **تصغير العرض** | متوسطة | العرض بطيء في الدفعة؛ الكتابة إلى الملفات بدلا من ذلك |
| **كومب/كومب-3** | متوسطة | الحقول الثنائية/المعبأة أسرع من DISPLAY الرقمي |
| **ضبط المخزن المؤقت** | متوسطة | ضبط أحجام المخزن المؤقت لمعالجة الملفات المتسلسلة |
---

## النشر والاستخدام في العالم الحقيقي
### نشر الحاسب المركزي (IBM z/OS)
يتم نشر برامج COBOL على الحواسيب المركزية كوحدات تحميل في مجموعات البيانات المقسمة (PDS). تتحكم JCL في التجميع والربط والتنفيذ.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### النشر الموزع (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### صناعات العالم الحقيقي باستخدام لغة COBOL
| صناعة | الاستخدام | مقياس |
|----------|-------|-------|
| **الخدمات المصرفية** | معالجة المعاملات، وإدارة الحساب | يعالج حوالي 85% من معاملات أجهزة الصراف الآلي |
| **التأمين** | إدارة السياسات ومعالجة المطالبات | تدير شركات التأمين الكبرى واجهات COBOL الخلفية |
| **الحكومة** | الضمان الاجتماعي، تجهيز الضرائب، الفوائد | تقوم SSA الأمريكية بمعالجة مليارات السجلات |
| **الرعاية الصحية** | سجلات المرضى وأنظمة الفواتير | نظم معلومات المستشفيات القديمة |
| **التجزئة** | إدارة المخزون، الواجهات الخلفية لنقاط البيع | تجار التجزئة الكبار بأنظمة قديمة |
| **الاتصالات** | أنظمة الفوترة ومعالجة سجلات المكالمات | معالجة سجل تفاصيل المكالمات |
---

## متى تستخدم كوبول
| السيناريو | لماذا كوبول | البديل الأفضل |
|----------|-------------------------|---|
| صيانة الحاسوب المركزي | قاعدة التعليمات البرمجية الموجودة | — |
| دفعة المعالجة المالية | الرياضيات العشرية المثبتة والموثوقة والدقيقة | جافا، بايثون للأنظمة الجديدة |
| الأنظمة التراثية الحكومية | قاعدة التعليمات البرمجية الموجودة | — |
| تعلم تاريخ الحوسبة | فهم تطور البرمجة | — |
| تطبيقات تجارية جديدة | ليس الخيار الحديث | جافا، سي#، بايثون |
| تطوير الويب/الجوال | غير مناسب | جافا سكريبت، سويفت، كوتلين |
| علم البيانات / تعلم الآلة | غير مناسب | بايثون، ر |
---

## أسئلة وأجوبة اصطناعية
### س1: لماذا لا يزال كوبول يستخدم في الخدمات المصرفية بعد أكثر من 60 عامًا؟
**ج:** تقوم COBOL بمعالجة ما يقدر بنحو 70-80% من المعاملات المصرفية. الأسباب:
- قواعد تعليمات برمجية ضخمة (ملايين الأسطر) تعمل بشكل صحيح
- الموثوقية القصوى - تم اختبار هذه الأنظمة في الإنتاج لعقود من الزمن
- تكلفة ومخاطر الهجرة تفوق تكاليف الصيانة
- بناء جملة COBOL المطول الشبيه باللغة الإنجليزية هو توثيق ذاتي
- الحساب العشري المدمج في اللغة (لا توجد أخطاء تقريب الفاصلة العائمة)
### السؤال الثاني: كيف تتعامل لغة COBOL مع الحساب العشري بدون أخطاء الفاصلة العائمة؟
**A:** يحتوي COBOL على أنواع عشرية أصلية بدقة ثابتة:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` هي علامة عشرية ضمنية. لا تستخدم COBOL أبدًا الفاصلة العائمة الثنائية مقابل المال.
### س3: ما هو هيكل برنامج كوبول؟
**ج:** يحتوي كل برنامج COBOL على أربعة أقسام:
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

### Q4: كيف يمكنني قراءة ومعالجة الملفات المتسلسلة في COBOL؟
**أ:** تتفوق لغة COBOL في معالجة الملفات:
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

### س5: ما هي الأدوات المتوفرة لتطوير لغة COBOL الحديثة؟
**ج:** توفر امتدادات GnuCOBOL (مفتوحة المصدر)، وIBM Enterprise COBOL، وMicro Focus، وVS Code بيئات تطوير حديثة. البناء باستخدام `cobc -x program.cob`.
---

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: إنشاء تقرير العميل
**الخطوة الأولى: فهم المشكلة**
قراءة سجلات العملاء وحساب الإجماليات وإنشاء تقرير منسق.
**الخطوة 2: تحديد النهج**
استخدم إمكانيات معالجة الملفات وكتابة التقارير في COBOL.
**الخطوة 3: التنفيذ**```cobol
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

**الخطوة 4: التحقق**
قم بمراجعة الإجماليات مقابل بيانات المصدر. اختبار مع حالات الحافة (ملف فارغ، أرصدة صفر).
### المشكلة الثانية: معالجة الدُفعات باستخدام فواصل التحكم
**الخطوة الأولى: فهم المشكلة**
معالجة المعاملات مجمعة حسب القسم وطباعة المجاميع الفرعية.
**الخطوة 2: تحديد النهج**
استخدم منطق فواصل التحكم - اكتشف متى يتغير مفتاح المجموعة.
**الخطوة 3: التنفيذ**```cobol
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

**الخطوة 4: التحقق**
تأكد من طباعة إجمالي المجموعة الأخيرة. التحقق من أن الإجمالي الكلي يساوي مجموع إجماليات القسم.
---

## ملخص
إن لغة COBOL هي إرث من العقود الأولى للحوسبة والتي لا تزال قيد الاستخدام النشط لأن الاستبدال ليس ممكنًا على نطاق واسع. تعتمد الأنظمة المصرفية والحكومية في العالم على برامج COBOL التي تم تشغيلها بشكل موثوق لعقود من الزمن. في حين أن لغة COBOL لا يتم اختيارها عادةً لمشروع جديد اليوم، إلا أن اللغة تظل مهمة للحفاظ على البنية التحتية التي تدعم التمويل العالمي. النقص في مطوري COBOL يجعلها مكانًا مربحًا.