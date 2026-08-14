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
# زبان اسمبلی
زبان اسمبلی پایین ترین زبان برنامه نویسی قابل خواندن توسط انسان است. این یک نمایش مستقیم از دستورالعمل‌های کد ماشین کامپیوتر با استفاده از کدهای یادگاری (مانند `MOV`، `ADD`، `JMP`) به جای باینری خام ارائه می‌کند. هر زبان اسمبلی مختص معماری پردازنده خاصی است (x86، ARM، MIPS، RISC-V) – کد نوشته شده برای یک معماری روی معماری دیگر اجرا نمی شود.
زبان اسمبلی برای ساخت برنامه ها استفاده نمی شود. زمانی استفاده می‌شود که به کنترل مطلق بر روی سخت‌افزار نیاز دارید: نوشتن هسته‌های سیستم‌عامل، درایورهای دستگاه، بوت‌لودرها، سفت‌افزار تعبیه‌شده، بخش‌های کد حیاتی عملکرد، مهندسی معکوس، و درک اینکه چگونه رایانه‌ها در واقع دستورالعمل‌ها را اجرا می‌کنند.
---

## چرا مجمع مهم است
- ** درک سخت افزار **: تنها راه برای دانستن اینکه CPU دقیقاً چه کاری را در سطح دستورالعمل انجام می دهد.
- **تنظیم عملکرد**: بخش های کد بحرانی را می توان فراتر از آنچه کامپایلرها تولید می کنند بهینه کرد.
- **مهندسی معکوس**: تجزیه و تحلیل بدافزار، تحقیقات امنیتی و درک نرم افزارهای اختصاصی.
- **سیستم های تعبیه شده**: برخی از میکروکنترلرها پشتیبانی از زبان سطح بالاتر ندارند.
- **توسعه سیستم عامل**: کد بوت، کنترل کننده های وقفه و تعویض متن نیاز به مونتاژ دارند.
- **آموزشی**: درک اسمبلی به شما می آموزد که کامپیوترها در واقع چگونه کار می کنند - حافظه، رجیسترها، پشته و خط لوله CPU.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **فوق العاده سطح پایین** | هر دستورالعمل به یک عملیات ماشین نگاشت می شود | از زبان های سطح بالاتر برای همه چیز به جز بخش های مهم | استفاده کنید
| **معماری خاص** | کد x86 روی ARM اجرا نمی شود | نوشتن کد قابل حمل در C/C++. از مونتاژ فقط در صورت نیاز استفاده کنید |
| **پرمخاطب** | کارهای ساده به دستورالعمل های زیادی نیاز دارند | استفاده از ماکروها؛ بخش های مونتاژ را حداقل نگه دارید |
| **بدون قابلیت حمل** | نحو مختلف برای هر اسمبلر (NASM، GAS، MASM) | استفاده از ذاتی کامپایلر یا اسمبلی درون خطی |
| **مشکل اشکال زدایی** | ردیابی منطق در سطح دستورالعمل سخت است | استفاده از اشکال زدا (GDB)؛ اضافه کردن نظرات آزادانه |
---

## مثال نحوی (مجموعه x86-64 - NASM)
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

### نمونه مونتاژ ARM
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

## نحو و الگوهای پیشرفته
### x86-64 حالت های آدرس دهی
درک حالت های آدرس دهی برای نوشتن مونتاژ کارآمد بسیار مهم است. هر حالت نحوه قرارگیری عملوندها را کنترل می کند.
| حالت | نحو (NASM) | توضیحات |
|------|---------------|-------------|
| **فوری** | `mov eax, 42`| عملوند یک مقدار ثابت است |
| **ثبت نام** | `mov eax, ebx`| عملوند در یک رجیستر است |
| **مستقیم** | `mov eax, [0x4000]`| عملوند در یک آدرس حافظه ثابت است |
| **ثبت نام غیر مستقیم** | `mov eax, [rbx]`| عملوند در آدرس موجود در یک ثبات |
| **پایه + جابجایی** | `mov eax, [rbx + 8]`| نشانی = ثبت + افست ثابت |
| **شاخص مقیاس شده** | `mov eax, [rbx + rcx*4]`| آدرس = پایه + (شاخص × مقیاس) |
| **SIB کامل** | `mov eax, [rbx + rcx*4 + 16]`| پایه + (شاخص × مقیاس) + جابجایی |
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

### سیستم ماکرو (NASM)
ماکروها به شما امکان می دهند توالی دستورالعمل های قابل استفاده مجدد را با پارامترها تعریف کنید و مونتاژ را کمتر تکرار کنید.
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

### چیدمان قاب پشته
درک قاب پشته برای نوشتن توابع و اشکال زدایی ضروری است.
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

## معماری و طراحی سیستم
### چیدمان حافظه یک فرآیند لینوکس معمولی x86-64
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

### کنوانسیون ساختار برنامه
یک برنامه مونتاژ به خوبی سازماندهی شده نگرانی ها را به بخش های مجزا تقسیم می کند:
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

