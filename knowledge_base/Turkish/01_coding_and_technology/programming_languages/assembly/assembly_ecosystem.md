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

# Montaj — Ekosistem ve Takımlama Kılavuzu
Bu kılavuz, Assembly ekosistemindeki temel araçları, derleyicileri ve altyapıyı kapsar.
---

## Mimariye Göre Montajcılar
### x86/x86-64
| Montajcı | Platformu | Notlar |
|-----------|----------|----------|
| **NASM** | Çapraz platform | En popüler, temiz sözdizimi |
| **MASM** | Windows | Microsoft Makro Birleştirici |
| **FASM** | Çapraz platform | Kendi kendine barındırma, hızlı |
| **GAZ (as)** | Linux/Unix | GNU Birleştirici (AT&T sözdizimi) |
| **YASM** | Çapraz platform | NASM uyumlu |
| **UASM** | Çapraz platform | MASM uyumlu |
### KOL
| Montajcı | Platformu | Notlar |
|-----------|----------|----------|
| **(ARM) olarak GNU** | Çapraz platform | ARM montajı |
| **Keil ASM** | Gömülü | ARM geliştirme |
| **ARM Birleştirici** | KOL | ARM derleyici paketi |
### Diğer
| Montajcı | Mimarlık | Notlar |
|-----------|----------------|-------|
| **avr-as** | AVR | Mikrodenetleyiciler |
| **rasm** | Z80 | Retro bilgi işlem |
| **ca65** | 6502 | NES, Komodor |
| **SPIM / MARS** | MIPS | eğitici |
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

## Hata ayıklayıcılar
| Araç | Mimarlık | Amaç |
|------|-------------|--------|
| **GDB** | x86/ARM | GNU hata ayıklayıcı |
| **lldb** | Çapraz platform | LLVM hata ayıklayıcı |
| **x64dbg** | x86/x86-64 | Windows GUI hata ayıklayıcı |
| **OllyDbg** | x86 | Klasik Windows hata ayıklayıcı |
| **IDA Pro** | Çapraz platform | Ayırıcı/derleyici çözücü |
| **Gıdra** | Çapraz platform | NSA tersine mühendislik |
| **radare2** | Çapraz platform | CLI tersine mühendislik |
| **Kesici** | Çapraz platform | radare2 için GUI |
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

## Emülatörler ve Simülatörler
| Araç | Mimarlık | Amaç |
|------|-------------|--------|
| **QEMU** | Çoklu kemer | Tam sistem emülasyonu |
| **Bochs** | x86 | x86 emülatörü |
| **DOSBox** | x86 | DOS ortamı |
| **MAME** | Çoklu | Atari salonu/retro emülasyonu |
| **SPIM** | MIPS | MIPS simülatörü |
| **MARS** | MIPS | MIPS IDE/simülatör |
| **SimAVR** | AVR | AVR simülatörü |
| **tek boynuzlu at** | Çoklu kemer | CPU emülasyon çerçevesi |
---

## Oluşturma Araçları
| Araç | Amaç |
|------|------------|
| **Yap** | Klasik yapı otomasyonu |
| **CMake** | Platformlar arası yapılar |
| **ld** | GNU bağlayıcı |
| **lld** | LLVM bağlayıcı |
| **nesne kopyası** | İkili manipülasyon |
| **objdump** | Sökme |
| **kendinioku / nm** | Sembol denetimi |
| **onaltılık döküm** | İkili inceleme |
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

## Anahtar Kitaplıklar
| Kütüphane | Mimarlık | Amaç |
|-----------|------------|------------|
| **libc** | x86/ARM | Standart C kitaplığı (sistem çağrısı sarmalayıcı) |
| **Linux sistem çağrıları** | x86/ARM | Doğrudan çekirdek çağrıları |
| **Windows API'si** | x86/x64 | Win32/64 API'si |
| **BIOS kesintileri** | x86 | Eski PC BIOS'u |
| **DOS kesintileri** | x86 | DOS hizmetleri |
| **libgcc** | Çapraz platform | GCC çalışma zamanı |
| **yenilib** | Gömülü | Hafif libc |
---

## Test etme
| Araç | Amaç |
|------|------------|
| **Özel test donanımı** | Montaj test çerçevesi |
| **Birlik** | C tabanlı birim testi (karma projeler için) |
| **Google Testi** | C++ testi (karma projeler için) |
| **Özel makrolar** | Onay makroları |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **objdump -d** | Demontaj muayenesi |
| **Gıdra** | Tersine mühendislik analizi |
| **IDA Pro** | Profesyonel sökme |
| **radare2** | CLI analizi |
| **Valgrind** | Bellek hatası tespiti |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + NASM** | Derleme sözdizimi vurgulama |
| **SASM** | Basit ASM IDE (eğitim amaçlı) |
| **Emacs + nasm modu** | Klasik montaj düzenleme |
| **MARS** | MIPS eğitici IDE |
| **DOSBox + düzenle** | Retro geliştirme |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Statik ikili** | Doğrudan makine kodu |
| **Önyükleme sektörü** | 512 bayt önyükleyici |
| **Çekirdek modülü** | İşletim Sistemi çekirdek kodu |
| **Bellenim** | Gömülü ürün yazılımı |
| **ROM/Flaş** | Mikrodenetleyici kodu |
| **Docker** | Oluşturma ortamı |
---

## Özet
Assembly'nin ekosistemi mimariye özgüdür ve tasarım gereği minimal düzeydedir. Standart araç zinciri şu şekildedir: Montaj için **NASM** (x86/x86-64) veya **GNU as** (ARM), bağlantı için **ld**, hata ayıklama için **GDB**, tersine mühendislik için **Ghidra** veya **IDA Pro** ve öykünme için **QEMU**. Assembly, işletim sistemi geliştirme, gömülü sistemler, tersine mühendislik, performans açısından kritik kod ve önyükleyici geliştirme konularında uzmandır. Ekosistem, bilgisayarların en düşük düzeyde nasıl çalıştığını anlamak için gereklidir. Öğrenme için **MARS** (MIPS) ve **SASM** (x86) yeni başlayanlara uygun ortamlar sağlar.