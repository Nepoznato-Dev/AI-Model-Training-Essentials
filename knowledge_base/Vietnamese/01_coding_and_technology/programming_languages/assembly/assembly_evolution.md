---
# Metadata
title: "Assembly Language — Version History & Evolution"
description: "Comprehensive version history and evolution of Assembly language from early machines to modern x86/ARM."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Ngôn ngữ hội - Lịch sử phiên bản & sự phát triển
## Dòng thời gian
| Thời đại | Năm | Chủ đề chính |
|------|------|----------|
| Những năm 1940 | 1945 | Mã máy - công tắc bật tắt, băng giấy |
| 1949 | 1949 | **Nhà lắp ráp đầu tiên** (Wilkes, Wheeler, Gill — EDSAC) |
| Những năm 1950 | 1951 | A-0 của Grace Hopper — "trình biên dịch" đầu tiên (trình biên dịch macro) |
| 1957 | 1957 | SOAP (Chương trình lắp ráp tối ưu tượng trưng) cho IBM 650 |
| thập niên 1960 | 1960 | BAL (Ngôn ngữ hội cơ bản) cho IBM System/360 |
| 1978 | 1978 | **Intel 8086** — kiến ​​trúc x86 ra đời |
| thập niên 1980 | 1981 | IBM PC — tập hợp x86 thống trị lập trình PC |
| 1985 | 1985 | **Intel 386** — 32-bit x86, chế độ được bảo vệ |
| 1993 | 1993 | **Intel Pentium** — siêu vô hướng, MMX sau |
| 1997 | 1997 | Hướng dẫn MMX (đa phương tiện) |
| 1999 | 1999 | SSE (Truyền tải tiện ích mở rộng SIMD) |
| 2000 | 2000 | **AMD64** — tiện ích mở rộng x86 64-bit |
| 2001 | 2001 | **ARM** giành được sự thống trị trên thiết bị di động |
| 2005 | 2005 | SSE3, bộ xử lý lõi kép |
| 2006 | 2006 | **x86-64** — 64-bit trở thành tiêu chuẩn |
| 2011 | 2011 | **AVX** (Phần mở rộng vectơ nâng cao) |
| 2013 | 2013 | **ARM64 (AArch64)** — CÁNH TAY 64-bit |
| 2017 | 2017 | **AVX-512** — Hoạt động vectơ 512-bit |
| 2020 | 2020 | **Apple M1** — ARM64 trên máy tính để bàn |
| 2023 | 2023 | **AVX-VNNI** — Tăng tốc AI/ML |
| 2024 | 2024 | **RISC-V** tăng lực kéo — mở ISA |
## Các cột mốc quan trọng
### Kỷ nguyên mã máy (thập niên 1940–1950)
- **1945**: ENIAC được lập trình thông qua bảng cắm và công tắc
- **1949**: EDSAC — máy tính lưu trữ chương trình đầu tiên; "nhà lắp ráp" đầu tiên (đơn đặt hàng ban đầu)
- **1951**: Grace Hopper's A-0 — dịch ký hiệu toán học sang mã máy
- **1957**: SOAP — trình biên dịch ký hiệu được sử dụng rộng rãi đầu tiên (IBM 650)
### x86 hội (1978–nay)
- **1978**: Kiến trúc Intel 8086 — x86 ra đời
  - Các thanh ghi 16 bit: AX, BX, CX, DX, SI, DI, SP, BP
  - Bộ nhớ được phân đoạn: CS, DS, SS, ES
  - Hướng dẫn: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32-bit x86 (IA-32)
  - Các thanh ghi 32 bit: EAX, EBX, ECX, EDX
  - Chế độ bảo vệ, phân trang, bộ nhớ ảo
- **2000**: AMD64 — phần mở rộng x86 64-bit
  - Các thanh ghi 64 bit: RAX, RBX, RCX, RDX
  - 16 thanh ghi đa năng (so với 8 trong 32-bit)
  - Địa chỉ tương đối RIP
### Hội ARM (1985–nay)
- **1985**: ARM1 — Máy tính Acorn (Anh)
  - Triết lý RISC: hướng dẫn đơn giản, có độ dài cố định
  - Kiến trúc tải/lưu trữ
  - 16 thanh ghi (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — ARM 64-bit
  - 31 thanh ghi 64-bit đa năng
  - SIMD: NEON, SVE
  - Được sử dụng trong: điện thoại thông minh, Apple Silicon, AWS Graviton
### RISC-V (2010–nay)
- **2010**: UC Berkeley tạo ISA mở
- **Những năm 2020**: RISC-V đạt được sức hút — mở, không có phí cấp phép
- Được sử dụng trong: hệ thống nhúng, chip tùy chỉnh, bộ đẩy bán dẫn của Trung Quốc
## Tiến hóa cú pháp
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

## Tiến hóa tập lệnh
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

## Nguyên tắc thiết kế chính
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

## Tăng trưởng hệ sinh thái
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
