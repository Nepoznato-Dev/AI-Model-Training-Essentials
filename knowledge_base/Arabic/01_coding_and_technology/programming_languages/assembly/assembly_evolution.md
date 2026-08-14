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
# لغة التجميع — تاريخ الإصدار وتطوره
## الجدول الزمني
| العصر | سنة | الموضوع الرئيسي |
|-----|------|-----------|
| الأربعينيات | 1945 | رمز الآلة — تبديل المفاتيح، الشريط الورقي |
| 1949 | 1949 | **المجمع الأول** (ويلكس، ويلر، جيل — EDSAC) |
| الخمسينيات | 1951 | Grace Hopper's A-0 — أول "مترجم" (مجمع ماكرو) |
| 1957 | 1957 | SOAP (برنامج التجميع الأمثل الرمزي) لـ IBM 650 |
| الستينيات | 1960 | BAL (لغة التجميع الأساسية) لنظام IBM System/360 |
| 1978 | 1978 | **Intel 8086** — ولادة بنية x86 |
| الثمانينيات | 1981 | IBM PC - التجميع x86 يهيمن على برمجة الكمبيوتر |
| 1985 | 1985 | **Intel 386** — 32 بت x86، الوضع المحمي |
| 1993 | 1993 | **Intel Pentium** — سلمية فائقة، MMX لاحقًا |
| 1997 | 1997 | تعليمات MMX (الوسائط المتعددة) |
| 1999 | 1999 | SSE (بث ملحقات SIMD) |
| 2000 | 2000 | **AMD64** — ملحق 64 بت x86 |
| 2001 | 2001 | **ARM** يهيمن على الهاتف المحمول |
| 2005 | 2005 | SSE3، معالجات ثنائية النواة |
| 2006 | 2006 | **x86-64** — أصبح الإصدار 64 بت قياسيًا |
| 2011 | 2011 | **AVX** (امتدادات المتجهات المتقدمة) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64 بت ARM |
| 2017 | 2017 | **AVX-512** — عمليات متجهة 512 بت |
| 2020 | 2020 | **Apple M1** — ARM64 على سطح المكتب |
| 2023 | 2023 | **AVX-VNNI** — تسريع AI/ML |
| 2024 | 2024 | **RISC-V** يكتسب قوة جذب — افتح ISA |
## المعالم الرئيسية
### عصر برمجة الآلة (من الأربعينيات إلى الخمسينيات)
- **1945**: تمت برمجة ENIAC عبر لوحات التوصيل والمفاتيح
- **1949**: EDSAC — أول كمبيوتر مزود ببرامج مخزنة؛ "المجمع" الأول (الأوامر الأولية)
- **1951**: A-0 لجريس هوبر — يترجم التدوين الرياضي إلى رمز الآلة
- **1957**: SOAP — أول مُجمِّع رمزي مستخدم على نطاق واسع (IBM 650)
### تجميع x86 (1978 إلى الوقت الحاضر)
- **1978**: ولادة بنية Intel 8086 — x86
  - سجلات 16 بت: AX، BX، CX، DX، SI، DI، SP، BP
  - الذاكرة المقسمة: CS، DS، SS، ES
  - التعليمات: MOV، ADD، SUB، JMP، CALL، RET، INT
- **1985**: Intel 386 — 32 بت x86 (IA-32)
  - سجلات 32 بت: EAX، EBX، ECX، EDX
  - الوضع المحمي، الترحيل، الذاكرة الافتراضية
- **2000**: AMD64 — امتداد x86 64 بت
  - سجلات 64 بت: RAX، RBX، RCX، RDX
  - 16 سجلًا للأغراض العامة (مقابل 8 في 32 بت)
  - معالجة نسبية لـ RIP
### جمعية ARM (1985 إلى الوقت الحاضر)
- **1985**: ARM1 — شركة Acorn Computers (المملكة المتحدة)
  - فلسفة RISC: تعليمات بسيطة وثابتة الطول
  - بنية التحميل/التخزين
  - 16 سجلًا (R0-R15)، R13=SP، R14=LR، R15=PC
- **2013**: ARM64 (AArch64) — 64 بت ARM
  - 31 سجلًا للأغراض العامة 64 بت
  - SIMD: نيون، SVE
  - يستخدم في: الهواتف الذكية، Apple Silicon، AWS Graviton
### RISC-V (2010 إلى الوقت الحاضر)
- **2010**: جامعة كاليفورنيا في بيركلي تنشئ ISA مفتوحة
- **عقد 2020**: RISC-V يكتسب قوة جذب كبيرة — مفتوح وبدون رسوم ترخيص
- يستخدم في: الأنظمة المدمجة، والرقائق المخصصة، ودفع أشباه الموصلات في الصين
## تطور بناء الجملة
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

## تطور مجموعة التعليمات
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

## مبادئ التصميم الرئيسية
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

## نمو النظام البيئي
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
