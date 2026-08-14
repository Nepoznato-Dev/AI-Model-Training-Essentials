---
# Metadata
title: "Assembly — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Assembly ecosystem including assemblers, debuggers, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [assembly, ecosystem, tooling, assemblers, debuggers, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# アセンブリ — エコシステムとツールのガイド
このガイドでは、アセンブリ エコシステムの重要なツール、アセンブラ、インフラストラクチャについて説明します。
---

## アーキテクチャ別のアセンブラー
### x86/x86-64
|アセンブラ |プラットフォーム |メモ |
|----------|----------|----------|
| **NASM** |クロスプラットフォーム |最も人気のある、クリーンな構文 |
| **マズム** |ウィンドウズ | Microsoft マクロ アセンブラ |
| **ファズム** |クロスプラットフォーム |セルフホスティング、高速 |
| **ガス (として)** | Linux/Unix | GNU アセンブラ (AT&T 構文) |
| **ヤズム** |クロスプラットフォーム | NASM対応 |
| **UASM** |クロスプラットフォーム | MASM対応 |
### アーム
|アセンブラ |プラットフォーム |メモ |
|----------|----------|----------|
| **GNU として (ARM)** |クロスプラットフォーム | ARM アセンブリ |
| **ケイル ASM** |埋め込み | ARM開発 |
| **ARM アセンブラ** |アーム | ARM コンパイラ スイート |
＃＃＃ 他の
|アセンブラ |建築 |メモ |
|----------|---------------|----------|
| **avr-as** | AVR |マイクロコントローラー |
| **ラスム** | Z80 |レトロコンピューティング |
| **ca65** | 6502 | NES、コモドール |
| **スピム / マーズ** | MIPS |教育 |
```bash
# NASM (Linux x86-64)
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello

# NASM (Windows)
nasm -f win64 hello.asm -o hello.obj
golink /console /entry _start hello.obj

# FASM
fasm hello.asm hello

# GAS (AT&T syntax)
as -o hello.o hello.s
ld hello.o -o hello
```

---

## デバッガー
|ツール |建築 |目的 |
|------|-------------|----------|
| **GDB** | x86/ARM | GNU デバッガ |
| **lldb** |クロスプラットフォーム | LLVM デバッガ |
| **x64dbg** | x86/x86-64 | Windows GUI デバッガ |
| **OllyDbg** | x86 |クラシック Windows デバッガー |
| **IDA プロ** |クロスプラットフォーム |逆アセンブラ/逆コンパイラ |
| **ギドラ** |クロスプラットフォーム | NSA リバースエンジニアリング |
| **レーダー2** |クロスプラットフォーム | CLI リバースエンジニアリング |
| **カッター** |クロスプラットフォーム |レーダー2のGUI |
```bash
# GDB
gdb ./hello
(gdb) break main
(gdb) run
(gdb) info registers
(gdb) stepi
(gdb) x/10i $rip        # disassemble 10 instructions

# x64dbg (Windows)
# GUI-based, load executable, set breakpoints, step through
```

---

## エミュレータとシミュレータ
|ツール |建築 |目的 |
|------|-------------|----------|
| **QEMU** |マルチアーチ |フルシステムエミュレーション |
| **ボックス** | x86 | x86エミュレータ |
| **DOSボックス** | x86 | DOS環境 |
| **まめ** |マルチ |アーケード/レトロエミュレーション |
| **スピム** | MIPS | MIPSシミュレーター |
| **マース** | MIPS | MIPS IDE/シミュレーター |
| **SimAVR** | AVR | AVRシミュレーター |
| **ユニコーン** |マルチアーチ | CPU エミュレーション フレームワーク |
---

