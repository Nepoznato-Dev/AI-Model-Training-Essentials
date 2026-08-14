---
# Metadata
title: "Assembly Language"
description: "Comprehensive reference for the Assembly programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [assembly, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# 組合語言
組合語言是最低階的人類可讀的程式語言。它使用助記符代碼（如`MOV`、`ADD`、`JMP`）而不是原始二進位來直接表示計算機的機器代碼指令。每種組合語言都特定於特定的處理器架構（x86、ARM、MIPS、RISC-V）——為一種架構編寫的程式碼無法在另一種架構上運作。
彙編語言不用於建立應用程式。當您需要對硬體進行絕對控制時，可以使用它：編寫作業系統核心、裝置驅動程式、引導程式、嵌入式韌體、效能關鍵程式碼部分、逆向工程以及了解電腦實際如何執行指令。
---

## 為什麼組裝很重要
- **硬體理解**：準確了解CPU在指令層級正在做什麼的唯一方法。
- **效能調整**：關鍵程式碼部分可以進行超出編譯器產生的最佳化。
- **逆向工程**：惡意軟體分析、安全研究和了解專有軟體。
- **嵌入式系統**：某些微控制器沒有高階語言支援。
- **作業系統開發**：啟動程式碼、中斷處理程序和上下文切換需要彙編。
- **教育**：了解彙編會教您電腦的實際工作方式 - 記憶體、暫存器、堆疊和 CPU 管道。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **極低級** |每條指令對應一台機器操作|除了關鍵部分之外的所有事情都使用高級語言 |
| **特定於架構** | x86 程式碼無法在 ARM 上運行 |用 C/C++ 編寫可移植程式碼；僅在需要時使用彙編 |
| **詳細** |簡單的任務需要很多指令 |使用巨集；盡量減少組裝部分 |
| **沒有便攜性** |每個彙編器的不同語法（NASM、GAS、MASM）|使用編譯器內部函數或內聯彙編 |
| **調試難度** |指令級邏輯難以追蹤|使用調試器（GDB）；隨意添加評論 |
---

## 語法範例（x86-64 彙編 — NASM）
```nasm
; A simple program that adds two numbers and exits
section .data
    num1    dd  10          ; 32-bit integer: 10
    num2    dd  20          ; 32-bit integer: 20

section .bss
    result  resd 1          ; Reserve space for result

section .text
    global _start

_start:
    ; Load numbers into registers
    mov     eax, [num1]     ; Move num1 into EAX register
    add     eax, [num2]     ; Add num2 to EAX
    
    ; Store result
    mov     [result], eax   ; Store EAX in result
    
    ; Exit system call (Linux)
    mov     eax, 60         ; syscall number for exit
    mov     edi, 0          ; exit code 0
    syscall                 ; invoke kernel
```

### ARM 組譯範例
```arm
; ARM assembly — add two numbers
    .data
num1:   .word 10
num2:   .word 20

    .text
    .global _start

_start:
    LDR R0, =num1       ; Load address of num1 into R0
    LDR R1, [R0]        ; Load value at address into R1
    LDR R2, =num2       ; Load address of num2 into R2
    LDR R3, [R2]        ; Load value at address into R3
    ADD R4, R1, R3      ; R4 = R1 + R3
```

---

## 進階語法和模式
### x86-64 尋址模式
了解尋址模式對於編寫高效的彙編至關重要。每種模式控制操作數的定位方式。
|模式|語法 (NASM) |描述 |
|------|----------------|-------------|
| **立即** |`mov eax, 42`|操作數是一個常數值 |
| **註冊** |`mov eax, ebx`|操作數在暫存器中 |
| **直接** |`mov eax, [0x4000]`|運算元位於固定的記憶體位址|
| **間接註冊** |`mov eax, [rbx]`|運算元位於暫存器中的位址 |
| **基礎+位移** |`mov eax, [rbx + 8]`|位址=暫存器+常數偏移|
| **比例索引** |`mov eax, [rbx + rcx*4]`|位址 = 基址 + (索引 × 小數位數) |
| **完整的SIB** |`mov eax, [rbx + rcx*4 + 16]`|底數+（索引×比例）+位移|
```nasm
; Demonstrating various addressing modes
section .data
    array   dd  10, 20, 30, 40, 50

section .text
    ; Register indirect — traverse an array
    lea     rbx, [array]        ; RBX points to array start
    mov     eax, [rbx]          ; eax = array[0] = 10
    mov     eax, [rbx + 4]     ; eax = array[1] = 20

    ; Scaled index — access array[i] where i is in rcx
    mov     rcx, 2              ; index = 2
    mov     eax, [rbx + rcx*4] ; eax = array[2] = 30

    ; Loop through array with scaled index
    xor     rcx, rcx            ; i = 0
.loop:
    mov     eax, [rbx + rcx*4] ; load array[i]
    add     eax, 1              ; increment value
    mov     [rbx + rcx*4], eax ; store back
    inc     rcx                 ; i++
    cmp     rcx, 5
    jl      .loop               ; continue while i < 5
```

