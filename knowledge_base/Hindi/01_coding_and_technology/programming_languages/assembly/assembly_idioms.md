<!--
---
# Metadata
title: "Assembly — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, maintainable Assembly code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [assembly, x86, x64, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# असेंबली - मुहावरेदार पैटर्न और सर्वोत्तम प्रथाएँ
यह मार्गदर्शिका स्वच्छ, रखरखाव योग्य असेंबली कोड (NASM सिंटैक्स के साथ x86/x64 फोकस) लिखने के लिए मुहावरेदार पैटर्न को कवर करती है।
---

## नामित स्थिरांक और मैक्रोज़
```nasm
; ✅ Use named constants instead of magic numbers
SYS_EXIT    equ 1
SYS_READ    equ 0
STDOUT      equ 1
MAX_BUFFER  equ 4096

section .bss
    buffer  resb MAX_BUFFER

; ✅ Define macros for repeated patterns
%macro print_str 2
    mov     rax, 1          ; sys_write
    mov     rdi, 1          ; stdout
    mov     rsi, %1         ; string address
    mov     rdx, %2         ; string length
    syscall
%endmacro

; Usage:
print_str msg, msg_len
```

---

## संरचित डेटा एक्सेस
```nasm
; ✅ Define structs with offsets for clarity
struc Process
    .pid    resd 1
    .state  resb 1
    .priority resb 1
    .name   resb 64
endstruc

; ✅ Access fields by offset
mov     eax, [rbx + Process.pid]
mov     cl, [rbx + Process.state]
lea     rdi, [rbx + Process.name]

; ✅ Use SIZEOF for iteration bounds
mov     rcx, array_count
.process_loop:
    ; ... process array[rcx]
    loop    .process_loop
```

---

## कन्वेंशन और प्रस्तावना/उपसंहार पंजीकृत करें
```nasm
; ✅ Standard function prologue (System V AMD64 ABI)
my_function:
    push    rbp             ; save frame pointer
    mov     rbp, rsp        ; set up new frame
    push    rbx             ; save callee-saved regs
    push    r12
    sub     rsp, 32         ; allocate local space

    ; ... function body ...

.epilogue:
    add     rsp, 32         ; deallocate locals
    pop     r12             ; restore callee-saved regs
    pop     rbx
    mov     rsp, rbp        ; restore stack pointer
    pop     rbp
    ret

; ✅ Follow ABI: caller-saved = rax, rcx, rdx, rsi, rdi, r8-r11
; ✅ Follow ABI: callee-saved = rbx, rbp, r12-r15
```

---

## स्थानीय लेबल एवं कोड संगठन
```nasm
; ✅ Use local labels (dot-prefixed) for scope
memcpy_loop:
    mov     al, [rsi]
    mov     [rdi], al
    inc     rsi
    inc     rdi
    dec     rcx
    jnz     .continue       ; local label — scoped to memcpy_loop
    ret
.continue:
    cmp     rcx, 16
    jge     memcpy_loop     ; back to global label
    ; handle remaining bytes
    ret

; ✅ Organize code into sections clearly
section .data
    ; initialized data
section .bss
    ; uninitialized data
section .text
    global _start
_start:
    ; entry point
```

---

## रक्षात्मक पैटर्न
```nasm
; ✅ Validate inputs at function entry
parse_number:
    test    rdi, rdi        ; null pointer check
    jz      .error_null
    cmp     byte [rdi], 0   ; empty string check
    je      .error_empty

    ; ... parsing logic ...
    ret

.error_null:
    mov     rax, -1         ; return error code
    ret
.error_empty:
    mov     rax, -2
    ret

; ✅ Use XOR for zeroing (shorter, clears flags predictably)
xor     eax, eax        ; ✅ preferred over mov eax, 0
xor     ecx, ecx        ; loop counter = 0

; ✅ Use LEA for address arithmetic (no flags affected)
lea     rax, [rbx + rcx*4]  ; array indexing
```

---

## सारांश
असेंबली मुहावरे जोर देते हैं: जादुई संख्याओं पर नामित स्थिरांक, दोहराए गए पैटर्न के लिए मैक्रोज़, डेटा लेआउट के लिए संरचनात्मक परिभाषाएं, एबीआई-अनुरूप प्रस्तावना/उपसंहार, पठनीयता के लिए स्थानीय लेबल, रक्षात्मक इनपुट सत्यापन, और कुशल संचालन के लिए`xor`/ `lea`। असेंबली सबसे ऊपर स्पष्टता को पुरस्कृत करती है - "यदि आप इसे पढ़ नहीं सकते हैं, तो आप इसे सुबह 3 बजे डीबग नहीं कर सकते।"