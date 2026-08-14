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
# Assembly Language — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Era | Taon | Pangunahing Tema |
|-----|------|-----------|
| 1940s | 1945 | Machine code — toggle switch, paper tape |
| 1949 | 1949 | **Unang assembler** (Wilkes, Wheeler, Gill — EDSAC) |
| 1950s | 1951 | A-0 ni Grace Hopper — unang "compiler" (macro assembler) |
| 1957 | 1957 | SOAP (Symbolic Optimal Assembly Program) para sa IBM 650 |
| 1960s | 1960 | BAL (Basic Assembly Language) para sa IBM System/360 |
| 1978 | 1978 | **Intel 8086** — ipinanganak ang x86 architecture |
| 1980s | 1981 | IBM PC — x86 assembly ang nangingibabaw sa PC programming |
| 1985 | 1985 | **Intel 386** — 32-bit x86, protected mode |
| 1993 | 1993 | **Intel Pentium** — superscalar, MMX mamaya |
| 1997 | 1997 | Mga tagubilin sa MMX (multimedia) |
| 1999 | 1999 | SSE (Streaming SIMD Extension) |
| 2000 | 2000 | **AMD64** — 64-bit x86 extension |
| 2001 | 2001 | Nakuha ng **ARM** ang pangingibabaw sa mobile |
| 2005 | 2005 | SSE3, mga dual-core na processor |
| 2006 | 2006 | **x86-64** — 64-bit ay nagiging standard |
| 2011 | 2011 | **AVX** (Mga Advanced na Vector Extension) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-bit na ARM |
| 2017 | 2017 | **AVX-512** — 512-bit vector operations |
| 2020 | 2020 | **Apple M1** — ARM64 sa desktop |
| 2023 | 2023 | **AVX-VNNI** — AI/ML acceleration |
| 2024 | 2024 | **RISC-V** nakakakuha ng traksyon — buksan ang ISA |
## Mga Pangunahing Milestone
### Machine Code Era (1940s–1950s)
- **1945**: Na-program ang ENIAC sa pamamagitan ng mga plug board at switch
- **1949**: EDSAC — unang stored-program na computer; unang "assembler" (mga unang order)
- **1951**: Grace Hopper's A-0 — nagsasalin ng mathematical notation sa machine code
- **1957**: SOAP — unang malawakang ginamit na symbolic assembler (IBM 650)
### x86 Assembly (1978–kasalukuyan)
- **1978**: Intel 8086 — ipinanganak ang x86 architecture
  - 16-bit na mga rehistro: AX, BX, CX, DX, SI, DI, SP, BP
  - Naka-segment na memory: CS, DS, SS, ES
  - Mga Tagubilin: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32-bit x86 (IA-32)
  - 32-bit na mga rehistro: EAX, EBX, ECX, EDX
  - Protektadong mode, paging, virtual memory
- **2000**: AMD64 — 64-bit x86 extension
  - 64-bit na mga rehistro: RAX, RBX, RCX, RDX
  - 16 na pangkalahatang layunin na rehistro (kumpara sa 8 sa 32-bit)
  - RIP-relative addressing
### ARM Assembly (1985–kasalukuyan)
- **1985**: ARM1 — Acorn Computers (UK)
  - Pilosopiya ng RISC: simple, fixed-length na mga tagubilin
  - Mag-load/mag-imbak ng arkitektura
  - 16 na rehistro (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — 64-bit na ARM
  - 31 pangkalahatang layunin na 64-bit na mga rehistro
  - SIMD: NEON, SVE
  - Ginagamit sa: mga smartphone, Apple Silicon, AWS Graviton
### RISC-V (2010–kasalukuyan)
- **2010**: Lumilikha ang UC Berkeley ng bukas na ISA
- **2020s**: Nagkakaroon ng traksyon ang RISC-V — bukas, walang bayad sa paglilisensya
- Ginamit sa: mga naka-embed na system, custom chips, semiconductor push ng China
## Syntax Evolution
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

## Pangunahing Prinsipyo ng Disenyo
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

## Paglago ng Ecosystem
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
