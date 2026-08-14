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
#لغة التجميع
لغة التجميع هي أدنى لغة برمجة يمكن قراءتها بواسطة الإنسان. وهو يوفر تمثيلاً مباشرًا لتعليمات رمز جهاز الكمبيوتر باستخدام رموز ذاكري (مثل`MOV`و`ADD`و`JMP`) بدلاً من الثنائي الخام. كل لغة تجميع خاصة ببنية معالج معينة (x86، ARM، MIPS، RISC-V) - لن يتم تشغيل التعليمات البرمجية المكتوبة لبنية واحدة على بنية أخرى.
لا يتم استخدام لغة التجميع لبناء التطبيقات. يتم استخدامه عندما تحتاج إلى التحكم المطلق في الأجهزة: كتابة نواة نظام التشغيل، وبرامج تشغيل الأجهزة، ومحملات التشغيل، والبرامج الثابتة المضمنة، وأقسام التعليمات البرمجية المهمة للأداء، والهندسة العكسية، وفهم كيفية تنفيذ أجهزة الكمبيوتر للتعليمات فعليًا.
---

## لماذا يهم التجميع
- **فهم الأجهزة**: الطريقة الوحيدة لمعرفة ما تفعله وحدة المعالجة المركزية بالضبط على مستوى التعليمات.
- **ضبط الأداء**: يمكن تحسين أقسام التعليمات البرمجية المهمة بشكل يتجاوز ما ينتجه المترجمون.
- **الهندسة العكسية**: تحليل البرامج الضارة، والبحث الأمني، وفهم البرامج الاحتكارية.
- **الأنظمة المضمنة**: لا تتمتع بعض وحدات التحكم الدقيقة بدعم لغوي عالي المستوى.
- **تطوير نظام التشغيل**: يتطلب رمز التمهيد ومعالجات المقاطعة وتبديل السياق التجميع.
- **تعليمية**: إن فهم التجميع يعلمك كيفية عمل أجهزة الكمبيوتر فعليًا - الذاكرة والسجلات والمكدس وخط أنابيب وحدة المعالجة المركزية.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **مستوى منخفض للغاية** | يتم تعيين كل تعليمات لعملية تشغيل جهاز واحد | استخدم لغات ذات مستوى أعلى لكل شيء باستثناء الأجزاء المهمة |
| ** خاص بالهندسة المعمارية ** | لا يعمل رمز x86 على ARM | كتابة التعليمات البرمجية المحمولة في C/C++؛ استخدم التجميع فقط عند الحاجة |
| **مطول** | المهام البسيطة تتطلب تعليمات كثيرة | استخدام وحدات الماكرو. حافظ على الحد الأدنى من أقسام التجميع |
| **لا يوجد قابلية للنقل** | بناء جملة مختلف لكل مجمع (NASM، GAS، MASM) | استخدم جوهر المترجم أو التجميع المضمن |
| ** صعوبة التصحيح ** | من الصعب تتبع المنطق على مستوى التعليمات | استخدام مصححات الأخطاء (GDB)؛ إضافة تعليقات بحرية |
---

## مثال على بناء الجملة (تجميع x86-64 — NASM)
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

### مثال على تجميع ARM
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

## بناء الجملة والأنماط المتقدمة
### x86-64 أوضاع العنونة
يعد فهم أوضاع العنونة أمرًا بالغ الأهمية لكتابة التجميع الفعال. يتحكم كل وضع في كيفية تحديد موقع المعاملات.
| الوضع | بناء الجملة (NASM) | الوصف |
|------|--------------|-------------|
| **فوري** | `mov eax, 42`| المعامل هو قيمة ثابتة |
| **التسجيل** | `mov eax, ebx`| المعامل موجود في السجل |
| **مباشر** | `mov eax, [0x4000]`| المعامل موجود على عنوان ذاكرة ثابت |
| **التسجيل غير المباشر** | `mov eax, [rbx]`| المعامل موجود على العنوان الموجود في السجل |
| **القاعدة + الإزاحة** | `mov eax, [rbx + 8]`| العنوان = التسجيل + الإزاحة الثابتة |
| **مؤشر مُقاس** | `mov eax, [rbx + rcx*4]`| العنوان = الأساس + (الفهرس × المقياس) |
| ** كامل SIB ** | `mov eax, [rbx + rcx*4 + 16]`| القاعدة + (المؤشر × المقياس) + الإزاحة |
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

