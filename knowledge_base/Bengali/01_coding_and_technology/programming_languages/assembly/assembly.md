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

# সমাবেশের ভাষা
সমাবেশ ভাষা হল সর্বনিম্ন স্তরের মানব-পাঠযোগ্য প্রোগ্রামিং ভাষা। এটি কাঁচা বাইনারির পরিবর্তে মেমোনিক কোড (যেমন`MOV`,`ADD`,`JMP`) ব্যবহার করে কম্পিউটারের মেশিন কোড নির্দেশাবলীর সরাসরি উপস্থাপনা প্রদান করে। প্রতিটি অ্যাসেম্বলি ভাষা একটি নির্দিষ্ট প্রসেসর আর্কিটেকচারের জন্য নির্দিষ্ট (x86, ARM, MIPS, RISC-V) — একটি আর্কিটেকচারের জন্য লেখা কোড অন্যটিতে চলবে না।
অ্যাসেম্বলি ভাষা নির্মাণ অ্যাপ্লিকেশনের জন্য ব্যবহার করা হয় না. এটি ব্যবহার করা হয় যখন আপনার হার্ডওয়্যারের উপর নিখুঁত নিয়ন্ত্রণের প্রয়োজন হয়: অপারেটিং সিস্টেমের কার্নেল, ডিভাইস ড্রাইভার, বুটলোডার, এমবেডেড ফার্মওয়্যার, কর্মক্ষমতা-সমালোচনামূলক কোড বিভাগ, রিভার্স ইঞ্জিনিয়ারিং এবং কম্পিউটারগুলি কীভাবে নির্দেশাবলী কার্যকর করে তা বোঝা।
---

## কেন বিধানসভা বিষয়
- **হার্ডওয়্যার বোঝা**: নির্দেশের স্তরে CPU ঠিক কী করছে তা জানার একমাত্র উপায়।
- **পারফরম্যান্স টিউনিং**: কম্পাইলার যা তৈরি করে তার থেকেও জটিল কোড বিভাগগুলি অপ্টিমাইজ করা যেতে পারে।
- **বিপরীত প্রকৌশল**: ম্যালওয়্যার বিশ্লেষণ, নিরাপত্তা গবেষণা, এবং মালিকানা সফ্টওয়্যার বোঝা।
- **এমবেডেড সিস্টেম**: কিছু মাইক্রোকন্ট্রোলারের উচ্চ-স্তরের ভাষা সমর্থন নেই।
- **OS ডেভেলপমেন্ট**: বুট কোড, ইন্টারাপ্ট হ্যান্ডলার এবং কনটেক্সট স্যুইচিংয়ের জন্য সমাবেশ প্রয়োজন।
- **শিক্ষামূলক**: সমাবেশ বোঝা আপনাকে শেখায় কিভাবে কম্পিউটার আসলে কাজ করে — মেমরি, রেজিস্টার, স্ট্যাক এবং CPU পাইপলাইন।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **অত্যন্ত নিম্ন-স্তরের** | প্রতিটি নির্দেশ একটি মেশিন অপারেশন মানচিত্র | সমালোচনামূলক অংশ ছাড়া সব কিছুর জন্য উচ্চ-স্তরের ভাষা ব্যবহার করুন |
| **স্থাপত্য-নির্দিষ্ট** | x86 কোড ARM এ চলে না | C/C++ এ পোর্টেবল কোড লিখুন; শুধুমাত্র প্রয়োজন যেখানে সমাবেশ ব্যবহার করুন |
| **ভার্বোস** | সহজ কাজ অনেক নির্দেশাবলী প্রয়োজন | ম্যাক্রো ব্যবহার করুন; সমাবেশ বিভাগ ন্যূনতম রাখুন |
| **কোন বহনযোগ্যতা নেই** | প্রতিটি অ্যাসেম্বলারের জন্য আলাদা সিনট্যাক্স (NASM, GAS, MASM) | কম্পাইলার ইন্ট্রিনসিক্স বা ইনলাইন সমাবেশ ব্যবহার করুন |
| **ডিবাগিং অসুবিধা** | নির্দেশের স্তরে যুক্তি খুঁজে পাওয়া কঠিন | ডিবাগার ব্যবহার করুন (GDB); উদারভাবে মন্তব্য যোগ করুন |
---

