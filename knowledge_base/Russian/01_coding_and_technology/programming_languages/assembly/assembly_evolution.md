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

# Язык ассемблера — история версий и эволюция
## Временная шкала
| Эра | Год | Ключевая тема |
|-----|------|-----------|
| 1940-е годы | 1945 год | Машинный код — тумблеры, бумажная лента |
| 1949 | 1949 | **Первый ассемблер** (Уилкс, Уилер, Гилл — EDSAC) |
| 1950-е годы | 1951 | A-0 Грейс Хоппер — первый «компилятор» (макроассемблер) |
| 1957 | 1957 | SOAP (программа символьной оптимальной сборки) для IBM 650 |
| 1960-е годы | 1960 | BAL (базовый язык ассемблера) для IBM System/360 |
| 1978 | 1978 | **Intel 8086** — рождение архитектуры x86 |
| 1980-е годы | 1981 | IBM PC — сборка x86 доминирует в программировании для ПК |
| 1985 | 1985 | **Intel 386** — 32-разрядная версия x86, защищенный режим |
| 1993 | 1993 | **Intel Pentium** — суперскаляр, позже MMX |
| 1997 | 1997 | Инструкции MMX (мультимедиа) |
| 1999 | 1999 | SSE (потоковые расширения SIMD) |
| 2000 | 2000 | **AMD64** — 64-битное расширение x86 |
| 2001 | 2001 | **ARM** завоевывает доминирование на мобильных устройствах |
| 2005 | 2005 | SSE3, двухъядерные процессоры |
| 2006 | 2006 | **x86-64** — 64-разрядная версия становится стандартной |
| 2011 | 2011 | **AVX** (расширенные векторные расширения) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-битный ARM |
| 2017 | 2017 | **AVX-512** — 512-битные векторные операции |
| 2020 | 2020 | **Apple M1** — ARM64 для настольных компьютеров |
| 2023 | 2023 | **AVX-VNNI** — ускорение AI/ML |
| 2024 | 2024 | **RISC-V** набирает обороты — открыт ISA |
## Основные вехи
### Эпоха машинного кода (1940–1950-е годы)
- **1945**: ENIAC программируется с помощью штепсельных плат и переключателей.
- **1949**: EDSAC — первый компьютер с хранимой программой; первый «сборщик» (первичные заказы)
- **1951**: A-0 Грейс Хоппер — переводит математические обозначения в машинный код.
- **1957**: SOAP — первый широко используемый символьный ассемблер (IBM 650).
### Сборка x86 (1978 – настоящее время)
- **1978**: родился Intel 8086 — архитектура x86.
  - 16-битные регистры: AX, BX, CX, DX, SI, DI, SP, BP
  - Сегментированная память: CS, DS, SS, ES
  - Инструкции: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32-битный процессор x86 (IA-32).
  - 32-битные регистры: EAX, EBX, ECX, EDX.
  - Защищенный режим, подкачка, виртуальная память
- **2000**: AMD64 — 64-битное расширение x86.
  - 64-битные регистры: RAX, RBX, RCX, RDX
  — 16 регистров общего назначения (против 8 в 32-битной версии)
  - RIP-относительная адресация
### Сборка ARM (1985 – настоящее время)
- **1985**: ARM1 — Acorn Computers (Великобритания)
  - Философия RISC: простые инструкции фиксированной длины.
  - Архитектура загрузки/сохранения
  - 16 регистров (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — 64-битный ARM.
  - 31 64-битный регистр общего назначения
  - SIMD: НЕОН, СВЕ
  - Используется в: смартфонах, Apple Silicon, AWS Graviton.
### RISC-V (2010 – настоящее время)
- **2010**: Калифорнийский университет в Беркли создает открытую ISA.
- **2020-е**: RISC-V набирает обороты — открыт, без лицензионных сборов
- Используется во встроенных системах, нестандартных чипах, развитии полупроводников в Китае.
## Эволюция синтаксиса
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

## Эволюция набора команд
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

## Ключевые принципы проектирования
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

## Рост экосистемы
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
