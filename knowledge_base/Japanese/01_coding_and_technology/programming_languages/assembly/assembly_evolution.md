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
# アセンブリ言語 — バージョン履歴と進化
## タイムライン
|時代 |年 |主要テーマ |
|-----|------|----------|
| 1940年代 | 1945年 |マシンコード - トグルスイッチ、紙テープ |
| 1949年 | 1949年 | **最初のアセンブラー** (Wilkes、Wheeler、Gill — EDSAC) |
| 1950年代 | 1951年 | Grace Hopper の A-0 — 最初の「コンパイラ」(マクロ アセンブラ) |
| 1957年 | 1957年 | IBM 650 用 SOAP (シンボリック最適アセンブリ プログラム) |
| 1960年代 | 1960年 | IBM System/360 用の BAL (基本アセンブリ言語) |
| 1978年 | 1978年 | **Intel 8086** — x86 アーキテクチャの誕生 |
| 1980年代 | 1981年 | IBM PC — x86 アセンブリが PC プログラミングを支配 |
| 1985年 | 1985年 | **Intel 386** — 32 ビット x86、プロテクト モード |
| 1993年 | 1993年 | **Intel Pentium** — スーパースカラ、MMX 以降 |
| 1997年 | 1997年 | MMX 命令 (マルチメディア) |
| 1999年 | 1999年 | SSE (ストリーミング SIMD 拡張機能) |
| 2000年 | 2000年 | **AMD64** — 64 ビット x86 拡張機能 |
| 2001年 | 2001年 | **ARM** がモバイルの優位性を獲得 |
| 2005年 | 2005年 | SSE3、デュアルコアプロセッサ |
| 2006年 | 2006年 | **x86-64** — 64 ビットが標準になります |
| 2011年 | 2011年 | **AVX** (高度なベクトル拡張機能) |
| 2013年 | 2013年 | **ARM64 (AArch64)** — 64 ビット ARM |
| 2017年 | 2017年 | **AVX-512** — 512 ビットのベクトル演算 |
| 2020年 | 2020年 | **Apple M1** — デスクトップ上の ARM64 |
| 2023年 | 2023年 | **AVX-VNNI** — AI/ML アクセラレーション |
| 2024年 | 2024年 | **RISC-V** が勢いを増す - オープン ISA |
## 主要なマイルストーン
### マシンコード時代 (1940 年代～1950 年代)
- **1945**: プラグボードとスイッチを介してENIACをプログラム
- **1949**: EDSAC — 最初のプログラム内蔵コンピュータ。最初の「アセンブラー」（最初の注文）
- **1951**: グレース・ホッパーの A-0 — 数学表記をマシンコードに変換
- **1957**: SOAP — 最初に広く使用されたシンボリック アセンブラ (IBM 650)
### x86 アセンブリ (1978 ～現在)
- **1978**: Intel 8086 — x86 アーキテクチャ誕生
  - 16ビットレジスタ: AX、BX、CX、DX、SI、DI、SP、BP
  - セグメント化されたメモリ: CS、DS、SS、ES
  - 命令: MOV、ADD、SUB、JMP、CALL、RET、INT
- **1985**: Intel 386 — 32 ビット x86 (IA-32)
  - 32ビットレジスタ: EAX、EBX、ECX、EDX
  - プロテクトモード、ページング、仮想メモリ
- **2000**: AMD64 — 64 ビット x86 拡張
  - 64ビットレジスタ: RAX、RBX、RCX、RDX
  - 16 個の汎用レジスタ (32 ビットでは 8 個)
  - RIP 相対アドレス指定
### ARM アセンブリ (1985 ～現在)
- **1985**: ARM1 — Acorn Computers (英国)
  - RISC 哲学: シンプルな固定長命令
  - ロード/ストアアーキテクチャ
  - 16 レジスタ (R0 ～ R15)、R13=SP、R14=LR、R15=PC
- **2013**: ARM64 (AArch64) — 64 ビット ARM
  - 31個の汎用64ビットレジスタ
  - SIMD: ネオン、SVE
  - 使用用途: スマートフォン、Apple Silicon、AWS Graviton
### RISC-V (2010–現在)
- **2010**: カリフォルニア大学バークレー校がオープン ISA を創設
- **2020年代**: RISC-Vが勢いを増す - オープン、ライセンス料なし
- 使用用途: 組み込みシステム、カスタムチップ、中国の半導体推進
## 構文の進化
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

## 命令セットの進化
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

## 主要な設計原則
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

## エコシステムの成長
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