### نظام الماكرو (NASM)
تتيح لك وحدات الماكرو تحديد تسلسلات التعليمات القابلة لإعادة الاستخدام باستخدام المعلمات، مما يجعل التجميع أقل تكرارًا.
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

### تخطيط الإطار المكدس
يعد فهم إطار المكدس أمرًا ضروريًا لكتابة الوظائف وتصحيح الأخطاء.
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

## الهندسة المعمارية وتصميم النظام
### تخطيط الذاكرة لعملية Linux x86-64 النموذجية
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

### اتفاقية هيكل البرنامج
يقوم برنامج التجميع المنظم جيدًا بفصل الاهتمامات إلى أقسام متميزة:
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

### هيكل دليل المشروع النموذجي
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

## تكوين المشروع ونظام البناء
### NASM + مجلس التعاون الخليجي على نظام التشغيل Linux
يتم تجميع روابط سير العمل الأكثر شيوعًا مع لغة C باستخدام دول مجلس التعاون الخليجي كرابط.
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

### MASM على نظام التشغيل Windows (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (مجمع GNU) مع بناء جملة AT&T
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

### ربط برنامج التجميع النقي (بدون وقت تشغيل C)
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

## المفاهيم الأساسية
| المفهوم | الوصف |
|---------|------------|
| **السجلات** | وحدة التخزين الداخلية لوحدة المعالجة المركزية (EAX وEBX وECX وEDX على x86 وR0-R15 على ARM) |
| **عنونة الذاكرة** | الوصول إلى ذاكرة الوصول العشوائي عبر العناوين (`MOV EAX, [0x1000]`) |
| **كومة** | منطقة ذاكرة LIFO لاستدعاءات الوظائف والمتغيرات المحلية (`PUSH`,`POP`) |
| **تعليمات** | العمليات الأساسية: الحساب، المنطق، حركة البيانات، التحكم في التدفق |
| ** المقاطعات / مكالمات النظام ** | طلب خدمات من نظام التشغيل |
| ** اصطلاحات الاتصال ** | كيف تتلقى الوظائف المعلمات وقيم الإرجاع (تختلف حسب البنية) |
---

## الاختبار والتصحيح
### GDB (مصحح أخطاء جنو)
GDB هو مصحح الأخطاء القياسي للتجميع على Linux. يتيح لك التنقل عبر التعليمات وفحص السجلات وفحص الذاكرة.
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

### تصحيح الأخطاء باستخدام وحدات ماكرو NASM
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

### أنماط التصحيح الشائعة
| مشكلة | العَرَض | تقنية التصحيح |
|---------|--------|------------------|
| سيجفولت | يتعطل البرنامج مع SIGSEGV | التحقق من قيم المؤشر. التحقق من محاذاة المكدس |
| حلقة لا نهائية | توقف البرنامج | تعيين نقطة التوقف في الحلقة؛ تحقق من أعلام الحالة |
| نتيجة خاطئة | حساب غير صحيح | خطوة من خلال الحساب. تحقق من قيم التسجيل بعد كل عملية |
| كومة الفساد | تحطم على RET | التحقق من رصيد PUSH/POP؛ تحقق من محاذاة RSP (يجب أن تكون محاذاة 16 بايت) |
| طلب نظام خاطئ | سلوك غير متوقع للنواة | التحقق من رقم syscall في RAX؛ تحقق من سجلات الوسيطة |
---

## إمكانية التشغيل البيني
### استدعاء وظائف C من التجميع
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

