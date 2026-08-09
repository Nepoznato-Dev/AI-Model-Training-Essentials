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
# Hợp ngữ
Hợp ngữ là ngôn ngữ lập trình cấp thấp nhất mà con người có thể đọc được. Nó cung cấp sự trình bày trực tiếp các hướng dẫn mã máy của máy tính bằng cách sử dụng các mã ghi nhớ (như`MOV`,`ADD`,`JMP`) thay vì nhị phân thô. Mỗi ngôn ngữ hợp ngữ dành riêng cho một kiến ​​trúc bộ xử lý cụ thể (x86, ARM, MIPS, RISC-V) — mã được viết cho một kiến ​​trúc sẽ không chạy trên kiến ​​trúc khác.
Ngôn ngữ hội không được sử dụng để xây dựng ứng dụng. Nó được sử dụng khi bạn cần kiểm soát tuyệt đối phần cứng: viết nhân hệ điều hành, trình điều khiển thiết bị, bộ tải khởi động, chương trình cơ sở nhúng, các đoạn mã quan trọng về hiệu năng, kỹ thuật đảo ngược và hiểu cách máy tính thực sự thực thi các hướng dẫn.
---

## Tại sao hội lại quan trọng
- **Hiểu về phần cứng**: Cách duy nhất để biết chính xác CPU đang làm gì ở cấp độ hướng dẫn.
- **Điều chỉnh hiệu suất**: Các phần mã quan trọng có thể được tối ưu hóa vượt xa những gì trình biên dịch tạo ra.
- **Kỹ thuật đảo ngược**: Phân tích phần mềm độc hại, nghiên cứu bảo mật và tìm hiểu phần mềm độc quyền.
- **Hệ thống nhúng**: Một số bộ vi điều khiển không hỗ trợ ngôn ngữ cấp cao hơn.
- **Phát triển hệ điều hành**: Mã khởi động, trình xử lý ngắt và chuyển đổi ngữ cảnh yêu cầu phải lắp ráp.
- **Giáo dục**: Hiểu cách lắp ráp sẽ dạy cho bạn cách máy tính thực sự hoạt động — bộ nhớ, thanh ghi, ngăn xếp và đường dẫn CPU.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Cấp độ cực thấp** | Mỗi hướng dẫn ánh xạ tới một hoạt động của máy | Sử dụng ngôn ngữ cấp cao hơn cho mọi thứ ngoại trừ những phần quan trọng |
| **Kiến trúc cụ thể** | mã x86 không chạy trên ARM | Viết mã di động bằng C/C++; chỉ sử dụng lắp ráp khi cần thiết |
| **Dài dòng** | Nhiệm vụ đơn giản cần nhiều hướng dẫn | Sử dụng macro; giữ các phần lắp ráp ở mức tối thiểu |
| **Không có tính di động** | Cú pháp khác nhau cho mỗi trình biên dịch mã (NASM, GAS, MASM) | Sử dụng nội tại của trình biên dịch hoặc lắp ráp nội tuyến |
| **Gỡ lỗi khó khăn** | Khó theo dõi logic ở cấp độ hướng dẫn | Sử dụng trình gỡ lỗi (GDB); thêm ý kiến ​​một cách tự do |
---

## Ví dụ về cú pháp (x86-64 Assembly - NASM)
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

### Ví dụ lắp ráp ARM
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

## Cú pháp & Mẫu nâng cao
### Chế độ đánh địa chỉ x86-64
Hiểu các chế độ địa chỉ là rất quan trọng để viết hợp ngữ hiệu quả. Mỗi chế độ kiểm soát cách các toán hạng được định vị.
| Chế độ | Cú pháp (NASM) | Mô tả |
|------|--------------||-------------|
| **Ngay lập tức** |  __BẢO VỆ_0__ | Toán hạng là một giá trị không đổi |
| **Đăng ký** |  __BẢO VỆ_1__ | Toán hạng nằm trong sổ đăng ký |
| **Trực tiếp** |  __BẢO VỆ_2__ | Toán hạng ở địa chỉ bộ nhớ cố định |
| **Đăng ký gián tiếp** |  __BẢO VỆ_3__ | Toán hạng ở địa chỉ trong sổ đăng ký |
| **Đế + chuyển vị** |  __BẢO VỆ_4__ | Địa chỉ = thanh ghi + offset không đổi |
| **Chỉ số được chia tỷ lệ** |  __BẢO VỆ_5__ | Địa chỉ = cơ sở + (chỉ số × tỷ lệ) |
| **SIB đầy đủ** |  __BẢO VỆ_6__ | Cơ sở + (chỉ số × tỷ lệ) + chuyển vị |
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

