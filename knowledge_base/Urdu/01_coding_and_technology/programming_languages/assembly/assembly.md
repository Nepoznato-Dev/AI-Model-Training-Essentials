<!--
---
# Metadata
title: "Assembly Language"
description: "Comprehensive reference for the Assembly programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# اسمبلی کی زبان
اسمبلی لینگویج سب سے نچلی سطح کی انسانی پڑھنے کے قابل پروگرامنگ زبان ہے۔ یہ خام بائنری کی بجائے یادداشت کوڈز (جیسے `MOV`، `ADD`،`JMP`) کا استعمال کرتے ہوئے کمپیوٹر کے مشین کوڈ کی ہدایات کی براہ راست نمائندگی فراہم کرتا ہے۔ ہر اسمبلی کی زبان ایک خاص پروسیسر فن تعمیر کے لیے مخصوص ہے (x86, ARM, MIPS, RISC-V) — ایک فن تعمیر کے لیے لکھا گیا کوڈ دوسرے پر نہیں چلے گا۔
اسمبلی کی زبان ایپلی کیشنز کی تعمیر کے لیے استعمال نہیں کی جاتی ہے۔ اس کا استعمال اس وقت ہوتا ہے جب آپ کو ہارڈ ویئر پر مکمل کنٹرول کی ضرورت ہوتی ہے: آپریٹنگ سسٹم کے کرنل لکھنا، ڈیوائس ڈرائیورز، بوٹ لوڈرز، ایمبیڈڈ فرم ویئر، کارکردگی کے اہم کوڈ سیکشن، ریورس انجینئرنگ، اور یہ سمجھنا کہ کمپیوٹر دراصل ہدایات پر عمل کیسے کرتے ہیں۔
---

## اسمبلی معاملات کیوں؟
- **ہارڈ ویئر کی سمجھ**: یہ جاننے کا واحد طریقہ کہ سی پی یو ہدایات کی سطح پر کیا کر رہا ہے۔
- **پرفارمنس ٹیوننگ**: اہم کوڈ سیکشنز کو کمپائلرز کی تیار کردہ چیزوں سے زیادہ بہتر بنایا جا سکتا ہے۔
- **ریورس انجینئرنگ**: مالویئر تجزیہ، سیکورٹی تحقیق، اور ملکیتی سافٹ ویئر کو سمجھنا۔
- **ایمبیڈڈ سسٹم**: کچھ مائیکرو کنٹرولرز کو اعلی سطحی زبان کی حمایت نہیں ہوتی ہے۔
- **OS ڈیولپمنٹ**: بوٹ کوڈ، انٹرپٹ ہینڈلرز، اور سیاق و سباق کے سوئچنگ کے لیے اسمبلی کی ضرورت ہوتی ہے۔
- **تعلیمی**: اسمبلی کو سمجھنا آپ کو سکھاتا ہے کہ کمپیوٹر دراصل کیسے کام کرتے ہیں — میموری، رجسٹر، اسٹیک، اور CPU پائپ لائن۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **انتہائی نچلی سطح** | ہر ہدایت کا نقشہ ایک مشین کے آپریشن کے لیے | اہم حصوں کے علاوہ ہر چیز کے لیے اعلیٰ درجے کی زبانیں استعمال کریں۔
| **فن تعمیر کے لیے مخصوص** | x86 کوڈ ARM پر نہیں چلتا ہے۔ پورٹیبل کوڈ C/C++ میں لکھیں؛ اسمبلی کا استعمال صرف جہاں ضرورت ہو |
| **لفظی** | آسان کاموں کے لیے بہت سی ہدایات کی ضرورت ہوتی ہے۔ میکرو استعمال کریں؛ اسمبلی حصوں کو کم سے کم رکھیں |
| **کوئی پورٹیبلٹی نہیں** | ہر اسمبلر کے لیے مختلف نحو (NASM, GAS, MASM) | کمپائلر انٹرنکس یا ان لائن اسمبلی کا استعمال کریں۔
| **ڈیبگ کرنے میں دشواری** | ہدایات کی سطح پر منطق کا سراغ لگانا مشکل | ڈیبگرز (GDB) کا استعمال کریں؛ آزادانہ طور پر تبصرے شامل کریں |
---

## نحو کی مثال (x86-64 اسمبلی — NASM)
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

### ARM اسمبلی کی مثال
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

