---
# Metadata
title: "Assembly — Cheat Sheet"
description: "Quick-reference cheat sheet for x86/x64 Assembly (NASM) syntax and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [assembly, x86, x64, nasm, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Hội — Bảng cheat
## Thanh ghi (x86-64)
```nasm
; General purpose registers
rax         ; accumulator / return value
rbx         ; callee-saved
rcx         ; counter / 4th arg
rdx         ; data / 3rd arg
rsi         ; source index / 2nd arg
rdi         ; destination index / 1st arg
rbp         ; base pointer (callee-saved)
rsp         ; stack pointer
r8 - r15    ; additional registers

; Sub-registers
eax         ; lower 32 bits of rax
ax          ; lower 16 bits
al, ah      ; lower/upper 8 bits

; Segment registers
cs, ds, ss, es, fs, gs

; Flags register
rflags      ; CF, ZF, SF, OF, PF
```

## Di chuyển dữ liệu
```nasm
; MOV — copy data
mov rax, rbx            ; reg to reg
mov rax, 42             ; immediate to reg
mov rax, [rbx]          ; memory to reg (dereference)
mov [rbx], rax          ; reg to memory
mov rax, [rsp + 8]      ; memory with offset

; LEA — load effective address
lea rax, [rbx + rcx*4]  ; compute address, don't dereference
lea rax, [rel message]  ; relative address

; XCHG — exchange
xchg rax, rbx           ; swap rax and rbx

; MOV variants
movzx rax, byte [rbx]   ; move with zero extension
movsx rax, byte [rbx]   ; move with sign extension
movabs rax, 0x123456789ABCDEF0  ; 64-bit immediate

; Size directives
mov byte [rbx], 0xFF
mov word [rbx], 0x1234
mov dword [rbx], 0x12345678
mov qword [rbx], 0x123456789ABCDEF0
```

## Số học
```nasm
; Addition / Subtraction
add rax, rbx            ; rax = rax + rbx
sub rax, rbx            ; rax = rax - rbx
inc rax                 ; rax++
dec rax                 ; rax--
neg rax                 ; rax = -rax

; Multiplication / Division
imul rax, rbx           ; rax = rax * rbx (signed)
mul rbx                 ; rdx:rax = rax * rbx (unsigned)
idiv rbx                ; rax = rax / rbx, rdx = remainder (signed)
div rbx                 ; rax = rax / rbx, rdx = remainder (unsigned)

; Shifts
shl rax, 3              ; rax <<= 3 (multiply by 8)
shr rax, 2              ; rax >>= 2 (unsigned divide by 4)
sar rax, 1              ; arithmetic right shift (signed)

; Bitwise
and rax, rbx            ; bitwise AND
or rax, rbx             ; bitwise OR
xor rax, rbx            ; bitwise XOR
not rax                 ; bitwise NOT
test rax, rbx           ; AND without storing (sets flags)
```

## Luồng điều khiển
```nasm
; Unconditional jump
jmp label

; Conditional jumps (after cmp or test)
cmp rax, rbx            ; compare (sets flags)
je label                ; jump if equal (ZF=1)
jne label               ; jump if not equal (ZF=0)
jg label                ; jump if greater (signed)
jl label                ; jump if less (signed)
jge label               ; jump if greater or equal
jle label               ; jump if less or equal
ja label                ; jump if above (unsigned)
jb label                ; jump if below (unsigned)
jz label                ; jump if zero
jnz label               ; jump if not zero
js label                ; jump if sign (negative)
jns label               ; jump if not sign

; Loop
mov rcx, 10
.loop:
    ; ... body ...
    loop .loop          ; rcx--; jump if rcx != 0

; Call / Return
call function           ; push RIP, jump to function
ret                     ; pop RIP, return

; Function prologue / epilogue
push rbp
mov rbp, rsp
; ... function body ...
mov rsp, rbp
pop rbp
ret
```

## Thao tác ngăn xếp
```nasm
push rax                ; rsp -= 8; [rsp] = rax
pop rax                 ; rax = [rsp]; rsp += 8

; Stack frame
push rbp
mov rbp, rsp
sub rsp, 32             ; allocate 32 bytes for locals

; Access locals
mov [rbp - 8], rax      ; local variable 1
mov [rbp - 16], rbx     ; local variable 2
mov rax, [rbp - 8]      ; read local variable 1
```

## Cuộc gọi hệ thống (Linux x86-64)
```nasm
; write(1, msg, len)
mov rax, 1              ; syscall number (sys_write)
mov rdi, 1              ; fd = stdout
mov rsi, message        ; buffer
mov rdx, msg_len        ; count
syscall

; read(0, buf, size)
mov rax, 0              ; sys_read
mov rdi, 0              ; fd = stdin
mov rsi, buffer
mov rdx, 256
syscall

; exit(code)
mov rax, 60             ; sys_exit
mov rdi, 0              ; exit code
syscall

; Common syscall numbers
; 0 = read, 1 = write, 2 = open, 3 = close
; 9 = mmap, 12 = brk
; 57 = fork, 59 = execve
; 60 = exit
```

## Phần dữ liệu
```nasm
section .data
    message db "Hello", 10, 0    ; string with newline
    number  dq 42                ; 64-bit integer
    array   dd 1, 2, 3, 4, 5    ; array of 32-bit ints

section .bss
    buffer  resb 256             ; reserve 256 bytes
    count   resq 1               ; reserve 1 qword

section .text
    global _start
_start:
    ; entry point
```