## সিনট্যাক্স উদাহরণ (x86-64 সমাবেশ — NASM)
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

### ARM সমাবেশের উদাহরণ
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### x86-64 অ্যাড্রেসিং মোড
অ্যাড্রেসিং মোড বোঝা দক্ষ সমাবেশ লেখার জন্য গুরুত্বপূর্ণ। প্রতিটি মোড নিয়ন্ত্রণ করে কিভাবে অপারেন্ডগুলি অবস্থিত।
| মোড | সিনট্যাক্স (NASM) | বর্ণনা |
|------|---------------|------------|
| **তাৎক্ষণিক** | `mov eax, 42`| Operand একটি ধ্রুবক মান |
| **নিবন্ধন** | `mov eax, ebx`| অপারেন্ড একটি রেজিস্টারে আছে |
| **সরাসরি** | `mov eax, [0x4000]`| Operand একটি নির্দিষ্ট মেমরি ঠিকানায় আছে |
| **পরোক্ষ নিবন্ধন করুন** | `mov eax, [rbx]`| Operand একটি রেজিস্টারে ঠিকানায় আছে |
| **বেস + স্থানচ্যুতি** | `mov eax, [rbx + 8]`| ঠিকানা = নিবন্ধন + ধ্রুবক অফসেট |
| **স্কেল করা সূচক** | `mov eax, [rbx + rcx*4]`| ঠিকানা = ভিত্তি + (সূচক × স্কেল) |
| **সম্পূর্ণ SIB** | `mov eax, [rbx + rcx*4 + 16]`| ভিত্তি + (সূচক × স্কেল) + স্থানচ্যুতি |
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

### ম্যাক্রো সিস্টেম (NASM)
ম্যাক্রো আপনাকে পরামিতি সহ পুনরায় ব্যবহারযোগ্য নির্দেশনা ক্রম সংজ্ঞায়িত করতে দেয়, যা সমাবেশকে কম পুনরাবৃত্তিমূলক করে তোলে।
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

### স্ট্যাক ফ্রেম লেআউট
স্ট্যাক ফ্রেম বোঝা ফাংশন এবং ডিবাগিং লেখার জন্য অপরিহার্য।
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

## আর্কিটেকচার এবং সিস্টেম ডিজাইন
### একটি সাধারণ x86-64 লিনাক্স প্রক্রিয়ার মেমরি লেআউট
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

### প্রোগ্রাম স্ট্রাকচার কনভেনশন
একটি সুসংগঠিত সমাবেশ প্রোগ্রাম উদ্বেগগুলিকে স্বতন্ত্র বিভাগে বিভক্ত করে:
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

### সাধারণ প্রকল্প ডিরেক্টরি কাঠামো
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### লিনাক্সে NASM + GCC
সবচেয়ে সাধারণ ওয়ার্কফ্লো লিঙ্কার হিসেবে GCC ব্যবহার করে C-এর সাথে সমাবেশ করে।
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

### উইন্ডোজে MASM (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### AT&T সিনট্যাক্স সহ GAS (GNU অ্যাসেম্বলার)
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

### একটি বিশুদ্ধ সমাবেশ প্রোগ্রাম লিঙ্ক করা (কোন সি রানটাইম নেই)
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

## মূল ধারণা
| ধারণা | বর্ণনা |
|---------|---------------|
| **রেজিস্টার** | CPU এর অভ্যন্তরীণ সঞ্চয়স্থান (EAX, EBX, ECX, EDX x86 এ; R0-R15 এআরএম) |
| **মেমরি অ্যাড্রেসিং** | ঠিকানার মাধ্যমে RAM অ্যাক্সেস করা হচ্ছে (`MOV EAX, [0x1000]`) |
| **স্ট্যাক** | ফাংশন কল এবং স্থানীয় ভেরিয়েবলের জন্য LIFO মেমরি অঞ্চল (`PUSH`,`POP`) |
| **নির্দেশ** | মৌলিক ক্রিয়াকলাপ: পাটিগণিত, যুক্তিবিদ্যা, ডেটা আন্দোলন, নিয়ন্ত্রণ প্রবাহ |
| **বিঘ্ন/সিস্কাল** | অপারেটিং সিস্টেম থেকে পরিষেবার জন্য অনুরোধ করা হচ্ছে |
| **কলিং কনভেনশন** | কিভাবে ফাংশন পরামিতি গ্রহণ করে এবং মান ফেরত দেয় (স্থাপত্য দ্বারা পরিবর্তিত হয়) |
---

