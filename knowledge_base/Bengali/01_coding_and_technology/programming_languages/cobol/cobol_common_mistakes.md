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

# COBOL — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ COBOL-এর সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1. 88-স্তরের অবস্থার নাম ব্যবহার করা হচ্ছে না
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

## 2. সংখ্যাসূচক ওভারফ্লো
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

## 3. ভেরিয়েবল শুরু করা হচ্ছে না
```cobol
* ❌ WRONG — uninitialized data
01  COUNTER  PIC 9(5).
* contains garbage from previous run

* ✅ CORRECT — VALUE clause
01  COUNTER  PIC 9(5) VALUE ZERO.
```

---

## 4. স্পষ্ট সীমানা ছাড়াই পারফর্ম করুন
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

## 5. আধুনিক COBOL বৈশিষ্ট্য ব্যবহার না করা
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

## সারাংশ
COBOL-এর ভার্বোস সিনট্যাক্স ফাঁদগুলিকে লুকিয়ে রাখে: 88-স্তরের কন্ডিশনের নাম ছাড়াই ম্যাজিক সংখ্যা, আন্ডারসাইজড PIC ক্লজ থেকে সাংখ্যিক ওভারফ্লো, অপ্রচলিত ভেরিয়েবল, এবং সীমাহীন পারফর্ম লুপ। আধুনিক COBOL (2002+) ফাংশন ট্রিম, ইনলাইন পারফর্ম এবং অন্যান্য উন্নতি যোগ করে। COBOL উপায় হল: 88-স্তরের অবস্থার নাম ব্যবহার করুন, সাইজ ত্রুটি পরীক্ষা করুন, মান দিয়ে আরম্ভ করুন এবং সমস্ত লুপকে আবদ্ধ করুন।