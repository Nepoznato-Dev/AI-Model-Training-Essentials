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
# Langage d'assemblage - Historique et évolution des versions
## Chronologie
| Ère | Année | Thème clé |
|-----|------|-----------|
| années 1940 | 1945 | Code machine — interrupteurs à bascule, ruban de papier |
| 1949 | 1949 | **Premier assembleur** (Wilkes, Wheeler, Gill — EDSAC) |
| années 1950 | 1951 | A-0 de Grace Hopper — premier « compilateur » (macro assembleur) |
| 1957 | 1957 | SOAP (Symbolic Optimal Assembly Program) pour IBM 650 |
| années 1960 | 1960 | BAL (langage d'assemblage de base) pour IBM System/360 |
| 1978 | 1978 | **Intel 8086** — Naissance de l'architecture x86 |
| années 1980 | 1981 | IBM PC — L'assemblage x86 domine la programmation PC |
| 1985 | 1985 | **Intel 386** — 32 bits x86, mode protégé |
| 1993 | 1993 | **Intel Pentium** — superscalaire, MMX plus tard |
| 1997 | 1997 | Instructions MMX (multimédia) |
| 1999 | 1999 | SSE (extensions SIMD en streaming) |
| 2000 | 2000 | **AMD64** — Extension x86 64 bits |
| 2001 | 2001 | **ARM** gagne en domination mobile |
| 2005 | 2005 | SSE3, processeurs double cœur |
| 2006 | 2006 | **x86-64** — Le 64 bits devient la norme |
| 2011 | 2011 | **AVX** (Extensions vectorielles avancées) |
| 2013 | 2013 | **ARM64 (AArch64)** — ARM 64 bits |
| 2017 | 2017 | **AVX-512** — Opérations vectorielles 512 bits |
| 2020 | 2020 | **Apple M1** — ARM64 sur ordinateur de bureau |
| 2023 | 2023 | **AVX-VNNI** — Accélération IA/ML |
| 2024 | 2024 | **RISC-V** gagne du terrain — ouvrez l'ISA |
## Étapes majeures
### L'ère du code machine (années 1940-1950)
- **1945** : ENIAC programmé via des cartes de connexion et des commutateurs
- **1949** : EDSAC — premier ordinateur à programme stocké ; premier "assembleur" (commandes initiales)
- **1951** : A-0 de Grace Hopper — traduit la notation mathématique en code machine
- **1957** : SOAP — premier assembleur symbolique largement utilisé (IBM 650)
### Assemblage x86 (depuis 1978)
- **1978** : naissance de l'Intel 8086 — architecture x86
  - Registres 16 bits : AX, BX, CX, DX, SI, DI, SP, BP
  - Mémoire segmentée : CS, DS, SS, ES
  -Instructions : MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985** : Intel 386 — 32 bits x86 (IA-32)
  - Registres 32 bits : EAX, EBX, ECX, EDX
  - Mode protégé, pagination, mémoire virtuelle
- **2000** : AMD64 — extension x86 64 bits
  - Registres 64 bits : RAX, RBX, RCX, RDX
  - 16 registres à usage général (contre 8 en 32 bits)
  - Adressage relatif RIP
### Assemblage ARM (1985-présent)
- **1985** : ARM1 — Acorn Computers (Royaume-Uni)
  - Philosophie RISC : instructions simples et de longueur fixe
  - Architecture de chargement/stockage
  - 16 registres (R0-R15), R13=SP, R14=LR, R15=PC
- **2013** : ARM64 (AArch64) — ARM 64 bits
  - 31 registres 64 bits à usage général
  - SIMD : NÉON, SVE
  - Utilisé dans : smartphones, Apple Silicon, AWS Graviton
### RISC-V (2010-présent)
- **2010** : l'UC Berkeley crée une ISA ouverte
- **Années 2020** : RISC-V gagne du terrain — ouvert, sans frais de licence
- Utilisé dans : les systèmes embarqués, les puces personnalisées, la poussée chinoise des semi-conducteurs
## Évolution de la syntaxe
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

## Évolution du jeu d'instructions
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

## Principes de conception clés
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

## Croissance de l'écosystème
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
