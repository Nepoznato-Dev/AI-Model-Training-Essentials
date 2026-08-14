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
# 어셈블리 언어 - 일반적인 실수 및 안티 패턴
이 문서에는 수정 사항이 포함된 x86-64 어셈블리의 가장 일반적인 실수, 트랩 및 안티 패턴이 나열되어 있습니다.
---

## 1. 레지스터를 보존하지 않음
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

## 2. 스택 정렬
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

## 3. 문자열 연산의 Off-by-One
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

## 4. 상위 비트를 지우지 않음
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

## 5. 종료 조건 누락으로 인한 무한 루프
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

## 요약
어셈블리 트랩: 호출 수신자가 저장한 레지스터를 보존하고, 16바이트 스택 정렬을 유지하고, 문자열에 Null 종결자를 포함하고, 피연산자 크기를 명시하고, 항상 루프 종료 조건을 제공합니다. 어셈블리 프로그래밍을 위해서는 가장 낮은 수준의 하드웨어를 이해해야 합니다. 모든 명령은 레지스터, 메모리 및 플래그에 영향을 미칩니다.