### 宏觀系統（NASM）
巨集可讓您使用參數定義可重複使用的指令序列，從而減少彙編的重複性。
```nasm
; Define a macro to print a string via Linux syscall
%macro print_string 2
    mov     rax, 1              ; syscall: write
    mov     rdi, 1              ; file descriptor: stdout
    mov     rsi, %1             ; address of string
    mov     rdx, %2             ; length of string
    syscall
%endmacro

; Define a macro for function prologue
%macro function_prologue 1
    push    rbp
    mov     rbp, rsp
    sub     rsp, %1             ; allocate local variable space
%endmacro

; Define a macro for function epilogue
%macro function_epilogue 0
    mov     rsp, rbp
    pop     rbp
    ret
%endmacro

section .data
    msg     db  'Hello, Macro!', 10
    msg_len equ $ - msg

section .text
    global _start

_start:
    print_string msg, msg_len

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
```

### 堆疊幀佈局
了解堆疊幀對於編寫函數和調試至關重要。
```
High Address
+------------------+
| Function args    |  (pushed by caller)
+------------------+
| Return address   |  (pushed by CALL instruction)
+------------------+
| Saved RBP        |  <-- RBP points here after prologue
+------------------+
| Local variables  |  <-- RSP points here (grows downward)
|                  |
Low Address
```

```nasm
; Function with stack-allocated local variables
section .text
    global compute_sum

; int compute_sum(int* arr, int count)
; System V AMD64 ABI: rdi = arr, rsi = count
compute_sum:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16             ; 16 bytes for locals

    mov     [rbp - 4], dword 0  ; int sum = 0
    mov     [rbp - 8], dword 0  ; int i = 0

.loop:
    mov     eax, [rbp - 8]      ; load i
    cmp     eax, esi            ; compare i with count
    jge     .done               ; if i >= count, exit loop

    ; sum += arr[i]
    mov     eax, [rbp - 4]                          ; load sum
    mov     ecx, [rbp - 8]                          ; load i
    add     eax, [rdi + rcx*4]                      ; add arr[i]
    mov     [rbp - 4], eax                          ; store sum

    mov     eax, [rbp - 8]
    inc     eax
    mov     [rbp - 8], eax                          ; i++
    jmp     .loop

.done:
    mov     eax, [rbp - 4]      ; return value in EAX
    mov     rsp, rbp
    pop     rbp
    ret
```

---

## 架構與系統設計
### 典型 x86-64 Linux 進程的記憶體佈局
```
Address
0x7FFF_FFFF_FFFF  +------------------+
                   | Stack            |  (grows downward)
                   |        ↓         |
                   |                  |
                   |        ↑         |
                   | Heap             |  (grows upward)
                   +------------------+
                   | BSS              |  (uninitialized data)
                   +------------------+
                   | Data             |  (initialized global/static data)
                   +------------------+
                   | Text (Code)      |  (executable instructions)
0x0040_0000        +------------------+
```

