---
# Metadata
title: "Assembly Language — Syntax Reference"
description: "Detailed syntax reference for x86-64 Assembly covering registers, addressing modes, instruction categories, macros, stack frames, and system programming patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [assembly, syntax-reference, x86-64, registers, addressing-modes, system-programming, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# 汇编语言 — 语法参考
本文档为 x86-64 汇编（NASM 语法）提供全面、结构化的语法参考。它通过关注详尽的指令类别、寻址模式、堆栈帧约定和系统编程模式来补充主要的汇编参考。
---

## 寄存器和数据大小
```nasm
; x86-64 General-Purpose Registers
; 64-bit   32-bit   16-bit   8-bit (high/low)
; RAX      EAX      AX       AH/AL       ← Accumulator
; RBX      EBX      BX       BH/BL       ← Base
; RCX      ECX      CX       CH/CL       ← Counter
; RDX      EDX      DX       DH/DL       ← Data
; RSI      ESI      SI       SIL          ← Source Index
; RDI      EDI      DI       DIL          ← Destination Index
; RBP      EBP      BP       BPL          ← Base Pointer
; RSP      ESP      SP       SPL          ← Stack Pointer
; R8-R15   R8D-R15D R8W-R15W R8B-R15B    ← Extended registers

; Data size directives
db  42              ; Define Byte (8-bit)
dw  1000            ; Define Word (16-bit)
dd  100000          ; Define Doubleword (32-bit)
dq  10000000000     ; Define Quadword (64-bit)
dt  3.14            ; Define Ten bytes (80-bit float)

; String/byte data
msg     db  'Hello', 10, 0      ; null-terminated string with newline
buffer  resb 256                 ; reserve 256 bytes (uninitialized)
array   dd  1, 2, 3, 4, 5       ; array of 32-bit integers
matrix  resd 16                  ; reserve 16 dwords (4x4 matrix)
```

---

## 寻址模式
```nasm
; Immediate — operand is a constant
mov     eax, 42              ; EAX = 42
add     ebx, 0xFF            ; EBX += 255

; Register — operand is in a register
mov     eax, ebx             ; EAX = EBX
add     ecx, edx             ; ECX += EDX

; Direct/Memory — operand is at a fixed address
mov     eax, [0x601000]      ; EAX = value at address
mov     [var], dword 100     ; store 100 at variable

; Register Indirect — operand is at address in register
mov     eax, [rbx]           ; EAX = memory[RBX]
mov     [rsi], ecx           ; memory[RSI] = ECX

; Base + Displacement — address = register + constant
mov     eax, [rbx + 8]       ; EAX = memory[RBX + 8]
mov     eax, [rbp - 16]      ; EAX = local variable on stack

; Base + Index — address = base + index register
mov     eax, [rbx + rcx]     ; EAX = memory[RBX + RCX]

; Scaled Index — address = base + (index × scale)
mov     eax, [rbx + rcx*4]   ; EAX = array[i] (4-byte elements)
mov     eax, [rbx + rcx*8]   ; EAX = array[i] (8-byte elements)

; Full SIB (Scale-Index-Base + Displacement)
mov     eax, [rbx + rcx*4 + 16]  ; Full addressing
mov     eax, [rel msg]           ; RIP-relative (position-independent)

; LEA — Load Effective Address (compute address, don't dereference)
lea     rax, [rbx + rcx*4]   ; RAX = address (not the value there)
lea     rax, [rip + msg]      ; RAX = address of msg (PIC)
```

---

