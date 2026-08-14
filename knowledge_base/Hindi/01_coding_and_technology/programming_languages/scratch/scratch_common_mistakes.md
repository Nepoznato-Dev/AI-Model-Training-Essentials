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

# स्क्रैच - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ स्क्रैच में सबसे आम गलतियों और जालों को सूचीबद्ध करता है।
---

## 1. स्क्रिप्ट को समाप्त करने के लिए "स्टॉप" का उपयोग न करना
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

## 2. क्लोन कन्फ्यूजन
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

## 3. प्रसारण समय
```
❌ WRONG — expecting immediate response
broadcast [jump v]
// code continues immediately, doesn't wait!

✅ CORRECT — use broadcast and wait
broadcast [jump v] and wait
// now waits for all recipients to finish
```

---

## 4. परिवर्तनीय दायरा
```
❌ WRONG — using global variable when local needed
// All sprites share the variable "my variable"
// Sprite A changes it, Sprite B sees the change

✅ CORRECT — use "For this sprite only"
// Create variable as "For this sprite only"
// Each sprite has its own copy
```

---

## 5. बिना उपज के अनंत लूप
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

## सारांश
स्क्रैच ट्रैप: गेम को समाप्त करने के लिए हमेशा "स्टॉप" का उपयोग करें, क्लोन लॉजिक को मूल स्प्राइट लॉजिक से अलग करें, सिंक्रोनस संचार के लिए "ब्रॉडकास्ट एंड वेट" का उपयोग करें, जरूरत पड़ने पर स्प्राइट-विशिष्ट वेरिएबल का उपयोग करें, और फ्रीजिंग को रोकने के लिए हमेशा के लिए लूप में वेट जोड़ें। स्क्रैच मौलिक अवधारणाएँ सिखाता है - घटना-संचालित मॉडल का सम्मान करें।