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
# COBOL
COBOL (সাধারণ বিজনেস-ওরিয়েন্টেড ল্যাঙ্গুয়েজ) হল প্রাচীনতম প্রোগ্রামিং ভাষাগুলির মধ্যে একটি যা এখনও ব্যবহৃত হয়, প্রথম 1959 সালে বিকশিত হয়েছিল৷ এটি ব্যবসায়িক ডেটা প্রক্রিয়াকরণের জন্য ডিজাইন করা হয়েছিল — আর্থিক ব্যবস্থা, বেতন, ব্যাংকিং, বীমা এবং সরকারী অ্যাপ্লিকেশনগুলির জন্য৷ COBOL-এর ইংরেজি-সদৃশ সিনট্যাক্সটি শুধুমাত্র প্রোগ্রামারদের নয়, ব্যবসায়িক পরিচালকদের দ্বারা পাঠযোগ্য হওয়ার উদ্দেশ্যে ছিল।
বয়স হওয়া সত্ত্বেও, COBOL বিশ্বব্যাপী সমস্ত ব্যবসায়িক লেনদেনের আনুমানিক 30% প্রক্রিয়া করে। প্রধান ব্যাঙ্ক, সরকারি সংস্থাগুলি (ইউএস সোশ্যাল সিকিউরিটি অ্যাডমিনিস্ট্রেশন সহ), এবং বীমা কোম্পানিগুলি এখনও COBOL মেইনফ্রেম সিস্টেমের উপর নির্ভর করে। 1999 সালে Y2K বাগ ভীতি COBOL কে জনসচেতনতায় ফিরিয়ে আনে এবং ভাষা বিশ্বব্যাপী সমালোচনামূলক অবকাঠামো চালিয়ে যাচ্ছে।
---

## কেন কোবল গুরুত্বপূর্ণ
- **ব্যবসা-সমালোচনামূলক অবকাঠামো**: ব্যাঙ্কিং এবং সরকার জুড়ে প্রতিদিন ট্রিলিয়ন ডলারের লেনদেন প্রক্রিয়া করে।
- **স্থিতিশীলতা**: 1970 এর দশকে লেখা COBOL প্রোগ্রামগুলি আজও নির্ভরযোগ্যভাবে চলে — ন্যূনতম পরিবর্তন প্রয়োজন।
- **পঠনযোগ্যতা**: ইংরেজির মতো সিনট্যাক্স ব্যবসায়িক যুক্তিকে অ-প্রোগ্রামারদের কাছে বোধগম্য করে তোলে।
- **দশমিক পাটিগণিত**: সুনির্দিষ্ট আর্থিক গণনার জন্য স্থানীয় সমর্থন (কোন ফ্লোটিং-পয়েন্ট রাউন্ডিং ত্রুটি নেই)।
- **ব্যাচ প্রক্রিয়াকরণ**: দক্ষতার সাথে রেকর্ডের বড় ভলিউম প্রক্রিয়াকরণের জন্য ডিজাইন করা হয়েছে।
- **চাকরীর বাজার**: COBOL ডেভেলপারদের তীব্র ঘাটতি রক্ষণাবেক্ষণের ভূমিকার জন্য উচ্চ চাহিদা (এবং উচ্চ বেতন) তৈরি করে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **ভার্বোস সিনট্যাক্স** | সহজ অপারেশনের জন্য অনেক লাইনের প্রয়োজন | ভাষা ডিজাইনের অংশ হিসাবে গ্রহণ করুন |
| **আধুনিক নয়** | কোন ক্লাস নেই, কোন কার্যকরী প্রোগ্রামিং নেই, সীমিত বিমূর্ততা | রক্ষণাবেক্ষণের জন্য ব্যবহার করুন; আধুনিক ভাষায় নতুন সিস্টেম তৈরি করুন |
| **মেনফ্রেম নির্ভরতা** | সাধারণত IBM মেইনফ্রেমে চলে (ব্যয়বহুল) | ডিস্ট্রিবিউটেড সিস্টেমে COBOL কম্পাইলার ব্যবহার করুন (GnuCOBOL) |
| **কর্মসংস্থান হ্রাস** | কম COBOL বিকাশকারী ক্ষেত্র প্রবেশ করছে | যারা এটা জানেন তাদের জন্য উচ্চ চাহিদা; ভাল কর্মজীবন কুলুঙ্গি |
| **কোন ওয়েব/মোবাইল নেই** | আধুনিক অ্যাপ্লিকেশন তৈরি করতে পারে না | ব্যাকএন্ড ব্যাচ প্রক্রিয়াকরণের জন্য ব্যবহার করুন; আধুনিক ফ্রন্টএন্ড |
---

