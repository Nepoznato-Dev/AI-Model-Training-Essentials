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
#ภาษาแอสเซมบลี
ภาษาแอสเซมบลีเป็นภาษาโปรแกรมระดับต่ำสุดที่มนุษย์สามารถอ่านได้ โดยให้การแสดงโดยตรงของคำสั่งรหัสเครื่องของคอมพิวเตอร์โดยใช้รหัสช่วยจำ (เช่น`MOV`,`ADD`,`JMP`) แทนที่จะเป็นไบนารีดิบ ภาษาแอสเซมบลีแต่ละภาษามีความเฉพาะเจาะจงสำหรับสถาปัตยกรรมโปรเซสเซอร์เฉพาะ (x86, ARM, MIPS, RISC-V) - โค้ดที่เขียนสำหรับสถาปัตยกรรมหนึ่งจะไม่ทำงานบนสถาปัตยกรรมอื่น
ภาษาแอสเซมบลีไม่ได้ใช้สำหรับการสร้างแอปพลิเคชัน ใช้เมื่อคุณต้องการควบคุมฮาร์ดแวร์อย่างสมบูรณ์: การเขียนเคอร์เนลของระบบปฏิบัติการ ไดรเวอร์อุปกรณ์ บูตโหลดเดอร์ เฟิร์มแวร์แบบฝัง ส่วนโค้ดที่มีความสำคัญต่อประสิทธิภาพการทำงาน วิศวกรรมย้อนกลับ และการทำความเข้าใจว่าคอมพิวเตอร์ดำเนินการตามคำสั่งอย่างไร
---

## ทำไมการประกอบจึงมีความสำคัญ
- **ความเข้าใจเกี่ยวกับฮาร์ดแวร์**: วิธีเดียวที่จะรู้ได้อย่างแน่ชัดว่า CPU กำลังทำอะไรในระดับคำสั่ง
- **การปรับแต่งประสิทธิภาพ**: ส่วนโค้ดที่สำคัญสามารถปรับให้เหมาะสมได้ นอกเหนือจากที่คอมไพเลอร์สร้างขึ้น
- **วิศวกรรมย้อนกลับ**: การวิเคราะห์มัลแวร์ การวิจัยด้านความปลอดภัย และการทำความเข้าใจซอฟต์แวร์ที่เป็นกรรมสิทธิ์
- **ระบบสมองกลฝังตัว**: ไมโครคอนโทรลเลอร์บางตัวไม่รองรับภาษาในระดับที่สูงกว่า
- **การพัฒนาระบบปฏิบัติการ**: โค้ดสำหรับบูต ตัวจัดการการขัดจังหวะ และการสลับบริบทจำเป็นต้องมีการประกอบ
- **การศึกษา**: การทำความเข้าใจแอสเซมบลีจะสอนให้คุณทราบว่าคอมพิวเตอร์ทำงานอย่างไร เช่น หน่วยความจำ รีจิสเตอร์ สแตก และไปป์ไลน์ CPU
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ระดับต่ำมาก** | ทุกคำสั่งแมปกับการทำงานของเครื่องเดียว | ใช้ภาษาระดับสูงสำหรับทุกสิ่ง ยกเว้นส่วนสำคัญ |
| **เฉพาะสถาปัตยกรรม** | รหัส x86 ไม่ทำงานบน ARM | เขียนโค้ดแบบพกพาใน C/C++; ใช้ชุดประกอบเฉพาะเมื่อจำเป็นเท่านั้น |
| **Verbose** | งานง่ายๆ ต้องใช้คำแนะนำมากมาย | Use macros; ทำให้ส่วนการประกอบน้อยที่สุด |
| **No portability** | ไวยากรณ์ที่แตกต่างกันสำหรับแอสเซมเบลอร์แต่ละตัว (NASM, GAS, MASM) | ใช้อินทรินซิกของคอมไพเลอร์หรือแอสเซมบลีแบบอินไลน์ |
| **ความยากในการดีบัก** | ตรรกะที่ติดตามได้ยากในระดับคำสั่ง | Use debuggers (GDB); add comments liberally |
---

