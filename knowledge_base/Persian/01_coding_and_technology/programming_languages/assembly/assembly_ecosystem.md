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
# مونتاژ - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، اسمبلرها و زیرساخت های ضروری در اکوسیستم اسمبلی را پوشش می دهد.
---

## اسمبلرها توسط معماری
### x86/x86-64
| مونتاژ کننده | پلت فرم | یادداشت ها |
|-----------|----------|-------|
| **NASM** | کراس پلتفرم | محبوب ترین، نحو تمیز |
| **MASM** | ویندوز | ماکرو اسمبلر مایکروسافت |
| **FASM** | کراس پلتفرم | میزبانی خود، سریع |
| **گاز (عج)** | لینوکس/یونیکس | اسمبلر گنو (سینتکس AT&T) |
| **YASM** | کراس پلتفرم | سازگار با NASM |
| **UASM** | کراس پلتفرم | سازگار با MASM |
### ARM
| مونتاژ کننده | پلت فرم | یادداشت ها |
|-----------|----------|-------|
| **گنو به عنوان (ARM)** | کراس پلتفرم | مونتاژ ARM |
| **Keil ASM** | تعبیه شده | توسعه ARM |
| **آرم اسمبلر** | ARM | مجموعه کامپایلر ARM |
### دیگر
| مونتاژ کننده | معماری | یادداشت ها |
|-----------|-------------|-------|
| **اورعاس** | AVR | میکروکنترلر |
| **راسم** | Z80 | محاسبات یکپارچهسازی با سیستمعامل |
| **ca65** | 6502 | NES، Commodore |
| **SPIM / مریخ ** | MIPS | آموزشی |
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

## اشکال زدا
| ابزار | معماری | هدف |
|------|-------------|---------|
| **GDB** | x86/ARM | دیباگر گنو |
| **lldb** | کراس پلتفرم | دیباگر LLVM |
| **x64dbg** | x86/x86-64 | دیباگر رابط کاربری گرافیکی ویندوز |
| **OllyDbg** | x86 | دیباگر کلاسیک ویندوز |
| **IDA Pro** | کراس پلتفرم | جداساز/دکامپایلر |
| **قیدرا** | کراس پلتفرم | مهندسی معکوس NSA |
| **radare2** | کراس پلتفرم | مهندسی معکوس CLI |
| **کاتر** | کراس پلتفرم | رابط کاربری گرافیکی برای radare2 |
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

## شبیه سازها و شبیه سازها
| ابزار | معماری | هدف |
|------|-------------|---------|
| **QEMU** | چند قوس | شبیه سازی کامل سیستم |
| **بوچس** | x86 | شبیه ساز x86 |
| **DOSBox** | x86 | محیط DOS |
| **MAME** | چند | شبیه سازی آرکید/رترو |
| **SPIM** | MIPS | شبیه ساز MIPS |
| **مارس** | MIPS | MIPS IDE/شبیه ساز |
| **SimAVR** | AVR | شبیه ساز AVR |
| **تک شاخ** | چند قوس | چارچوب شبیه سازی CPU |
---

## ابزارهای ساخت
| ابزار | هدف |
|------|---------|
| **ساخت ** | اتوماسیون ساخت کلاسیک |
| **CMake** | ساخت های کراس پلتفرم |
| **ld** | پیوند دهنده گنو |
| **lld** | لینکر LLVM |
| **objcopy** | دستکاری باینری |
| **objdump** | جداسازی قطعات |
| **readelf / nm** | بازرسی نماد |
| **hexdump** | بازرسی باینری |
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

## کتابخانه های کلیدی
| کتابخانه | معماری | هدف |
|---------|-------------|---------|
| **libc** | x86/ARM | کتابخانه استاندارد C (syscall wrapper) |
| **سیستم های لینوکس** | x86/ARM | فراخوانی مستقیم هسته |
| **ویندوز API** | x86/x64 | Win32/64 API |
| **قطعات BIOS** | x86 | بایوس PC قدیمی |
| **قطعات DOS** | x86 | خدمات DOS |
| **libgcc** | کراس پلتفرم | زمان اجرا GCC |
| **newlib** | تعبیه شده | سبک وزن libc |
---

## تست
| ابزار | هدف |
|------|---------|
| ** مهار تست سفارشی ** | چارچوب تست اسمبلی |
| **وحدت** | تست واحد مبتنی بر C (برای پروژه های مختلط) |
| **تست گوگل** | تست ++C (برای پروژه های ترکیبی) |
| **ماکروهای سفارشی** | ماکروهای ادعا |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **objdump -d** | بازرسی جداسازی قطعات |
| **قیدرا** | تحلیل مهندسی معکوس |
| **IDA Pro** | دمونتاژ حرفه ای |
| **radare2** | تجزیه و تحلیل CLI |
| **والگریند** | تشخیص خطای حافظه |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + NASM** | برجسته کردن نحو اسمبلی |
| **SASM** | ساده ASM IDE (آموزشی) |
| **Emacs + nasm-mode** | ویرایش مونتاژ کلاسیک |
| **مارس** | IDE آموزشی MIPS |
| **DOSBox + ویرایش** | توسعه یکپارچهسازی با سیستمعامل |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **باینری استاتیک** | کد مستقیم ماشین |
| **بخش بوت** | بوت لودر 512 بایتی |
| **ماژول هسته** | کد هسته سیستم عامل |
| **سخت افزار** | سیستم عامل تعبیه شده |
| **ROM/Flash** | کد میکروکنترلر |
| **داکر** | محیط ساخت |
---

## خلاصه
اکوسیستم اسمبلی مختص معماری و از نظر طراحی مینیمال است. زنجیره ابزار استاندارد عبارتند از: **NASM** (x86/x86-64) یا **GNU as** (ARM) برای مونتاژ، **ld** برای پیوند، **GDB** برای اشکال زدایی، **Ghidra** یا **IDA Pro** برای مهندسی معکوس، و **QEMU** برای شبیه سازی. اسمبلی در توسعه سیستم عامل، سیستم های جاسازی شده، مهندسی معکوس، کدهای حیاتی عملکرد و توسعه بوت لودر برتری دارد. اکوسیستم برای درک اینکه چگونه کامپیوترها در پایین ترین سطح کار می کنند ضروری است. برای یادگیری، **MARS** (MIPS) و **SASM** (x86) محیط های مبتدی را فراهم می کنند.