## পরীক্ষা এবং ডিবাগিং
### GDB (GNU ডিবাগার)
লিনাক্সে সমাবেশের জন্য GDB হল স্ট্যান্ডার্ড ডিবাগার। এটি আপনাকে নির্দেশাবলীর মধ্য দিয়ে যেতে, রেজিস্টারগুলি পরিদর্শন করতে এবং মেমরি পরীক্ষা করতে দেয়।
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

### NASM ম্যাক্রোর সাথে ডিবাগিং
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

### সাধারণ ডিবাগিং প্যাটার্ন
| সমস্যা | উপসর্গ | ডিবাগিং টেকনিক |
|---------|---------|-------------------|
| সেগফল্ট | SIGSEGV এর সাথে প্রোগ্রাম ক্র্যাশ | পয়েন্টার মান পরীক্ষা করুন; স্ট্যাক প্রান্তিককরণ যাচাই করুন |
| অসীম লুপ | প্রোগ্রাম হ্যাং | লুপে ব্রেকপয়েন্ট সেট করুন; চেক কন্ডিশন পতাকা |
| ভুল ফলাফল | ভুল গণনা | পাটিগণিত মাধ্যমে ধাপ; প্রতিটি অপের পর রেজিস্টার মান চেক করুন |
| স্তূপ দুর্নীতি | RET এ ক্র্যাশ | PUSH/POP ব্যালেন্স যাচাই করুন; RSP প্রান্তিককরণ পরীক্ষা করুন (16-বাইট সারিবদ্ধ হতে হবে) |
| ভুল syscall | অপ্রত্যাশিত কার্নেল আচরণ | RAX-এ syscall নম্বর যাচাই করুন; চেক আর্গুমেন্ট রেজিস্টার |
---

## ইন্টারঅপারেবিলিটি
### সমাবেশ থেকে সি ফাংশন কল করা
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

### সিস্টেম কল রেফারেন্স (লিনাক্স x86-64)
| Syscall | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|---------|------|------------|------------|------------|------------|
| পড়ুন | 0 | fd | buf | গণনা | — |
| লিখুন | 1 | fd | buf | গণনা | — |
| খোলা | 2 | পথনাম | পতাকা | মোড | — |
| বন্ধ | 3 | fd | — | — | — |
| mmap | 9 | addr | দৈর্ঘ্য | prot | পতাকা |
| প্রস্থান | 60 | অবস্থা | — | — | — |
### ইনলাইন অ্যাসেম্বলি ইন সি (জিসিসি)
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: অ্যাকুমুলেটর দিয়ে লুপ
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

### প্যাটার্ন 2: স্ট্রিং প্রসেসিং পাইপলাইন
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

### প্যাটার্ন 3: ডিসপ্যাচ টেবিল (সুইচ/কেস)
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

### প্যাটার্ন ৪: লিংকড লিস্ট ট্রাভার্সাল
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### নির্দেশের সময়সূচী
আধুনিক সিপিইউগুলি পাইপলাইনিং এবং অর্ডার বহির্ভূত কার্য সম্পাদনের মাধ্যমে প্রতি চক্রে একাধিক নির্দেশাবলী কার্যকর করে। এটি বোঝা দ্রুত সমাবেশ লিখতে সাহায্য করে।
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

### ক্যাশে অপ্টিমাইজেশান
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

