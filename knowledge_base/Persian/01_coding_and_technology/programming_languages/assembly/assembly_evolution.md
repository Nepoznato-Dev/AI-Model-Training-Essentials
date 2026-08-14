---
# Metadata
title: "Assembly Language — Version History & Evolution"
description: "Comprehensive version history and evolution of Assembly language from early machines to modern x86/ARM."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# زبان اسمبلی - تاریخچه نسخه و تکامل
## جدول زمانی
| دوران | سال | تم کلید |
|-----|------|-----------|
| دهه 1940 | 1945 | کد ماشین — کلیدهای ضامن، نوار کاغذی |
| 1949 | 1949 | **اولین مونتاژگر** (Wilkes, Wheeler, Gill — EDSAC) |
| دهه 1950 | 1951 | Grace Hopper's A-0 — اولین "کامپایلر" (مونتاژکننده ماکرو) |
| 1957 | 1957 | SOAP (برنامه مونتاژ بهینه نمادین) برای IBM 650 |
| دهه 1960 | 1960 | BAL (Basic Assembly Language) برای IBM System/360 |
| 1978 | 1978 | **اینتل 8086** — معماری x86 متولد |
| دهه 1980 | 1981 | IBM PC — اسمبلی x86 بر برنامه نویسی رایانه شخصی غالب است |
| 1985 | 1985 | **اینتل 386** — 32 بیت x86، حالت محافظت شده |
| 1993 | 1993 | **Intel Pentium** — superscalar، MMX later |
| 1997 | 1997 | دستورالعمل های MMX (چند رسانه ای) |
| 1999 | 1999 | SSE (Streaming SIMD Extensions) |
| 2000 | 2000 | **AMD64** — پسوند 64 بیتی x86 |
| 2001 | 2001 | **ARM** بر موبایل برتری پیدا کرد |
| 2005 | 2005 | SSE3، پردازنده های دو هسته ای |
| 2006 | 2006 | **x86-64** — 64 بیت استاندارد می شود |
| 2011 | 2011 | **AVX** (افزونه های وکتور پیشرفته) |
| 2013 | 2013 | **ARM64 (AArc64)** — ARM 64 بیتی |
| 2017 | 2017 | **AVX-512** — عملیات برداری 512 بیتی |
| 2020 | 2020 | **Apple M1** — ARM64 روی دسکتاپ |
| 2023 | 2023 | **AVX-VNNI** — شتاب AI/ML |
| 2024 | 2024 | **RISC-V** کشش به دست می آورد — ISA باز |
## نقاط عطف اصلی
### عصر کد ماشین (1940-1950)
- **1945**: ENIAC از طریق بردهای پلاگین و سوئیچ ها برنامه ریزی شده است
- **1949**: EDSAC - اولین کامپیوتر برنامه ذخیره شده. اولین "مونتاژ کننده" (سفارشات اولیه)
- **1951**: Grace Hopper's A-0 - نمادهای ریاضی را به کد ماشین ترجمه می کند
- **1957**: SOAP - اولین اسمبلر نمادین پرکاربرد (IBM 650)
### x86 مونتاژ (1978–اکنون)
- **1978**: Intel 8086 — معماری x86 متولد شد
  - ثبات های 16 بیتی: AX، BX، CX، DX، SI، DI، SP، BP
  - حافظه تقسیم شده: CS، DS، SS، ES
  - دستورالعمل: MOV، ADD، SUB، JMP، CALL، RET، INT
- **1985**: Intel 386 — 32 بیتی x86 (IA-32)
  - رجیسترهای 32 بیتی: EAX، EBX، ECX، EDX
  - حالت محافظت شده، صفحه بندی، حافظه مجازی
- **2000**: AMD64 — پسوند 64 بیتی x86
  - ثبات های 64 بیتی: RAX، RBX، RCX، RDX
  - 16 رجیستر همه منظوره (در مقابل 8 در 32 بیت)
  - آدرس دهی نسبی RIP
### مجمع ARM (1985–اکنون)
- **1985**: ARM1 — Acorn Computers (بریتانیا)
  - فلسفه RISC: دستورالعمل های ساده و با طول ثابت
  - معماری بار/فروشگاه
  - 16 رجیستر (R0-R15)، R13=SP، R14=LR، R15=PC
- **2013**: ARM64 (AAarch64) — ARM 64 بیتی
  - 31 رجیستر 64 بیتی همه منظوره
  - SIMD: نئون، SVE
  - مورد استفاده در: گوشی های هوشمند، Apple Silicon، AWS Graviton
### RISC-V (2010–اکنون)
- **2010**: UC Berkeley ISA باز ایجاد می کند
- **دهه 2020**: RISC-V کشش پیدا می کند - باز، بدون هزینه مجوز
- مورد استفاده در: سیستم های جاسازی شده، تراشه های سفارشی، فشار نیمه هادی چین
## تکامل نحو
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

## Instruction Set Evolution
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

## اصول کلیدی طراحی
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

## رشد اکوسیستم
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