### 程式結構約定
組織良好的組裝程序將關注點分為不同的部分：
```nasm
; ============================================================
; Program: example.asm
; Description: Demonstrates standard program layout
; Assembler: NASM
; Platform:  Linux x86-64
; ============================================================

; --- Constants ---
section .rodata
    fmt_int     db  "%d", 10, 0     ; printf format for integer
    fmt_str     db  "%s", 0         ; printf format for string
    MAX_SIZE    equ 1024

; --- Initialized data ---
section .data
    greeting    db  "Hello, World!", 0
    numbers     dd  1, 2, 3, 4, 5
    count       dq  5

; --- Uninitialized data ---
section .bss
    buffer      resb MAX_SIZE       ; 1KB buffer
    result      resd 1              ; single 32-bit integer
    temp_array  resd 256            ; 256 integers

; --- Code ---
section .text
    global main
    extern printf

main:
    push    rbp
    mov     rbp, rsp

    ; ... program logic ...

    xor     eax, eax                ; return 0
    mov     rsp, rbp
    pop     rbp
    ret
```

### 典型的專案目錄結構
```
project/
├── src/
│   ├── main.asm           ; Entry point
│   ├── io.asm             ; I/O routines
│   ├── math.asm           ; Arithmetic helpers
│   └── string.asm         ; String operations
├── include/
│   ├── constants.inc      ; Equ/constant definitions
│   ├── macros.inc         ; Shared macro definitions
│   └── structs.inc        ; Structure definitions
├── Makefile               ; Build configuration
├── linker.ld              ; Custom linker script (optional)
└── README.md
```

---

## 專案配置與建置系統
### Linux 上的 NASM + GCC
最常見的工作流程使用 GCC 作為連結器將彙編與 C 連結。
```makefile
# Makefile for NASM + GCC project
ASM      = nasm
CC       = gcc
ASMFLAGS = -f elf64 -g -F dwarf
CFLAGS   = -Wall -g -no-pie
LDFLAGS  =

SRCS     = main.asm io.asm math.asm
OBJS     = $(SRCS:.asm=.o)
TARGET   = program

all: $(TARGET)

%.o: %.asm
$(ASM) $(ASMFLAGS) $< -o $@

$(TARGET): $(OBJS)
$(CC) $(CFLAGS) $(OBJS) -o $(TARGET) $(LDFLAGS)

clean:
rm -f $(OBJS) $(TARGET)

debug: $(TARGET)
gdb ./$(TARGET)

run: $(TARGET)
./$(TARGET)

.PHONY: all clean debug run
```

### Windows 上的 MASM (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS（GNU 彙編器）與 AT&T 語法
```makefile
# Makefile for GAS (AT&T syntax)
AS       = as
LD       = ld
ASFLAGS  = --gstabs
LDFLAGS  = -static

TARGET   = program

all: $(TARGET)

$(TARGET): main.o
$(LD) $(LDFLAGS) main.o -o $(TARGET)

main.o: main.s
$(AS) $(ASFLAGS) main.s -o main.o

clean:
rm -f main.o $(TARGET)
```

### 連結純組譯器（無 C 運行時）
```nasm
; standalone.asm — No C library dependency, Linux x86-64
section .data
    msg     db  'Standalone program', 10
    msg_len equ $ - msg

section .text
    global _start           ; Entry point for ELF (no main)

_start:
    ; write(1, msg, msg_len)
    mov     rax, 1          ; sys_write
    mov     rdi, 1          ; stdout
    mov     rsi, msg
    mov     rdx, msg_len
    syscall

    ; exit(0)
    mov     rax, 60         ; sys_exit
    xor     rdi, rdi        ; code 0
    syscall
```

```bash
# Build without C runtime
nasm -f elf64 standalone.asm -o standalone.o
ld standalone.o -o standalone
```

---

## 關鍵概念
|概念 |描述 |
|---------|-------------|
| **寄存器** | CPU 的内部存储（x86 上的 EAX、EBX、ECX、EDX；ARM 上的 R0-R15）|
| **内存寻址** |通过地址访问 RAM (`MOV EAX, [0x1000]`) |
| **堆栈** |用于函数调用和局部变量的 LIFO 内存区域（`PUSH`、`POP`） |
| **说明** |基本运算：算术、逻辑、数据移动、控制流 |
| **中断/系统调用** |向操作系统请求服务 |
| **调用约定** |函数如何接收参数和返回值（因架构而异）|
---

## 測試和調試
### GDB（GNU 偵錯器）
GDB 是 Linux 上彙編的標準偵錯器。它可以讓您逐步執行指令、檢查暫存器並檢查記憶體。
```bash
# Build with debug symbols
nasm -f elf64 -g -F dwarf program.asm -o program.o
gcc -g -no-pie program.o -o program

# Start GDB
gdb ./program
```