### অপ্টিমাইজেশান চেকলিস্ট
| টেকনিক | প্রভাব | বর্ণনা |
|------------|---------|---------------|
| **নিবন্ধন ব্যবহার** | উচ্চ | রেজিস্টারে গরম ভেরিয়েবল রাখুন; মেমরি অ্যাক্সেস এড়িয়ে চলুন |
| **লুপ আনরোলিং** | মাঝারি | প্রতি পুনরাবৃত্তির একাধিক আইটেম প্রক্রিয়া করে লুপ ওভারহেড হ্রাস করুন |
| **SIMD (SSE/AVX)** | খুব উচ্চ | ভেক্টর নির্দেশাবলীর সাথে একযোগে 4-16 মান প্রক্রিয়া করুন |
| **শাখা নির্মূল** | মাঝারি | যেখানে সম্ভব কন্ডিশনাল জাম্পের পরিবর্তে CMOV ব্যবহার করুন |
| **ক্যাশে প্রান্তিককরণ** | মাঝারি | হট লুপগুলিকে 16/32-বাইটের সীমানায় সারিবদ্ধ করুন |
| **মেমরি অ্যাক্সেস প্যাটার্ন** | উচ্চ | অনুক্রমিক অ্যাক্সেস; ক্যাশে লাইন বিভাজন এড়িয়ে চলুন |
---

## স্থাপনা এবং বাস্তব-বিশ্ব ব্যবহার
### কিভাবে সমাবেশ প্রোগ্রাম স্থাপন করা হয়
অ্যাসেম্বলি প্রোগ্রামগুলি সরাসরি নেটিভ মেশিন কোড এক্সিকিউটেবলে কম্পাইল করে। কোন রানটাইম নেই, কোন VM নেই, এবং কোন দোভাষীর প্রয়োজন নেই। স্থাপনা টার্গেট সিস্টেমে বাইনারি কপি করার মতোই সহজ।
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### বাস্তব-বিশ্ব ব্যবহারের ক্ষেত্রে
| শিল্প | আবেদন | কেন সমাবেশ |
|------------|---------------|------------|
| **অপারেটিং সিস্টেম** | লিনাক্স কার্নেল বুট স্টাব, উইন্ডোজ HAL | সরাসরি হার্ডওয়্যার নিয়ন্ত্রণ, হ্যান্ডলিং বাধা |
| **এমবেডেড ফার্মওয়্যার** | মাইক্রোকন্ট্রোলার বুটলোডার, IoT ডিভাইস | কোন OS বা রানটাইম উপলব্ধ নেই; কঠোর মেমরি সীমা |
| **নিরাপত্তা** | শোষণ উন্নয়ন, ম্যালওয়্যার বিশ্লেষণ, বিপরীত প্রকৌশল | সংকলিত বাইনারিগুলির সাথে যোগাযোগ করার একমাত্র উপায় |
| **গেম ইঞ্জিন** | SIMD-অপ্টিমাইজ করা গণিত (ম্যাট্রিক্স রূপান্তর, পদার্থবিদ্যা) | প্রতি-ফ্রেম গণনার জন্য সর্বাধিক থ্রুপুট |
| **কম্পাইলার** | কোড জেনারেশন ব্যাকএন্ড (LLVM, GCC) | অপ্টিমাইজড মেশিন কোড নির্গত করা |
| **ক্রিপ্টোগ্রাফি** | AES-NI, SHA নির্দেশ ত্বরণ | হার্ডওয়্যার-ত্বরিত ক্রিপ্টো অপারেশন |
| **ডিভাইস ড্রাইভার** | GPU ড্রাইভার, নেটওয়ার্ক কার্ড ফার্মওয়্যার | সরাসরি রেজিস্টার-স্তরের হার্ডওয়্যার অ্যাক্সেস |
### লিগ্যাসি সিস্টেম ইন্টিগ্রেশন
অনেক লিগ্যাসি সিস্টেমে সি কোডবেসের মধ্যে এমবেড করা সমাবেশের রুটিন থাকে। এগুলি সাধারণত কর্মক্ষমতা-সমালোচনামূলক ফাংশন বা হার্ডওয়্যার-নির্দিষ্ট রুটিন যা কয়েক দশক ধরে বজায় রাখা হয়েছে।
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

