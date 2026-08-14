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
# Assemblage — Modèles idiomatiques et meilleures pratiques
Ce guide couvre les modèles idiomatiques pour écrire du code Assembly propre et maintenable (focus x86/x64 avec syntaxe NASM).
---

## Constantes et macros nommées
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

## Accès aux données structurées
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

## S'inscrire Conventions & Prologue/Épilogue
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

## Étiquettes locales et organisation du code
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

## Modèles défensifs
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

## Résumé
Les idiomes d'assemblage mettent l'accent sur : les constantes nommées sur les nombres magiques, les macros pour les modèles répétés, les définitions de structures pour la disposition des données, le prologue/épilogue conforme à l'ABI, les étiquettes locales pour la lisibilité, la validation des entrées défensives et `xor`/`lea` pour des opérations efficaces. L'assemblage récompense avant tout la clarté : "si vous ne pouvez pas le lire, vous ne pouvez pas le déboguer à 3 heures du matin".