```gdb
# Essential GDB commands for assembly debugging
(gdb) break _start              # Set breakpoint at entry point
(gdb) break *0x401040           # Set breakpoint at specific address
(gdb) run                       # Start execution
(gdb) si                        # Step one instruction (stepi)
(gdb) ni                        # Step over one instruction (nexti)
(gdb) info registers            # Show all register values
(gdb) print $rax                # Print specific register
(gdb) x/10xw $rsp               # Examine 10 words of stack in hex
(gdb) x/s 0x402000              # Examine memory as string
(gdb) disas /r                  # Disassemble with raw bytes
(gdb) layout regs               # Show register + assembly view
(gdb) continue                  # Continue execution
```

### 使用 NASM 巨集進行偵錯
```nasm
; Debug print macro — prints register value via C printf
%macro debug_print_reg 1
    push    rax
    push    rdi
    push    rsi
    mov     rsi, %1             ; value to print
    mov     rdi, fmt_int        ; format string
    xor     eax, eax            ; AL = 0 (no FP args)
    call    printf wrt ..plt
    pop     rsi
    pop     rdi
    pop     rax
%endmacro
```

### 常見偵錯模式
|問題 |症狀|調試技術|
|--------|---------|--------------------|
|段錯誤 |程式因 SIGSEGV 崩潰 |檢查指標值；驗證堆疊對齊 |
|無限循環|程式掛起 |在循環中設定斷點；檢查條件標誌|
|錯誤結果 |計算錯誤 |逐步進行算術運算；每次操作後檢查暫存器值 |
|堆疊損壞 | RET 崩潰 |驗證PUSH/POP餘額；檢查 RSP 對齊（必須是 16 位元組對齊） |
|錯誤的系統呼叫 |意外的核心行為 |驗證 RAX 中的系統呼叫號碼；檢查參數暫存器|
---

## 互通性
### 從組譯呼叫 C 函數
```nasm
; Calling printf from assembly (Linux x86-64, System V ABI)
section .data
    fmt     db  "The answer is: %d", 10, 0

section .text
    global main
    extern printf

main:
    push    rbp
    mov     rbp, rsp

    ; printf requires RAX = 0 when passing integer args in registers
    mov     rdi, fmt            ; 1st arg: format string
    mov     rsi, 42             ; 2nd arg: the integer value
    xor     eax, eax            ; AL = 0 (no vector registers used)
    call    printf

    xor     eax, eax            ; return 0
    mov     rsp, rbp
    pop     rbp
    ret
```

### 系統呼叫參考 (Linux x86-64)
|系統呼叫|拉克斯|精胺酸1 (RDI) | Arg2 (RSI) |精胺酸3 (RDX) | Arg4 (R10) |
|--------|-----|------------|------------|------------|------------|
|閱讀 | 0 | FD |緩衝區|計數| — |
|寫入 | 1 | FD |緩衝區|計數| — |
|開啟| 2 |路徑名稱 |旗幟|模式 | — |
| 關閉 | 3 | FD | — | — | — |
|映射 | 9 |地址|長度|普特|旗幟|
|退出 | 60|狀態 | — | — | — |
### C 中的內聯彙編 (GCC)
```c
// Using GCC inline assembly to access CPUID
#include <stdio.h>

int main() {
    unsigned int eax, ebx, ecx, edx;

    __asm__ volatile(
        "cpuid"
        : "=a"(eax), "=b"(ebx), "=c"(ecx), "=d"(edx)
        : "a"(0)  // input: EAX = 0 (get vendor string)
    );

    printf("CPU Vendor: %.4s%.4s%.4s\n",
           (char*)&ebx, (char*)&edx, (char*)&ecx);
    return 0;
}
```

---

## 設計模式
### 模式 1：有累加器的循環
```nasm
; Sum an array of integers — classic accumulator pattern
; RDI = pointer to array, ESI = count
; Returns sum in EAX
array_sum:
    xor     eax, eax            ; sum = 0 (accumulator)
    xor     ecx, ecx            ; i = 0 (counter)
.loop:
    cmp     ecx, esi
    jge     .done
    add     eax, [rdi + rcx*4]  ; sum += arr[i]
    inc     ecx
    jmp     .loop
.done:
    ret
```

