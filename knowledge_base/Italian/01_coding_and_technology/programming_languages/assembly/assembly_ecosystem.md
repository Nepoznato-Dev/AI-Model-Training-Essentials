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
# Assemblaggio: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, gli assemblatori e l'infrastruttura essenziali nell'ecosistema Assembly.
---

## Assemblatori per Architettura
###x86/x86-64
| Assemblatore | Piattaforma | Note |
|-----------|----------|-------|
| **NASM** | Multipiattaforma | Sintassi più popolare e pulita |
| **MASM** | Finestre | Assemblatore di macro Microsoft |
| **FASM** | Multipiattaforma | Hosting autonomo, veloce |
| **GAS (come)** | Linux/Unix | Assemblatore GNU (sintassi AT&T) |
| **YASM** | Multipiattaforma | Compatibile con NASM |
| **UASM** | Multipiattaforma | Compatibile con MASM |
### BRACCIO
| Assemblatore | Piattaforma | Note |
|-----------|----------|-------|
| **GNU come (ARM)** | Multipiattaforma | Assemblaggio BRACCIO |
| **KeilASM** | Incorporato | Sviluppo ARM |
| **Assemblatore ARM** | BRACCIO | Suite di compilazione ARM |
### Altro
| Assemblatore | Architettura | Note |
|-----------|-------------|-------|
| **avr-as** | AVR | Microcontrollori |
| **rasma** | Z80| Informatica retrò |
| **ca65** | 6502| NES, Commodoro |
| **SPIM/MARTE** | MIPS | Educativo |
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
| Strumento | Architettura | Scopo |
|------|-------------|---------|
| **GDB** | x86/BRACCIO | Debugger GNU |
| **lldb** | Multipiattaforma | Debugger LLVM |
| **x64dbg** | x86/x86-64 | Debugger della GUI di Windows |
| **OllyDbg** | x86 | Debugger classico di Windows |
| **IDA Pro** | Multipiattaforma | Disassemblatore/decompilatore |
| **Ghidra** | Multipiattaforma | Ingegneria inversa della NSA |
| **radare2** | Multipiattaforma | Ingegneria inversa CLI |
| **Taglierina** | Multipiattaforma | GUI per radare2 |
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

## Emulatori e simulatori
| Strumento | Architettura | Scopo |
|------|-------------|---------|
| **QEMU** | Multiarco | Emulazione completa del sistema |
| **Boch** | x86 | Emulatore x86 |
| **DOSBox** | x86 | Ambiente DOS |
| **MAME** | Multi | Emulazione arcade/retrò |
| **SPIM** | MIPS | Simulatore MIPS |
| **MARTE** | MIPS | IDE/simulatore MIPS |
| **SimAVR** | AVR | Simulatore AVR |
| **unicorno** | Multiarco | Framework di emulazione CPU |
---

## Strumenti di creazione
| Strumento | Scopo |
|------|---------|
| **Fai** | Automazione di costruzione classica |
| **CMake** | Build multipiattaforma |
| **ld** | Collegamento GNU |
| **lld** | Collegamento LLVM |
| **oggettocopia** | Manipolazione binaria |
| **objdump** | Smontaggio |
| **readif / nm** | Ispezione dei simboli |
| **hexdump** | Ispezione binaria |
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

## Biblioteche chiave
| Biblioteca | Architettura | Scopo |
|---------|-----|---------|
| **libc** | x86/BRACCIO | Libreria C standard (wrapper syscall) |
| **Chiamate di sistema Linux** | x86/BRACCIO | Chiamate dirette del kernel |
| **API di Windows** | x86/x64 | API Win32/64 |
| **Interruzioni del BIOS** | x86 | BIOS del PC precedente |
| **Interruzioni DOS** | x86 | Servizi DOS |
| **libgcc** | Multipiattaforma | Tempo di esecuzione GCC |
| **nuovalib** | Incorporato | Libc leggero |
---

## Test
| Strumento | Scopo |
|------|---------|
| **Cablaggio di prova personalizzato** | Quadro di prova dell'assemblaggio |
| **Unità** | Unit test basati su C (per progetti misti) |
| **Test di Google** | Test C++ (per progetti misti) |
| **Macro personalizzate** | Macro di asserzioni |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **objdump -d** | Ispezione di smontaggio |
| **Ghidra** | Analisi di reverse engineering |
| **IDA Pro** | Smontaggio professionale |
| **radare2** | Analisi CLI |
| **Valgrind** | Rilevamento errori di memoria |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + NASM** | Evidenziazione della sintassi dell'assembly |
| **SASM** | IDE ASM semplice (didattico) |
| **Emacs + modalità nasm** | Modifica di assiemi classici |
| **MARTE** | IDE educativo MIPS |
| **DOSBox + modifica** | Sviluppo retrò |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Binario statico** | Codice macchina diretto |
| **Settore avvio** | Bootloader da 512 byte |
| **Modulo del kernel** | Codice del kernel del sistema operativo |
| **Firmware** | Firmware integrato |
| **ROM/Flash** | Codice microcontrollore |
| **Docker** | Costruisci ambiente |
---

## Riepilogo
L'ecosistema di Assembly è specifico dell'architettura e minimale per progettazione. La toolchain standard è: **NASM** (x86/x86-64) o **GNU as** (ARM) per l'assemblaggio, **ld** per il collegamento, **GDB** per il debug, **Ghidra** o **IDA Pro** per il reverse engineering e **QEMU** per l'emulazione. L'assemblaggio eccelle nello sviluppo di sistemi operativi, sistemi embedded, reverse engineering, codice critico per le prestazioni e sviluppo di bootloader. L'ecosistema è essenziale per comprendere come funzionano i computer al livello più basso. Per l'apprendimento, **MARS** (MIPS) e **SASM** (x86) forniscono ambienti adatti ai principianti.