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

# アセンブリ言語 — よくある間違いとアンチパターン
このドキュメントでは、x86-64 アセンブリにおける最も一般的な間違い、罠、およびアンチパターンを修正とともにカタログ化します。
---

## 1. レジスタを保持しない
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

## 2. スタックのアライメント
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

## 3. 文字列操作におけるオフバイワン
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

## 4. 上位ビットをクリアしない
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

## 5. 終了条件の欠落による無限ループ
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

＃＃ まとめ
アセンブリ トラップ: 呼び出し先が保存したレジスタを保持し、16 バイトのスタック アライメントを維持し、文字列に null ターミネータを含め、オペランドのサイズを明示し、常にループ終了条件を提供します。アセンブリ プログラミングでは、ハードウェアを最低レベルで理解する必要があります。すべての命令はレジスタ、メモリ、フラグに影響を与えます。