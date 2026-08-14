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
# 組合語言 — 版本歷史與演變
## 時間軸
|時代|年份|關鍵主題 |
|-----|------|------------|
| 20 世紀 40 年代 | 1945 |機器代碼 — 撥動開關、紙帶 |
| 1949 | 1949 | **第一個彙編器**（Wilkes、Wheeler、Gill — EDSAC）|
| 20 世紀 50 年代 | 1951 | Grace Hopper 的 A-0 — 第一個「編譯者」（宏彙編器）|
| 1957 | 1957 | IBM 650 的 SOAP（符號最佳化組裝程式）|
| 20 世紀 60 年代 | 1960 | IBM System/360 的 BAL（基本彙編語言）|
| 1978 | 1978 | **英特爾 8086** — x86 架構誕生 |
| 20 世紀 80 年代 | 1981 | IBM PC — x86 彙編主導 PC 程式設計 |
| 1985 | 1985 | **Intel 386** — 32 位元 x86，保護模式 |
| 1993 | 1993 | **Intel Pentium** — 超標量，後來的 MMX |
| 1997 | 1997 | MMX 指令（多媒體）|
| 1999 | 1999 | SSE（流SIMD 擴充）|
| 2000 | 2000 2000 | 2000 **AMD64** — 64 位元 x86 擴充 |
| 2001 | 2001 | **ARM** 獲得移動主導地位 |
| 2005 | 2005 | SSE3，雙核心處理器|
| 2006 | 2006 | **x86-64** — 64 位元成為標準 |
| 2011 | 2011 | **AVX**（進階向量擴充）|
| 2013 | 2013 | **ARM64 (AArch64)** — 64 位元 ARM |
| 2017 | 2017 2017 | 2017 **AVX-512** — 512 位元向量運算 |
| 2020 | 2020 | **Apple M1** — 桌面上的 ARM64 |
| 2023 | 2023 | **AVX-VNNI** — AI/ML 加速 |
| 2024 | 2024 2024 | 2024 **RISC-V** 獲得關注－開放 ISA |
## 主要里程碑
### 機器碼時代（1940 年代–1950 年代）
- **1945**：ENIAC 透過插接板和開關進行編程
- **1949**：EDSAC — 第一台儲存程式計算機；第一個「彙編器」（初始訂單）
- **1951**：Grace Hopper 的 A-0 — 將數學符號轉換為機器碼
- **1957**：SOAP — 第一個廣泛使用的符號彙編器 (IBM 650)
### x86 彙編（1978 年至今）
- **1978**：Intel 8086 — x86 架構誕生
  - 16位元暫存器：AX、BX、CX、DX、SI、DI、SP、BP
  - 分段記憶體：CS、DS、SS、ES
  - 指令：MOV、ADD、SUB、JMP、CALL、RET、INT
- **1985**：Intel 386 — 32 位元 x86 (IA-32)
  - 32位元暫存器：EAX、EBX、ECX、EDX
  - 保護模式、分頁、虛擬內存
- **2000**：AMD64 — 64 位元 x86 擴展
  - 64位元暫存器：RAX、RBX、RCX、RDX
  - 16 個通用暫存器（32 位元為 8 個）
  - RIP 相對尋址
### ARM 大會（1985 年至今）
- **1985**：ARM1 — Acorn Computers（英國）
  - RISC理念：簡單、固定長度的指令
  - 載入/儲存架構
  - 16個暫存器（R0-R15），R13=SP，R14=LR，R15=PC
- **2013**：ARM64 (AArch64) — 64 位元 ARM
  - 31個通用64位元暫存器
  - SIMD：氖、SVE
  - 用於：智慧型手機、Apple Silicon、AWS Graviton
### RISC-V（2010 年至今）
- **2010**：加州大學柏克萊分校創建開放 ISA
- **2020 年代**：RISC-V 受到關注 - 開放，無許可費
- 應用於：嵌入式系統、客製化晶片、中國半導體推
## 語法演變
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

## 指令集演變
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

## 關鍵設計原則
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

## 生態系成長
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
