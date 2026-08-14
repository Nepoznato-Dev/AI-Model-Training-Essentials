<!--
---
# Metadata
title: "COBOL — Cheat Sheet"
description: "Quick-reference cheat sheet for COBOL syntax, data divisions, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [cobol, mainframe, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# COBOL — Hoja de referencia
## Estructura del programa
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.
       AUTHOR. AI-TEAM.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INPUT-FILE ASSIGN TO 'data.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD INPUT-FILE.
       01 INPUT-RECORD.
           05 NAME-FIELD     PIC X(30).
           05 AMOUNT-FIELD   PIC 9(7)V99.

       WORKING-STORAGE SECTION.
       01 WS-COUNTER         PIC 9(5) VALUE 0.
       01 WS-TOTAL           PIC 9(9)V99 VALUE 0.
       01 WS-EOF             PIC X VALUE 'N'.
           88 EOF-FLAG       VALUE 'Y'.
       01 WS-DISPLAY-AMT     PIC $$$,$$$,$$9.99.
       01 WS-MSG             PIC X(50).
```

## Tipos de datos
```cobol
       * Numeric
       01 WS-INTEGER         PIC 9(5).           *> 00000-99999
       01 WS-SIGNED          PIC S9(5).          *> signed
       01 WS-DECIMAL         PIC 9(7)V99.        *> 7 digits, 2 decimal
       01 WS-DISPLAY-NUM     PIC +Z(6)9.99.      *> formatted
       01 WS-CURRENCY        PIC $$$$,$$$,$$9.99. *> currency
       01 WS-ZEROS           PIC Z(9).            *> zero-suppressed

       * Alphanumeric
       01 WS-NAME            PIC X(30).           *> 30 chars
       01 WS-CODE            PIC X(3).            *> 3 chars
       01 WS-INITIAL         PIC X.               *> 1 char

       * Group items
       01 WS-EMPLOYEE.
           05 EMP-ID         PIC 9(6).
           05 EMP-NAME.
               10 EMP-FIRST   PIC X(20).
               10 EMP-LAST    PIC X(20).
           05 EMP-DEPT       PIC X(10).
           05 EMP-SALARY     PIC 9(7)V99.

       * 88-level (condition names)
       01 WS-STATUS          PIC X.
           88 STATUS-ACTIVE  VALUE 'A'.
           88 STATUS-INACTIVE VALUE 'I'.
           88 STATUS-DELETED VALUE 'D'.

       * COMP / BINARY
       01 WS-BINARY          PIC 9(9) COMP.
       01 WS-BINARY-LONG     PIC S9(18) COMP-3.
```

## Controlar el flujo
```cobol
       * IF
       IF WS-AGE >= 18
           DISPLAY "Adult"
       ELSE IF WS-AGE >= 13
           DISPLAY "Teen"
       ELSE
           DISPLAY "Child"
       END-IF

       * EVALUATE (switch)
       EVALUATE TRUE
           WHEN WS-AGE >= 65
               DISPLAY "Senior"
           WHEN WS-AGE >= 18
               DISPLAY "Adult"
           WHEN OTHER
               DISPLAY "Minor"
       END-EVALUATE

       EVALUATE WS-STATUS
           WHEN 'A'
               PERFORM PROCESS-ACTIVE
           WHEN 'I'
               PERFORM PROCESS-INACTIVE
           WHEN OTHER
               DISPLAY "Unknown status"
       END-EVALUATE

       * PERFORM (loops)
       PERFORM VARYING I FROM 1 BY 1
               UNTIL I > 10
           DISPLAY I
       END-PERFORM

       PERFORM UNTIL EOF-FLAG
           READ INPUT-FILE
               AT END SET EOF-FLAG TO TRUE
               NOT AT END
                   ADD 1 TO WS-COUNTER
                   PERFORM PROCESS-RECORD
           END-READ
       END-PERFORM

       * Paragraphs
       PERFORM 100-INITIALIZE.
       PERFORM 200-PROCESS.
       PERFORM 300-CLEANUP.

       * Inline PERFORM
       PERFORM
           DISPLAY "Processing..."
           ADD 1 TO WS-COUNTER
       END-PERFORM
```

## Operaciones de cadena
```cobol
       * MOVE
       MOVE "Alice" TO WS-NAME.
       MOVE 42 TO WS-INTEGER.
       MOVE WS-AMOUNT TO WS-DISPLAY-AMT.

       * String concatenation
       STRING WS-FIRST DELIMITED BY SIZE
              " " DELIMITED BY SIZE
              WS-LAST DELIMITED BY SIZE
              INTO WS-FULL-NAME.

       * UNSTRING (split)
       UNSTRING WS-FULL-NAME DELIMITED BY " "
           INTO WS-FIRST WS-LAST.

       * INSPECT
       INSPECT WS-NAME TALLYING WS-COUNT
           FOR CHARACTERS.
       INSPECT WS-NAME REPLACING ALL " " BY "_".
       INSPECT WS-TEXT CONVERTING "abcdef"
           TO "ABCDEF".

       * Reference modification
       WS-NAME (1:3)                    *> first 3 chars
       WS-NAME (LENGTH OF WS-NAME:1)    *> last char

       * Intrinsic functions
       FUNCTION LENGTH(WS-NAME)
       FUNCTION UPPER-CASE(WS-NAME)
       FUNCTION LOWER-CASE(WS-NAME)
       FUNCTION TRIM(WS-NAME)
       FUNCTION REVERSE(WS-NAME)
       FUNCTION SUBSTITUTE(WS-NAME "Alice" "Bob")
```

## E/S de archivos
```cobol
       * Sequential read
       OPEN INPUT INPUT-FILE.
       PERFORM UNTIL EOF-FLAG
           READ INPUT-FILE
               AT END SET EOF-FLAG TO TRUE
               NOT AT END
                   DISPLAY NAME-FIELD AMOUNT-FIELD
           END-READ
       END-PERFORM.
       CLOSE INPUT-FILE.

       * Sequential write
       OPEN OUTPUT OUTPUT-FILE.
       MOVE "Alice" TO OUT-NAME.
       MOVE 1000.00 TO OUT-AMOUNT.
       WRITE OUTPUT-RECORD.
       CLOSE OUTPUT-FILE.

       * Indexed file (random access)
       SELECT CUST-FILE ASSIGN TO 'customers.dat'
           ORGANIZATION IS INDEXED
           ACCESS MODE IS DYNAMIC
           RECORD KEY IS CUST-ID.

       READ CUST-FILE INVALID KEY
           DISPLAY "Not found"
       END-READ.
```

## Manejo de errores
```cobol
       * File status
       01 WS-FILE-STATUS PIC XX.

       READ INPUT-FILE
           INVALID KEY DISPLAY "Read error"
           NOT INVALID KEY PERFORM PROCESS
       END-READ.

       * EC (exception class)
       READ INPUT-FILE
           AT END SET EOF-FLAG TO TRUE
           NOT AT END PERFORM PROCESS-RECORD
       END-READ.

       * GOBACK / STOP RUN
       GOBACK.          *> return from called program
       STOP RUN.        *> terminate
```