## ตัวอย่างไวยากรณ์ (ชุดประกอบ x86-64 - NASM)
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

### ตัวอย่างการประกอบ ARM
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

## ไวยากรณ์และรูปแบบขั้นสูง
### โหมดการกำหนดที่อยู่ x86-64
การทำความเข้าใจโหมดการกำหนดแอดเดรสเป็นสิ่งสำคัญสำหรับการเขียนแอสเซมบลีที่มีประสิทธิภาพ แต่ละโหมดควบคุมวิธีการระบุตำแหน่งของตัวถูกดำเนินการ
| โหมด | ไวยากรณ์ (NASM) | คำอธิบาย |
|------|---------------|-------------|
| **ทันที** | `mov eax, 42`| ตัวถูกดำเนินการคือค่าคงที่ |
| **ลงทะเบียน** | `mov eax, ebx`| ตัวถูกดำเนินการอยู่ในการลงทะเบียน |
| **โดยตรง** | `mov eax, [0x4000]`| ตัวถูกดำเนินการอยู่ที่ที่อยู่หน่วยความจำคงที่ |
| **ลงทะเบียนทางอ้อม** | `mov eax, [rbx]`| ตัวถูกดำเนินการอยู่ที่ที่อยู่ในการลงทะเบียน |
| **ฐาน + การกระจัด** | `mov eax, [rbx + 8]`| ที่อยู่ = ลงทะเบียน + ออฟเซ็ตคงที่ |
| **ดัชนีที่ปรับขนาด** | `mov eax, [rbx + rcx*4]`| ที่อยู่ = ฐาน + (ดัชนี × สเกล) |
| **SIB เต็ม** | `mov eax, [rbx + rcx*4 + 16]`| ฐาน + (ดัชนี × สเกล) + การกระจัด |
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

### ระบบมาโคร (NASM)
มาโครช่วยให้คุณกำหนดลำดับคำสั่งที่ใช้ซ้ำได้พร้อมพารามิเตอร์ ทำให้การประกอบซ้ำน้อยลง
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

### เค้าโครงเฟรมสแต็ก
การทำความเข้าใจสแต็กเฟรมถือเป็นสิ่งสำคัญสำหรับการเขียนฟังก์ชันและการดีบัก
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

## สถาปัตยกรรมและการออกแบบระบบ
### เค้าโครงหน่วยความจำของกระบวนการ x86-64 Linux ทั่วไป
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

### อนุสัญญาโครงสร้างโปรแกรม
โปรแกรมการชุมนุมที่ได้รับการจัดการอย่างดีจะแยกข้อกังวลออกเป็นส่วนต่างๆ:
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

### โครงสร้างไดเร็กทอรีโครงการทั่วไป
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### NASM + GCC บน Linux
เวิร์กโฟลว์ลิงก์แอสเซมบลีที่พบบ่อยที่สุดกับ C โดยใช้ GCC เป็นตัวเชื่อมโยง
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

### MASM บน Windows (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (GNU Assembler) พร้อมไวยากรณ์ AT&T
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

### การเชื่อมโยงโปรแกรม Pure Assembly (ไม่มีรันไทม์ C)
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

## แนวคิดหลัก
| แนวคิด | คำอธิบาย |
|---------|-------------|
| **ลงทะเบียน** | ที่เก็บข้อมูลภายในของ CPU (EAX, EBX, ECX, EDX บน x86; R0-R15 บน ARM) |
| **การกำหนดที่อยู่หน่วยความจำ** | การเข้าถึง RAM ผ่านที่อยู่ (`MOV EAX, [0x1000]`) |
| **กองซ้อน** | พื้นที่หน่วยความจำ LIFO สำหรับการเรียกใช้ฟังก์ชันและตัวแปรท้องถิ่น (`PUSH`,`POP`) |
| **คำแนะนำ** | การดำเนินการพื้นฐาน: เลขคณิต ตรรกะ การเคลื่อนที่ของข้อมูล โฟลว์ควบคุม |
| **ขัดจังหวะ / syscalls** | การร้องขอบริการจากระบบปฏิบัติการ |
| **แบบแผนการเรียก** | วิธีที่ฟังก์ชันรับพารามิเตอร์และค่าที่ส่งคืน (แตกต่างกันไปตามสถาปัตยกรรม) |
---

