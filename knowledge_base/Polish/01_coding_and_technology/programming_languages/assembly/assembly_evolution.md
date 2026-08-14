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
# Język asemblera — historia wersji i ewolucja
## Oś czasu
| epoka | Rok | Kluczowy motyw |
|---------|------|-----------|
| lata 40. | 1945 | Kod maszynowy — przełączniki dźwigniowe, taśma papierowa |
| 1949 | 1949 | **Pierwszy asembler** (Wilkes, Wheeler, Gill — EDSAC) |
| lata 50. | 1951 | A-0 Grace Hopper — pierwszy „kompilator” (asembler makr) |
| 1957 | 1957 | SOAP (Symboliczny program optymalnego montażu) dla IBM 650 |
| lata 60. | 1960 | BAL (podstawowy język asemblera) dla IBM System/360 |
| 1978 | 1978 | **Intel 8086** — narodziła się architektura x86 |
| Lata 80. | 1981 | IBM PC — montaż x86 dominuje w programowaniu komputerów PC |
| 1985 | 1985 | **Intel 386** — 32-bitowy x86, tryb chroniony |
| 1993 | 1993 | **Intel Pentium** — superskalarny, później MMX |
| 1997 | 1997 | Instrukcje MMX (multimedia) |
| 1999 | 1999 | SSE (rozszerzenia SIMD do transmisji strumieniowej) |
| 2000 | 2000 | **AMD64** — 64-bitowe rozszerzenie x86 |
| 2001 | 2001 | **ARM** zyskuje dominację na urządzeniach mobilnych |
| 2005 | 2005 | SSE3, procesory dwurdzeniowe |
| 2006 | 2006 | **x86-64** — wersja 64-bitowa staje się standardem |
| 2011 | 2011 | **AVX** (zaawansowane rozszerzenia wektorowe) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-bitowy ARM |
| 2017 | 2017 | **AVX-512** — 512-bitowe operacje wektorowe |
| 2020 | 2020 | **Apple M1** — ARM64 na komputerze stacjonarnym |
| 2023 | 2023 | **AVX-VNNI** — akceleracja AI/ML |
| 2024 | 2024 | **RISC-V** zyskuje przyczepność — otwórz ISA |
## Główne kamienie milowe
### Era kodu maszynowego (lata 40.–50. XX wieku)
- **1945**: ENIAC programowany za pomocą płytek wtykowych i przełączników
- **1949**: EDSAC — pierwszy komputer z zapisanym programem; pierwszy „asembler” (wstępne zamówienia)
- **1951**: A-0 Grace Hopper — tłumaczy zapis matematyczny na kod maszynowy
- **1957**: SOAP — pierwszy powszechnie używany asembler symboliczny (IBM 650)
### Zespół x86 (1978 – obecnie)
- **1978**: Narodziny Intel 8086 — architektura x86
  - rejestry 16-bitowe: AX, BX, CX, DX, SI, DI, SP, BP
  - Pamięć segmentowana: CS, DS, SS, ES
  - Instrukcje: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32-bitowy x86 (IA-32)
  - Rejestry 32-bitowe: EAX, EBX, ECX, EDX
  - Tryb chroniony, stronicowanie, pamięć wirtualna
- **2000**: AMD64 — 64-bitowe rozszerzenie x86
  - Rejestry 64-bitowe: RAX, RBX, RCX, RDX
  - 16 rejestrów ogólnego przeznaczenia (w porównaniu do 8 w 32-bitowych)
  - Adresowanie względne w protokole RIP
### Zespół ramienia (1985 – obecnie)
- **1985**: ARM1 — Acorn Computers (Wielka Brytania)
  - Filozofia RISC: proste instrukcje o stałej długości
  - Architektura ładowania/przechowywania
  - 16 rejestrów (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — 64-bitowy ARM
  - 31 rejestrów 64-bitowych ogólnego przeznaczenia
  - SIMD: NEON, SVE
  - Stosowany w: smartfonach, Apple Silicon, AWS Graviton
### RISC-V (2010 – obecnie)
- **2010**: Uniwersytet Kalifornijski w Berkeley tworzy otwarte ISA
- **2020 rok**: RISC-V zyskuje na popularności — otwarty, bez opłat licencyjnych
- Stosowany w: systemach wbudowanych, niestandardowych chipach, chińskim pusherze półprzewodnikowym
## Ewolucja składni
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

## Ewolucja zestawu instrukcji
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

## Kluczowe zasady projektowania
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

## Rozwój ekosystemu
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
