---
# Metadata
title: "COBOL — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in COBOL with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [cobol, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# COBOL — Common Mistakes & Anti-Patterns

This document catalogs the most common mistakes, traps, and anti-patterns in COBOL with corrections.

---

## 1. Not Using 88-Level Condition Names

```cobol
* ❌ WRONG — magic numbers
01  STATUS-CODE     PIC 9.
    88  STATUS-ACTIVE   VALUE 1.
    88  STATUS-INACTIVE VALUE 2.

IF STATUS-CODE = 1  * what does 1 mean?
```

```cobol
* ✅ CORRECT — use 88-level for readability
01  STATUS-CODE     PIC 9.
    88  STATUS-ACTIVE   VALUE 1.
    88  STATUS-INACTIVE VALUE 2.

IF STATUS-ACTIVE
    PERFORM PROCESS-RECORD
END-IF
```

---

## 2. Numeric Overflow

```cobol
* ❌ WRONG — field too small
01  TOTAL    PIC 9(4).  * max 9999
COMPUTE TOTAL = A + B.   * silent truncation if > 9999

* ✅ CORRECT — adequate size or check ON SIZE ERROR
01  TOTAL    PIC 9(10).
COMPUTE TOTAL = A + B
    ON SIZE ERROR
        DISPLAY "Overflow!"
END-COMPUTE
```

---

## 3. Not Initializing Variables

```cobol
* ❌ WRONG — uninitialized data
01  COUNTER  PIC 9(5).
* contains garbage from previous run

* ✅ CORRECT — VALUE clause
01  COUNTER  PIC 9(5) VALUE ZERO.
```

---

## 4. PERFORM Without Explicit Bounds

```cobol
* ❌ WRONG — unbounded PERFORM
PERFORM PROCESS-RECORD UNTIL EOF-FLAG = 'Y'.
* if EOF-FLAG never set, infinite loop

* ✅ CORRECT — bounded PERFORM
PERFORM PROCESS-RECORD
    VARYING I FROM 1 BY 1
    UNTIL I > MAX-RECORDS
END-PERFORM
```

---

## 5. Not Using Modern COBOL Features

```cobol
* ❌ WRONG — old-style COBOL
MOVE SPACES TO WS-NAME.
IF WS-NAME = SPACES
    DISPLAY "EMPTY"
END-IF.

* ✅ CORRECT — modern COBOL (2002+)
IF FUNCTION TRIM(WS-NAME) = ""
    DISPLAY "EMPTY"
END-IF
```

---

## Summary

COBOL's verbose syntax hides traps: magic numbers without 88-level condition names, numeric overflow from undersized PIC clauses, uninitialized variables, and unbounded PERFORM loops. Modern COBOL (2002+) adds FUNCTION TRIM, inline PERFORM, and other improvements. The COBOL way is: use 88-level condition names, check ON SIZE ERROR, initialize with VALUE, and bound all loops.