## การทดสอบและการดีบัก
### GDB (ดีบักเกอร์ GNU)
GDB เป็นดีบักเกอร์มาตรฐานสำหรับแอสเซมบลีบน Linux ช่วยให้คุณดำเนินการตามคำแนะนำ ตรวจสอบรีจิสเตอร์ และตรวจสอบหน่วยความจำ
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

### การดีบักด้วย NASM Macros
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

### รูปแบบการดีบักทั่วไป
| ปัญหา | อาการ | เทคนิคการดีบัก |
|---------|---------|-------------------|
| เซ็กฟอลต์ | โปรแกรมขัดข้องด้วย SIGSEGV | ตรวจสอบค่าตัวชี้ ตรวจสอบการจัดตำแหน่งสแต็ก |
| วนซ้ำไม่สิ้นสุด | โปรแกรมค้าง | ตั้งค่าเบรกพอยต์ในวง; ตรวจสอบเงื่อนไขแฟล็ก |
| ผลลัพธ์ไม่ถูกต้อง | การคำนวณไม่ถูกต้อง | ก้าวผ่านเลขคณิต ตรวจสอบค่ารีจิสเตอร์หลังแต่ละ op |
| ซ้อนความเสียหาย | ความผิดพลาดใน RET | ตรวจสอบยอดคงเหลือ PUSH/POP ตรวจสอบการจัดตำแหน่ง RSP (ต้องจัดชิด 16 ไบต์) |
| syscall ผิด | ลักษณะการทำงานของเคอร์เนลที่ไม่คาดคิด | ตรวจสอบหมายเลข syscall ใน RAX; ตรวจสอบการลงทะเบียนอาร์กิวเมนต์ |
---

## การทำงานร่วมกัน
### การเรียกใช้ฟังก์ชัน C จาก Assembly
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

### การอ้างอิงการโทรของระบบ (Linux x86-64)
| ซิสคอล | แร็กซ์ | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | อาร์จี4 (R10) |
|---------|-----|------------|------------|------------|------------|
| อ่าน | 0 | เอฟดี | บุฟ | นับ | — |
| เขียน | 1 | เอฟดี | บุฟ | นับ | — |
| เปิด | 2 | ชื่อพาธ | ธง | โหมด | — |
| ปิด | 3 | เอฟดี | — | — | — |
| เอ็มแมป | 9 | เพิ่ม | ความยาว | โปร | ธง |
| ออก | 60 | สถานะ | — | — | — |
### การประกอบแบบอินไลน์ใน C (GCC)
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

## รูปแบบการออกแบบ
### รูปแบบ 1: วนซ้ำพร้อมตัวสะสม
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

### รูปแบบ 2: ไปป์ไลน์การประมวลผลสตริง
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

### รูปแบบ 3: ตารางการจัดส่ง (สวิตช์/เคส)
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

### รูปแบบ 4: การข้ามผ่านรายการที่เชื่อมโยง
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### กำหนดการเรียนการสอน
CPU สมัยใหม่ดำเนินการหลายคำสั่งต่อรอบผ่านการวางท่อและการดำเนินการที่ไม่อยู่ในลำดับ การทำความเข้าใจสิ่งนี้จะช่วยให้เขียนแอสเซมบลีได้เร็วขึ้น
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

### การเพิ่มประสิทธิภาพแคช
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