## সিনট্যাক্স মৌলিক
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

### ফাইল প্রসেসিং উদাহরণ
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### ডেটা বিভাগ গভীর ডুব
COBOL-এর ডেটা বিভাগ হল ভাষার সবচেয়ে স্বতন্ত্র বৈশিষ্ট্য। এটি ডেটা স্ট্রাকচার সংজ্ঞায়িত করার জন্য একটি ক্রমিক সংখ্যা পদ্ধতি (স্তর 01-88) ব্যবহার করে।
| স্তর | উদ্দেশ্য | উদাহরণ |
|-------|---------|---------|
| **01** | রেকর্ড-স্তরের আইটেম (শীর্ষ-স্তরের পরিবর্তনশীল বা রেকর্ড) | `01 WS-EMPLOYEE.`|
| **02–49** | গ্রুপ বা প্রাথমিক আইটেম (উপ-ক্ষেত্র) | `05 EMP-NAME PIC X(30).`|
| **66** | ধারা পুনঃনামকরণ (ডেটার বিকল্প দৃশ্য) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | স্বতন্ত্র প্রাথমিক আইটেম (কোন উপ-আইটেম নেই) | `77 WS-COUNTER PIC 9(5).`|
| **88** | অবস্থার নাম (বুলিয়ানের মতো পতাকা) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### কপি স্টেটমেন্ট (কপিবুক)
কপিবুক হল কোড পুনঃব্যবহারের জন্য COBOL-এর মেকানিজম — C-তে `#include`-এর মতো। এগুলি আলাদা সদস্য হিসাবে সংরক্ষণ করা হয় এবং কম্পাইলের সময় ঢোকানো হয়।
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

### পারফর্ম বৈচিত্র
COBOL কাঠামোগত প্রোগ্রামিংয়ের জন্য পারফর্ম স্টেটমেন্টের বিভিন্ন স্বাদ প্রদান করে।
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

### স্ট্রিং হ্যান্ডলিং এবং পরিদর্শন
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

## আর্কিটেকচার এবং সিস্টেম ডিজাইন
### চারটি বিভাগ
প্রতিটি COBOL প্রোগ্রাম চারটি বিভাগে বিভক্ত, প্রতিটি একটি স্বতন্ত্র উদ্দেশ্য পরিবেশন করে:
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

### প্রোগ্রামের অনুক্রম
COBOL সিস্টেমগুলি সাধারণত একটি প্রধান প্রোগ্রামের সাথে একটি কলিং অনুক্রম ব্যবহার করে যা সাবপ্রোগ্রামগুলিকে কল করে।
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

### সাধারণ প্রকল্প ডিরেক্টরি কাঠামো
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### GnuCOBOL (ওপেন-সোর্স COBOL কম্পাইলার)
GnuCOBOL (পূর্বে OpenCOBOL) COBOL কে C থেকে এবং তারপর নেটিভ মেশিন কোডে কম্পাইল করে, COBOL কে Linux, Windows এবং macOS-এ চালানোর জন্য সক্ষম করে।
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

### আইবিএম মেইনফ্রেম জেসিএল (চাকরি নিয়ন্ত্রণ ভাষা)
IBM মেইনফ্রেমগুলিতে, COBOL প্রোগ্রামগুলি JCL ব্যবহার করে সংকলিত এবং কার্যকর করা হয়।
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

