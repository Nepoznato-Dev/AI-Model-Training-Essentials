<!--
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

-->
# স্ক্র্যাচ — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ স্ক্র্যাচ-এ সবচেয়ে সাধারণ ভুল এবং ফাঁদগুলি ক্যাটালগ করে৷
---

## 1. স্ক্রিপ্ট শেষ করতে "স্টপ" ব্যবহার করা হচ্ছে না
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

## 2. ক্লোন বিভ্রান্তি
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

## 3. সম্প্রচারের সময়
```
❌ WRONG — expecting immediate response
broadcast [jump v]
// code continues immediately, doesn't wait!

✅ CORRECT — use broadcast and wait
broadcast [jump v] and wait
// now waits for all recipients to finish
```

---

## 4. পরিবর্তনশীল স্কোপ
```
❌ WRONG — using global variable when local needed
// All sprites share the variable "my variable"
// Sprite A changes it, Sprite B sees the change

✅ CORRECT — use "For this sprite only"
// Create variable as "For this sprite only"
// Each sprite has its own copy
```

---

## 5. ফলন ছাড়াই অসীম লুপ
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

## সারাংশ
স্ক্র্যাচ ট্র্যাপ: গেমগুলি শেষ করতে সর্বদা "স্টপ" ব্যবহার করুন, মূল স্প্রাইট লজিক থেকে ক্লোন লজিক আলাদা করুন, সিঙ্ক্রোনাস যোগাযোগের জন্য "সম্প্রচার এবং অপেক্ষা করুন" ব্যবহার করুন, যখন প্রয়োজন হয় তখন স্প্রাইট-নির্দিষ্ট ভেরিয়েবল ব্যবহার করুন এবং জমাট প্রতিরোধ করতে চিরকালের লুপগুলিতে অপেক্ষা করুন৷ স্ক্র্যাচ মৌলিক ধারণা শেখায় — ইভেন্ট-চালিত মডেলকে সম্মান করুন।