## 指令类别
```nasm
; === Data Movement ===
mov     eax, ebx             ; Copy: EAX = EBX
movzx   eax, byte [rsi]      ; Move with zero-extension (8→32)
movsx   eax, word [rsi]      ; Move with sign-extension (16→32)
xchg    eax, ebx             ; Exchange: swap EAX and EBX
lea     rax, [rbx + rcx*4]  ; Load effective address
cmovz   eax, ebx             ; Conditional move if zero flag set

; === Arithmetic ===
add     eax, ebx             ; EAX = EAX + EBX
sub     eax, ebx             ; EAX = EAX - EBX
imul    eax, ebx             ; EAX = EAX * EBX (signed)
mul     ebx                  ; EDX:EAX = EAX * EBX (unsigned)
idiv    ebx                  ; EAX=quotient, EDX=remainder (signed)
div     ebx                  ; EAX=quotient, EDX=remainder (unsigned)
inc     eax                  ; EAX++
dec     eax                  ; EAX--
neg     eax                  ; EAX = -EAX

; === Comparison & Logic ===
cmp     eax, ebx             ; Compare: set flags (EAX - EBX)
test    eax, eax             ; Test: set flags (EAX AND EAX)
and     eax, ebx             ; EAX = EAX AND EBX
or      eax, ebx             ; EAX = EAX OR EBX
xor     eax, eax             ; EAX = 0 (idiom for zeroing)
not     eax                  ; EAX = NOT EAX
shl     eax, 3               ; EAX <<= 3 (multiply by 8)
shr     eax, 2               ; EAX >>= 2 (unsigned divide by 4)
sar     eax, 1               ; Arithmetic right shift (signed)

; === Control Flow ===
jmp     .label               ; Unconditional jump
je      .label               ; Jump if equal (ZF=1)
jne     .label               ; Jump if not equal (ZF=0)
jg      .label               ; Jump if greater (signed)
jl      .label               ; Jump if less (signed)
jge     .label               ; Jump if greater or equal
jle     .label               ; Jump if less or equal
ja      .label               ; Jump if above (unsigned)
jb      .label               ; Jump if below (unsigned)
jz      .label               ; Jump if zero
jnz     .label               ; Jump if not zero
jc      .label               ; Jump if carry
jnc     .label               ; Jump if no carry
js      .label               ; Jump if sign (negative)

; === Stack Operations ===
push    rax                  ; Push RAX onto stack (RSP -= 8)
pop     rax                  ; Pop top of stack into RAX (RSP += 8)
push    rbp                  ; Save base pointer
mov     rbp, rsp             ; Set new base pointer
sub     rsp, 32              ; Allocate 32 bytes for locals
; ... use [rbp-4], [rbp-8], etc. ...
mov     rsp, rbp             ; Deallocate locals
pop     rbp                  ; Restore base pointer
ret                          ; Return to caller

; === Function Call ===
call    function_name        ; Push RIP, jump to function
call    [rbx]                ; Indirect call through pointer
nop                          ; No operation (padding/alignment)
```

---

## 函数和调用约定
```nasm
; === System V AMD64 ABI (Linux/macOS) ===
; Arguments: RDI, RSI, RDX, RCX, R8, R9 (then stack)
; Return value: RAX (integer), XMM0 (float)
; Caller-saved: RAX, RCX, RDX, RSI, RDI, R8-R11
; Callee-saved: RBX, RBP, R12-R15
; Stack must be 16-byte aligned before CALL

section .text
    global compute_sum
    extern printf

; int compute_sum(int* arr, int count)
compute_sum:
    push    rbp                  ; prologue
    mov     rbp, rsp
    sub     rsp, 16              ; 16 bytes for locals

    mov     [rbp - 4], dword 0   ; int sum = 0
    mov     [rbp - 8], dword 0   ; int i = 0

.loop:
    mov     eax, [rbp - 8]       ; load i
    cmp     eax, esi             ; compare i with count
    jge     .done                ; if i >= count, exit

    mov     eax, [rbp - 4]       ; load sum
    mov     ecx, [rbp - 8]       ; load i
    add     eax, [rdi + rcx*4]   ; sum += arr[i]
    mov     [rbp - 4], eax       ; store sum

    inc     dword [rbp - 8]      ; i++
    jmp     .loop

.done:
    mov     eax, [rbp - 4]       ; return value in EAX
    mov     rsp, rbp             ; epilogue
    pop     rbp
    ret

; === Windows x64 ABI ===
; Arguments: RCX, RDX, R8, R9 (then stack)
; Return value: RAX
; Caller-saved: RAX, RCX, RDX, R8-R11
; Callee-saved: RBX, RBP, RDI, RSI, R12-R15
; Requires 32-byte shadow space before call
```