### مرجع استدعاء النظام (Linux x86-64)
| سيسكال | راكس | Arg1 (RDI) | Arg2 (مؤشر القوة النسبية) | Arg3 (RDX) | Arg4 (R10) |
|---------|-----|------------------|------------|-------------|---------|
| قراءة | 0 | فد | بوف | العد | — |
| أكتب | 1 | فد | بوف | العد | — |
| مفتوح | 2 | اسم المسار | أعلام | الوضع | — |
| إغلاق | 3 | فد | — | — | — |
| مماب | 9 | العنوان | الطول | بروت | أعلام |
| خروج | 60 | الحالة | — | — | — |
### التجميع المضمن في لغة C (دول مجلس التعاون الخليجي)
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

## أنماط التصميم
### النموذج 1: حلقة مع المجمع
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

### النموذج 2: خط أنابيب معالجة السلسلة
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

### النموذج 3: جدول الإرسال (المفتاح/العلبة)
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

### النموذج 4: اجتياز القائمة المرتبطة
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

## الأداء والتحسين
### جدولة التعليمات
تقوم وحدات المعالجة المركزية الحديثة بتنفيذ تعليمات متعددة في كل دورة من خلال خطوط الأنابيب والتنفيذ خارج الترتيب. يساعد فهم هذا في كتابة التجميع بشكل أسرع.
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

### تحسين ذاكرة التخزين المؤقت
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

### قائمة التحقق من التحسين
| تقنية | التأثير | الوصف |
|-----------|-------|-------------|
| **تسجيل الاستخدام** | عالية | احتفظ بالمتغيرات الساخنة في السجلات؛ تجنب الوصول إلى الذاكرة |
| **فتح الحلقة** | متوسطة | تقليل الحمل الزائد للحلقة عن طريق معالجة عناصر متعددة لكل تكرار |
| **سيمد (SSE/AVX)** | عالية جدًا | قم بمعالجة القيم من 4 إلى 16 في وقت واحد باستخدام تعليمات المتجهات |
| **إزالة الفرع** | متوسطة | استخدم CMOV بدلاً من القفزات الشرطية حيثما أمكن ذلك |
| **محاذاة ذاكرة التخزين المؤقت** | متوسطة | قم بمحاذاة الحلقات الفعالة إلى حدود 16/32 بايت |
| **أنماط الوصول إلى الذاكرة** | عالية | الوصول المتسلسل تجنب انقسامات سطر ذاكرة التخزين المؤقت |
---

## النشر والاستخدام في العالم الحقيقي
### كيفية نشر برامج التجميع
يتم تجميع برامج التجميع مباشرة إلى الملفات التنفيذية الخاصة بكود الجهاز الأصلي. لا يوجد وقت تشغيل ولا جهاز افتراضي ولا يتطلب مترجمًا. النشر بسيط مثل نسخ الملف الثنائي إلى النظام المستهدف.
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### حالات الاستخدام في العالم الحقيقي
| صناعة | التطبيق | لماذا الجمعية |
|----------|------------|-------------|
| **أنظمة التشغيل** | كعب تمهيد Linux kernel، Windows HAL | التحكم المباشر في الأجهزة ومعالجة المقاطعة |
| ** البرامج الثابتة المضمنة ** | محمل إقلاع المتحكم الدقيق، أجهزة إنترنت الأشياء | لا يتوفر نظام تشغيل أو وقت تشغيل؛ حدود الذاكرة الصارمة |
| **الأمن** | تطوير برامج الاستغلال، تحليل البرامج الضارة، الهندسة العكسية | الطريقة الوحيدة للتفاعل مع الثنائيات المترجمة |
| **محركات اللعبة** | الرياضيات المحسنة لـ SIMD (تحويلات المصفوفة، الفيزياء) | الحد الأقصى من الإنتاجية لحسابات كل إطار |
| **المجمعات** | الواجهات الخلفية لتوليد التعليمات البرمجية (LLVM، دول مجلس التعاون الخليجي) | انبعاث رمز الجهاز الأمثل |
| **التشفير** | AES-NI، تسريع تعليمات SHA | عمليات التشفير المسرَّعة بالأجهزة |
| ** برامج تشغيل الأجهزة ** | برامج تشغيل GPU والبرامج الثابتة لبطاقة الشبكة | الوصول المباشر إلى الأجهزة على مستوى التسجيل |
### تكامل النظام القديم
تحتوي العديد من الأنظمة القديمة على إجراءات تجميع مضمنة في قواعد تعليمات C البرمجية. عادةً ما تكون هذه وظائف مهمة للأداء أو إجراءات روتينية خاصة بالأجهزة والتي تم الحفاظ عليها لعقود من الزمن.
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

