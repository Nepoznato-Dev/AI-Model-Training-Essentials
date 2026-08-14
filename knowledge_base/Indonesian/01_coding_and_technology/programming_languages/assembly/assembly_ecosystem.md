<!--
---
# Metadata
title: "Assembly — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Assembly ecosystem including assemblers, debuggers, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Perakitan — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, perakit, dan infrastruktur penting dalam ekosistem Majelis.
---

## Assembler berdasarkan Arsitektur
###x86/x86-64
| Perakit | Peron | Catatan |
|-----------|----------|-------|
| **NASM** | Lintas platform | Sintaks paling populer dan bersih |
| **MASM** | jendela | Microsoft Makro Assembler |
| **FASM** | Lintas platform | Hosting mandiri, cepat |
| **GAS (as)** | Linux/Unix | GNU Assembler (sintaks AT&T) |
| **YASM** | Lintas platform | Kompatibel dengan NASM |
| **UASM** | Lintas platform | Kompatibel dengan MASM |
### LENGAN
| Perakit | Peron | Catatan |
|-----------|----------|-------|
| **GNU sebagai (ARM)** | Lintas platform | Perakitan LENGAN |
| **Keil ASM** | Tertanam | Pengembangan ARM |
| **Perakitan ARM** | LENGAN | Rangkaian kompiler ARM |
### Lainnya
| Perakit | Arsitektur | Catatan |
|-----------|-------------|-------|
| **avr-as** | AVR | Mikrokontroler |
| **rasm** | Z80 | Komputasi retro |
| **ca65** | 6502 | NES, Komodor |
| **SPIM / MARS** | MIPS | Pendidikan |
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

## Debugger
| Alat | Arsitektur | Tujuan |
|------|-------------|---------|
| **GDB** | x86/LENGAN | Pendebug GNU |
| **lldb** | Lintas platform | debugger LLVM |
| **x64dbg** | x86/x86-64 | Debugger GUI Windows |
| **OllyDbg** | x86 | Debugger Windows klasik |
| **IDA Pro** | Lintas platform | Pembongkar/dekompiler |
| **Ghidra** | Lintas platform | Rekayasa balik NSA |
| **radar2** | Lintas platform | Rekayasa balik CLI |
| **Pemotong** | Lintas platform | GUI untuk radare2 |
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

## Emulator & Simulator
| Alat | Arsitektur | Tujuan |
|------|-------------|---------|
| **QEMU** | Multi-lengkungan | Emulasi sistem penuh |
| **Boch** | x86 | emulator x86 |
| **Kotak DOS** | x86 | Lingkungan DOS |
| **MAME** | Multi | Emulasi arcade/retro |
| **SPIM** | MIPS | Simulator MIPS |
| **MARS** | MIPS | IDE/simulator MIPS |
| **SimAVR** | AVR | Simulator AVR |
| **unicorn** | Multi-lengkungan | Kerangka kerja emulasi CPU |
---

## Alat Bangun
| Alat | Tujuan |
|------|---------|
| **Buat** | Otomatisasi pembangunan klasik |
| **CMembuat** | Pembuatan lintas platform |
| **ld** | Tautan GNU |
| **lld** | Tautan LLVM |
| **salinan objek** | Manipulasi biner |
| **objdump** | Pembongkaran |
| **baca sendiri / nm** | Inspeksi simbol |
| **hexdump** | Inspeksi biner |
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

## Perpustakaan Utama
| Perpustakaan | Arsitektur | Tujuan |
|---------|-------------|---------|
| **libc** | x86/LENGAN | Pustaka C standar (pembungkus syscall) |
| **Panggilan sistem Linux** | x86/LENGAN | Panggilan kernel langsung |
| **API Windows** | x86/x64 | API Win32/64 |
| **BIOS mengganggu** | x86 | BIOS PC Lama |
| **Interupsi DOS** | x86 | Layanan DOS |
| **libgcc** | Lintas platform | Waktu proses GCC |
| **lib baru** | Tertanam | Libc ringan |
---

## Pengujian
| Alat | Tujuan |
|------|---------|
| **Harnes pengujian khusus** | Kerangka uji perakitan |
| **Persatuan** | Pengujian unit berbasis C (untuk proyek campuran) |
| **Tes Google** | Pengujian C++ (untuk proyek campuran) |
| **Makro khusus** | Makro pernyataan |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **objdump -d** | Inspeksi pembongkaran |
| **Ghidra** | Analisis rekayasa terbalik |
| **IDA Pro** | Pembongkaran profesional |
| **radar2** | Analisis CLI |
| **Valgrind** | Deteksi kesalahan memori |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + NASM** | Penyorotan sintaksis perakitan |
| **SASM** | IDE ASM Sederhana (pendidikan) |
| **Emacs + mode nasm** | Pengeditan perakitan klasik |
| **MARS** | IDE pendidikan MIPS |
| **DOSBox + edit** | Perkembangan retro |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Biner statis** | Kode mesin langsung |
| **Sektor boot** | bootloader 512 byte |
| **Modul kernel** | Kode kernel OS |
| **Firmware** | Firmware tertanam |
| **ROM/Flash** | Kode mikrokontroler |
| **Buruh pelabuhan** | Membangun lingkungan |
---

## Ringkasan
Ekosistem Majelis bersifat spesifik arsitektur dan dirancang minimal. Toolchain standarnya adalah: **NASM** (x86/x86-64) atau **GNU as** (ARM) untuk perakitan, **ld** untuk penautan, **GDB** untuk debugging, **Ghidra** atau **IDA Pro** untuk rekayasa balik, dan **QEMU** untuk emulasi. Perakitan unggul dalam pengembangan sistem operasi, sistem tertanam, rekayasa balik, kode kritis kinerja, dan pengembangan bootloader. Ekosistem sangat penting untuk memahami cara kerja komputer pada tingkat terendah. Untuk pembelajaran, **MARS** (MIPS) dan **SASM** (x86) menyediakan lingkungan yang ramah bagi pemula.