## اعلی درجے کی نحو اور نمونے۔
### x86-64 ایڈریسنگ موڈز
ایڈریسنگ طریقوں کو سمجھنا موثر اسمبلی لکھنے کے لیے اہم ہے۔ ہر موڈ کنٹرول کرتا ہے کہ آپرینڈز کیسے واقع ہیں۔
| موڈ | نحو (NASM) | تفصیل |
|------|---------------|------------|
| **فوری** | `mov eax, 42`| اوپرینڈ ایک مستقل قدر ہے |
| **رجسٹر** | `mov eax, ebx`| اوپرینڈ ایک رجسٹر میں ہے |
| **براہ راست** | `mov eax, [0x4000]`| اوپرینڈ ایک مقررہ میموری ایڈریس پر ہے |
| **بالواسطہ رجسٹر کریں** | `mov eax, [rbx]`| اوپرینڈ رجسٹر میں پتے پر ہے |
| **بیس + نقل مکانی** | `mov eax, [rbx + 8]`| پتہ = رجسٹر + مستقل آفسیٹ |
| **اسکیلڈ انڈیکس** | `mov eax, [rbx + rcx*4]`| پتہ = بنیاد + (انڈیکس × پیمانہ) |
| **مکمل SIB** | `mov eax, [rbx + rcx*4 + 16]`| بیس + (انڈیکس × پیمانہ) + نقل مکانی |
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

### میکرو سسٹم (NASM)
میکروس آپ کو پیرامیٹرز کے ساتھ دوبارہ قابل استعمال ہدایات کے سلسلے کی وضاحت کرنے دیتا ہے، جس سے اسمبلی کم دہرائی جاتی ہے۔
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

### اسٹیک فریم لے آؤٹ
فنکشن لکھنے اور ڈیبگ کرنے کے لیے اسٹیک فریم کو سمجھنا ضروری ہے۔
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

## آرکیٹیکچر اور سسٹم ڈیزائن
### ایک عام x86-64 لینکس عمل کا میموری لے آؤٹ
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

### پروگرام کا ڈھانچہ کنونشن
ایک اچھی طرح سے منظم اسمبلی پروگرام خدشات کو الگ الگ حصوں میں الگ کرتا ہے:
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

### عام پروجیکٹ ڈائرکٹری کا ڈھانچہ
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### لینکس پر NASM + GCC
سب سے عام ورک فلو GCC کو لنکر کے طور پر استعمال کرتے ہوئے C کے ساتھ اسمبلی کو لنک کرتا ہے۔
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

### ونڈوز پر MASM (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (GNU اسمبلر) AT&T Syntax کے ساتھ
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

### خالص اسمبلی پروگرام کو جوڑنا (کوئی سی رن ٹائم نہیں)
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

## کلیدی تصورات
| تصور | تفصیل |
|---------|---------------|
| **رجسٹرز** | CPU کا اندرونی اسٹوریج (EAX, EBX, ECX, EDX x86 پر؛ R0-R15 ARM پر) |
| **میموری ایڈریسنگ** | پتوں کے ذریعے رام تک رسائی حاصل کرنا (`MOV EAX, [0x1000]`) |
| **اسٹیک** | فنکشن کالز اور مقامی متغیرات کے لیے LIFO میموری ریجن (`PUSH`,`POP`) |
| **ہدایات** | بنیادی آپریشنز: ریاضی، منطق، ڈیٹا کی نقل و حرکت، کنٹرول بہاؤ |
| **انٹرپٹس / سیسکلز** | آپریٹنگ سسٹم سے خدمات کی درخواست کرنا |
| **کالنگ کنونشن** | فنکشن کس طرح پیرامیٹرز وصول کرتے ہیں اور قدریں واپس کرتے ہیں (فن تعمیر کے لحاظ سے مختلف ہوتا ہے) |
---

## ٹیسٹنگ اور ڈیبگنگ
### GDB (GNU ڈیبگر)
GDB لینکس پر اسمبلی کے لیے معیاری ڈیبگر ہے۔ یہ آپ کو ہدایات پر عمل کرنے، رجسٹروں کا معائنہ کرنے اور میموری کی جانچ کرنے دیتا ہے۔
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

### NASM میکرو کے ساتھ ڈیبگنگ
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

### عام ڈیبگنگ پیٹرنز
| مسئلہ | علامت | ڈیبگنگ تکنیک |
|---------|---------|-------------------|
| Segfault | SIGSEGV کے ساتھ پروگرام کریش | پوائنٹر اقدار کی جانچ کریں؛ اسٹیک سیدھ کی تصدیق کریں |
| لامحدود لوپ | پروگرام ہینگ | لوپ میں بریک پوائنٹ سیٹ کریں؛ حالت کے جھنڈے چیک کریں |
| غلط نتیجہ | غلط حساب | ریاضی کے ذریعے قدم; ہر ایک کے بعد رجسٹر کی اقدار کو چیک کریں |
| اسٹیک کرپشن | RET پر کریش | PUSH/POP بیلنس کی تصدیق کریں؛ RSP الائنمنٹ چیک کریں (16 بائٹ سیدھ میں ہونا چاہیے) |
| غلط syscall | غیر متوقع دانا سلوک | RAX میں syscall نمبر کی تصدیق کریں؛ دلیل کے رجسٹر چیک کریں |
---

