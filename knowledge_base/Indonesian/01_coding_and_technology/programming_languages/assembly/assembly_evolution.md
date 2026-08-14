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
# Bahasa Majelis — Riwayat Versi & Evolusi
## Garis Waktu
| Zaman | Tahun | Tema Utama |
|-----|------|-----------|
| 1940-an | 1945 | Kode mesin — sakelar sakelar, pita kertas |
| 1949 | 1949 | **Perakitan pertama** (Wilkes, Wheeler, Gill — EDSAC) |
| 1950-an | 1951 | A-0 Grace Hopper — "kompiler" pertama (perakitan makro) |
| 1957 | 1957 | SOAP (Program Perakitan Optimal Simbolik) untuk IBM 650 |
| 1960-an | 1960 | BAL (Bahasa Perakitan Dasar) untuk IBM System/360 |
| 1978 | 1978 | **Intel 8086** — lahirnya arsitektur x86 |
| 1980-an | 1981 | IBM PC — perakitan x86 mendominasi pemrograman PC |
| 1985 | 1985 | **Intel 386** — 32-bit x86, mode terlindungi |
| 1993 | 1993 | **Intel Pentium** — superscalar, MMX nanti |
| 1997 | 1997 | Instruksi MMX (multimedia) |
| 1999 | 1999 | SSE (Streaming Ekstensi SIMD) |
| 2000 | 2000 | **AMD64** — ekstensi x86 64-bit |
| 2001 | 2001 | **ARM** memperoleh dominasi seluler |
| 2005 | 2005 | SSE3, prosesor inti ganda |
| 2006 | 2006 | **x86-64** — 64-bit menjadi standar |
| 2011 | 2011 | **AVX** (Ekstensi Vektor Tingkat Lanjut) |
| 2013 | 2013 | **ARM64 (AArch64)** — ARM 64-bit |
| 2017 | 2017 | **AVX-512** — Operasi vektor 512-bit |
| 2020 | 2020 | **Apple M1** — ARM64 di desktop |
| 2023 | 2023 | **AVX-VNNI** — akselerasi AI/ML |
| 2024 | 2024 | **RISC-V** mendapatkan daya tarik — buka ISA |
## Tonggak Penting
### Era Kode Mesin (1940an–1950an)
- **1945**: ENIAC diprogram melalui papan konektor dan sakelar
- **1949**: EDSAC — komputer program tersimpan pertama; "assembler" pertama (pesanan awal)
- **1951**: A-0 Grace Hopper — menerjemahkan notasi matematika ke kode mesin
- **1957**: SOAP — assembler simbolik pertama yang banyak digunakan (IBM 650)
### Majelis x86 (1978–sekarang)
- **1978**: Intel 8086 — lahirnya arsitektur x86
  - Register 16-bit: AX, BX, CX, DX, SI, DI, SP, BP
  - Memori tersegmentasi: CS, DS, SS, ES
  - Petunjuk: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32-bit x86 (IA-32)
  - Register 32-bit: EAX, EBX, ECX, EDX
  - Mode terproteksi, paging, memori virtual
- **2000**: AMD64 — ekstensi x86 64-bit
  - Register 64-bit: RAX, RBX, RCX, RDX
  - 16 register tujuan umum (vs. 8 dalam 32-bit)
  - Pengalamatan relatif RIP
### Majelis ARM (1985–sekarang)
- **1985**: ARM1 — Acorn Computers (Inggris Raya)
  - Filosofi RISC: instruksi sederhana dengan panjang tetap
  - Memuat/menyimpan arsitektur
  - 16 register (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — ARM 64-bit
  - 31 register 64-bit tujuan umum
  - SIMD: NEON, SVE
  - Digunakan di: ponsel pintar, Apple Silicon, AWS Graviton
### RISC-V (2010–sekarang)
- **2010**: UC Berkeley membuat ISA terbuka
- **2020-an**: RISC-V mendapatkan daya tarik — terbuka, tanpa biaya lisensi
- Digunakan dalam: sistem tertanam, chip khusus, dorongan semikonduktor Tiongkok
## Evolusi Sintaks
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

## Instruksi Set Evolusi
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

## Prinsip Desain Utama
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

## Pertumbuhan Ekosistem
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
