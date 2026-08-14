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
# Montaż — Przewodnik po ekosystemie i narzędziach
W tym przewodniku opisano podstawowe narzędzia, asemblery i infrastrukturę w ekosystemie Assembly.
---

## Asemblery według architektury
### x86/x86-64
| Asembler | Platforma | Notatki |
|----------|-----|-------|
| **NASM** | Wieloplatformowe | Najpopularniejsza, czysta składnia |
| **MASM** | Okna | Asembler makr firmy Microsoft |
| **FASM** | Wieloplatformowe | Hosting własny, szybki |
| **GAZ (jako)** | Linux/Unix | Asembler GNU (składnia AT&T) |
| **YASM** | Wieloplatformowe | Kompatybilny z NASM |
| **UASM** | Wieloplatformowe | Kompatybilny z MASM |
### RAMIĘ
| Asembler | Platforma | Notatki |
|----------|-----|-------|
| **GNU jako (ARM)** | Wieloplatformowe | Zespół ramienia |
| **Keil ASM** | Wbudowany | Rozwój ARM |
| **Asembler ARM** | RAMIĘ | Pakiet kompilatorów ARM |
### Inny
| Asembler | Architektura | Notatki |
|----------|------------|-------|
| **avr-as** | AVR | Mikrokontrolery |
| **rasizm** | Z80 | Komputery retro |
| **ca65** | 6502 | NES-a, Commodore |
| **SPIM / MARS** | MIPS | Edukacyjne |
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

## Debugery
| Narzędzie | Architektura | Cel |
|------|------------|--------|
| **GDB** | x86/ARM | Debuger GNU |
| **lldb** | Wieloplatformowe | Debuger LLVM |
| **x64dbg** | x86/x86-64 | Debuger GUI systemu Windows |
| **OllyDbg** | x86 | Klasyczny debuger systemu Windows |
| **IDA Pro** | Wieloplatformowe | Dezasembler/dekompilator |
| **Ghidra** | Wieloplatformowe | Inżynieria odwrotna NSA |
| **radare2** | Wieloplatformowe | Inżynieria odwrotna CLI |
| **Nóż** | Wieloplatformowe | GUI dla Radare2 |
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

## Emulatory i symulatory
| Narzędzie | Architektura | Cel |
|------|------------|--------|
| **QEMU** | Wielołukowe | Pełna emulacja systemu |
| **Bochs** | x86 | emulator x86 |
| **DOSBox** | x86 | Środowisko DOS |
| **MAMO** | Wielu | Emulacja zręcznościowa/retro |
| **SPIM** | MIPS | Symulator MIPS |
| **MARS** | MIPS | MIPS IDE/symulator |
| **SimAVR** | AVR | Symulator AVR |
| **jednorożec** | Wielołukowe | Struktura emulacji procesora |
---

## Narzędzia do tworzenia
| Narzędzie | Cel |
|------|-------------|
| **Zrób** | Klasyczna automatyzacja kompilacji |
| **CMrób** | Kompilacje międzyplatformowe |
| **ld** | Linker GNU |
| **lld** | Linker LLVM |
| **kopia obj** | Manipulacja binarna |
| **zrzut obj** | Demontaż |
| **readelf / nm** | Kontrola symboli |
| **zrzut heksowy** | Kontrola binarna |
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

## Kluczowe biblioteki
| Biblioteka | Architektura | Cel |
|--------|-------------|--------|
| **libc** | x86/ARM | Standardowa biblioteka C (opakowanie syscall) |
| **Wywołania systemowe Linuksa** | x86/ARM | Bezpośrednie wywołania jądra |
| **API systemu Windows** | x86/x64 | API Win32/64 |
| **BIOS przerywa** | x86 | Starszy BIOS komputera |
| **DOS przerywa** | x86 | Usługi DOS-owe |
| **libgcc** | Wieloplatformowe | Środowisko wykonawcze GCC |
| **nowa biblioteka** | Wbudowany | Lekka biblioteka |
---

## Testowanie
| Narzędzie | Cel |
|------|-------------|
| **Niestandardowa uprząż testowa** | Ramy testów montażu |
| **Jedność** | Testowanie jednostkowe w języku C (dla projektów mieszanych) |
| **Test Google** | Testowanie C++ (dla projektów mieszanych) |
| **Niestandardowe makra** | Makra asercji |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **objdump -d** | Kontrola demontażu |
| **Ghidra** | Analiza inżynierii odwrotnej |
| **IDA Pro** | Profesjonalny demontaż |
| **radare2** | Analiza CLI |
| **Valgrind** | Wykrywanie błędów pamięci |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + NASM** | Podświetlanie składni zestawu |
| **SASM** | Proste ASM IDE (edukacyjne) |
| **Emacs + tryb nasm** | Klasyczna edycja złożenia |
| **MARS** | Edukacyjne IDE MIPS |
| **DOSBox + edycja** | Rozwój retro |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Statyczny plik binarny** | Bezpośredni kod maszynowy |
| **Sektor rozruchowy** | Program rozruchowy 512-bajtowy |
| **Moduł jądra** | Kod jądra systemu operacyjnego |
| **Oprogramowanie sprzętowe** | Wbudowane oprogramowanie |
| **ROM/Flash** | Kod mikrokontrolera |
| **Doker** | Zbuduj środowisko |
---

## Streszczenie
Ekosystem Assembly jest specyficzny dla architektury i minimalistyczny z założenia. Standardowy zestaw narzędzi to: **NASM** (x86/x86-64) lub **GNU as** (ARM) do montażu, **ld** do łączenia, **GDB** do debugowania, **Ghidra** lub **IDA Pro** do inżynierii wstecznej i **QEMU** do emulacji. Assembly specjalizuje się w opracowywaniu systemów operacyjnych, systemów wbudowanych, inżynierii wstecznej, kodzie krytycznym dla wydajności i opracowywaniu programu ładującego. Ekosystem jest niezbędny do zrozumienia, jak działają komputery na najniższym poziomie. Do nauki **MARS** (MIPS) i **SASM** (x86) zapewniają środowiska przyjazne dla początkujących.