### รายการตรวจสอบการเพิ่มประสิทธิภาพ
| เทคนิค | ผลกระทบ | คำอธิบาย |
|----------|--------|-------------|
| **ลงทะเบียนการใช้งาน** | สูง | เก็บตัวแปรร้อนไว้ในรีจิสเตอร์ หลีกเลี่ยงการเข้าถึงหน่วยความจำ |
| **กำลังคลี่ลูป** | ปานกลาง | ลดค่าใช้จ่ายการวนซ้ำโดยการประมวลผลหลายรายการต่อการวนซ้ำ |
| **ซิม (SSE/AVX)** | สูงมาก | ประมวลผลค่า 4-16 พร้อมกันด้วยคำสั่งเวกเตอร์ |
| **กำจัดสาขา** | ปานกลาง | ใช้ CMOV แทนการข้ามแบบมีเงื่อนไขเมื่อเป็นไปได้ |
| **การจัดตำแหน่งแคช** | ปานกลาง | จัดตำแหน่ง hot loops ให้อยู่ในขอบเขต 16/32-ไบต์ |
| **รูปแบบการเข้าถึงหน่วยความจำ** | สูง | การเข้าถึงตามลำดับ หลีกเลี่ยงการแยกบรรทัดแคช |
---

## การปรับใช้และการใช้งานในโลกแห่งความเป็นจริง
### วิธีการปรับใช้โปรแกรมแอสเซมบลี
โปรแกรมแอสเซมบลีคอมไพล์โดยตรงกับไฟล์ปฏิบัติการโค้ดเครื่องเนทีฟ ไม่มีรันไทม์ ไม่มี VM และไม่จำเป็นต้องมีล่าม การปรับใช้นั้นง่ายดายเพียงแค่คัดลอกไบนารีไปยังระบบเป้าหมาย
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### กรณีการใช้งานจริง
| อุตสาหกรรม | ใบสมัคร | ทำไมต้องประกอบ |
|----------|-------------|-------------|
| **ระบบปฏิบัติการ** | ต้นขั้วการบูตเคอร์เนล Linux, Windows HAL | การควบคุมฮาร์ดแวร์โดยตรง การจัดการขัดจังหวะ |
| **เฟิร์มแวร์ในตัว** | ไมโครคอนโทรลเลอร์บูตโหลดเดอร์ อุปกรณ์ IoT | ไม่มีระบบปฏิบัติการหรือรันไทม์ ขีดจำกัดหน่วยความจำที่เข้มงวด |
| **ความปลอดภัย** | ใช้ประโยชน์จากการพัฒนา การวิเคราะห์มัลแวร์ วิศวกรรมย้อนกลับ | วิธีเดียวที่จะโต้ตอบกับไบนารีที่คอมไพล์แล้ว |
| **เอ็นจิ้นเกม** | คณิตศาสตร์ที่ปรับให้เหมาะสม SIMD (การแปลงเมทริกซ์, ฟิสิกส์) | ปริมาณงานสูงสุดสำหรับการคำนวณต่อเฟรม |
| **คอมไพเลอร์** | แบ็กเอนด์การสร้างโค้ด (LLVM, GCC) | กำลังเปล่งรหัสเครื่องที่ปรับให้เหมาะสม |
| **วิทยาการเข้ารหัสลับ** | AES-NI, การเร่งความเร็วคำสั่ง SHA | การดำเนินการเข้ารหัสลับที่เร่งด้วยฮาร์ดแวร์ |
| **ไดรเวอร์อุปกรณ์** | ไดรเวอร์ GPU, เฟิร์มแวร์การ์ดเครือข่าย | การเข้าถึงฮาร์ดแวร์ระดับการลงทะเบียนโดยตรง |
### บูรณาการระบบเดิม
ระบบเดิมจำนวนมากมีรูทีนการประกอบที่ฝังอยู่ภายในโค้ดเบส C โดยทั่วไปแล้วสิ่งเหล่านี้คือฟังก์ชันที่มีความสำคัญต่อประสิทธิภาพหรือรูทีนเฉพาะฮาร์ดแวร์ที่ได้รับการบำรุงรักษามานานหลายทศวรรษ
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

