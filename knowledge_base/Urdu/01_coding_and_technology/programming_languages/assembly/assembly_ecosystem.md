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

# اسمبلی - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ اسمبلی ماحولیاتی نظام میں ضروری ٹولز، اسمبلرز اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## آرکیٹیکچر کے لحاظ سے اسمبلرز
### x86/x86-64
| جمع کرنے والا | پلیٹ فارم | نوٹس |
|------------|---------|---------|
| **NASM** | کراس پلیٹ فارم | سب سے زیادہ مقبول، صاف نحو |
| **MASM** | ونڈوز | مائیکروسافٹ میکرو اسمبلر |
| **FASM** | کراس پلیٹ فارم | خود میزبانی، تیز |
| **GAS (as)** | لینکس/یونکس | GNU اسمبلر (AT&T نحو) |
| **یاسم** | کراس پلیٹ فارم | NASM کے موافق |
| **UASM** | کراس پلیٹ فارم | MASM کے موافق |
### بازو
| جمع کرنے والا | پلیٹ فارم | نوٹس |
|------------|---------|---------|
| **GNU بطور (ARM)** | کراس پلیٹ فارم | اے آر ایم اسمبلی |
| **کیل ASM** | ایمبیڈڈ | بازو کی ترقی |
| **آرم اسمبلر** | ARM | ARM کمپائلر سویٹ |
### دیگر
| جمع کرنے والا | فن تعمیر | نوٹس |
|------------|---------------|---------|
| **avr-as** | اے وی آر | مائیکرو کنٹرولرز |
| **رسم** | Z80 | ریٹرو کمپیوٹنگ |
| **ca65** | 6502 | NES، کموڈور |
| **اسپم / مارس** | MIPS | تعلیمی |
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

## ڈیبگرز
| ٹول | فن تعمیر | مقصد |
|------|---------------|---------|
| **GDB** | x86/ARM | GNU ڈیبگر |
| **lldb** | کراس پلیٹ فارم | LLVM ڈیبگر |
| **x64dbg** | x86/x86-64 | ونڈوز GUI ڈیبگر |
| **OllyDbg** | x86 | کلاسک ونڈوز ڈیبگر |
| **IDA Pro** | کراس پلیٹ فارم | جدا کرنے والا/ڈیکمپائلر |
| **غدرہ** | کراس پلیٹ فارم | NSA ریورس انجینئرنگ |
| **radare2** | کراس پلیٹ فارم | CLI ریورس انجینئرنگ |
| **کٹر** | کراس پلیٹ فارم | GUI for radare2 |
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

## ایمولیٹر اور سمیلیٹر
| ٹول | فن تعمیر | مقصد |
|------|---------------|---------|
| **QEMU** | کثیر محراب | مکمل نظام ایمولیشن |
| **بوچس** | x86 | x86 ایمولیٹر |
| **ڈاسباکس** | x86 | DOS ماحول |
| **MAME** | ملٹی | آرکیڈ/ریٹرو ایمولیشن |
| **SPIM** | MIPS | MIPS سمیلیٹر |
| **مارس** | MIPS | MIPS IDE/simulator |
| **SimAVR** | اے وی آر | اے وی آر سمیلیٹر |
| **ایک تنگاوالا** | کثیر محراب | CPU ایمولیشن فریم ورک |
---

## ٹولز بنائیں
| ٹول | مقصد |
|------|---------|
| **بناؤ** | کلاسک بلڈ آٹومیشن |
| **CMake** | کراس پلیٹ فارم بناتا ہے |
| **ld** | GNU لنکر |
| **lld** | LLVM لنکر |
| **objcopy** | بائنری ہیرا پھیری |
| **objdump** | بے ترکیبی |
| **ریڈیلف / این ایم** | علامت معائنہ |
| **ہیکسڈمپ** | بائنری معائنہ |
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

## کلیدی لائبریریاں
| لائبریری | فن تعمیر | مقصد |
|---------|------------|---------|
| **libc** | x86/ARM | معیاری C لائبریری (syscall wrapper) |
| **Linux syscalls** | x86/ARM | براہ راست کرنل کالز |
| **ونڈوز API** | x86/x64 | Win32/64 API |
| **BIOS رکاوٹیں** | x86 | لیگیسی PC BIOS |
| **DOS رکاوٹیں** | x86 | DOS خدمات |
| **libgcc** | کراس پلیٹ فارم | GCC رن ٹائم |
| **نیولیب** | ایمبیڈڈ | ہلکا پھلکا libc |
---

## ٹیسٹنگ
| ٹول | مقصد |
|------|---------|
| **کسٹم ٹیسٹ ہارنس** | اسمبلی ٹیسٹ فریم ورک |
| **اتحاد** | سی پر مبنی یونٹ ٹیسٹنگ (مخلوط منصوبوں کے لیے) |
| **گوگل ٹیسٹ** | C++ ٹیسٹنگ (مخلوط منصوبوں کے لیے) |
| **حسب ضرورت میکرو** | دعویٰ میکرو |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **objdump -d** | بے ترکیبی معائنہ |
| **غدرہ** | ریورس انجینئرنگ تجزیہ |
| **IDA Pro** | پیشہ ورانہ بے ترکیبی |
| **radare2** | CLI تجزیہ |
| **والگرینڈ** | میموری کی خرابی کا پتہ لگانا |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + NASM** | اسمبلی نحو کو نمایاں کرنا |
| **SASM** | سادہ ASM IDE (تعلیمی) |
| **Emacs + nasm-mode** | کلاسک اسمبلی ایڈیٹنگ |
| **مارس** | MIPS تعلیمی IDE |
| **DOSBox + ترمیم** | ریٹرو ترقی |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **جامد بائنری** | براہ راست مشین کوڈ |
| **بوٹ سیکٹر** | 512 بائٹ بوٹ لوڈر |
| **کرنل ماڈیول** | OS کرنل کوڈ |
| **فرم ویئر** | ایمبیڈڈ فرم ویئر |
| **ROM/Flash** | مائیکرو کنٹرولر کوڈ |
| **ڈوکر** | ماحول بنائیں |
---

## خلاصہ
اسمبلی کا ماحولیاتی نظام فن تعمیر سے مخصوص اور ڈیزائن کے لحاظ سے کم سے کم ہے۔ معیاری ٹول چین ہے: **NASM** (x86/x86-64) یا **GNU as** (ARM) اسمبلی کے لیے، **ld** لنک کرنے کے لیے، **GDB** ڈیبگنگ کے لیے، **Ghidra** یا **IDA Pro** ریورس انجینئرنگ کے لیے، اور **QEMU** ایمولیشن کے لیے۔ آپریٹنگ سسٹم ڈویلپمنٹ، ایمبیڈڈ سسٹمز، ریورس انجینئرنگ، پرفارمنس کرٹیکل کوڈ، اور بوٹ لوڈر ڈویلپمنٹ میں اسمبلی کو سبقت حاصل ہے۔ یہ سمجھنے کے لیے ماحولیاتی نظام ضروری ہے کہ کمپیوٹر کس طرح نچلی سطح پر کام کرتے ہیں۔ سیکھنے کے لیے، **MARS** (MIPS) اور **SASM** (x86) ابتدائی طور پر دوستانہ ماحول فراہم کرتے ہیں۔