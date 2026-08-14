<!--
---
# Metadata
title: "COBOL — Syntax Reference"
description: "Detailed syntax reference for COBOL covering divisions, data descriptions, file handling, report generation, and business processing patterns."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [cobol, syntax-reference, data-divisions, file-handling, business-logic, mainframe, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# COBOL - সিনট্যাক্স রেফারেন্স
এই নথিটি COBOL (2014+) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, ডেটা বর্ণনা, ফাইল প্রসেসিং এবং ব্যবসায়িক যুক্তিতে ফোকাস করে প্রধান COBOL রেফারেন্সের পরিপূরক।
---

## প্রোগ্রামের কাঠামো
```cobol
       IDENTIFICATION DIVISION.
           PROGRAM-ID. PROGRAM-NAME.
           AUTHOR. DEVELOPER.
           DATE-WRITTEN. 2026-08-09.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT FILE-NAME ASSIGN TO 'filename.dat'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD FILE-NAME.
       01 RECORD-NAME.
           05 FIELD-1    PIC X(20).
           05 FIELD-2    PIC 9(5)V99.

       WORKING-STORAGE SECTION.
       01 WS-COUNTER     PIC 9(5) VALUE 0.
       01 WS-EOF         PIC X VALUE 'N'.
       01 WS-TOTAL       PIC 9(9)V99 VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM INIT-PARA
           PERFORM PROCESS-PARA
               UNTIL WS-EOF = 'Y'
           PERFORM CLEANUP-PARA
           STOP RUN.
```

---

## ডেটা বর্ণনা
```cobol
       *> Numeric types
       01 WS-INTEGER       PIC 9(5).           *> 00000 to 99999
       01 WS-DECIMAL       PIC 9(5)V99.        *> 99999.99
       01 WS-SIGNED        PIC S9(5).          *> -99999 to 99999
       01 WS-DISPLAY       PIC +Z(4)9.99.      *> formatted output

       *> Character types
       01 WS-NAME          PIC X(30).          *> 30 characters
       01 WS-CODE          PIC X(3).           *> 3 characters

       *> Group items
       01 WS-EMPLOYEE.
           05 WS-EMP-ID    PIC 9(6).
           05 WS-EMP-NAME.
               10 WS-FIRST  PIC X(15).
               10 WS-LAST   PIC X(15).
           05 WS-SALARY    PIC 9(7)V99.

       *> Constants
       01 WS-PI            CONSTANT AS 3.14159265.
       01 WS-MAX-RETRIES   CONSTANT AS 3.

       *> Condition names (88-level)
       01 WS-STATUS        PIC X.
           88 STATUS-ACTIVE    VALUE 'A'.
           88 STATUS-INACTIVE  VALUE 'I'.
           88 STATUS-PENDING   VALUE 'P'.
```

---

## নিয়ন্ত্রণ প্রবাহ
```cobol
       *> if / else
       IF WS-AGE >= 18
           DISPLAY "Adult"
       ELSE IF WS-AGE >= 13
           DISPLAY "Teenager"
       ELSE
           DISPLAY "Child"
       END-IF

       *> EVALUATE (switch/case)
       EVALUATE WS-STATUS
           WHEN 'A'
               PERFORM ACTIVE-LOGIC
           WHEN 'I'
               PERFORM INACTIVE-LOGIC
           WHEN OTHER
               DISPLAY "Unknown status"
       END-EVALUATE

       *> PERFORM (loop)
       PERFORM VARYING I FROM 1 BY 1
               UNTIL I > 10
           DISPLAY I
       END-PERFORM

       *> PERFORM UNTIL
       PERFORM UNTIL WS-EOF = 'Y'
           READ INPUT-FILE
               AT END MOVE 'Y' TO WS-EOF
               NOT AT END
                   PERFORM PROCESS-RECORD
           END-READ
       END-PERFORM
```

---

## ফাইল অপারেশন
```cobol
       *> Open / Close
       OPEN INPUT CUSTOMER-FILE
       OPEN OUTPUT REPORT-FILE
       CLOSE CUSTOMER-FILE

       *> Sequential read
       READ CUSTOMER-FILE
           AT END
               MOVE 'Y' TO WS-EOF
           NOT AT END
               ADD CUST-BALANCE TO WS-TOTAL
       END-READ

       *> Write
       WRITE REPORT-RECORD FROM WS-OUTPUT-LINE

       *> String operations
       STRING WS-FIRST DELIMITED BY SPACE
              ' ' DELIMITED BY SIZE
              WS-LAST DELIMITED BY SPACE
              INTO WS-FULL-NAME
       END-STRING

       UNSTRING WS-FULL-NAME DELIMITED BY SPACE
           INTO WS-FIRST WS-LAST
       END-UNSTRING
```

---

## পাটিগণিত
```cobol
       *> COMPUTE
       COMPUTE WS-TOTAL = WS-PRICE * WS-QUANTITY
       COMPUTE WS-TAX = WS-TOTAL * 0.08
       COMPUTE WS-GRAND = WS-TOTAL + WS-TAX

       *> ADD / SUBTRACT / MULTIPLY / DIVIDE
       ADD WS-AMOUNT TO WS-BALANCE
       SUBTRACT WS-DISCOUNT FROM WS-PRICE
       MULTIPLY WS-RATE BY WS-AMOUNT GIVING WS-RESULT
       DIVIDE WS-TOTAL BY WS-COUNT GIVING WS-AVG
           REMAINDER WS-REM

       *> INSPECT (string operations)
       INSPECT WS-TEXT TALLYING WS-COUNT
           FOR ALL 'ERROR'
       INSPECT WS-TEXT REPLACING ALL 'OLD' BY 'NEW'
```

---

## সারাংশ
COBOL-এর সিনট্যাক্সটি ডিজাইন অনুসারে ভার্বস - প্রতিটি বিবৃতি ইংরেজির মতো পড়ে। পিআইসি ক্লজ সহ ডেটা বিবরণ ক্ষেত্র বিন্যাসকে সুনির্দিষ্টভাবে সংজ্ঞায়িত করে। চার-বিভাগের কাঠামো উদ্বেগের বিচ্ছেদ কার্যকর করে। ফাইল হ্যান্ডলিং ভাষায় নির্মিত হয়. ব্যবসায়িক তথ্য প্রক্রিয়াকরণের জন্য, COBOL-এর দশমিক পাটিগণিত এবং রেকর্ড-ভিত্তিক I/O তুলনাহীন থাকে। COBOL বোঝার অর্থ হল এন্টারপ্রাইজ কম্পিউটিং এর ভিত্তি বোঝা।