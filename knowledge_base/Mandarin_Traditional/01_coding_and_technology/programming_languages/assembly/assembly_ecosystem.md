---
# Metadata
title: "Assembly — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Assembly ecosystem including assemblers, debuggers, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [assembly, ecosystem, tooling, assemblers, debuggers, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Assembly — 生態系統和工具指南
本指南涵蓋了 Assembly 生態系統中的基本工具、彙編器和基礎設施。
---

## 以架構劃分的彙編器
### x86/x86-64
|彙編器|平台|筆記|
|------------|----------|--------|
| **NASM** |跨平台|最受歡迎、簡潔的文法 |
| **MASM** |窗|微軟宏彙編器|
| **FASM** |跨平台|自架，速度快 |
| **氣體（作為）** | Linux/Unix | GNU 彙編器（AT&T 語法）|
| **亞斯姆** |跨平台| NASM 相容 |
| **UASM** |跨平台| MASM 相容 |
＃＃＃ 手臂
|彙編器|平台|筆記|
|------------|----------|--------|
| **GNU 作為 (ARM)** |跨平台| ARM 彙編 |
| **Keil ASM** |嵌入式| ARM開發|
| **ARM 組譯器** | ARM | ARM 編譯器套件 |
＃＃＃ 其他
|彙編器|建築|筆記|
|------------|-------------|--------|
| **avr-as** | AVR |微控制器|
| **拉斯姆** | Z80 |復古計算 |
| **ca65** | 6502 | 6502 NES，準將 |
| **SPIM / 火星** |米普斯 |教育 |
```bash
# NASM (Linux x86-64)
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello

# NASM (Windows)
nasm -f win64 hello.asm -o hello.obj
golink /console /entry _start hello.obj

# FASM
fasm hello.asm hello

# GAS (AT&T syntax)
as -o hello.o hello.s
ld hello.o -o hello
```

---

## 偵錯工具
|工具|建築|目的|
|------|-------------|---------|
| **GDB** | x86/ARM | GNU 偵錯器 |
| **lldb** |跨平台| LLVM 偵錯器 |
| **x64dbg** | x86/x86-64 | Windows GUI 偵錯器 |
| **OllyDbg** | x86 |經典 Windows 偵錯器 |
| **IDA 專業版** |跨平台|反組譯器/反編譯器 |
| **吉德拉** |跨平台| NSA 逆向工程 |
| **雷達雷2** |跨平台| CLI 逆向工程 |
| **切割機** |跨平台|雷達2的GUI |
```bash
# GDB
gdb ./hello
(gdb) break main
(gdb) run
(gdb) info registers
(gdb) stepi
(gdb) x/10i $rip        # disassemble 10 instructions

# x64dbg (Windows)
# GUI-based, load executable, set breakpoints, step through
```

---

## 仿真器與模擬器
|工具|建築|目的|
|------|-------------|---------|
| **QEMU** |多拱 |全系統模擬 |
| **博克斯** | x86 | x86 模擬器 |
| **DOSBox** | x86 | DOS環境|
| **媽媽** |多|街機/復古模擬|
| **SPIM** |米普斯 | MIPS 模擬器 |
| **火星** |米普斯 | MIPS IDE/模擬器 |
| **SIMAVR** | AVR | AVR模擬器|
| **獨角獸** |多拱 | CPU模擬框架|
---

## 建置工具
|工具|目的|
|------|---------|
| **製作** |經典建置自動化 |
| **CMake** |跨平台建置 |
| **ld** | GNU 連結器 |
| **lld** | LLVM 連結器 |
| **物件複製** |二進位操作 |
| **objdump** |拆解|
| **readelf / nm** |符號檢查|
| **十六進位轉儲** |二元檢定|
```makefile
# Makefile for NASM project
ASM = nasm
ASM_FLAGS = -f elf64
LD = ld
TARGET = hello

all: $(TARGET)

$(TARGET): hello.o
	$(LD) hello.o -o $(TARGET)

hello.o: hello.asm
	$(ASM) $(ASM_FLAGS) hello.asm -o hello.o

clean:
	rm -f *.o $(TARGET)
```

---

## 關鍵庫
|圖書館 |建築|目的|
|---------|-------------|---------|
| **libc** | x86/ARM |標準 C 函式庫（系統呼叫包裝器）|
| **Linux 系統呼叫** | x86/ARM |直接核心呼叫|
| **Windows API** | x86/x64 | Win32/64 API |
| **BIOS 中斷** | x86 |傳統 PC BIOS |
| **DOS 中斷** | x86 | DOS 服務 |
| **libgcc** |跨平台| GCC 運行時 |
| **新函式庫** |嵌入式|輕量級 libc |
---

## 測試
|工具|目的|
|------|---------|
| **自訂測試工具** |組裝測試框架|
| **團結** |基於 C 的單元測試（適用於混合項目）|
| **Google測試** | C++ 測試（針對混合專案）|
| **自訂巨集** |斷言巨集 |
```nasm
; NASM test example
section .data
    test_pass db "PASS", 10, 0
    test_fail db "FAIL", 10, 0

section .text
    global _start

test_add:
    mov rax, 2
    mov rbx, 3
    add rax, rbx
    cmp rax, 5
    jne .fail
    ; print pass
    mov rax, 1
    mov rdi, 1
    mov rsi, test_pass
    mov rdx, 5
    syscall
    ret
.fail:
    mov rax, 1
    mov rdi, 1
    mov rsi, test_fail
    mov rdx, 5
    syscall
    ret

_start:
    call test_add
    mov rax, 60
    xor rdi, rdi
    syscall
```

---

## 程式碼品質
|工具|目的|
|------|---------|
| **objdump -d** |拆檢|
| **吉德拉** |逆向工程分析 |
| **IDA 專業版** |專業拆解|
| **雷達雷2** | CLI分析|
| **瓦爾格林德** |內存錯誤檢測|
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS 代碼 + NASM** |彙編語法高亮|
| **SASM** |簡單的 ASM IDE（教育）|
| **Emacs + nasm 模式** |經典組裝編輯 |
| **火星** | MIPS 教育 IDE |
| **DOSBox + 編輯** |復古發展|
---

## 部署
|方法|筆記|
|--------|--------|
| **靜態二進位** |直接機器碼|
| **引導磁區** | 512 位元組引導程式 |
| **核心模組** |作業系統核心程式碼|
| **韌體** |嵌入式韌體|
| **ROM/快閃記憶體** |微控制器程式碼|
| **碼頭工人** |搭建環境|
---

＃＃ 概括
Assembly 的生態系統是特定於體系結構的，並且設計極簡。標準工具鍊是：用於彙編的 **NASM** (x86/x86-64) 或 **GNU as** (ARM)、用於連結的 **ld**、用於調試的 **GDB**、用於逆向工程的 **Ghidra** 或 **IDA Pro** 以及用於模擬的 **QEMU**。 Assembly 擅長作業系統開發、嵌入式系統、逆向工程、效能關鍵程式碼和引導程式開發。此生態系統對於理解電腦如何在最低層級運作至關重要。對於學習而言，**MARS** (MIPS) 和 **SASM** (x86) 提供了適合初學者的環境。