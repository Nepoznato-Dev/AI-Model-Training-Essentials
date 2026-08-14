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
# Linguagem Assembly - Histórico e evolução da versão
## Linha do tempo
| Época | Ano | Tema principal |
|-----|------|-----------|
| Década de 1940 | 1945 | Código de máquina — interruptores, fita de papel |
| 1949 | 1949 | **Primeira montadora** (Wilkes, Wheeler, Gill — EDSAC) |
| Década de 1950 | 1951 | A-0 de Grace Hopper — primeiro "compilador" (macro assembler) |
| 1957 | 1957 | SOAP (Programa Simbólico de Montagem Ideal) para IBM 650 |
| Década de 1960 | 1960 | BAL (linguagem assembly básica) para IBM System/360 |
| 1978 | 1978 | **Intel 8086** — Nasce a arquitetura x86 |
| Década de 1980 | 1981 | IBM PC – assembly x86 domina a programação de PC |
| 1985 | 1985 | **Intel 386** — x86 de 32 bits, modo protegido |
| 1993 | 1993 | **Intel Pentium** — superescalar, MMX posterior |
| 1997 | 1997 | Instruções MMX (multimídia) |
| 1999 | 1999 | SSE (extensões SIMD de streaming) |
| 2000 | 2000 | **AMD64** — extensão x86 de 64 bits |
| 2001 | 2001 | **ARM** ganha domínio móvel |
| 2005 | 2005 | SSE3, processadores dual-core |
| 2006 | 2006 | **x86-64** — 64 bits se torna padrão |
| 2011 | 2011 | **AVX** (extensões de vetor avançadas) |
| 2013 | 2013 | **ARM64 (AArch64)** — ARM de 64 bits |
| 2017 | 2017 | **AVX-512** — operações vetoriais de 512 bits |
| 2020 | 2020 | **Apple M1** — ARM64 no desktop |
| 2023 | 2023 | **AVX-VNNI** — Aceleração de IA/ML |
| 2024 | 2024 | **RISC-V** ganha força — ISA aberto |
## Marcos importantes
### Era do código de máquina (décadas de 1940 a 1950)
- **1945**: ENIAC programado através de placas de encaixe e interruptores
- **1949**: EDSAC — primeiro computador com programa armazenado; primeiro "montador" (pedidos iniciais)
- **1951**: A-0 de Grace Hopper — traduz notação matemática para código de máquina
- **1957**: SOAP — primeiro montador simbólico amplamente utilizado (IBM 650)
### Assembleia x86 (1978-presente)
- **1978**: Intel 8086 — nasce a arquitetura x86
  - Registros de 16 bits: AX, BX, CX, DX, SI, DI, SP, BP
  - Memória segmentada: CS, DS, SS, ES
  - Instruções: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — x86 de 32 bits (IA-32)
  - Registradores de 32 bits: EAX, EBX, ECX, EDX
  - Modo protegido, paginação, memória virtual
- **2000**: AMD64 — extensão x86 de 64 bits
  - Registros de 64 bits: RAX, RBX, RCX, RDX
  - 16 registros de uso geral (vs. 8 em 32 bits)
  - Endereçamento relativo ao RIP
### Assembleia ARM (1985-presente)
- **1985**: ARM1 — Acorn Computers (Reino Unido)
  - Filosofia RISC: instruções simples e de comprimento fixo
  - Arquitetura de carga/armazenamento
  - 16 registros (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — ARM de 64 bits
  - 31 registros de uso geral de 64 bits
  - SIMD: NÉON, SVE
  - Usado em: smartphones, Apple Silicon, AWS Graviton
### RISC-V (2010-presente)
- **2010**: UC Berkeley cria ISA aberto
- **2020**: RISC-V ganha força — aberto, sem taxas de licenciamento
- Usado em: sistemas embarcados, chips personalizados, impulso de semicondutores da China
## Evolução da Sintaxe
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

## Evolução do conjunto de instruções
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

## Princípios-chave de design
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

## Crescimento do Ecossistema
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
