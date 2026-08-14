---
# Metadata
title: "Assembly Language — Version History & Evolution"
description: "Comprehensive version history and evolution of Assembly language from early machines to modern x86/ARM."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [assembly, x86, arm, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# اسمبلی کی زبان - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| دور | سال | کلیدی تھیم |
|------|------|------------|
| 1940 کی دہائی | 1945 | مشین کوڈ - ٹوگل سوئچز، پیپر ٹیپ |
| 1949 | 1949 | **پہلا جمع کرنے والا** (ولکس، وہیلر، گل — ای ڈی ایس اے سی) |
| 1950 کی دہائی | 1951 | گریس ہوپر کا A-0 - پہلا "مرتب" (میکرو اسمبلر) |
| 1957 | 1957 | SOAP (علامتی بہترین اسمبلی پروگرام) IBM 650 کے لیے |
| 1960 کی دہائی | 1960 | BAL (بنیادی اسمبلی لینگویج) IBM System/360 کے لیے |
| 1978 | 1978 | **Intel 8086** — x86 فن تعمیر کی پیدائش |
| 1980 کی دہائی | 1981 | IBM PC - x86 اسمبلی PC پروگرامنگ پر حاوی ہے |
| 1985 | 1985 | **Intel 386** — 32-bit x86، محفوظ وضع |
| 1993 | 1993 | **انٹیل پینٹیم** — سپر اسکیلر، MMX بعد میں |
| 1997 | 1997 | MMX ہدایات (ملٹی میڈیا) |
| 1999 | 1999 | SSE (سٹریمنگ سم ڈی ایکسٹینشنز) |
| 2000 | 2000 | **AMD64** — 64 بٹ x86 ایکسٹینشن |
| 2001 | 2001 | **ARM** موبائل پر غلبہ حاصل کرتا ہے |
| 2005 | 2005 | SSE3، ڈوئل کور پروسیسرز |
| 2006 | 2006 | **x86-64** — 64 بٹ معیاری بن جاتا ہے۔
| 2011 | 2011 | **AVX** (ایڈوانسڈ ویکٹر ایکسٹینشنز) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-bit ARM |
| 2017 | 2017 | **AVX-512** — 512 بٹ ویکٹر آپریشنز |
| 2020 | 2020 | **Apple M1** — ARM64 ڈیسک ٹاپ پر |
| 2023 | 2023 | **AVX-VNNI** — AI/ML ایکسلریشن |
| 2024 | 2024 | **RISC-V** نے کرشن حاصل کیا — کھولیں ISA |
## اہم سنگ میل
### مشین کوڈ کا دور (1940-1950)
- **1945**: ENIAC پلگ بورڈز اور سوئچز کے ذریعے پروگرام کیا گیا
- **1949**: EDSAC - پہلا ذخیرہ شدہ پروگرام کمپیوٹر؛ پہلا "اسمبلر" (ابتدائی احکامات)
- **1951**: Grace Hopper's A-0 - مشینی کوڈ میں ریاضیاتی اشارے کا ترجمہ کرتا ہے
- **1957**: SOAP - سب سے پہلے بڑے پیمانے پر استعمال ہونے والا علامتی اسمبلر (IBM 650)
### x86 اسمبلی (1978–موجودہ)
- **1978**: Intel 8086 — x86 فن تعمیر کی پیدائش
  - 16 بٹ رجسٹر: AX، BX، CX، DX، SI، DI، SP، BP
  - منقسم میموری: CS, DS, SS, ES
  - ہدایات: MOV، ADD، SUB، JMP، کال، RET، INT
- **1985**: Intel 386 — 32-bit x86 (IA-32)
  - 32 بٹ رجسٹر: EAX، EBX، ECX، EDX
  - پروٹیکٹڈ موڈ، پیجنگ، ورچوئل میموری
- **2000**: AMD64 — 64 بٹ x86 ایکسٹینشن
  - 64 بٹ رجسٹر: RAX، RBX، RCX، RDX
  - 16 عام مقصد والے رجسٹر (بمقابلہ 8 32 بٹ میں)
  - RIP رشتہ دار ایڈریسنگ
### ARM اسمبلی (1985–موجودہ)
- **1985**: ARM1 — Acorn Computers (UK)
  - RISC فلسفہ: سادہ، مقررہ لمبائی کی ہدایات
  - لوڈ/اسٹور فن تعمیر
  - 16 رجسٹر (R0-R15)، R13=SP، R14=LR، R15=PC
- **2013**: ARM64 (AArch64) — 64-bit ARM
  - 31 عام مقصد کے 64 بٹ رجسٹر
  - سمڈ: نیین، ایس وی ای
  - اس میں استعمال کیا جاتا ہے: اسمارٹ فونز، Apple Silicon، AWS Graviton
### RISC-V (2010–موجودہ)
- **2010**: UC برکلے نے کھلا ISA بنایا
- **2020s**: RISC-V نے کرشن حاصل کیا - کھلا، کوئی لائسنسنگ فیس نہیں
- اس میں استعمال کیا جاتا ہے: ایمبیڈڈ سسٹمز، کسٹم چپس، چین کا سیمی کنڈکٹر پش
## نحوی ارتقاء
```asm
; 1978: Intel 8086 — 16-bit x86
MOV AX, 0x1234    ; load immediate into AX
MOV BX, AX        ; copy AX to BX
ADD AX, BX        ; AX = AX + BX
JMP loop_start    ; unconditional jump
INT 0x21          ; DOS interrupt (system call)

; 1985: Intel 386 — 32-bit x86
MOV EAX, 0x12345678  ; 32-bit register
PUSH EBP             ; save frame pointer
MOV EBP, ESP         ; set up stack frame
CALL printf          ; call C function
ADD ESP, 4           ; clean up stack

; 2006: x86-64 — 64-bit
MOV RAX, 0x123456789ABCDEF0  ; 64-bit register
MOV RDI, RSP                  ; RDI = first argument (System V ABI)
CALL puts                     ; call C function
SYSCALL                       ; Linux system call (instead of INT)

; ARM32 assembly
MOV R0, #42          ; load immediate
LDR R1, [R2, #4]    ; load from memory (R2 + 4)
ADD R0, R0, R1      ; R0 = R0 + R1
BL printf            ; branch with link (call)
BX LR                ; return

; ARM64 (AArch64) assembly
MOV X0, #42          ; 64-bit register
LDR X1, [X2, #8]    ; 64-bit load
ADD X0, X0, X1      ; 64-bit add
BL printf            ; branch with link
RET                  ; return

; RISC-V assembly
LI a0, 42            ; load immediate
LW a1, 8(a2)         ; load word from memory
ADD a0, a0, a1       ; add
CALL printf           ; call function
RET                   ; return
```

## انسٹرکشن سیٹ ایوولوشن
```
1978: 8086 — basic arithmetic, string ops, interrupts
1985: 386 — 32-bit, protected mode, paging
1997: MMX — SIMD for multimedia (64-bit)
1999: SSE — 128-bit SIMD, floating-point
2001: SSE2 — integer SIMD
2006: x86-64 — 64-bit, 16 GPRs
2008: SSE4 — string comparison, popcount
2011: AVX — 256-bit SIMD, 3-operand instructions
2013: AVX2 — gather, FMA
2017: AVX-512 — 512-bit SIMD (Xeon, server)
2020: AVX-VNNI — neural network instructions
2023: AMX — Advanced Matrix Extensions (AI acceleration)
```

## ڈیزائن کے کلیدی اصول
```
CISC (x86):
1. "Complex instructions" — one instruction can do a lot
2. "Variable length" — instructions are 1-15 bytes
3. "Memory-to-memory" — operate directly on memory
4. "Backward compatible" — 40+ years of code still runs

RISC (ARM, RISC-V):
5. "Simple instructions" — one instruction does one thing
6. "Fixed length" — all instructions same size (ARM: 32-bit)
7. "Load/store" — only load/store access memory
8. "Registers" — operate on registers, not memory
```

## ماحولیاتی نظام کی نمو
```
1940s: Machine code — toggle switches
1949: First assembler (EDSAC)
1957: SOAP — symbolic assembly
1978: x86 — IBM PC standard
1985: ARM — RISC for embedded
2000: AMD64 — 64-bit x86
2013: ARM64 — 64-bit ARM, mobile + server
2020: Apple M1 — ARM64 on desktop
2023: RISC-V — open ISA gains traction
2025: Assembly still used in:
       - OS kernels (boot code, context switching)
       - Device drivers (hardware access)
       - Compilers (code generation output)
       - Reverse engineering / security research
       - Embedded systems (resource-constrained)
       - Performance-critical code (SIMD, crypto)
       Tools: NASM, GAS, MASM, LLVM MC
```