## متى يجب استخدام التجميع
| السيناريو | لماذا الجمعية | البديل الأفضل |
|----------|------------|------------------|
| تطوير نواة نظام التشغيل | رمز التمهيد، معالجات المقاطعة | C لمعظم رموز النواة |
| برامج تشغيل الأجهزة | الوصول المباشر للأجهزة | ج، الصدأ |
| الهندسة العكسية / الأمن | الطريقة الوحيدة لتحليل الثنائيات المترجمة | — |
| كود الأداء الحرج | أقصى قدر من التحسين | C/C++ مع جوهر المترجم |
| البرامج الثابتة المضمنة (المعادن العارية) | لا تتوفر لغة ذات مستوى أعلى | ج، الصدأ |
| تعليم | فهم هندسة الكمبيوتر | — |
| تطوير التطبيقات العامة | غير عملي للبرامج المعقدة | أي لغة ذات مستوى أعلى |
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين تجميع RISC وCISC؟
**أ:** يحتوي CISC (x86) على تعليمات معقدة ومتغيرة الطول. يحتوي RISC (ARM) على تعليمات بسيطة وثابتة الطول:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### السؤال الثاني: كيف تعمل المكدسة أثناء التجميع؟
**أ:** المكدس ينمو للأسفل. `push`ينقص SP والمتاجر؛ `pop`يقوم بتحميل وزيادات SP:
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

### س3: كيف يمكنني استدعاء الوظائف في التجميع؟
**ج:** اتبع اصطلاح الاتصال (System V AMD64 على Linux، Windows x64 على Windows):
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

### س4: ما هي أهم تعليمات التجميع التي يجب معرفتها؟
**أ:** تشكل حركة البيانات، والحساب، والتحكم في التدفق، وعمليات المكدس النواة.
### س5: كيف يتم استخدام التجميع في الأبحاث الأمنية؟
**ج:** تتطلب الهندسة العكسية، وتطوير الاستغلال، وتحليل البرامج الضارة، وفهم مخرجات برنامج التحويل البرمجي معرفة القراءة والكتابة بالتجميع.
---

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: تنفيذ حلقة في التجميع
**الخطوة الأولى: فهم المشكلة**
جمع الأعداد الصحيحة من 1 إلى N
**الخطوة 2: تحديد النهج**
استخدم سجل العداد والمراكم.
**الخطوة 3: التنفيذ**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**الخطوة 4: التحسين**
استخدم الصيغة N*(N+1)/2 لـ O(1) بدلاً من O(N).
---

## ملخص
لغة التجميع هي الجسر بين التعليمات البرمجية التي يمكن قراءتها بواسطة الإنسان والثنائي الخام الذي تنفذه وحدات المعالجة المركزية (CPU). إنه ليس خيارًا عمليًا لبناء التطبيقات، ولكنه ضروري لفهم كيفية عمل أجهزة الكمبيوتر عند أدنى مستوى. بالنسبة لمبرمجي الأنظمة والباحثين الأمنيين والمطورين المضمنين، فإن معرفة التجميع لا تقدر بثمن. بالنسبة لأي شخص آخر، فإن فهم مفاهيم التجميع (السجلات، والمكدس، ودورات التعليمات) يجعلك مبرمجًا أفضل في أي لغة.