### Hệ thống vĩ mô (NASM)
Macro cho phép bạn xác định các chuỗi lệnh có thể sử dụng lại bằng các tham số, giúp việc lắp ráp ít lặp lại hơn.
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

### Bố cục khung ngăn xếp
Hiểu khung ngăn xếp là điều cần thiết để viết hàm và gỡ lỗi.
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

## Thiết kế kiến ​​trúc & hệ thống
### Bố cục bộ nhớ của quy trình Linux x86-64 điển hình
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

### Quy ước về cấu trúc chương trình
Một chương trình tập hợp được tổ chức tốt sẽ chia các mối quan tâm thành các phần riêng biệt:
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

### Cấu trúc thư mục dự án điển hình
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

## Cấu hình dự án & xây dựng hệ thống
### NASM + GCC trên Linux
Quy trình làm việc phổ biến nhất liên kết tập hợp với C bằng cách sử dụng GCC làm trình liên kết.
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

### MASM trên Windows (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (GNU Assembler) với Cú pháp AT&T
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

### Liên kết một chương trình Pure Assembly (No C Runtime)
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

## Các khái niệm chính
| Khái niệm | Mô tả |
|----------|-------------|
| **Đăng ký** | Bộ nhớ trong của CPU (EAX, EBX, ECX, EDX trên x86; R0-R15 trên ARM) |
| **Địa chỉ bộ nhớ** | Truy cập RAM qua địa chỉ (`MOV EAX, [0x1000]`) |
| **Chồng** | Vùng bộ nhớ LIFO cho lệnh gọi hàm và biến cục bộ (`PUSH`,`POP`) |
| **Hướng dẫn** | Các phép toán cơ bản: số học, logic, di chuyển dữ liệu, luồng điều khiển |
| **Ngắt / cuộc gọi tòa nhà** | Yêu cầu dịch vụ từ hệ điều hành |
| **Quy ước gọi điện** | Cách các hàm nhận tham số và giá trị trả về (thay đổi tùy theo kiến ​​trúc) |
---

## Kiểm tra & gỡ lỗi
### GDB (Trình gỡ lỗi GNU)
GDB là trình gỡ lỗi tiêu chuẩn để lắp ráp trên Linux. Nó cho phép bạn xem qua các hướng dẫn, kiểm tra sổ đăng ký và kiểm tra bộ nhớ.
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

### Gỡ lỗi bằng Macro NASM
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

### Các mẫu gỡ lỗi phổ biến
| Vấn đề | Triệu chứng | Kỹ thuật gỡ lỗi |
|----------|----------|-------------------|
| Lỗi phân đoạn | Chương trình gặp sự cố với SIGSEGV | Kiểm tra giá trị con trỏ; xác minh căn chỉnh ngăn xếp |
| Vòng lặp vô hạn | Chương trình bị treo | Đặt điểm dừng trong vòng lặp; kiểm tra cờ điều kiện |
| Kết quả sai | Tính toán sai | Bước qua số học; kiểm tra giá trị đăng ký sau mỗi lần hoạt động |
| Ngăn xếp tham nhũng | Sự cố trên RET | Xác minh số dư PUSH/POP; kiểm tra căn chỉnh RSP (phải căn chỉnh 16 byte) |
| Tòa nhà sai | Hành vi hạt nhân không mong muốn | Xác minh số tòa nhà trong RAX; kiểm tra sổ đăng ký đối số |
---

## Khả năng tương tác
### Gọi hàm C từ Assembly
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

### Tham chiếu cuộc gọi hệ thống (Linux x86-64)
| Tòa nhà | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|----------|------|-------------|-------------|----------||-----------|
| đọc | 0 | fd | buf | đếm | — |
| viết | 1 | fd | buf | đếm | — |
| mở | 2 | tên đường dẫn | cờ | chế độ | — |
| đóng | 3 | fd | — | — | — |
| mmap | 9 | địa chỉ | chiều dài | ủng hộ | cờ |
| thoát | 60 | trạng thái | — | — | — |
### Hợp ngữ nội tuyến trong C (GCC)
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

## Mẫu thiết kế
### Mẫu 1: Lặp với Accumulator
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

### Mẫu 2: Đường ống xử lý chuỗi
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

### Mẫu 3: Bảng điều phối (Switch/Case)
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

### Mẫu 4: Truyền tải danh sách liên kết
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

## Hiệu suất & Tối ưu hóa
### Lập kế hoạch hướng dẫn
Các CPU hiện đại thực thi nhiều lệnh trong mỗi chu kỳ thông qua đường dẫn và thực thi không theo thứ tự. Hiểu điều này giúp viết lắp ráp nhanh hơn.
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

### Tối ưu hóa bộ đệm
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

