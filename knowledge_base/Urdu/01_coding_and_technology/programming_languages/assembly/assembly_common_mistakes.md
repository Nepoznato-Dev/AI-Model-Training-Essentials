<!--
---
# Metadata
title: "Assembly Language — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Assembly language with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [assembly, common-mistakes, anti-patterns, pitfalls, x86-64, coding-and-technology]
difficulty_level: "advanced"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# اسمبلی کی زبان — عام غلطیاں اور مخالف پیٹرن
یہ دستاویز تصحیح کے ساتھ x86-64 اسمبلی میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کی فہرست بناتی ہے۔
---

## 1. رجسٹروں کو محفوظ نہیں کرنا
```asm
; ❌ WRONG — clobbering caller-saved registers
my_function:
    mov rbx, rax    ; rbx is callee-saved!
    ; ... use rbx ...
    ret             ; rbx is now corrupted

; ✅ CORRECT — preserve callee-saved registers (rbx, rbp, r12-r15)
my_function:
    push rbx        ; save
    mov rbx, rax
    ; ... use rbx ...
    pop rbx         ; restore
    ret
```

---

## 2. اسٹیک الائنمنٹ
```asm
; ❌ WRONG — misaligned stack (crashes on SSE/AVX)
my_function:
    sub rsp, 8      ; stack now misaligned
    movdqa [rsp], xmm0  ; segfault!

; ✅ CORRECT — maintain 16-byte alignment
my_function:
    push rbp
    mov rbp, rsp
    sub rsp, 16     ; aligned to 16 bytes
    movdqa [rsp], xmm0  ; works
```

---

## 3. سٹرنگ آپریشنز میں ایک دوسرے سے الگ
```asm
; ❌ WRONG — forgetting null terminator
    mov rsi, source
    mov rdi, dest
    mov rcx, 10
    rep movsb       ; copies 10 bytes, no null terminator!

; ✅ CORRECT — include null terminator
    mov rcx, 11     ; 10 chars + null
    rep movsb
```

---

## 4. اوپری بٹس کو صاف نہیں کرنا
```asm
; ❌ WRONG — upper bits may contain garbage
    mov eax, 42     ; sets rax to 42 (zero-extends to 64 bits)
    mov al, 0xFF    ; only sets low byte, upper bits of rax unchanged!

; ✅ CORRECT — be explicit about sizes
    movzx eax, al   ; zero-extend al to eax
    ; or
    mov rax, 0      ; clear first, then set low byte
    mov al, 0xFF
```

---

## 5. لاپتہ ایگزٹ کنڈیشن سے لامحدود لوپس
```asm
; ❌ WRONG — no exit condition
.loop:
    ; do work
    jmp .loop       ; infinite!

; ✅ CORRECT — check condition
.loop:
    ; do work
    dec rcx
    jnz .loop       ; exits when rcx = 0
```

---

## خلاصہ
اسمبلی ٹریپس: کالی محفوظ شدہ رجسٹروں کو محفوظ رکھیں، 16 بائٹ اسٹیک الائنمنٹ کو برقرار رکھیں، سٹرنگز میں نال ٹرمینیٹرز شامل کریں، آپرینڈ سائز کے بارے میں واضح رہیں، اور ہمیشہ لوپ سے باہر نکلنے کے حالات فراہم کریں۔ اسمبلی پروگرامنگ کے لیے ہارڈ ویئر کو سب سے نچلی سطح پر سمجھنے کی ضرورت ہوتی ہے - ہر ہدایت کے رجسٹر، میموری اور جھنڈوں کے لیے نتائج ہوتے ہیں۔