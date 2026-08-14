---
# Metadata
title: "Assembly Language — Version History & Evolution"
description: "Comprehensive version history and evolution of Assembly language from early machines to modern x86/ARM."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [assembly, x86, arm, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# ภาษาแอสเซมบลี - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| ยุค | ปี | ธีมหลัก |
|-----|-|-----------|
| ทศวรรษที่ 1940 | 2488 | รหัสเครื่อง — สวิตช์สลับ, เทปกระดาษ |
| 2492 | 2492 | **ผู้ประกอบรายแรก** (วิลค์ส, วีลเลอร์, กิลล์ — EDSAC) |
| ทศวรรษ 1950 | 2494 | A-0 ของ Grace Hopper — "คอมไพเลอร์" ตัวแรก (แอสเซมเบลอร์แมโคร) |
| 2500 | 2500 | SOAP (Symbolic Optimal Assembly Program) สำหรับ IBM 650 |
| ทศวรรษ 1960 | 1960 | BAL (ภาษาแอสเซมบลีพื้นฐาน) สำหรับ IBM System/360 |
| 1978 | 1978 | **Intel 8086** — สถาปัตยกรรม x86 ถือกำเนิด |
| ทศวรรษที่ 1980 | 1981 | IBM PC — ชุดประกอบ x86 ครอบงำการเขียนโปรแกรมพีซี |
| 1985 | 1985 | **Intel 386** — 32-บิต x86, โหมดป้องกัน |
| 1993 | 1993 | **Intel Pentium** — ซุปเปอร์สเกลาร์, MMX ในภายหลัง |
| 1997 | 1997 | คำแนะนำ MMX (มัลติมีเดีย) |
| 1999 | 1999 | SSE (ส่วนขยาย SIMD สตรีมมิ่ง) |
| 2000 | 2000 | **AMD64** — ส่วนขยาย x86 64 บิต |
| 2544 | 2544 | **ARM** ครองตลาดมือถือ |
| 2548 | 2548 | SSE3 โปรเซสเซอร์ดูอัลคอร์ |
| 2549 | 2549 | **x86-64** — 64 บิตกลายเป็นมาตรฐาน |
| 2554 | 2554 | **AVX** (ส่วนขยายเวกเตอร์ขั้นสูง) |
| 2013 | 2013 | **ARM64 (AArch64)** — ARM 64 บิต |
| 2017 | 2017 | **AVX-512** — การทำงานของเวกเตอร์ 512 บิต |
| 2020 | 2020 | **Apple M1** — ARM64 บนเดสก์ท็อป |
| 2023 | 2023 | **AVX-VNNI** — การเร่งความเร็ว AI/ML |
| 2024 | 2024 | **RISC-V** ได้รับแรงฉุด — open ISA |
## เหตุการณ์สำคัญที่สำคัญ
### ยุครหัสเครื่องจักร (ค.ศ. 1940–1950)
- **1945**: ENIAC ตั้งโปรแกรมผ่านปลั๊กบอร์ดและสวิตช์
- **1949**: EDSAC — คอมพิวเตอร์โปรแกรมจัดเก็บเครื่องแรก "ผู้ประกอบ" คนแรก (คำสั่งเริ่มต้น)
- **1951**: A-0 ของ Grace Hopper — แปลสัญกรณ์ทางคณิตศาสตร์เป็นรหัสเครื่อง
- **1957**: SOAP — แอสเซมบลีสัญลักษณ์ที่ใช้กันอย่างแพร่หลายตัวแรก (IBM 650)
### สภา x86 (พ.ศ. 2521–ปัจจุบัน)
- **1978**: เกิดสถาปัตยกรรม Intel 8086 — x86
  - รีจิสเตอร์ 16 บิต: AX, BX, CX, DX, SI, DI, SP, BP
  - หน่วยความจำแบบแบ่งส่วน: CS, DS, SS, ES
  - คำแนะนำ: MOV, เพิ่ม, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32 บิต x86 (IA-32)
  - รีจิสเตอร์ 32 บิต: EAX, EBX, ECX, EDX
  - โหมดป้องกัน, เพจ, หน่วยความจำเสมือน
- **2000**: AMD64 — ส่วนขยาย x86 64 บิต
  - รีจิสเตอร์ 64 บิต: RAX, RBX, RCX, RDX
  - รีจิสเตอร์เอนกประสงค์ 16 รีจิสเตอร์ (เทียบกับ 8 ใน 32 บิต)
  - ที่อยู่ญาติ RIP
### การประกอบ ARM (พ.ศ. 2528–ปัจจุบัน)
- **1985**: ARM1 — Acorn Computers (สหราชอาณาจักร)
  - ปรัชญา RISC: คำสั่งที่เรียบง่ายและมีความยาวคงที่
  - สถาปัตยกรรมการโหลด/การจัดเก็บ
  - 16 รีจิสเตอร์ (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — ARM 64 บิต
  - รีจิสเตอร์อเนกประสงค์ 64 บิต 31 รายการ
  - SIMD: นีออน, SVE
  - ใช้ใน: สมาร์ทโฟน, Apple Silicon, AWS Graviton
### RISC-V (2010–ปัจจุบัน)
- **2010**: UC Berkeley สร้าง ISA แบบเปิด
- **ยุค 2020**: RISC-V ได้รับความสนใจ — เปิดกว้าง ไม่มีค่าธรรมเนียมใบอนุญาต
- ใช้ใน: ระบบฝังตัว, ชิปแบบกำหนดเอง, การผลักดันเซมิคอนดักเตอร์ของจีน
## วิวัฒนาการไวยากรณ์
```asm
; 1978: Intel 8086 — 16-bit x86
MOV AX, 0x1234    ; load immediate into AX
MOV BX, AX        ; copy AX to BX
ADD AX, BX        ; AX = AX + BX
JMP loop_start    ; unconditional jump
INT 0x21          ; DOS interrupt (system call)

; 1985: Intel 386 — 32-bit x86
MOV EAX, 0x12345678  ; 32-bit register
PUSH EBP             ; save frame pointer
MOV EBP, ESP         ; set up stack frame
CALL printf          ; call C function
ADD ESP, 4           ; clean up stack

; 2006: x86-64 — 64-bit
MOV RAX, 0x123456789ABCDEF0  ; 64-bit register
MOV RDI, RSP                  ; RDI = first argument (System V ABI)
CALL puts                     ; call C function
SYSCALL                       ; Linux system call (instead of INT)

; ARM32 assembly
MOV R0, #42          ; load immediate
LDR R1, [R2, #4]    ; load from memory (R2 + 4)
ADD R0, R0, R1      ; R0 = R0 + R1
BL printf            ; branch with link (call)
BX LR                ; return

; ARM64 (AArch64) assembly
MOV X0, #42          ; 64-bit register
LDR X1, [X2, #8]    ; 64-bit load
ADD X0, X0, X1      ; 64-bit add
BL printf            ; branch with link
RET                  ; return

; RISC-V assembly
LI a0, 42            ; load immediate
LW a1, 8(a2)         ; load word from memory
ADD a0, a0, a1       ; add
CALL printf           ; call function
RET                   ; return
```

## วิวัฒนาการชุดคำสั่ง
```
1978: 8086 — basic arithmetic, string ops, interrupts
1985: 386 — 32-bit, protected mode, paging
1997: MMX — SIMD for multimedia (64-bit)
1999: SSE — 128-bit SIMD, floating-point
2001: SSE2 — integer SIMD
2006: x86-64 — 64-bit, 16 GPRs
2008: SSE4 — string comparison, popcount
2011: AVX — 256-bit SIMD, 3-operand instructions
2013: AVX2 — gather, FMA
2017: AVX-512 — 512-bit SIMD (Xeon, server)
2020: AVX-VNNI — neural network instructions
2023: AMX — Advanced Matrix Extensions (AI acceleration)
```

## หลักการออกแบบที่สำคัญ
```
CISC (x86):
1. "Complex instructions" — one instruction can do a lot
2. "Variable length" — instructions are 1-15 bytes
3. "Memory-to-memory" — operate directly on memory
4. "Backward compatible" — 40+ years of code still runs

RISC (ARM, RISC-V):
5. "Simple instructions" — one instruction does one thing
6. "Fixed length" — all instructions same size (ARM: 32-bit)
7. "Load/store" — only load/store access memory
8. "Registers" — operate on registers, not memory
```

## การเติบโตของระบบนิเวศ
```
1940s: Machine code — toggle switches
1949: First assembler (EDSAC)
1957: SOAP — symbolic assembly
1978: x86 — IBM PC standard
1985: ARM — RISC for embedded
2000: AMD64 — 64-bit x86
2013: ARM64 — 64-bit ARM, mobile + server
2020: Apple M1 — ARM64 on desktop
2023: RISC-V — open ISA gains traction
2025: Assembly still used in:
       - OS kernels (boot code, context switching)
       - Device drivers (hardware access)
       - Compilers (code generation output)
       - Reverse engineering / security research
       - Embedded systems (resource-constrained)
       - Performance-critical code (SIMD, crypto)
       Tools: NASM, GAS, MASM, LLVM MC
```
