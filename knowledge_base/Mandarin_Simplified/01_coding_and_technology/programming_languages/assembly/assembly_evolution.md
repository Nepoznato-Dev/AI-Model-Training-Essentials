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
# 汇编语言 — 版本历史和演变
## 时间轴
|时代|年份|关键主题 |
|-----|------|------------|
| 20 世纪 40 年代 | 1945 |机器代码 — 拨动开关、纸带 |
| 1949 | 1949 | **第一个汇编器**（Wilkes、Wheeler、Gill — EDSAC）|
| 20 世纪 50 年代 | 1951 | Grace Hopper 的 A-0 — 第一个“编译器”（宏汇编器）|
| 1957 | 1957 | IBM 650 的 SOAP（符号优化装配程序）|
| 20 世纪 60 年代 | 1960 | IBM System/360 的 BAL（基本汇编语言）|
| 1978 | 1978 | **英特尔 8086** — x86 架构诞生 |
| 20 世纪 80 年代 | 1981 | IBM PC — x86 汇编主导 PC 编程 |
| 1985 | 1985 | **Intel 386** — 32 位 x86，保护模式 |
| 1993 | 1993 | **Intel Pentium** — 超标量，后来的 MMX |
| 1997 | 1997 | MMX 指令（多媒体）|
| 1999 | 1999 | SSE（流SIMD 扩展）|
| 2000 | 2000 2000 | 2000 **AMD64** — 64 位 x86 扩展 |
| 2001 | 2001 | **ARM** 获得移动主导地位 |
| 2005 | 2005 | SSE3，双核处理器|
| 2006 | 2006 | **x86-64** — 64 位成为标准 |
| 2011 | 2011 | **AVX**（高级矢量扩展）|
| 2013 | 2013 | **ARM64 (AArch64)** — 64 位 ARM |
| 2017 | 2017 2017 | 2017 **AVX-512** — 512 位向量运算 |
| 2020 | 2020 | **Apple M1** — 桌面上的 ARM64 |
| 2023 | 2023 | **AVX-VNNI** — AI/ML 加速 |
| 2024 | 2024 2024 | 2024 **RISC-V** 获得关注——开放 ISA |
## 主要里程碑
### 机器代码时代（1940 年代–1950 年代）
- **1945**：ENIAC 通过插接板和开关进行编程
- **1949**：EDSAC — 第一台存储程序计算机；第一个“汇编器”（初始订单）
- **1951**：Grace Hopper 的 A-0 — 将数学符号转换为机器代码
- **1957**：SOAP — 第一个广泛使用的符号汇编器 (IBM 650)
### x86 汇编（1978 年至今）
- **1978**：Intel 8086 — x86 架构诞生
  - 16位寄存器：AX、BX、CX、DX、SI、DI、SP、BP
  - 分段存储器：CS、DS、SS、ES
  - 指令：MOV、ADD、SUB、JMP、CALL、RET、INT
- **1985**：Intel 386 — 32 位 x86 (IA-32)
  - 32位寄存器：EAX、EBX、ECX、EDX
  - 保护模式、分页、虚拟内存
- **2000**：AMD64 — 64 位 x86 扩展
  - 64位寄存器：RAX、RBX、RCX、RDX
  - 16 个通用寄存器（32 位为 8 个）
  - RIP 相对寻址
### ARM 大会（1985 年至今）
- **1985**：ARM1 — Acorn Computers（英国）
  - RISC理念：简单、固定长度的指令
  - 加载/存储架构
  - 16个寄存器（R0-R15），R13=SP，R14=LR，R15=PC
- **2013**：ARM64 (AArch64) — 64 位 ARM
  - 31个通用64位寄存器
  - SIMD：氖、SVE
  - 用于：智能手机、Apple Silicon、AWS Graviton
### RISC-V（2010 年至今）
- **2010**：加州大学伯克利分校创建开放 ISA
- **2020 年代**：RISC-V 受到关注 - 开放，无许可费
- 应用于：嵌入式系统、定制芯片、中国半导体推
## 语法演变
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

## 指令集演变
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

## 关键设计原则
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

## 生态系统增长
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
