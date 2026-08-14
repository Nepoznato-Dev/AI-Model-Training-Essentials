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

# COBOL — Yaygın Hatalar ve Anti-Kalıplar
Bu belge, COBOL'deki en yaygın hataları, tuzakları ve anti-kalıpları düzeltmelerle birlikte kataloglamaktadır.
---

## 1. 88 Seviyeli Koşul Adlarını Kullanmamak
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

## 2. Sayısal Taşma
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

## 3. Değişkenleri Başlatmamak
```cobol
* ❌ WRONG — uninitialized data
01  COUNTER  PIC 9(5).
* contains garbage from previous run

* ✅ CORRECT — VALUE clause
01  COUNTER  PIC 9(5) VALUE ZERO.
```

---

## 4. Açık Sınırlar Olmadan GERÇEKLEŞTİRİN
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

## 5. Modern COBOL Özelliklerini Kullanmamak
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

## Özet
COBOL'un ayrıntılı sözdizimi tuzakları gizler: 88 düzeyli koşul adları olmayan sihirli sayılar, küçük boyutlu PIC yan tümcelerinden sayısal taşma, başlatılmamış değişkenler ve sınırsız PERFORM döngüleri. Modern COBOL (2002+), FUNCTION TRIM, satır içi PERFORM ve diğer iyileştirmeleri ekler. COBOL yöntemi şu şekildedir: 88 seviyeli koşul adlarını kullanın, AÇIK BOYUT HATASI'nı kontrol edin, VALUE ile başlatın ve tüm döngüleri bağlayın.