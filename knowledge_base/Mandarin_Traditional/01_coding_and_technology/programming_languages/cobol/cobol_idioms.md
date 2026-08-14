<!--
---
# Metadata
title: "COBOL — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern COBOL code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [cobol, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# COBOL — 慣用模式與最佳實踐
本指南涵蓋了編寫簡潔、現代 COBOL 程式碼的慣用模式。
---

## 現代 COBOL
```cobol
       *> ✅ Free-format (COBOL 2002+)
       identification division.
       program-id. hello-world.
       
       data division.
       working-storage section.
       01 ws-name    pic x(50).
       01 ws-age     pic 999.
       01 ws-salary  pic 99999.99.
       
       procedure division.
           display "Hello, World!"
           accept ws-name
           display "Hello, " ws-name
           stop run.
```

---

## 資料部門
```cobol
       *> ✅ 88-level condition names
       01 ws-status pic x.
           88 status-active  value "A".
           88 status-inactive value "I".
       
       if status-active
           display "User is active"
       end-if
       
       *> ✅ Group items for structure
       01 ws-user.
           05 ws-user-id    pic 9(10).
           05 ws-user-name  pic x(50).
           05 ws-user-email pic x(100).
```

---

＃＃ 概括
COBOL 習慣用法強調：88 層級條件名稱、結構組項目和自由格式來源。遵循企業 COBOL 標準。 COBOL 重視可讀性和以業務為導向的資料處理。