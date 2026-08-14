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
# Assembly Dili — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Çağ | Yıl | Anahtar Tema |
|-----|------|-----------|
| 1940'lar | 1945 | Makine kodu — geçiş anahtarları, kağıt bant |
| 1949 | 1949 | **İlk montajcı** (Wilkes, Wheeler, Gill — EDSAC) |
| 1950'ler | 1951 | Grace Hopper'ın A-0'ı — ilk "derleyici" (makro birleştirici) |
| 1957 | 1957 | IBM 650 için SOAP (Sembolik Optimal Montaj Programı) |
| 1960'lar | 1960 | IBM System/360 için BAL (Temel Montaj Dili) |
| 1978 | 1978 | **Intel 8086** — x86 mimarisinden doğan |
| 1980'ler | 1981 | IBM PC — x86 derlemesi PC programlamaya hakimdir |
| 1985 | 1985 | **Intel 386** — 32 bit x86, korumalı mod |
| 1993 | 1993 | **Intel Pentium** — süperskalar, MMX sonrası |
| 1997 | 1997 | MMX talimatları (multimedya) |
| 1999 | 1999 | SSE (SIMD Uzantıları Akışı) |
| 2000 | 2000 | **AMD64** — 64 bit x86 uzantısı |
| 2001 | 2001 | **ARM** mobilde hakimiyet kazanıyor |
| 2005 | 2005 | SSE3, çift çekirdekli işlemciler |
| 2006 | 2006 | **x86-64** — 64 bit standart hale geliyor |
| 2011 | 2011 | **AVX** (Gelişmiş Vektör Uzantıları) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64 bit ARM |
| 2017 | 2017 | **AVX-512** — 512 bit vektör işlemleri |
| 2020 | 2020 | **Apple M1** — Masaüstünde ARM64 |
| 2023 | 2023 | **AVX-VNNI** — AI/ML hızlandırma |
| 2024 | 2024 | **RISC-V** ilgi görüyor — açık ISA |
## Önemli Kilometre Taşları
### Makine Kodu Çağı (1940'lar – 1950'ler)
- **1945**: ENIAC, fiş kartları ve anahtarlar aracılığıyla programlanır
- **1949**: EDSAC — ilk depolanan program bilgisayarı; ilk "montajcı" (ilk siparişler)
- **1951**: Grace Hopper'ın A-0'ı — matematiksel gösterimi makine koduna çevirir
- **1957**: SOAP — yaygın olarak kullanılan ilk sembolik birleştirici (IBM 650)
### x86 Düzeneği (1978 – günümüz)
- **1978**: Intel 8086 — x86 mimarisi doğdu
  - 16 bitlik kayıtlar: AX, BX, CX, DX, SI, DI, SP, BP
  - Bölümlere ayrılmış bellek: CS, DS, SS, ES
  - Talimatlar: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32 bit x86 (IA-32)
  - 32 bit kayıtlar: EAX, EBX, ECX, EDX
  - Korumalı mod, sayfalama, sanal bellek
- **2000**: AMD64 — 64 bit x86 uzantısı
  - 64 bit kayıtlar: RAX, RBX, RCX, RDX
  - 16 genel amaçlı kayıt (32 bitte 8'e karşılık)
  - RIP'e bağlı adresleme
### ARM Düzeneği (1985 – günümüz)
- **1985**: ARM1 — Acorn Computers (İngiltere)
  - RISC felsefesi: basit, sabit uzunlukta talimatlar
  - Yükleme/depolama mimarisi
  - 16 kayıt (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — 64 bit ARM
  - 31 genel amaçlı 64 bit kayıt
  - SIMD: NEON, SVE
  - Kullanıldığı yerler: akıllı telefonlar, Apple Silicon, AWS Graviton
### RISC-V (2010 – günümüz)
- **2010**: UC Berkeley açık ISA'yı oluşturdu
- **2020'ler**: RISC-V ilgi görüyor — açık, lisans ücreti yok
- Kullanılan yerler: gömülü sistemler, özel çipler, Çin'in yarı iletken teknolojisi
## Söz Dizimi Gelişimi
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

## Komut Seti Gelişimi
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

## Temel Tasarım İlkeleri
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

## Ekosistem Büyümesi
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