## انٹرآپریبلٹی
### اسمبلی سے C فنکشنز کو کال کرنا
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

### سسٹم کال کا حوالہ (لینکس x86-64)
| Syscall | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|---------|------|------------|------------|------------|------------|
| پڑھیں | 0 | fd | buf | شمار | - |
| لکھیں | 1 | fd | buf | شمار | - |
| کھولیں | 2 | راستے کا نام | جھنڈے | موڈ | - |
| بند | 3 | fd | - | - | - |
| mmap | 9 | addr | لمبائی | پروٹ | جھنڈے |
| باہر نکلیں | 60 | حیثیت | - | - | - |
### C (GCC) میں ان لائن اسمبلی
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

## ڈیزائن پیٹرن
### پیٹرن 1: ایکومولیٹر کے ساتھ لوپ
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

### پیٹرن 2: سٹرنگ پروسیسنگ پائپ لائن
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

### پیٹرن 3: ڈسپیچ ٹیبل (سوئچ/کیس)
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

### پیٹرن 4: لنکڈ لسٹ ٹراورسل
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

## کارکردگی اور اصلاح
### ہدایات کا شیڈولنگ
جدید CPUs پائپ لائننگ اور آؤٹ آف آرڈر ایگزیکیوشن کے ذریعے فی سائیکل متعدد ہدایات پر عمل درآمد کرتے ہیں۔ اس کو سمجھنے سے تیزی سے اسمبلی لکھنے میں مدد ملتی ہے۔
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

### کیشے آپٹیمائزیشن
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

### آپٹیمائزیشن چیک لسٹ
| تکنیک | اثر | تفصیل |
|------------|---------|------------|
| ** رجسٹر استعمال ** | ہائی | گرم متغیرات کو رجسٹر میں رکھیں؛ میموری تک رسائی سے بچیں |
| **لوپ انرولنگ** | میڈیم | ایک سے زیادہ آئٹمز فی تکرار پر کارروائی کرکے لوپ اوور ہیڈ کو کم کریں |
| **SIMD (SSE/AVX)** | بہت اعلیٰ | ویکٹر ہدایات کے ساتھ بیک وقت 4-16 اقدار پر کارروائی کریں |
| **برانچ کا خاتمہ** | میڈیم | جہاں ممکن ہو مشروط چھلانگ کے بجائے CMOV استعمال کریں۔
| **کیشے کی سیدھ** | میڈیم | ہاٹ لوپس کو 16/32 بائٹ کی حدود میں سیدھ میں رکھیں |
| **میموری تک رسائی کے نمونے** | ہائی | ترتیب وار رسائی؛ کیش لائن تقسیم سے بچیں |
---

## تعیناتی اور حقیقی دنیا کا استعمال
### اسمبلی پروگراموں کو کیسے تعینات کیا جاتا ہے۔
اسمبلی پروگرام براہ راست مقامی مشین کوڈ ایگزیکیوٹیبل پر مرتب کرتے ہیں۔ کوئی رن ٹائم، کوئی VM، اور کسی ترجمان کی ضرورت نہیں ہے۔ تعیناتی اتنا ہی آسان ہے جتنا بائنری کو ٹارگٹ سسٹم میں کاپی کرنا۔
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### حقیقی دنیا کے استعمال کے کیسز
| صنعت | درخواست | اسمبلی کیوں |
|------------|------------|------------|
| **آپریٹنگ سسٹم** | لینکس کرنل بوٹ اسٹب، ونڈوز HAL | براہ راست ہارڈویئر کنٹرول، مداخلت ہینڈلنگ |
| **ایمبیڈڈ فرم ویئر** | مائیکرو کنٹرولر بوٹ لوڈرز، IoT آلات | کوئی OS یا رن ٹائم دستیاب نہیں ہے۔ یادداشت کی سخت حدود |
| **سیکیورٹی** | استحصال کی ترقی، مالویئر تجزیہ، ریورس انجینئرنگ | مرتب شدہ بائنریز کے ساتھ تعامل کا واحد طریقہ |
| **گیم انجن** | SIMD-آپٹمائزڈ ریاضی (میٹرکس ٹرانسفارمز، فزکس) | فی فریم حساب کے لیے زیادہ سے زیادہ تھرو پٹ |
| ** مرتب کرنے والے** | کوڈ جنریشن بیک اینڈز (LLVM, GCC) | آپٹمائزڈ مشین کوڈ کا اخراج |
| **کرپٹوگرافی** | AES-NI, SHA انسٹرکشن ایکسلریشن | ہارڈ ویئر کے تیز رفتار کرپٹو آپریشنز |
| ** ڈیوائس ڈرائیورز** | GPU ڈرائیور، نیٹ ورک کارڈ فرم ویئر | براہ راست رجسٹر کی سطح کے ہارڈ ویئر تک رسائی |
### لیگیسی سسٹم انٹیگریشن
بہت سے میراثی نظاموں میں اسمبلی کے معمولات C کوڈ بیس کے اندر شامل ہوتے ہیں۔ یہ عام طور پر کارکردگی کے لیے اہم افعال یا ہارڈ ویئر کے لیے مخصوص معمولات ہیں جو کئی دہائیوں سے برقرار ہیں۔
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

