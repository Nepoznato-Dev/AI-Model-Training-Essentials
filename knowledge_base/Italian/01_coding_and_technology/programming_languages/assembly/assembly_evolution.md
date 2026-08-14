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

# Linguaggio Assembly: storia ed evoluzione delle versioni
## Cronologia
| Epoca | Anno | Tema chiave |
|-----|------|-----------|
| Anni '40 | 1945 | Codice macchina: interruttori a levetta, nastro di carta |
| 1949 | 1949 | **Primo assemblatore** (Wilkes, Wheeler, Gill — EDSAC) |
| Anni '50 | 1951 | A-0 di Grace Hopper — primo "compilatore" (macroassemblatore) |
| 1957 | 1957 | SOAP (Programma di assemblaggio ottimale simbolico) per IBM 650 |
| Anni '60 | 1960 | BAL (Basic Assembly Language) per IBM System/360 |
| 1978 | 1978 | **Intel 8086**: nasce l'architettura x86 |
| Anni '80 | 1981 | PC IBM: l'assembly x86 domina la programmazione dei PC |
| 1985 | 1985 | **Intel 386** — x86 a 32 bit, modalità protetta |
| 1993 | 1993 | **Intel Pentium** — superscalare, MMX successivo |
| 1997 | 1997 | Istruzioni MMX (multimediali) |
| 1999 | 1999 | SSE (estensioni SIMD in streaming) |
| 2000 | 2000 | **AMD64**: estensione x86 a 64 bit |
| 2001 | 2001 | **ARM** conquista il dominio mobile |
| 2005| 2005| SSE3, processori dual-core |
| 2006| 2006| **x86-64** — 64 bit diventa standard |
| 2011 | 2011 | **AVX** (estensioni vettoriali avanzate) |
| 2013| 2013| **ARM64 (AArch64)**: ARM a 64 bit |
| 2017 | 2017 | **AVX-512** — Operazioni vettoriali a 512 bit |
| 2020 | 2020 | **Apple M1** — ARM64 su desktop |
| 2023 | 2023 | **AVX-VNNI**: accelerazione AI/ML |
| 2024 | 2024 | **RISC-V** guadagna terreno: apre ISA |
## Traguardi importanti
### Era del codice macchina (anni '40-'50)
- **1945**: ENIAC programmato tramite schede e interruttori
- **1949**: EDSAC — primo computer a programma memorizzato; primo "assemblatore" (ordini iniziali)
- **1951**: A-0 di Grace Hopper: traduce la notazione matematica in codice macchina
- **1957**: SOAP — primo assemblatore simbolico ampiamente utilizzato (IBM 650)
### Assemblea x86 (1978-oggi)
- **1978**: Intel 8086: nascita dell'architettura x86
  - Registri a 16 bit: AX, BX, CX, DX, SI, DI, SP, BP
  - Memoria segmentata: CS, DS, SS, ES
  - Istruzioni: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386: x86 a 32 bit (IA-32)
  - Registri a 32 bit: EAX, EBX, ECX, EDX
  - Modalità protetta, paginazione, memoria virtuale
- **2000**: AMD64: estensione x86 a 64 bit
  - Registri a 64 bit: RAX, RBX, RCX, RDX
  - 16 registri per uso generale (contro 8 a 32 bit)
  - Indirizzamento relativo al RIP
### Assemblea ARM (1985-oggi)
- **1985**: ARM1 — Acorn Computer (Regno Unito)
  - Filosofia RISC: istruzioni semplici e di lunghezza fissa
  - Architettura di caricamento/archiviazione
  - 16 registri (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — ARM a 64 bit
  - 31 registri a 64 bit per uso generale
  - SIMD: NEON, SVE
  - Utilizzato in: smartphone, Apple Silicon, AWS Graviton
### RISC-V (2010-oggi)
- **2010**: l'UC Berkeley crea un ISA aperto
- **Anni '20**: RISC-V guadagna terreno: aperto, senza costi di licenza
- Utilizzato in: sistemi embedded, chip personalizzati, spinta cinese dei semiconduttori
## Evoluzione della sintassi
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

## Evoluzione del set di istruzioni
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

## Principi chiave di progettazione
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

## Crescita dell'ecosistema
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