### Danh sách kiểm tra tối ưu hóa
| Kỹ thuật | Tác động | Mô tả |
|----------|----------|-------------|
| **Đăng ký sử dụng** | Cao | Giữ các biến nóng trong sổ đăng ký; tránh truy cập bộ nhớ |
| **Bỏ vòng lặp** | Trung bình | Giảm chi phí vòng lặp bằng cách xử lý nhiều mục trong mỗi lần lặp |
| **SIMD (SSE/AVX)** | Rất Cao | Xử lý đồng thời 4-16 giá trị bằng lệnh vector |
| **Loại bỏ chi nhánh** | Trung bình | Sử dụng CMOV thay vì nhảy có điều kiện nếu có thể |
| **Căn chỉnh bộ đệm** | Trung bình | Căn chỉnh các vòng lặp nóng theo ranh giới 16/32 byte |
| **Mẫu truy cập bộ nhớ** | Cao | Truy cập tuần tự; tránh chia tách dòng bộ đệm |
---

## Triển khai & Sử dụng trong Thế giới Thực
### Chương trình lắp ráp được triển khai như thế nào
Các chương trình hợp ngữ biên dịch trực tiếp thành các tệp thực thi mã máy gốc. Không có thời gian chạy, không có VM và không cần trình thông dịch. Triển khai đơn giản như sao chép tệp nhị phân vào hệ thống đích.
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### Các trường hợp sử dụng trong thế giới thực
| Công nghiệp | Ứng dụng | Tại sao hội |
|----------|-------------|-------------|
| **Hệ điều hành** | Sơ khai khởi động nhân Linux, Windows HAL | Điều khiển phần cứng trực tiếp, xử lý ngắt |
| **Phần mềm nhúng** | Bộ tải khởi động vi điều khiển, thiết bị IoT | Không có hệ điều hành hoặc thời gian chạy; giới hạn bộ nhớ nghiêm ngặt |
| **An ninh** | Phát triển khai thác, phân tích phần mềm độc hại, kỹ thuật đảo ngược | Cách duy nhất để tương tác với các tệp nhị phân được biên dịch |
| **Công cụ trò chơi** | Toán học được tối ưu hóa SIMD (biến đổi ma trận, vật lý) | Thông lượng tối đa để tính toán trên mỗi khung hình |
| **Trình biên dịch** | Phần phụ trợ tạo mã (LLVM, GCC) | Phát ra mã máy được tối ưu hóa |
| **Mật mã** | Tăng tốc lệnh AES-NI, SHA | Hoạt động tiền điện tử được tăng tốc phần cứng |
| **Trình điều khiển thiết bị** | Trình điều khiển GPU, phần mềm card mạng | Truy cập phần cứng cấp đăng ký trực tiếp |
### Tích hợp hệ thống kế thừa
Nhiều hệ thống cũ chứa các quy trình lắp ráp được nhúng trong cơ sở mã C. Đây thường là các chức năng quan trọng về hiệu năng hoặc các quy trình dành riêng cho phần cứng đã được duy trì trong nhiều thập kỷ.
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

## Khi nào nên sử dụng hội
| Kịch bản | Tại sao hội | Thay thế tốt hơn |
|----------|-------------|-------------------|
| Phát triển nhân hệ điều hành | Mã khởi động, xử lý ngắt | C cho hầu hết mã hạt nhân |
| Trình điều khiển thiết bị | Truy cập phần cứng trực tiếp | C, Rỉ Sét |
| Kỹ thuật đảo ngược / bảo mật | Cách duy nhất để phân tích các tệp nhị phân đã biên dịch | — |
| Mã quan trọng về hiệu suất | Tối ưu hóa tối đa | C/C++ với bản chất của trình biên dịch |
| Phần mềm nhúng (kim loại trần) | Không có ngôn ngữ cấp cao hơn | C, Rỉ Sét |
| Giáo dục | Tìm hiểu kiến ​​trúc máy tính | — |
| Phát triển ứng dụng chung | Không thực tế đối với các chương trình phức tạp | Bất kỳ ngôn ngữ cấp cao nào |
---

## Bản tóm tắt
Hợp ngữ là cầu nối giữa mã mà con người có thể đọc được và mã nhị phân thô mà CPU thực thi. Nó không phải là một lựa chọn thực tế để xây dựng các ứng dụng, nhưng nó cần thiết để hiểu cách thức hoạt động của máy tính ở mức thấp nhất. Đối với các lập trình viên hệ thống, nhà nghiên cứu bảo mật và nhà phát triển nhúng, kiến ​​thức về lắp ráp là vô giá. Đối với những người khác, việc hiểu các khái niệm lắp ráp (thanh ghi, ngăn xếp, chu trình lệnh) giúp bạn trở thành lập trình viên giỏi hơn trong bất kỳ ngôn ngữ nào.