## ビルドツール
|ツール |目的 |
|-----|----------|
| **作る** |クラシックなビルド自動化 |
| **CMake** |クロスプラットフォーム ビルド |
| **ld** | GNU リンカー |
| **lld** | LLVMリンカー |
| **オブジェクトコピー** |バイナリ操作 |
| **objdump** |分解 |
| **readelf / nm** |シンボル検査 |
| **16 進ダンプ** |バイナリ検査 |
```makefile
# Makefile for NASM project
ASM = nasm
ASM_FLAGS = -f elf64
LD = ld
TARGET = hello

all: $(TARGET)

$(TARGET): hello.o
	$(LD) hello.o -o $(TARGET)

hello.o: hello.asm
	$(ASM) $(ASM_FLAGS) hello.asm -o hello.o

clean:
	rm -f *.o $(TARGET)
```

---

## 主要なライブラリ
|図書館 |建築 |目的 |
|----------|---------------|----------|
| **libc** | x86/ARM |標準 C ライブラリ (syscall ラッパー) |
| **Linux システムコール** | x86/ARM |カーネルの直接呼び出し |
| **Windows API** | x86/x64 | Win32/64 API |
| **BIOS 割り込み** | x86 |レガシー PC BIOS |
| **DOS 割り込み** | x86 | DOS サービス |
| **libgcc** |クロスプラットフォーム | GCC ランタイム |
| **新しいライブラリ** |埋め込み |軽量libc |
---

## テスト
|ツール |目的 |
|-----|----------|
| **カスタム テスト ハーネス** |アセンブリテストフレームワーク |
| **団結** | C ベースの単体テスト (混合プロジェクト用) |
| **Google テスト** | C++ テスト (混合プロジェクト用) |
| **カスタム マクロ** |アサーション マクロ |
```nasm
; NASM test example
section .data
    test_pass db "PASS", 10, 0
    test_fail db "FAIL", 10, 0

section .text
    global _start

test_add:
    mov rax, 2
    mov rbx, 3
    add rax, rbx
    cmp rax, 5
    jne .fail
    ; print pass
    mov rax, 1
    mov rdi, 1
    mov rsi, test_pass
    mov rdx, 5
    syscall
    ret
.fail:
    mov rax, 1
    mov rdi, 1
    mov rsi, test_fail
    mov rdx, 5
    syscall
    ret

_start:
    call test_add
    mov rax, 60
    xor rdi, rdi
    syscall
```

---

## コードの品質
|ツール |目的 |
|-----|----------|
| **objdump -d** |分解検査 |
| **ギドラ** |リバースエンジニアリング分析 |
| **IDA プロ** |プロの分解 |
| **レーダー2** | CLI 分析 |
| **ヴァルグリンド** |メモリエラー検出 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + NASM** |アセンブリ構文の強調表示 |
| **SASM** |シンプルな ASM IDE (教育用) |
| **Emacs + nasm モード** |クラシックなアセンブリ編集 |
| **マース** | MIPS 教育用 IDE |
| **DOSBox + 編集** |レトロな開発 |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **静的バイナリ** |ダイレクトマシンコード |
| **ブート セクター** | 512 バイトのブートローダー |
| **カーネルモジュール** | OS カーネル コード |
| **ファームウェア** |組み込みファームウェア |
| **ROM/フラッシュ** |マイクロコントローラーコード |
| **ドッカー** |構築環境 |
---

＃＃ まとめ
Assembly のエコシステムはアーキテクチャに特化しており、最小限の設計となっています。標準ツールチェーンは、アセンブリ用の **NASM** (x86/x86-64) または **GNU as** (ARM)、リンク用の **ld**、デバッグ用の **GDB**、リバース エンジニアリング用の **Ghidra** または **IDA Pro**、エミュレーション用の **QEMU** です。 Assembly は、オペレーティング システム開発、組み込みシステム、リバース エンジニアリング、パフォーマンスが重要なコード、ブートローダー開発を得意としています。エコシステムは、コンピューターが最低レベルでどのように動作するかを理解するために不可欠です。学習には、**MARS** (MIPS) と **SASM** (x86) が初心者に優しい環境を提供します。