## เมื่อใดจึงควรใช้ชุดประกอบ
| สถานการณ์ | ทำไมต้องประกอบ | ทางเลือกที่ดีกว่า |
|----------|-------------|-------------------|
| การพัฒนาเคอร์เนล OS | รหัสบูต, ตัวจัดการขัดจังหวะ | C สำหรับโค้ดเคอร์เนลส่วนใหญ่ |
| ไดรเวอร์อุปกรณ์ | การเข้าถึงฮาร์ดแวร์โดยตรง | C, สนิม |
| วิศวกรรมย้อนกลับ / ความปลอดภัย | วิธีเดียวที่จะวิเคราะห์ไบนารีที่คอมไพล์แล้ว | — |
| รหัสที่มีความสำคัญต่อประสิทธิภาพ | การเพิ่มประสิทธิภาพสูงสุด | C/C++ พร้อมคอมไพเลอร์ภายใน |
| เฟิร์มแวร์แบบฝัง (โลหะเปลือย) | ไม่มีภาษาระดับสูงกว่า | C, สนิม |
| การศึกษา | ทำความเข้าใจสถาปัตยกรรมคอมพิวเตอร์ | — |
| การพัฒนาแอพพลิเคชั่นทั่วไป | ทำไม่ได้สำหรับโปรแกรมที่ซับซ้อน | ภาษาระดับสูงใดๆ |
---

## คำถามและคำตอบสังเคราะห์
### Q1: อะไรคือความแตกต่างระหว่างการประกอบ RISC และ CISC?
**A:** CISC (x86) มีคำสั่งที่ซับซ้อนและมีความยาวผันแปรได้ RISC (ARM) มีคำสั่งง่ายๆ ที่มีความยาวคงที่:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### Q2: สแต็กทำงานอย่างไรในชุดประกอบ?
**A:** สแต็กจะขยายลงด้านล่าง `push`ลด SP และร้านค้า `pop`โหลดและเพิ่ม SP:
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

### Q3: ฉันจะเรียกใช้ฟังก์ชันในแอสเซมบลีได้อย่างไร
**A:** ปฏิบัติตามหลักการเรียก (System V AMD64 บน Linux, Windows x64 บน Windows):
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

### Q4: คำแนะนำในการประกอบที่สำคัญที่สุดที่ควรรู้คืออะไร?
**ตอบ:** การเคลื่อนไหวของข้อมูล เลขคณิต โฟลว์การควบคุม และการดำเนินการสแต็กเป็นแกนกลาง
### Q5: การประกอบถูกนำมาใช้ในการวิจัยด้านความปลอดภัยอย่างไร?
**ตอบ:** การทำวิศวกรรมย้อนกลับ การพัฒนาช่องโหว่ การวิเคราะห์มัลแวร์ และการทำความเข้าใจเอาต์พุตของคอมไพเลอร์ ล้วนแต่ต้องใช้ความรู้ด้านแอสเซมบลี
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การนำลูปไปใช้ในแอสเซมบลี
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
รวมจำนวนเต็มตั้งแต่ 1 ถึง N
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้เคาน์เตอร์ลงทะเบียนและสะสม
**ขั้นตอนที่ 3: นำไปใช้**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**ขั้นตอนที่ 4: เพิ่มประสิทธิภาพ**
ใช้สูตร N*(N+1)/2 สำหรับ O(1) แทน O(N)
---

## สรุป
ภาษาแอสเซมบลีเป็นสะพานเชื่อมระหว่างโค้ดที่มนุษย์อ่านได้กับไบนารีดิบที่ CPU ดำเนินการ ไม่ใช่ทางเลือกที่เป็นประโยชน์สำหรับการสร้างแอปพลิเคชัน แต่จำเป็นสำหรับการทำความเข้าใจว่าคอมพิวเตอร์ทำงานอย่างไรในระดับต่ำสุด สำหรับโปรแกรมเมอร์ระบบ นักวิจัยด้านความปลอดภัย และนักพัฒนาแบบฝังตัว ความรู้ด้านการประกอบถือเป็นสิ่งล้ำค่า สำหรับคนอื่นๆ การทำความเข้าใจแนวคิดแอสเซมบลี (รีจิสเตอร์ สแตก วงจรคำสั่ง) จะทำให้คุณเป็นโปรแกรมเมอร์ที่ดีขึ้นในทุกภาษา