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
# COBOL - الگوهای اصطلاحی و بهترین شیوه ها
این راهنما الگوهای اصطلاحی برای نوشتن کد COBOL تمیز و مدرن را پوشش می دهد.
---

## COBOL مدرن
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

## بخش داده
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

## خلاصه
اصطلاحات COBOL بر این موارد تأکید دارند: نام‌های شرط سطح 88، موارد گروهی برای ساختار، و منبع با فرمت آزاد. استانداردهای COBOL سازمانی را دنبال کنید. COBOL به خوانایی و پردازش داده های کسب و کار گرا اهمیت می دهد.