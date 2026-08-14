<!--
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

-->
# সমাবেশের ভাষা — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| যুগ | বছর | মূল থিম |
|------|------|------------|
| 1940 | 1945 | মেশিন কোড — টগল সুইচ, কাগজ টেপ |
| 1949 | 1949 | **প্রথম সংযোজনকারী** (উইলকস, হুইলার, গিল — EDSAC) |
| 1950 এর দশক | 1951 | গ্রেস হপারের A-0 — প্রথম "কম্পাইলার" (ম্যাক্রো অ্যাসেম্বলার) |
| 1957 | 1957 | IBM 650 এর জন্য SOAP (সিম্বলিক অপ্টিমাল অ্যাসেম্বলি প্রোগ্রাম) |
| 1960 | 1960 | IBM System/360 এর জন্য BAL (বেসিক অ্যাসেম্বলি ল্যাঙ্গুয়েজ) |
| 1978 | 1978 | **Intel 8086** — x86 আর্কিটেকচারের জন্ম |
| 1980 | 1981 | IBM PC — x86 সমাবেশ PC প্রোগ্রামিংকে প্রাধান্য দেয় |
| 1985 | 1985 | **Intel 386** — 32-বিট x86, সুরক্ষিত মোড |
| 1993 | 1993 | **ইন্টেল পেন্টিয়াম** — সুপারস্কলার, MMX পরে |
| 1997 | 1997 | MMX নির্দেশাবলী (মাল্টিমিডিয়া) |
| 1999 | 1999 | SSE (স্ট্রিমিং SIMD এক্সটেনশন) |
| 2000 | 2000 | **AMD64** — 64-বিট x86 এক্সটেনশন |
| 2001 | 2001 | **ARM** মোবাইলের আধিপত্য অর্জন করে |
| 2005 | 2005 | SSE3, ডুয়াল-কোর প্রসেসর |
| 2006 | 2006 | **x86-64** — 64-বিট স্ট্যান্ডার্ড হয়ে যায় |
| 2011 | 2011 | **AVX** (উন্নত ভেক্টর এক্সটেনশন) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-বিট ARM |
| 2017 | 2017 | **AVX-512** — 512-বিট ভেক্টর অপারেশন |
| 2020 | 2020 | **Apple M1** — ARM64 ডেস্কটপে |
| 2023 | 2023 | **AVX-VNNI** — AI/ML ত্বরণ |
| 2024 | 2024 | **RISC-V** ট্র্যাকশন লাভ করে — ওপেন ISA |
## প্রধান মাইলফলক
### মেশিন কোড যুগ (1940-1950)
- **1945**: ENIAC প্লাগ বোর্ড এবং সুইচের মাধ্যমে প্রোগ্রাম করা হয়েছে
- **1949**: EDSAC — প্রথম সঞ্চিত-প্রোগ্রাম কম্পিউটার; প্রথম "সংযোজনকারী" (প্রাথমিক আদেশ)
- **1951**: গ্রেস হপারের A-0 — মেশিন কোডে গাণিতিক স্বরলিপি অনুবাদ করে
- **1957**: SOAP — প্রথম ব্যাপকভাবে ব্যবহৃত সিম্বলিক অ্যাসেম্বলার (IBM 650)
### x86 সমাবেশ (1978-বর্তমান)
- **1978**: ইন্টেল 8086 — x86 আর্কিটেকচারের জন্ম
  - 16-বিট রেজিস্টার: AX, BX, CX, DX, SI, DI, SP, BP
  - সেগমেন্টেড মেমরি: CS, DS, SS, ES
  - নির্দেশাবলী: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: ইন্টেল 386 — 32-বিট x86 (IA-32)
  - 32-বিট রেজিস্টার: EAX, EBX, ECX, EDX
  - সুরক্ষিত মোড, পেজিং, ভার্চুয়াল মেমরি
- **2000**: AMD64 — 64-বিট x86 এক্সটেনশন
  - 64-বিট রেজিস্টার: RAX, RBX, RCX, RDX
  - 16টি সাধারণ-উদ্দেশ্য রেজিস্টার (32-বিটের মধ্যে 8 বনাম)
  - আরআইপি-সম্পর্কিত ঠিকানা
### ARM সমাবেশ (1985-বর্তমান)
- **1985**: ARM1 — অ্যাকর্ন কম্পিউটারস (ইউকে)
  - RISC দর্শন: সহজ, নির্দিষ্ট দৈর্ঘ্য নির্দেশাবলী
  - লোড/স্টোর আর্কিটেকচার
  - 16টি রেজিস্টার (R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64 (AArch64) — 64-বিট ARM
  - 31টি সাধারণ-উদ্দেশ্য 64-বিট রেজিস্টার
  - সিমড: নিওন, এসভিই
  - এতে ব্যবহৃত হয়: স্মার্টফোন, অ্যাপল সিলিকন, AWS Graviton
### RISC-V (2010-বর্তমান)
- **2010**: UC বার্কলে ওপেন ISA তৈরি করেছে
- **2020s**: RISC-V ট্র্যাকশন লাভ করে — খোলা, লাইসেন্সিং ফি নেই
- এতে ব্যবহৃত হয়: এমবেডেড সিস্টেম, কাস্টম চিপ, চীনের সেমিকন্ডাক্টর পুশ
## সিনট্যাক্স বিবর্তন
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

## নির্দেশনা সেট বিবর্তন
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

## মূল ডিজাইনের নীতি
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

## ইকোসিস্টেম বৃদ্ধি
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