## কখন অ্যাসেম্বলি ব্যবহার করবেন
| দৃশ্যকল্প | কেন সমাবেশ | ভাল বিকল্প |
|------------|---------------|---------|
| OS কার্নেল উন্নয়ন | বুট কোড, ইন্টারাপ্ট হ্যান্ডলার | বেশিরভাগ কার্নেল কোডের জন্য C |
| ডিভাইস ড্রাইভার | সরাসরি হার্ডওয়্যার অ্যাক্সেস | সি, মরিচা |
| বিপরীত প্রকৌশল / নিরাপত্তা | সংকলিত বাইনারি বিশ্লেষণ করার একমাত্র উপায় | — |
| কর্মক্ষমতা-সমালোচনা কোড | সর্বোচ্চ অপ্টিমাইজেশান | কম্পাইলার ইন্ট্রিনসিক্স সহ C/C++ |
| এমবেডেড ফার্মওয়্যার (বেয়ার মেটাল) | কোন উচ্চ-স্তরের ভাষা উপলব্ধ | সি, মরিচা |
| শিক্ষা | কম্পিউটার আর্কিটেকচার বোঝা | — |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | জটিল প্রোগ্রামের জন্য অকার্যকর | যে কোনো উচ্চ-স্তরের ভাষা |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: RISC এবং CISC সমাবেশের মধ্যে পার্থক্য কী?
**A:** CISC (x86) এর জটিল, পরিবর্তনশীল-দৈর্ঘ্য নির্দেশাবলী রয়েছে। RISC (ARM) এর সহজ, নির্দিষ্ট দৈর্ঘ্যের নির্দেশাবলী রয়েছে:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### প্রশ্ন 2: স্ট্যাক কিভাবে সমাবেশে কাজ করে?
**A:** স্ট্যাক নিচের দিকে বৃদ্ধি পায়। `push`কমছে SP এবং স্টোর; `pop`লোড এবং বৃদ্ধি এসপি:
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

### প্রশ্ন 3: আমি কিভাবে সমাবেশে ফাংশন কল করব?
**A:** কলিং কনভেনশন অনুসরণ করুন (লিনাক্সে সিস্টেম V AMD64, উইন্ডোজে Windows x64):
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

### প্রশ্ন 4: সবচেয়ে গুরুত্বপূর্ণ সমাবেশ নির্দেশাবলী কি জানতে হবে?
**A:** ডেটা চলাচল, পাটিগণিত, নিয়ন্ত্রণ প্রবাহ এবং স্ট্যাক অপারেশনগুলি মূল গঠন করে।
### প্রশ্ন 5: নিরাপত্তা গবেষণায় কীভাবে সমাবেশ ব্যবহার করা হয়?
**A:** রিভার্স ইঞ্জিনিয়ারিং, এক্সপ্লয়েট ডেভেলপমেন্ট, ম্যালওয়্যার বিশ্লেষণ এবং কম্পাইলার আউটপুট বোঝার জন্য সমাবেশ সাক্ষরতার প্রয়োজন।
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: সমাবেশে একটি লুপ প্রয়োগ করা
**ধাপ 1: সমস্যাটি বুঝুন**
1 থেকে N পর্যন্ত পূর্ণসংখ্যার যোগফল।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
একটি কাউন্টার রেজিস্টার এবং সঞ্চয়কারী ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**ধাপ ৪: অপ্টিমাইজ**
O(N) এর পরিবর্তে O(1) এর জন্য N*(N+1)/2 সূত্র ব্যবহার করুন।
---

## সারাংশ
অ্যাসেম্বলি ল্যাঙ্গুয়েজ হল মানব-পাঠযোগ্য কোড এবং CPU গুলি চালানোর কাঁচা বাইনারির মধ্যে সেতু। এটি অ্যাপ্লিকেশন তৈরির জন্য একটি ব্যবহারিক পছন্দ নয়, তবে কম্পিউটার কীভাবে সর্বনিম্ন স্তরে কাজ করে তা বোঝার জন্য এটি অপরিহার্য। সিস্টেম প্রোগ্রামার, নিরাপত্তা গবেষক এবং এমবেডেড ডেভেলপারদের জন্য সমাবেশ জ্ঞান অমূল্য। অন্য সবার জন্য, সমাবেশের ধারণাগুলি (রেজিস্টার, স্ট্যাক, নির্দেশনা চক্র) বোঝা আপনাকে যে কোনও ভাষায় আরও ভাল প্রোগ্রামার করে তোলে।