---

## 宏和条件汇编
```nasm
; === NASM Macros ===
%macro print_string 2
    mov     rax, 1              ; syscall: write
    mov     rdi, 1              ; fd: stdout
    mov     rsi, %1             ; buffer address
    mov     rdx, %2             ; length
    syscall
%endmacro

%macro function_prologue 1
    push    rbp
    mov     rbp, rsp
    sub     rsp, %1
    push    rbx
    push    r12
%endmacro

%macro function_epilogue 0
    pop     r12
    pop     rbx
    mov     rsp, rbp
    pop     rbp
    ret
%endmacro

; Conditional assembly
%ifdef DEBUG
    %macro debug_break 0
        int3                    ; breakpoint instruction
    %endmacro
%else
    %macro debug_break 0
        nop
    %endmacro
%endif

; Loop unrolling macro
%macro process_four 2
    movdqu  xmm0, [%1]
    movdqu  xmm1, [%1 + 16]
    paddd   xmm0, [%2]
    paddd   xmm1, [%2 + 16]
    movdqu  [%1], xmm0
    movdqu  [%1 + 16], xmm1
%endmacro

; String length at assembly time
msg     db  'Hello, World!', 10
msg_len equ $ - msg             ; $ = current address
```

---

## SIMD（SSE/AVX）
```nasm
; === SSE2 Integer Operations ===
; XMM0-XMM15: 128-bit registers (4×32-bit or 2×64-bit)

movdqu  xmm0, [rsi]            ; Load 4 packed ints (unaligned)
movdqa  xmm0, [rsi]            ; Load 4 packed ints (16-byte aligned)
paddd   xmm0, xmm1             ; Add 4 packed 32-bit integers
psubd   xmm0, xmm1             ; Subtract 4 packed 32-bit integers
pmulld  xmm0, xmm1             ; Multiply 4 packed 32-bit integers
pcmpeqd xmm0, xmm1             ; Compare 4 packed ints for equality
pshufd  xmm0, xmm0, 0xE4       ; Shuffle/rearrange elements

; === AVX (256-bit) ===
; YMM0-YMM15: 256-bit registers (8×32-bit or 4×64-bit)

vmovdqu ymm0, [rsi]            ; Load 8 packed ints
vpaddd  ymm0, ymm0, ymm1       ; Add 8 packed 32-bit integers
vpmulld ymm0, ymm0, ymm1       ; Multiply 8 packed 32-bit integers

; === SIMD Loop: Sum Array ===
; int sum_array(int* arr, int n)
sum_array_simd:
    xor     eax, eax
    vpxor   ymm0, ymm0, ymm0   ; accumulator = {0,0,0,0,0,0,0,0}
    xor     ecx, ecx            ; i = 0

.loop:
    cmp     ecx, esi
    jge     .horizontal_add
    vmovdqu ymm1, [rdi + rcx*4]
    vpaddd  ymm0, ymm0, ymm1
    add     ecx, 8
    jmp     .loop

.horizontal_add:
    ; Sum the 8 elements in YMM0
    vextracti128 xmm1, ymm0, 1
    paddd   xmm0, xmm1
    movdqa  xmm1, xmm0
    punpckhqdq xmm1, xmm1
    paddd   xmm0, xmm1
    pshufd  xmm1, xmm0, 1
    paddd   xmm0, xmm1
    movd    eax, xmm0           ; final scalar sum
    vzeroupper
    ret
```

---

＃＃ 概括
汇编语言语法由处理器体系结构和汇编器（NASM、GAS、MASM）定义。 x86-64 提供 16 个通用寄存器、多种寻址模式以及数百条涵盖数据移动、算术、逻辑、控制流、SIMD 和系统调用的指令。这里使用的 NASM 语法是 Linux x86-64 开发中最常见的语法。掌握汇编需要了解寄存器、堆栈、调用约定以及高级结构如何映射到机器指令。