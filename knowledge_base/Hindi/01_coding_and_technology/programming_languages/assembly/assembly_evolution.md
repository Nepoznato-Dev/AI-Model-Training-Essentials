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
# असेंबली भाषा - संस्करण इतिहास और विकास
## समयरेखा
| युग | वर्ष | मुख्य विषय |
|----|------|-----------|
| 1940 का दशक | 1945 | मशीन कोड - टॉगल स्विच, पेपर टेप |
| 1949 | 1949 | **प्रथम असेंबलर** (विल्केस, व्हीलर, गिल - ईडीएसएसी) |
| 1950 का दशक | 1951 | ग्रेस हॉपर का A-0 - पहला "कंपाइलर" (मैक्रो असेंबलर) |
| 1957 | 1957 | IBM 650 के लिए SOAP (प्रतीकात्मक इष्टतम असेंबली प्रोग्राम) |
| 1960 का दशक | 1960 | आईबीएम सिस्टम/360 के लिए बीएएल (बेसिक असेंबली लैंग्वेज) |
| 1978 | 1978 | **इंटेल 8086** — x86 आर्किटेक्चर का जन्म |
| 1980 का दशक | 1981 | आईबीएम पीसी - x86 असेंबली पीसी प्रोग्रामिंग पर हावी है |
| 1985 | 1985 | **इंटेल 386** — 32-बिट x86, सुरक्षित मोड |
| 1993 | 1993 | **इंटेल पेंटियम** - सुपरस्केलर, एमएमएक्स बाद में |
| 1997 | 1997 | एमएमएक्स निर्देश (मल्टीमीडिया) |
| 1999 | 1999 | एसएसई (स्ट्रीमिंग SIMD एक्सटेंशन) |
| 2000 | 2000 | **AMD64** — 64-बिट x86 एक्सटेंशन |
| 2001 | 2001 | **एआरएम** ने मोबाइल प्रभुत्व हासिल किया |
| 2005 | 2005 | SSE3, डुअल-कोर प्रोसेसर |
| 2006 | 2006 | **x86-64** — 64-बिट मानक बन गया |
| 2011 | 2011 | **एवीएक्स** (उन्नत वेक्टर एक्सटेंशन) |
| 2013 | 2013 | **ARM64 (AArch64)** — 64-बिट ARM |
| 2017 | 2017 | **AVX-512** — 512-बिट वेक्टर ऑपरेशन |
| 2020 | 2020 | **Apple M1** — डेस्कटॉप पर ARM64 |
| 2023 | 2023 | **AVX-VNNI** — AI/ML त्वरण |
| 2024 | 2024 | **RISC-V** ने गति पकड़ी - ISA खोलें |
## प्रमुख मील के पत्थर
### मशीन कोड युग (1940-1950)
- **1945**: ENIAC को प्लग बोर्ड और स्विच के माध्यम से प्रोग्राम किया गया
- **1949**: ईडीएसएसी - पहला संग्रहित-प्रोग्राम कंप्यूटर; पहला "असेंबलर" (प्रारंभिक आदेश)
- **1951**: ग्रेस हॉपर का ए-0 - गणितीय संकेतन को मशीन कोड में अनुवादित करता है
- **1957**: SOAP - पहला व्यापक रूप से इस्तेमाल किया जाने वाला प्रतीकात्मक असेंबलर (IBM 650)
### x86 असेंबली (1978-वर्तमान)
- **1978**: इंटेल 8086 — x86 आर्किटेक्चर का जन्म
  - 16-बिट रजिस्टर: एएक्स, बीएक्स, सीएक्स, डीएक्स, एसआई, डीआई, एसपी, बीपी
  - खंडित मेमोरी: सीएस, डीएस, एसएस, ईएस
  - निर्देश: MOV, ADD, SUB, JMP, कॉल, RET, INT
- **1985**: इंटेल 386 — 32-बिट x86 (आईए-32)
  - 32-बिट रजिस्टर: ईएक्स, ईबीएक्स, ईसीएक्स, ईडीएक्स
  - संरक्षित मोड, पेजिंग, वर्चुअल मेमोरी
- **2000**: AMD64 — 64-बिट x86 एक्सटेंशन
  - 64-बिट रजिस्टर: RAX, RBX, RCX, RDX
  - 16 सामान्य प्रयोजन रजिस्टर (बनाम 32-बिट में 8)
  - आरआईपी-सापेक्ष संबोधन
### एआरएम असेंबली (1985-वर्तमान)
- **1985**: एआरएम1 - एकॉर्न कम्प्यूटर्स (यूके)
  - आरआईएससी दर्शन: सरल, निश्चित-लंबाई निर्देश
  - लोड/स्टोर आर्किटेक्चर
  - 16 रजिस्टर (आर0-आर15), आर13=एसपी, आर14=एलआर, आर15=पीसी
- **2013**: ARM64 (AArch64) — 64-बिट ARM
  - 31 सामान्य प्रयोजन 64-बिट रजिस्टर
  - सिमड: नियॉन, एसवीई
  - इसमें उपयोग किया जाता है: स्मार्टफोन, ऐप्पल सिलिकॉन, एडब्ल्यूएस ग्रेविटॉन
### आरआईएससी-वी (2010-वर्तमान)
- **2010**: यूसी बर्कले ने खुला आईएसए बनाया
- **2020**: आरआईएससी-वी ने लोकप्रियता हासिल की - खुला, कोई लाइसेंस शुल्क नहीं
- इसमें उपयोग किया जाता है: एम्बेडेड सिस्टम, कस्टम चिप्स, चीन का सेमीकंडक्टर पुश
## सिंटेक्स इवोल्यूशन
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

## निर्देश सेट विकास
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

## मुख्य डिज़ाइन सिद्धांत
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

## पारिस्थितिकी तंत्र का विकास
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