### কম্পাইলার অপশন রেফারেন্স
| বিকল্প | বর্ণনা | উদাহরণ |
|---------|---------------|---------|
| `-free`| ফ্রি-ফরম্যাট উৎস (কোন কলাম সীমাবদ্ধতা নেই) | `cobc -free prog.cbl`|
| `-fixed`| স্থির বিন্যাস (প্রথাগত কলাম 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| অপ্টিমাইজেশান লেভেল 2 | `cobc -O2 prog.cbl`|
| `-g`| ডিবাগ তথ্য তৈরি করুন | `cobc -g prog.cbl`|
| `-std=cobol2014`| COBOL 2014 মান ব্যবহার করুন | `cobc -std=cobol2014 prog.cbl`|
| `-x`| বিল্ড এক্সিকিউটেবল (শুধু কম্পাইল নয়) | `cobc -x prog.cbl`|
| `-I`| কপিবুক অনুসন্ধান পথ | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| সমস্ত সতর্কতা সক্রিয় করুন | `cobc -Wall prog.cbl`|
---

## পরীক্ষা এবং ডিবাগিং
### COBOL ডিবাগার কৌশল
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

### gdb দিয়ে GnuCOBOL ডিবাগিং
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

### সাধারণ ডিবাগিং প্যাটার্ন
| সমস্যা | উপসর্গ | সমাধান |
|---------|---------|----------|
| কাটা ডেটা | ক্ষেত কাটা | PIC ধারার মাপ রেকর্ড লেআউটের সাথে মেলে |
| সংখ্যাগত ওভারফ্লো | ভুল হিসাব | যাচাই করুন PIC 9(n) এ যথেষ্ট সংখ্যা আছে |
| ফাইল স্থিতি ত্রুটি | WS-FILE-STATUS '00' নয় | ফাইল ডিডি নাম, পাথ, এবং অনুমতি পরীক্ষা করুন |
| অসীম লুপ | শেষ না হওয়া পর্যন্ত পারফর্ম করুন | যাচাই লুপ ভেরিয়েবল লুপের ভিতরে পরিবর্তিত হয়েছে |
| কল ব্যর্থতা | রিটার্নিং অ-শূন্য | LINKAGE SECTION কলিং প্রোগ্রামের সাথে মেলে দেখুন |
---

## ইন্টারঅপারেবিলিটি
### কল স্টেটমেন্ট — কলিং সাবপ্রোগ্রাম
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

### সি ইন্টারঅপারেবিলিটি (GnuCOBOL)
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

### ডেটাবেস সংযোগ (DB2/COBOL)
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: কন্ট্রোল ব্রেক সহ ব্যাচ প্রসেসিং
কন্ট্রোল ব্রেক প্যাটার্ন হল সবচেয়ে মৌলিক COBOL ডিজাইন প্যাটার্ন — একটি মূল ক্ষেত্র দ্বারা গোষ্ঠীভুক্ত রেকর্ড প্রক্রিয়াকরণ এবং সাবটোটাল তৈরি করা।
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

### প্যাটার্ন 2: সম্পাদনা/বৈধকরণ প্যাটার্ন
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

### প্যাটার্ন 3: টেবিল লুকআপ (ইন-মেমরি অ্যারে)
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### ফাইল I/O অপ্টিমাইজেশান
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

### ব্যাচ প্রসেসিং অপ্টিমাইজেশান
| টেকনিক | প্রভাব | বর্ণনা |
|------------|---------|---------------|
| **ব্লক I/O** | উচ্চ | শারীরিক I/O অপারেশন কমাতে ব্লক কন্টেইন্স ব্যবহার করুন |
| **সূচিবদ্ধ অ্যাক্সেস** | উচ্চ | র্যান্ডম-অ্যাক্সেস লুকআপের জন্য সূচকযুক্ত সংস্থা ব্যবহার করুন |
| **বাছাই/একত্রিত করুন** | মাঝারি | বড় ডেটাসেট অর্ডার করার জন্য SORT ক্রিয়া ব্যবহার করুন |
| **ডিসপ্লেকে ছোট করুন** | মাঝারি | ডিসপ্লে ব্যাচে ধীর; পরিবর্তে ফাইল লিখুন |
| **COMP/COMP-3** | মাঝারি | বাইনারি/প্যাকড ক্ষেত্রগুলি DISPLAY সাংখ্যিক | থেকে দ্রুত
| **বাফার টিউনিং** | মাঝারি | অনুক্রমিক ফাইল প্রক্রিয়াকরণের জন্য বাফার আকার টিউন করুন |
---

## স্থাপনা এবং বাস্তব-বিশ্ব ব্যবহার
### মেইনফ্রেম স্থাপনা (IBM z/OS)
মেইনফ্রেমে COBOL প্রোগ্রামগুলিকে পার্টিশন করা ডেটাসেটে (PDS) লোড মডিউল হিসাবে স্থাপন করা হয়। JCL কম্পাইলেশন, লিঙ্কিং এবং এক্সিকিউশন নিয়ন্ত্রণ করে।
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### বিতরণকৃত স্থাপনা (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### COBOL ব্যবহার করে বাস্তব-বিশ্বের শিল্প
| শিল্প | ব্যবহার | স্কেল |
|----------|-------|-------|
| **ব্যাংকিং** | লেনদেন প্রক্রিয়াকরণ, অ্যাকাউন্ট ব্যবস্থাপনা | এটিএম লেনদেনের ~85% প্রক্রিয়া |
| **বীমা** | নীতি প্রশাসন, দাবি প্রক্রিয়াকরণ | প্রধান বীমাকারীরা COBOL ব্যাকএন্ড চালায় |
| **সরকার** | সামাজিক নিরাপত্তা, ট্যাক্স প্রক্রিয়াকরণ, সুবিধা | ইউএস এসএসএ কোটি কোটি রেকর্ড প্রক্রিয়া করে |
| **স্বাস্থ্যসেবা** | রোগীর রেকর্ড, বিলিং সিস্টেম | উত্তরাধিকার হাসপাতাল তথ্য সিস্টেম |
| **খুচরা** | ইনভেন্টরি ম্যানেজমেন্ট, পয়েন্ট-অফ-সেল ব্যাকএন্ড | লিগ্যাসি সিস্টেম সহ বড় খুচরা বিক্রেতা |
| **টেলিকম** | বিলিং সিস্টেম, কল রেকর্ড প্রসেসিং | কল বিস্তারিত রেকর্ড প্রক্রিয়াকরণ |
---

## কখন COBOL ব্যবহার করবেন
| দৃশ্যকল্প | কেন COBOL | ভাল বিকল্প |
|------------|------------|---------|
| মেইনফ্রেম রক্ষণাবেক্ষণ | বিদ্যমান কোডবেস | — |
| ব্যাচ আর্থিক প্রক্রিয়াকরণ | প্রমাণিত, নির্ভরযোগ্য, সুনির্দিষ্ট দশমিক গণিত | জাভা, নতুন সিস্টেমের জন্য পাইথন |
| সরকারী উত্তরাধিকার ব্যবস্থা | বিদ্যমান কোডবেস | — |
| কম্পিউটিং ইতিহাস শেখা | প্রোগ্রামিং এর বিবর্তন বোঝা | — |
| নতুন ব্যবসায়িক অ্যাপ্লিকেশন | আধুনিক পছন্দ নয় | জাভা, সি#, পাইথন |
| ওয়েব/মোবাইল উন্নয়ন | উপযুক্ত নয় | জাভাস্ক্রিপ্ট, সুইফট, কোটলিন |
| ডেটা সায়েন্স / এমএল | উপযুক্ত নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: কেন COBOL এখনও 60+ বছর পরেও ব্যাঙ্কিংয়ে ব্যবহার করা হয়?
**A:** COBOL আনুমানিক 70-80% ব্যাঙ্কিং লেনদেন প্রক্রিয়া করে। কারণগুলি:
- বিশাল কোডবেস (লক্ষ লক্ষ লাইন) যা সঠিকভাবে কাজ করে
- চরম নির্ভরযোগ্যতা - এই সিস্টেমগুলি কয়েক দশক ধরে উৎপাদনে পরীক্ষা করা হয়েছে
- মাইগ্রেশনের খরচ এবং ঝুঁকি রক্ষণাবেক্ষণ খরচের চেয়ে বেশি
- COBOL-এর ভার্বস, ইংরেজির মতো সিনট্যাক্স স্ব-ডকুমেন্টিং
- ভাষাতে তৈরি দশমিক পাটিগণিত (কোন ফ্লোটিং-পয়েন্ট রাউন্ডিং ত্রুটি নেই)
### প্রশ্ন 2: কিভাবে COBOL ফ্লোটিং-পয়েন্ট ত্রুটি ছাড়া দশমিক পাটিগণিত পরিচালনা করে?
**A:** COBOL এর নির্দিষ্ট নির্ভুলতার সাথে স্থানীয় দশমিক প্রকার রয়েছে:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` হল একটি উহ্য দশমিক বিন্দু। COBOL কখনও অর্থের জন্য বাইনারি ফ্লোটিং-পয়েন্ট ব্যবহার করে না।
### প্রশ্ন 3: একটি COBOL প্রোগ্রামের গঠন কী?
**A:** প্রতিটি COBOL প্রোগ্রামের চারটি বিভাগ রয়েছে:
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

### প্রশ্ন 4: আমি কিভাবে COBOL-এ অনুক্রমিক ফাইলগুলি পড়ব এবং প্রক্রিয়া করব?
**A:** ফাইল প্রসেসিংয়ে COBOL এক্সেল:
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

### প্রশ্ন 5: আধুনিক COBOL ডেভেলপমেন্টের জন্য কি কি টুল পাওয়া যায়?
**A:** GnuCOBOL (ওপেন সোর্স), IBM Enterprise COBOL, মাইক্রো ফোকাস, এবং VS কোড এক্সটেনশনগুলি আধুনিক উন্নয়ন পরিবেশ প্রদান করে।`cobc -x program.cob`দিয়ে তৈরি করুন।
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি গ্রাহক প্রতিবেদন তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
গ্রাহকের রেকর্ড পড়ুন, মোট গণনা করুন এবং একটি ফর্ম্যাটেড রিপোর্ট তৈরি করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
COBOL এর ফাইল হ্যান্ডলিং এবং রিপোর্ট লেখার ক্ষমতা ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```cobol
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

**পদক্ষেপ 4: যাচাই করুন**
উৎস ডেটার বিপরীতে ক্রস-চেক মোট। প্রান্তের ক্ষেত্রে পরীক্ষা করুন (খালি ফাইল, শূন্য ব্যালেন্স)।
### সমস্যা 2: কন্ট্রোল ব্রেক সহ ব্যাচ প্রসেসিং
**ধাপ 1: সমস্যাটি বুঝুন**
বিভাগ দ্বারা গোষ্ঠীবদ্ধ প্রক্রিয়া লেনদেন, মুদ্রণ সাবটোটাল।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
কন্ট্রোল ব্রেক লজিক ব্যবহার করুন — গ্রুপ কী পরিবর্তন হলে সনাক্ত করুন।
**ধাপ 3: প্রয়োগ করুন**```cobol
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

**পদক্ষেপ 4: যাচাই করুন**
শেষ গ্রুপের মোট মুদ্রিত হয়েছে কিনা পরীক্ষা করুন। গ্রান্ড টোটাল ডিপার্টমেন্টের মোট যোগফলের সমতুল্য যাচাই করুন।
---

## সারাংশ
COBOL হল কম্পিউটিংয়ের প্রথম দশকের একটি উত্তরাধিকার যা সক্রিয় ব্যবহারে রয়ে গেছে কারণ প্রতিস্থাপন স্কেলে সম্ভব নয়। বিশ্বের ব্যাংকিং এবং সরকারী ব্যবস্থাগুলি কয়েক দশক ধরে নির্ভরযোগ্যভাবে পরিচালিত COBOL প্রোগ্রামগুলির উপর নির্ভর করে। যদিও COBOL সাধারণত আজ একটি নতুন প্রকল্পের জন্য নির্বাচিত হবে না, ভাষাটি বিশ্বব্যাপী অর্থায়নকে সমর্থন করে এমন অবকাঠামো বজায় রাখার জন্য গুরুত্বপূর্ণ। COBOL বিকাশকারীদের ঘাটতি এটিকে একটি লাভজনক স্থান করে তোলে।