### ساختار دایرکتوری پروژه معمولی
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

## پیکربندی پروژه و سیستم ساخت
### NASM + GCC در لینوکس
رایج ترین پیوندهای گردش کار با C با استفاده از GCC به عنوان پیونددهنده پیوند می دهد.
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

### MASM در ویندوز (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (GNU Assembler) با AT&T Syntax
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

### پیوند دادن یک برنامه Pure Assembly (بدون زمان اجرا C)
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

## مفاهیم کلیدی
| مفهوم | توضیحات |
|---------|-------------|
| **ثبت نام** | حافظه داخلی CPU (EAX، EBX، ECX، EDX در x86؛ R0-R15 در ARM) |
| ** آدرس دهی حافظه ** | دسترسی به رم از طریق آدرس ها (`MOV EAX, [0x1000]`) |
| **پشته** | منطقه حافظه LIFO برای فراخوانی تابع و متغیرهای محلی (`PUSH`، `POP`) |
| **دستورالعمل** | عملیات اساسی: حساب، منطق، حرکت داده، جریان کنترل |
| **وقفه/سیستال** | درخواست خدمات از سیستم عامل |
| ** فراخوان همایش** | نحوه دریافت پارامترها و مقادیر بازگشتی توابع (بر اساس معماری متفاوت است) |
---

## تست و اشکال زدایی
### GDB (اشکال‌زدای گنو)
GDB دیباگر استاندارد برای مونتاژ در لینوکس است. این به شما امکان می دهد دستورالعمل ها را مرور کنید، رجیسترها را بررسی کنید و حافظه را بررسی کنید.
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

### اشکال زدایی با ماکروهای NASM
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

### الگوهای رایج اشکال زدایی
| مشکل | علامت | تکنیک رفع اشکال |
|---------|---------|-------------------|
| Segfault | برنامه با SIGSEGV خراب می شود | بررسی مقادیر اشاره گر؛ بررسی تراز پشته |
| حلقه بی نهایت | برنامه قطع می شود | تنظیم نقطه شکست در حلقه. بررسی پرچم های شرایط |
| نتیجه اشتباه | محاسبه نادرست | قدم از طریق حساب؛ بعد از هر عملیات | مقادیر ثبت نام را بررسی کنید
| پشته فساد | خرابی در RET | بررسی تعادل PUSH/POP. تراز RSP را بررسی کنید (باید 16 بایت تراز شود) |
| Syscall اشتباه | رفتار غیرمنتظره هسته | بررسی شماره syscall در RAX. بررسی آرگومان های ثبت |
---

## قابلیت همکاری
### فراخوانی توابع C از اسمبلی
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

### مرجع تماس سیستم (Linux x86-64)
| Syscall | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|---------|-----|-----------|------------|-----------|------------|
| خواندن | 0 | fd | بوف | شمارش | — |
| نوشتن | 1 | fd | بوف | شمارش | — |
| باز کردن | 2 | نام مسیر | پرچم ها | حالت | — |
| بستن | 3 | fd | — | — | — |
| mmap | 9 | افزودن | طول | prot | پرچم ها |
| خروج | 60 | وضعیت | — | — | — |
### اسمبلی درون خطی در C (GCC)
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

## الگوهای طراحی
### الگوی 1: حلقه با Acumulator
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

### الگوی 2: خط لوله پردازش رشته
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

### الگوی 3: جدول اعزام (سوئیچ/مورد)
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

### الگوی 4: پیمایش لیست پیوندی
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

## عملکرد و بهینه سازی
### زمانبندی آموزش
CPUهای مدرن چندین دستورالعمل را در هر چرخه از طریق خط لوله و اجرای خارج از نظم اجرا می کنند. درک این موضوع به نوشتن مونتاژ سریعتر کمک می کند.
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

### بهینه سازی کش
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

### چک لیست بهینه سازی
| تکنیک | تاثیر | توضیحات |
|-----------|--------|-------------|
| **ثبت استفاده** | بالا | نگه داشتن متغیرهای داغ در رجیسترها. اجتناب از دسترسی به حافظه |
| **حلقه باز شدن** | متوسط ​​| کاهش سربار حلقه با پردازش چندین مورد در هر تکرار |
| **SIMD (SSE/AVX)** | خیلی بالا | مقادیر 4-16 را همزمان با دستورالعمل های برداری پردازش کنید |
| **حذف شعبه** | متوسط ​​| در صورت امکان به جای پرش های شرطی از CMOV استفاده کنید
| **تراز کش** | متوسط ​​| حلقه های داغ را با مرزهای 16/32 بایت تراز کنید |
| **الگوهای دسترسی به حافظه** | بالا | دسترسی متوالی؛ اجتناب از شکاف خط کش |
---

