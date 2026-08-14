---
# Metadata
title: "Scratch — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Scratch with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [scratch, common-mistakes, anti-patterns, pitfalls, visual-programming, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# خراش - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات و تله های موجود در Scratch را با اصلاحات فهرست می کند.
---

## 1. عدم استفاده از "Stop" برای پایان دادن به اسکریپت ها
```
❌ WRONG — script keeps running after game over
when green flag clicked
forever
    if <touching [edge v]?> then
        say [Game Over]
        // script continues!
    end
end

✅ CORRECT — use stop block
when green flag clicked
forever
    if <touching [edge v]?> then
        say [Game Over]
        stop [all v]
    end
end
```

---

## 2. کلون سردرگمی
```
❌ WRONG — modifying original sprite thinking it's a clone
when I start as a clone
change [score v] by (1)  // modifies global variable
// but "when green flag clicked" also runs on clones!

✅ CORRECT — separate clone logic from original
when green flag clicked
// setup code only

when I start as a clone
// clone-specific behavior only
```

---

## 3. زمان پخش
```
❌ WRONG — expecting immediate response
broadcast [jump v]
// code continues immediately, doesn't wait!

✅ CORRECT — use broadcast and wait
broadcast [jump v] and wait
// now waits for all recipients to finish
```

---

## 4. دامنه متغیر
```
❌ WRONG — using global variable when local needed
// All sprites share the variable "my variable"
// Sprite A changes it, Sprite B sees the change

✅ CORRECT — use "For this sprite only"
// Create variable as "For this sprite only"
// Each sprite has its own copy
```

---

## 5. حلقه های بی نهایت بدون بازده
```
❌ WRONG — freezes the program
when green flag clicked
forever
    // no wait or visual change
    // locks up the interface
end

✅ CORRECT — add a small wait
when green flag clicked
forever
    // do work
    wait (0.1) seconds
end
```

---

## خلاصه
تله‌های خراش: همیشه از "توقف" برای پایان دادن به بازی‌ها استفاده کنید، منطق کلون را از منطق اصلی اسپرایت جدا کنید، از "پخش و انتظار" برای ارتباط همزمان استفاده کنید، در صورت نیاز از متغیرهای خاص اسپرایت استفاده کنید و برای جلوگیری از انجماد، انتظارها را در حلقه‌های همیشه اضافه کنید. Scratch مفاهیم اساسی را آموزش می دهد - به مدل رویداد محور احترام بگذارید.