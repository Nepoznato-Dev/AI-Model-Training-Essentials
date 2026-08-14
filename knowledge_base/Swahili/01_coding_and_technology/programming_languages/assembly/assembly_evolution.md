<!--
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

-->
# Lugha ya Mkutano - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Enzi | Mwaka | Mandhari Muhimu |
|-----|------|-----------|
| Miaka ya 1940 | 1945 | Msimbo wa mashine — geuza swichi, mkanda wa karatasi |
| 1949 | 1949 | **Mkusanyaji wa kwanza** (Wilkes, Wheeler, Gill - EDSAC) |
| Miaka ya 1950 | 1951 | Grace Hopper's A-0 — kwanza "compiler" (macro assembler) |
| 1957 | 1957 | SABUNI (Mpango wa Kusanyiko Bora wa Alama) kwa IBM 650 |
| Miaka ya 1960 | 1960 | BAL (Lugha ya Kusanyiko Msingi) ya Mfumo wa IBM/360 |
| 1978 | 1978 | **Intel 8086** — Usanifu wa x86 umezaliwa |
| Miaka ya 1980 | 1981 | IBM PC — mkusanyiko wa x86 unatawala upangaji wa Kompyuta |
| 1985 | 1985 | **Intel 386** — 32-bit x86, hali iliyolindwa |
| 1993 | 1993 | **Intel Pentium** — superscalar, MMX baadaye |
| 1997 | 1997 | Maagizo ya MMX (multimedia) |
| 1999 | 1999 | SSE (Utiririshaji wa Viendelezi vya SIMD) |
| 2000 | 2000 | **AMD64** — kiendelezi cha 64-bit x86 |
| 2001 | 2001 | **ARM** inapata utawala wa rununu |
| 2005 | 2005 | SSE3, vichakataji vya msingi-mbili |
| 2006 | 2006 | **x86-64** — 64-bit inakuwa ya kawaida |
| 2011 | 2011 | **AVX** (Viendelezi vya Juu vya Vekta) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-bit ARM |
| 2017 | 2017 | **AVX-512** — shughuli za vekta 512 |
| 2020 | 2020 | **Apple M1** — ARM64 kwenye eneo-kazi |
| 2023 | 2023 | **AVX-VNNI** — AI/ML kuongeza kasi |
| 2024 | 2024 | **RISC-V** inapata kuvutia - fungua ISA |
## Mafanikio Makuu
### Enzi ya Msimbo wa Mashine (1940-1950s)
- **1945**: ENIAC iliyopangwa kupitia bodi za kuziba na swichi
- **1949**: EDSAC — kompyuta ya kwanza iliyohifadhiwa ya programu; kwanza "mkusanyaji" (maagizo ya awali)
- **1951**: Grace Hopper's A-0 - hutafsiri nukuu za hisabati kuwa msimbo wa mashine
- **1957**: SABUNI - kiunganishi cha ishara kilitumika mara ya kwanza (IBM 650)
### x86 Bunge (1978–sasa)
- **1978**: Intel 8086 — x86 usanifu kuzaliwa
  - rejista 16-bit: AX, BX, CX, DX, SI, DI, SP, BP
  - Kumbukumbu iliyogawanywa: CS, DS, SS, ES
  - Maagizo: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32-bit x86 (IA-32)
  - rejista za 32-bit: EAX, EBX, ECX, EDX
  - Hali iliyolindwa, paging, kumbukumbu ya kawaida
- **2000**: AMD64 — 64-bit x86 ugani
  - rejista za 64-bit: RAX, RBX, RCX, RDX
  - rejista 16 za madhumuni ya jumla (mst. 8 katika 32-bit)
  - RIP-jamaa anwani
### Bunge la ARM (1985–sasa)
- **1985**: ARM1 — Kompyuta za Acorn (Uingereza)
  - Falsafa ya RISC: maagizo rahisi, ya urefu usiobadilika
  - Usanifu wa mzigo / duka
  - rejista 16 (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) - 64-bit ARM
  - rejista 31 za madhumuni ya jumla ya 64-bit
  - SIMD: NEON, SVE
  - Inatumika katika: simu mahiri, Apple Silicon, AWS Graviton
### RISC-V (2010–sasa)
- **2010**: UC Berkeley inaunda ISA wazi
- **2020**: RISC-V inapata kuvutia - wazi, hakuna ada za leseni
- Inatumika katika: mifumo iliyopachikwa, chipsi maalum, msukumo wa semiconductor wa China
## Mageuzi ya Sintaksia
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

## Maelekezo Weka Mageuzi
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

## Kanuni Muhimu za Usanifu
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

## Ukuaji wa Mfumo ikolojia
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