## استقرار و استفاده در دنیای واقعی
### چگونه برنامه های اسمبلی مستقر می شوند
برنامه های اسمبلی مستقیماً به فایل های اجرایی کد ماشین بومی کامپایل می شوند. هیچ زمان اجرا، VM و مترجمی مورد نیاز نیست. استقرار به سادگی کپی کردن باینری در سیستم هدف است.
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### موارد استفاده در دنیای واقعی
| صنعت | برنامه | چرا مونتاژ |
|----------|------------|------------|
| **سیستم عامل** | خرد بوت هسته لینوکس، ویندوز HAL | کنترل مستقیم سخت افزار، مدیریت وقفه |
| **سیستم افزار تعبیه شده** | بوت لودرهای میکروکنترلر، دستگاه های اینترنت اشیا | هیچ سیستم عامل یا زمان اجرا در دسترس نیست. محدودیت های سخت حافظه |
| **امنیتی** | توسعه اکسپلویت، تجزیه و تحلیل بدافزار، مهندسی معکوس | تنها راه تعامل با باینری های کامپایل شده |
| **موتورهای بازی** | ریاضی بهینه شده با SIMD (تبدیل ماتریس، فیزیک) | حداکثر توان برای محاسبات هر فریم |
| **کامپایلر** | باطن تولید کد (LLVM، GCC) | انتشار کد ماشین بهینه شده |
| **رمز نگاری** | شتاب دستورالعمل AES-NI, SHA | عملیات کریپتو با شتاب سخت افزاری |
| **درایورهای دستگاه** | درایورهای GPU، سیستم عامل کارت شبکه | دسترسی مستقیم سخت افزاری در سطح ثبت |
### یکپارچه سازی سیستم قدیمی
بسیاری از سیستم های قدیمی شامل روال های اسمبلی هستند که در پایگاه های کد C تعبیه شده اند. اینها معمولاً عملکردهای حیاتی یا روال های سخت افزاری خاص هستند که برای دهه ها حفظ شده اند.
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

## چه زمانی از اسمبلی استفاده کنیم
| سناریو | چرا مونتاژ | جایگزین بهتر |
|----------|------------|------------------|
| توسعه هسته سیستم عامل | کد بوت، کنترل کننده وقفه | C برای اکثر کدهای هسته |
| درایورهای دستگاه | دسترسی مستقیم سخت افزاری | ج، زنگ |
| مهندسی معکوس / امنیت | تنها راه برای تجزیه و تحلیل باینری های کامپایل شده | — |
| کد حیاتی عملکرد | حداکثر بهینه سازی | C/C++ با ذاتی کامپایلر |
| سیستم عامل تعبیه شده (فلز لخت) | زبان سطح بالاتر موجود نیست | ج، زنگ |
| آموزش و پرورش | آشنایی با معماری کامپیوتر | — |
| توسعه برنامه عمومی | غیر عملی برای برنامه های پیچیده | هر زبان سطح بالاتر |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین مونتاژ RISC و CISC چیست؟
**A:** CISC (x86) دارای دستورالعمل های پیچیده و با طول متغیر است. RISC (ARM) دارای دستورالعمل های ساده و با طول ثابت است:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### Q2: پشته در مونتاژ چگونه کار می کند؟
**A:** پشته به سمت پایین رشد می کند. `push`SP را کاهش می دهد و ذخیره می کند. `pop`بارها و SP را افزایش می دهد:
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

### Q3: چگونه توابع را در اسمبلی فراخوانی کنم؟
**A:** قرارداد تماس را دنبال کنید (System V AMD64 در لینوکس، Windows x64 در ویندوز):
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

### Q4: مهمترین دستورالعمل های مونتاژی که باید بدانید چیست؟
**A:** عملیات حرکت داده، حساب، کنترل جریان و پشته هسته را تشکیل می دهند.
### Q5: اسمبلی چگونه در تحقیقات امنیتی استفاده می شود؟
**A:** مهندسی معکوس، توسعه اکسپلویت، تجزیه و تحلیل بدافزار، و درک خروجی کامپایلر همگی به سواد اسمبلی نیاز دارند.
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: پیاده سازی یک حلقه در اسمبلی
**مرحله 1: مشکل را درک کنید**
مجموع اعداد صحیح از 1 تا N.
**مرحله 2: رویکرد را شناسایی کنید**
از یک رجیستر شمارنده و انباشته کننده استفاده کنید.
**مرحله 3: پیاده سازی **```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**مرحله 4: بهینه سازی**
از فرمول N*(N+1)/2 برای O(1) به جای O(N) استفاده کنید.
---

## خلاصه
زبان اسمبلی پل ارتباطی بین کدهای قابل خواندن توسط انسان و باینری خامی است که CPU ها اجرا می کنند. این یک انتخاب عملی برای ساخت برنامه های کاربردی نیست، اما برای درک اینکه چگونه کامپیوترها در پایین ترین سطح کار می کنند ضروری است. برای برنامه نویسان سیستم، محققان امنیتی و توسعه دهندگان جاسازی شده، دانش اسمبلی بسیار ارزشمند است. برای بقیه، درک مفاهیم اسمبلی (رجیسترها، پشته، چرخه‌های دستورالعمل) شما را به برنامه‌نویس بهتری در هر زبانی تبدیل می‌کند.