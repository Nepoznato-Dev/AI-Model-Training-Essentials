---
# Metadata
title: "Scratch — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Scratch with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# سکریچ - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز سکریچ میں سب سے عام غلطیوں اور ٹریپس کو درست کرنے کے ساتھ کیٹلاگ کرتا ہے۔
---

## 1. سکرپٹ کو ختم کرنے کے لیے "اسٹاپ" کا استعمال نہیں کرنا
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

## 2. کلون کنفیوژن
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

## 3. براڈکاسٹ ٹائمنگ
```
❌ WRONG — expecting immediate response
broadcast [jump v]
// code continues immediately, doesn't wait!

✅ CORRECT — use broadcast and wait
broadcast [jump v] and wait
// now waits for all recipients to finish
```

---

## 4. متغیر دائرہ کار
```
❌ WRONG — using global variable when local needed
// All sprites share the variable "my variable"
// Sprite A changes it, Sprite B sees the change

✅ CORRECT — use "For this sprite only"
// Create variable as "For this sprite only"
// Each sprite has its own copy
```

---

## 5. پیداوار کے بغیر لامحدود لوپس
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

## خلاصہ
سکریچ ٹریپس: گیمز کو ختم کرنے کے لیے ہمیشہ "اسٹاپ" کا استعمال کریں، کلون لاجک کو اصل اسپرائٹ لاجک سے الگ کریں، سنکرونس کمیونیکیشن کے لیے "براڈکاسٹ اور انتظار کریں" کا استعمال کریں، ضرورت پڑنے پر اسپرائٹ کے مخصوص متغیرات کا استعمال کریں، اور منجمد ہونے سے بچنے کے لیے ہمیشہ کے لیے لوپ میں انتظار شامل کریں۔ سکریچ بنیادی تصورات سکھاتا ہے — ایونٹ سے چلنے والے ماڈل کا احترام کریں۔