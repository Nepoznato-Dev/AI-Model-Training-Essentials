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

# Assemblersprache – Versionsgeschichte und Entwicklung
## Zeitleiste
| Ära | Jahr | Schlüsselthema |
|-----|------|-----------|
| 1940er Jahre | 1945 | Maschinencode – Kippschalter, Papierband |
| 1949 | 1949 | **Erster Assembler** (Wilkes, Wheeler, Gill – EDSAC) |
| 1950er Jahre | 1951 | Grace Hoppers A-0 – erster „Compiler“ (Makro-Assembler) |
| 1957 | 1957 | SOAP (Symbolic Optimal Assembly Program) für IBM 650 |
| 1960er Jahre | 1960 | BAL (Basic Assembly Language) für IBM System/360 |
| 1978 | 1978 | **Intel 8086** – Geburt der x86-Architektur |
| 1980er Jahre | 1981 | IBM PC – x86-Assembly dominiert PC-Programmierung |
| 1985 | 1985 | **Intel 386** – 32-Bit x86, geschützter Modus |
| 1993 | 1993 | **Intel Pentium** – superskalar, MMX später |
| 1997 | 1997 | MMX-Anleitung (Multimedia) |
| 1999 | 1999 | SSE (Streaming SIMD-Erweiterungen) |
| 2000 | 2000 | **AMD64** – 64-Bit-x86-Erweiterung |
| 2001 | 2001 | **ARM** erlangt mobile Dominanz |
| 2005 | 2005 | SSE3, Dual-Core-Prozessoren |
| 2006 | 2006 | **x86-64** – 64-Bit wird zum Standard |
| 2011 | 2011 | **AVX** (Erweiterte Vektorerweiterungen) |
| 2013 | 2013 | **ARM64 (AArch64)** – 64-Bit-ARM |
| 2017 | 2017 | **AVX-512** – 512-Bit-Vektoroperationen |
| 2020 | 2020 | **Apple M1** – ARM64 auf dem Desktop |
| 2023 | 2023 | **AVX-VNNI** – KI/ML-Beschleunigung |
| 2024 | 2024 | **RISC-V** gewinnt an Bedeutung – ISA öffnen |
## Wichtige Meilensteine
### Maschinencode-Ära (1940er–1950er Jahre)
- **1945**: ENIAC über Steckplatinen und Schalter programmiert
- **1949**: EDSAC – erster Computer mit gespeicherten Programmen; erster „Assembler“ (Erstbestellungen)
- **1951**: Grace Hoppers A-0 – übersetzt mathematische Notation in Maschinencode
- **1957**: SOAP – erster weit verbreiteter symbolischer Assembler (IBM 650)
### x86-Baugruppe (1978–heute)
- **1978**: Intel 8086 – Geburt der x86-Architektur
  - 16-Bit-Register: AX, BX, CX, DX, SI, DI, SP, BP
  - Segmentierter Speicher: CS, DS, SS, ES
  - Anweisungen: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 – 32-Bit x86 (IA-32)
  - 32-Bit-Register: EAX, EBX, ECX, EDX
  - Geschützter Modus, Paging, virtueller Speicher
- **2000**: AMD64 – 64-Bit-x86-Erweiterung
  - 64-Bit-Register: RAX, RBX, RCX, RDX
  - 16 Allzweckregister (im Vergleich zu 8 in 32-Bit)
  - RIP-relative Adressierung
### ARM-Versammlung (1985–heute)
- **1985**: ARM1 – Acorn Computers (UK)
  - RISC-Philosophie: einfache Anweisungen mit fester Länge
  - Architektur laden/speichern
  - 16 Register (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) – 64-Bit-ARM
  - 31 universelle 64-Bit-Register
  - SIMD: NEON, SVE
  - Verwendet in: Smartphones, Apple Silicon, AWS Graviton
### RISC-V (2010–heute)
- **2010**: UC Berkeley erstellt offene ISA
- **2020er Jahre**: RISC-V gewinnt an Bedeutung – offen, keine Lizenzgebühren
- Verwendet in: eingebetteten Systemen, kundenspezifischen Chips, Chinas Halbleiter-Push
## Syntaxentwicklung
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

## Befehlssatzentwicklung
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

## Wichtige Designprinzipien
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

## Ökosystemwachstum
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
