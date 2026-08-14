---
# Metadata
title: "Assembly Language — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Assembly language with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# زبان اسمبلی - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها در اسمبلی x86-64 را با اصلاحات فهرست می کند.
---

## 1. عدم حفظ رجیسترها
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

## 2. تراز پشته
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

## 3. Off-by-One در عملیات رشته
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

## 4. پاک نشدن بیت های بالایی
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

## 5. حلقه های بی نهایت از شرایط خروج از دست رفته
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

## خلاصه
تله‌های اسمبلی: حفظ ثبات‌های ذخیره‌شده توسط callee، حفظ تراز پشته 16 بایتی، شامل پایان‌دهنده‌های تهی در رشته‌ها، صریح بودن در مورد اندازه‌های عملوند، و همیشه شرایط خروج از حلقه را فراهم می‌کند. برنامه‌نویسی اسمبلی مستلزم درک سخت‌افزار در پایین‌ترین سطح است - هر دستورالعمل پیامدهایی برای ثبات‌ها، حافظه و پرچم‌ها دارد.