## اسمبلی کب استعمال کریں۔
| منظر نامہ | اسمبلی کیوں | بہتر متبادل |
|------------|---------------|-------------------|
| OS کرنل کی ترقی | بوٹ کوڈ، انٹرپٹ ہینڈلرز | زیادہ تر کرنل کوڈ کے لیے C |
| ڈیوائس ڈرائیورز | براہ راست ہارڈ ویئر تک رسائی | سی، زنگ |
| ریورس انجینئرنگ / سیکورٹی | مرتب شدہ بائنریز کا تجزیہ کرنے کا واحد طریقہ | - |
| کارکردگی کا اہم کوڈ | زیادہ سے زیادہ اصلاح | C/C++ کمپائلر انٹرنکس کے ساتھ |
| ایمبیڈڈ فرم ویئر (ننگی دھات) | کوئی اعلیٰ سطحی زبان دستیاب نہیں ہے۔ سی، زنگ |
| تعلیم | کمپیوٹر فن تعمیر کو سمجھنا | - |
| عام درخواست کی ترقی | پیچیدہ پروگراموں کے لیے غیر عملی | کوئی بھی اعلیٰ سطحی زبان |
---

## مصنوعی سوال و جواب
### Q1: RISC اور CISC اسمبلی میں کیا فرق ہے؟
**A:** CISC (x86) میں پیچیدہ، متغیر لمبائی کی ہدایات ہیں۔ RISC (ARM) کی سادہ، مقررہ لمبائی کی ہدایات ہیں:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### Q2: اسٹیک اسمبلی میں کیسے کام کرتا ہے؟
**A:** اسٹیک نیچے کی طرف بڑھتا ہے۔ `push`SP اور اسٹورز میں کمی `pop`بوجھ اور اضافہ SP:
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

### Q3: میں اسمبلی میں فنکشنز کو کیسے کال کروں؟
**A:** کالنگ کنونشن پر عمل کریں (Linux پر سسٹم V AMD64، ونڈوز پر Windows x64):
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

### Q4: اسمبلی کی سب سے اہم ہدایات کونسی جاننا ضروری ہیں؟
**A:** ڈیٹا کی نقل و حرکت، ریاضی، کنٹرول کا بہاؤ، اور اسٹیک آپریشنز بنیادی حیثیت رکھتے ہیں۔
### Q5: سیکیورٹی ریسرچ میں اسمبلی کا استعمال کیسے کیا جاتا ہے؟
**A:** ریورس انجینئرنگ، ایکسپلائٹ ڈیولپمنٹ، مالویئر تجزیہ، اور کمپائلر آؤٹ پٹ کو سمجھنے کے لیے اسمبلی خواندگی کی ضرورت ہوتی ہے۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: اسمبلی میں لوپ کا نفاذ
**مرحلہ 1: مسئلہ کو سمجھیں**
1 سے N تک جمع عدد۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
کاؤنٹر رجسٹر اور جمع کرنے والا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**مرحلہ 4: بہتر بنائیں**
O(N) کے بجائے O(1) کے لیے فارمولہ N*(N+1)/2 استعمال کریں۔
---

## خلاصہ
اسمبلی لینگویج انسانی پڑھنے کے قابل کوڈ اور خام بائنری کے درمیان پل ہے جسے CPUs عمل میں لاتے ہیں۔ ایپلی کیشنز بنانے کے لیے یہ کوئی عملی انتخاب نہیں ہے، لیکن یہ سمجھنے کے لیے ضروری ہے کہ کمپیوٹر کس طرح نچلی سطح پر کام کرتے ہیں۔ سسٹم پروگرامرز، سیکورٹی ریسرچرز، اور ایمبیڈڈ ڈویلپرز کے لیے، اسمبلی کا علم انمول ہے۔ باقی سب کے لیے، اسمبلی کے تصورات (رجسٹرز، اسٹیک، انسٹرکشن سائیکل) کو سمجھنا آپ کو کسی بھی زبان میں ایک بہتر پروگرامر بناتا ہے۔