### 模式 2：字串處理管道
```nasm
; Convert string to uppercase in-place
; RDI = pointer to null-terminated string
to_upper:
    mov     al, [rdi]           ; load byte
    test    al, al              ; check for null terminator
    jz      .done
    cmp     al, 'a'             ; if byte < 'a', skip
    jl      .next
    cmp     al, 'z'             ; if byte > 'z', skip
    jg      .next
    sub     al, 32              ; convert lowercase to uppercase
    mov     [rdi], al
.next:
    inc     rdi
    jmp     to_upper
.done:
    ret
```

### 模式 3：調度表（開關/案例）
```nasm
; Jump table implementation — equivalent to switch/case
section .data
    dispatch_table dq case_0, case_1, case_2, case_3
    default_msg    db "Unknown option", 10, 0

section .text
; RDI = option number (0-3)
dispatch:
    cmp     rdi, 3
    ja      .default            ; out of range -> default
    jmp     [dispatch_table + rdi*8]

case_0:
    ; handle case 0
    ret
case_1:
    ; handle case 1
    ret
case_2:
    ; handle case 2
    ret
case_3:
    ; handle case 3
    ret
.default:
    ret
```

### 模式4：鍊錶遍歷
```nasm
; Structure: Node { int value; Node* next; }
; RDI = pointer to head node
; Returns sum of all node values in EAX
list_sum:
    xor     eax, eax            ; sum = 0
    test    rdi, rdi            ; check for NULL head
    jz      .done
.traverse:
    add     eax, [rdi]          ; add node.value to sum
    mov     rdi, [rdi + 8]      ; move to node.next (offset 8)
    test    rdi, rdi            ; check for NULL
    jnz     .traverse
.done:
    ret
```

---

## 效能與最佳化
### 指令調度
現代 CPU 透過管線和亂序執行在每個週期執行多條指令。理解這一點有助於編寫更快的彙編。
```nasm
; BAD: Data dependency stalls the pipeline
mov     eax, [mem]          ; load (latency ~4 cycles)
add     ebx, eax            ; must wait for load to complete
mov     [mem2], ebx         ; must wait for add

; GOOD: Independent instructions fill the pipeline
mov     eax, [mem]          ; load
mov     ecx, [mem3]         ; independent load (executes in parallel)
add     ebx, eax            ; depends on first load
add     edx, ecx            ; independent — can execute while waiting
mov     [mem2], ebx
mov     [mem4], edx
```

### 快取優化
```nasm
; BAD: Stride access pattern (cache-unfriendly)
    xor     rcx, rcx
.loop:
    mov     al, [buffer + rcx*64]   ; each access is a cache miss
    inc     rcx
    cmp     rcx, 1024
    jl      .loop

; GOOD: Sequential access (cache-friendly)
    xor     rcx, rcx
.loop:
    mov     al, [buffer + rcx]      ; sequential — prefetcher helps
    inc     rcx
    cmp     rcx, 1024
    jl      .loop
```

### 優化清單
|技術|影響 |描述 |
|------------|--------|-------------|
| **註冊使用** |高|將熱變數保存在暫存器中；避免記憶體存取|
| **循環展開** |中等|透過每次迭代處理多個項目來減少循環開銷 |
| **SIMD（SSE/AVX）** |非常高 |使用向量指令同時處理 4-16 個值 |
| **分支消除** |中|盡可能使用 CMOV 而不是條件跳躍 |
| **快取對齊** |中|將熱循環與 16/32 位元組邊界對齊 |
| **記憶體存取模式** |高|順序存取；避免快取行分割 |
---

