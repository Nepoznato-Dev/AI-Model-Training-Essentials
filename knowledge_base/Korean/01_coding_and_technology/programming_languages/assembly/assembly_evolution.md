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

# 어셈블리 언어 — 버전 기록 및 진화
## 타임라인
| 시대 | 연도 | 주요 테마 |
|------|------|------------|
| 1940년대 | 1945년 | 기계 코드 - 토글 스위치, 종이 테이프 |
| 1949년 | 1949년 | **최초의 어셈블러**(Wilkes, Wheeler, Gill — EDSAC) |
| 1950년대 | 1951 | Grace Hopper의 A-0 — 최초의 "컴파일러"(매크로 어셈블러) |
| 1957 | 1957 | IBM 650용 SOAP(Symbolic Optimal Assembly Program) |
| 1960년대 | 1960 | IBM System/360용 BAL(기본 어셈블리 언어) |
| 1978 | 1978 | **인텔 8086** — x86 아키텍처 탄생 |
| 1980년대 | 1981 | IBM PC - x86 어셈블리가 PC 프로그래밍을 지배 |
| 1985 | 1985 | **Intel 386** — 32비트 x86, 보호 모드 |
| 1993년 | 1993년 | **Intel Pentium** — 수퍼스칼라, MMX 이후 버전 |
| 1997 | 1997 | MMX 명령어(멀티미디어) |
| 1999 | 1999 | SSE(스트리밍 SIMD 확장) |
| 2000 | 2000 | **AMD64** — 64비트 x86 확장 |
| 2001 | 2001 | **ARM**, 모바일 지배력 확보 |
| 2005년 | 2005년 | SSE3, 듀얼 코어 프로세서 |
| 2006년 | 2006년 | **x86-64** — 64비트가 표준이 됩니다 |
| 2011 | 2011 | **AVX**(고급 벡터 확장) |
| 2013 | 2013 | **ARM64(AArch64)** — 64비트 ARM |
| 2017 | 2017 | **AVX-512** — 512비트 벡터 연산 |
| 2020 | 2020 | **Apple M1** — 데스크탑의 ARM64 |
| 2023년 | 2023년 | **AVX-VNNI** — AI/ML 가속 |
| 2024 | 2024 | **RISC-V** 인기 상승 - ISA 공개 |
## 주요 이정표
### 기계 코드 시대(1940년대~1950년대)
- **1945**: 플러그 보드 및 스위치를 통해 프로그래밍된 ENIAC
- **1949**: EDSAC — 최초의 저장 프로그램 컴퓨터; 최초의 "어셈블러"(초기 주문)
- **1951**: Grace Hopper의 A-0 — 수학적 표기법을 기계어 코드로 변환
- **1957**: SOAP — 최초로 널리 사용되는 기호 어셈블러(IBM 650)
### x86 조립(1978~현재)
- **1978**: Intel 8086 — x86 아키텍처 탄생
  - 16비트 레지스터: AX, BX, CX, DX, SI, DI, SP, BP
  - 세그먼트 메모리: CS, DS, SS, ES
  - 명령: MOV, ADD, SUB, JMP, CALL, RET, INT
- **1985**: Intel 386 — 32비트 x86(IA-32)
  - 32비트 레지스터: EAX, EBX, ECX, EDX
  - 보호 모드, 페이징, 가상 메모리
- **2000**: AMD64 — 64비트 x86 확장
  - 64비트 레지스터: RAX, RBX, RCX, RDX
  - 16개의 범용 레지스터(32비트에서는 8개)
  - RIP 상대 주소 지정
### ARM 조립(1985~현재)
- **1985**: ARM1 — Acorn Computers(영국)
  - RISC 철학: 단순하고 고정된 길이의 명령어
  - 로드/스토어 아키텍처
  - 16개 레지스터(R0-R15), R13=SP, R14=LR, R15=PC
- **2013**: ARM64(AArch64) — 64비트 ARM
  - 31개의 범용 64비트 레지스터
  - SIMD: 네온, SVE
  - 사용 대상: 스마트폰, Apple Silicon, AWS Graviton
### RISC-V(2010~현재)
- **2010년**: UC Berkeley가 개방형 ISA를 만들었습니다.
- **2020년대**: RISC-V 인기 상승 - 개방형, 라이선스 비용 없음
- 사용 분야: 임베디드 시스템, 맞춤형 칩, 중국 반도체 푸시
## 구문 진화
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

## 명령어 세트의 진화
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

## 주요 디자인 원칙
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

## 생태계 성장
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
