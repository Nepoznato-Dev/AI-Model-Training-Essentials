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

# COBOL — Những lỗi thường gặp và các mẫu chống đối
Tài liệu này liệt kê các lỗi, bẫy và phản mẫu phổ biến nhất trong COBOL kèm theo các bản sửa lỗi.
---

## 1. Không sử dụng tên điều kiện cấp 88
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

## 2. Tràn số
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

## 3. Không khởi tạo biến
```cobol
* ❌ WRONG — uninitialized data
01  COUNTER  PIC 9(5).
* contains garbage from previous run

* ✅ CORRECT — VALUE clause
01  COUNTER  PIC 9(5) VALUE ZERO.
```

---

## 4. THỰC HIỆN KHÔNG GIỚI HẠN
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

## 5. Không sử dụng các tính năng COBOL hiện đại
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

## Bản tóm tắt
Cú pháp dài dòng của COBOL che giấu các bẫy: các số ma thuật không có tên điều kiện cấp 88, tràn số từ các mệnh đề PIC có kích thước nhỏ, các biến chưa được khởi tạo và các vòng lặp PERFORM không giới hạn. COBOL hiện đại (2002+) bổ sung CHỨC NĂNG TRIM, HIỆU SUẤT nội tuyến và các cải tiến khác. Cách COBOL là: sử dụng tên điều kiện cấp 88, kiểm tra LỖI KÍCH THƯỚC, khởi tạo bằng VALUE và ràng buộc tất cả các vòng lặp.