## 部署和實際使用
### 彙編程式是如何部署的
彙編程式直接編譯為本機機器碼可執行檔。沒有運作時，沒有虛擬機，也不需要解釋器。部署就像將二進位檔案複製到目標系統一樣簡單。
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### 現實世界用例
|工業|應用 |為什麼要裝配|
|----------|-------------|-------------|
| **作業系統** | Linux 核心啟動存根、Windows HAL |直接硬體控制、中斷處理|
| **嵌入式韌體** |微控制器引導程式、物聯網設備 |沒有可用的作業系統或運行時；嚴格的記憶體限制|
| **安全性** |漏洞利用開發、惡意軟體分析、逆向工程 |與已編譯的二進位檔案互動的唯一方法|
| **遊戲引擎** | SIMD 最佳化數學（矩陣變換、物理）|每幀計算的最大吞吐量|
| **編譯器** |程式碼產生後端（LLVM、GCC）|發出最佳化的機器碼 |
| **密碼學** | AES-NI、SHA指令加速 |硬體加速加密作業 |
| **裝置驅動程式** | GPU驅動程式、網路卡韌體|直接暫存器級硬體存取|
### 遺留系統集成
許多遺留系統包含嵌入 C 程式碼庫中的彙編例程。這些通常是性能關鍵函數或已維護數十年的特定於硬體的例程。
```c
// Legacy pattern: C code calling an assembly-optimized function
extern void fast_memcpy(void* dest, const void* src, size_t n);

void process_data(void) {
    char buffer[4096];
    // Calls hand-optimized assembly using REP MOVSQ or SIMD
    fast_memcpy(buffer, source_data, sizeof(buffer));
}
```

---

## 何時使用彙編
|場景|為什麼要組裝|更好的選擇|
|----------|-------------|--------------------|
|作業系統核心開發|引導程式碼、中斷處理程序|用於大多數核心程式碼的 C |
|設備驅動程式|直接硬體存取| C、鐵鏽|
|逆向工程/安全|分析編譯的二進位檔案的唯一方法| — |
|效能關鍵程式碼 |最大最佳化|具有編譯器內在函數的 C/C++ |
|嵌入式韌體（裸機）|沒有可用的高階語言 | C、鐵鏽|
|教育 |了解電腦體系結構 | — |
|通用應用程式開發 |對於複雜的程式來說不切實際 |任何高階語言 |
---

## 綜合問答
### Q1：RISC 和 CISC 彙編有什麼不同？
**答：** CISC (x86) 具有複雜的、可變長度的指令。 RISC (ARM) 有簡單、固定長度的指令：
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### Q2：堆疊在彙編中如何運作？
**A:** 堆疊向下增長。 `push`減少 SP 並儲存；`pop`載入並遞增 SP：
```asm
; x86 stack operations
push rax          ; save rax on stack
push rbx          ; save rbx
; ... do work ...
pop rbx           ; restore rbx
pop rax           ; restore rax

; Stack frame for functions
push rbp          ; save old base pointer
mov rbp, rsp      ; set new base pointer
sub rsp, 32       ; allocate 32 bytes for locals
; ... function body ...
mov rsp, rbp      ; deallocate locals
pop rbp           ; restore base pointer
ret               ; return
```

### Q3：如何在組譯中呼叫函數？
**A:** 遵循呼叫約定（Linux 上為 System V AMD64，Windows 上為 Windows x64）：
```asm
; System V AMD64: args in rdi, rsi, rdx, rcx, r8, r9
; Return value in rax
extern printf

section .data
    fmt db "Result: %d", 10, 0

section .text
global main
main:
    mov rdi, fmt      ; first arg: format string
    mov rsi, 42       ; second arg: integer
    xor rax, rax      ; no vector registers used
    call printf       ; call C function
    xor rax, rax      ; return 0
    ret
```

### Q4：需要了解的最重要的組裝說明是什麼？
**A:** 資料移動、算術、控制流和堆疊操作構成了核心。
### Q5：彙編如何用於安全研究？
**答：** 逆向工程、漏洞利用開發、惡意軟體分析和理解編譯器輸出都需要組合語言。
---

## 解決問題的思路
### 問題 1：在組譯中實作循環
**第 1 步：了解問題**
對 1 到 N 之間的整數求和。
**第 2 步：確定方法**
使用计数器寄存器和累加器。
**步驟 3：實施**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**第 4 步：優化**
使用公式 N*(N+1)/2 表示 O(1)，而不是 O(N)。
---

＃＃ 概括
組譯語言是人類可讀程式碼和 CPU 執行的原始二進位檔案之間的橋樑。它不是建立應用程式的實用選擇，但對於理解電腦在最低層級的工作方式至關重要。對於系統程式設計師、安全研究人員和嵌入式開發人員來說，彙編知識是無價的。對於其他人來說，理解彙編概念（暫存器、堆疊、指令週期）可以讓你成為任何語言的更好的程式設計師。