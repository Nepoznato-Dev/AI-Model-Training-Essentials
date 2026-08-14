---
# Metadata
title: "Assembly Language"
description: "Comprehensive reference for the Assembly programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [assembly, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Montaj Dili
Assembly dili, insan tarafından okunabilen en düşük seviyeli programlama dilidir. Ham ikili kod yerine anımsatıcı kodları (`MOV`, `ADD`,`JMP`gibi) kullanarak bir bilgisayarın makine kodu talimatlarının doğrudan temsilini sağlar. Her derleme dili belirli bir işlemci mimarisine (x86, ARM, MIPS, RISC-V) özeldir; bir mimari için yazılan kod diğerinde çalışmaz.
Montaj dili uygulamalar oluşturmak için kullanılmaz. Donanım üzerinde mutlak kontrole ihtiyaç duyduğunuzda kullanılır: işletim sistemi çekirdekleri, aygıt sürücüleri, önyükleyiciler, yerleşik donanım yazılımı, performans açısından kritik kod bölümleri yazma, tersine mühendislik ve bilgisayarların talimatları gerçekte nasıl yürüttüğünü anlama.
---

## Montaj Neden Önemlidir
- **Donanımı anlama**: CPU'nun talimat düzeyinde tam olarak ne yaptığını bilmenin tek yolu.
- **Performans ayarlama**: Kritik kod bölümleri, derleyicilerin ürettiğinin ötesinde optimize edilebilir.
- **Tersine mühendislik**: Kötü amaçlı yazılım analizi, güvenlik araştırması ve özel yazılımların anlaşılması.
- **Gömülü sistemler**: Bazı mikro denetleyicilerin üst düzey dil desteği yoktur.
- **İşletim sistemi geliştirme**: Önyükleme kodu, kesme işleyicileri ve içerik değiştirme, derleme gerektirir.
- **Eğitici**: Montajı anlamak size bilgisayarların gerçekte nasıl çalıştığını (bellek, kayıtlar, yığın ve CPU hattı) öğretir.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Son derece düşük düzey** | Her talimat bir makine operasyonuyla eşleşir | Kritik parçalar dışındaki her şey için üst düzey diller kullanın |
| **Mimariye özel** | x86 kodu ARM'de çalışmıyor | Taşınabilir kodu C/C++ dilinde yazın; montajı yalnızca gerektiğinde kullanın |
| **Ayrıntılı** | Basit görevler birçok talimat gerektirir | Makroları kullanın; montaj bölümlerini minimum düzeyde tutun |
| **Taşınabilirlik yok** | Her derleyici için farklı sözdizimi (NASM, GAS, MASM) | Derleyici iç bilgilerini veya satır içi derlemeyi kullanın |
| **Hata ayıklama zorluğu** | Talimat düzeyinde mantığı izlemek zor | Hata ayıklayıcıları (GDB) kullanın; serbestçe yorum ekleyin |
---

## Sözdizimi Örneği (x86-64 Derlemesi — NASM)
```nasm
; A simple program that adds two numbers and exits
section .data
    num1    dd  10          ; 32-bit integer: 10
    num2    dd  20          ; 32-bit integer: 20

section .bss
    result  resd 1          ; Reserve space for result

section .text
    global _start

_start:
    ; Load numbers into registers
    mov     eax, [num1]     ; Move num1 into EAX register
    add     eax, [num2]     ; Add num2 to EAX
    
    ; Store result
    mov     [result], eax   ; Store EAX in result
    
    ; Exit system call (Linux)
    mov     eax, 60         ; syscall number for exit
    mov     edi, 0          ; exit code 0
    syscall                 ; invoke kernel
```

### ARM Montaj Örneği
```arm
; ARM assembly — add two numbers
    .data
num1:   .word 10
num2:   .word 20

    .text
    .global _start

_start:
    LDR R0, =num1       ; Load address of num1 into R0
    LDR R1, [R0]        ; Load value at address into R1
    LDR R2, =num2       ; Load address of num2 into R2
    LDR R3, [R2]        ; Load value at address into R3
    ADD R4, R1, R3      ; R4 = R1 + R3
```

---

## Gelişmiş Sözdizimi ve Desenler
### x86-64 Adresleme Modları
Adresleme modlarını anlamak, verimli derleme yazmak için kritik öneme sahiptir. Her mod, işlenenlerin nasıl konumlandırıldığını kontrol eder.
| Modu | Sözdizimi (NASM) | Açıklama |
|------|---------------|------------|
| **Hemen** | `mov eax, 42`| İşlenen sabit bir değerdir |
| **Kayıt Ol** | `mov eax, ebx`| İşlenen bir kayıt defterinde |
| **Doğrudan** | `mov eax, [0x4000]`| İşlenen sabit bir bellek adresindedir |
| **Dolaylı kayıt olun** | `mov eax, [rbx]`| İşlenen bir kayıt defterindeki adrestedir |
| **Taban + yer değiştirme** | `mov eax, [rbx + 8]`| Adres = kayıt + sabit ofset |
| **Ölçeklendirilmiş dizin** | `mov eax, [rbx + rcx*4]`| Adres = baz + (indeks × ölçek) |
| **Tam SIB** | `mov eax, [rbx + rcx*4 + 16]`| Taban + (indeks × ölçek) + yer değiştirme |
```nasm
; Demonstrating various addressing modes
section .data
    array   dd  10, 20, 30, 40, 50

section .text
    ; Register indirect — traverse an array
    lea     rbx, [array]        ; RBX points to array start
    mov     eax, [rbx]          ; eax = array[0] = 10
    mov     eax, [rbx + 4]     ; eax = array[1] = 20

    ; Scaled index — access array[i] where i is in rcx
    mov     rcx, 2              ; index = 2
    mov     eax, [rbx + rcx*4] ; eax = array[2] = 30

    ; Loop through array with scaled index
    xor     rcx, rcx            ; i = 0
.loop:
    mov     eax, [rbx + rcx*4] ; load array[i]
    add     eax, 1              ; increment value
    mov     [rbx + rcx*4], eax ; store back
    inc     rcx                 ; i++
    cmp     rcx, 5
    jl      .loop               ; continue while i < 5
```

### Makro Sistem (NASM)
Makrolar, parametrelerle yeniden kullanılabilir talimat dizilerini tanımlamanıza olanak tanıyarak montajı daha az tekrarlı hale getirir.
```nasm
; Define a macro to print a string via Linux syscall
%macro print_string 2
    mov     rax, 1              ; syscall: write
    mov     rdi, 1              ; file descriptor: stdout
    mov     rsi, %1             ; address of string
    mov     rdx, %2             ; length of string
    syscall
%endmacro

; Define a macro for function prologue
%macro function_prologue 1
    push    rbp
    mov     rbp, rsp
    sub     rsp, %1             ; allocate local variable space
%endmacro

; Define a macro for function epilogue
%macro function_epilogue 0
    mov     rsp, rbp
    pop     rbp
    ret
%endmacro

section .data
    msg     db  'Hello, Macro!', 10
    msg_len equ $ - msg

section .text
    global _start

_start:
    print_string msg, msg_len

    ; Exit
    mov     rax, 60
    xor     rdi, rdi
    syscall
```

### Yığın Çerçeve Düzeni
Yığın çerçevesini anlamak, işlevleri yazmak ve hata ayıklamak için çok önemlidir.
```
High Address
+------------------+
| Function args    |  (pushed by caller)
+------------------+
| Return address   |  (pushed by CALL instruction)
+------------------+
| Saved RBP        |  <-- RBP points here after prologue
+------------------+
| Local variables  |  <-- RSP points here (grows downward)
|                  |
Low Address
```

```nasm
; Function with stack-allocated local variables
section .text
    global compute_sum

; int compute_sum(int* arr, int count)
; System V AMD64 ABI: rdi = arr, rsi = count
compute_sum:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16             ; 16 bytes for locals

    mov     [rbp - 4], dword 0  ; int sum = 0
    mov     [rbp - 8], dword 0  ; int i = 0

.loop:
    mov     eax, [rbp - 8]      ; load i
    cmp     eax, esi            ; compare i with count
    jge     .done               ; if i >= count, exit loop

    ; sum += arr[i]
    mov     eax, [rbp - 4]                          ; load sum
    mov     ecx, [rbp - 8]                          ; load i
    add     eax, [rdi + rcx*4]                      ; add arr[i]
    mov     [rbp - 4], eax                          ; store sum

    mov     eax, [rbp - 8]
    inc     eax
    mov     [rbp - 8], eax                          ; i++
    jmp     .loop

.done:
    mov     eax, [rbp - 4]      ; return value in EAX
    mov     rsp, rbp
    pop     rbp
    ret
```

---

## Mimari ve Sistem Tasarımı
### Tipik bir x86-64 Linux Sürecinin Bellek Düzeni
```
Address
0x7FFF_FFFF_FFFF  +------------------+
                   | Stack            |  (grows downward)
                   |        ↓         |
                   |                  |
                   |        ↑         |
                   | Heap             |  (grows upward)
                   +------------------+
                   | BSS              |  (uninitialized data)
                   +------------------+
                   | Data             |  (initialized global/static data)
                   +------------------+
                   | Text (Code)      |  (executable instructions)
0x0040_0000        +------------------+
```

### Program Yapısı Kuralı
İyi organize edilmiş bir montaj programı, konuları farklı bölümlere ayırır:
```nasm
; ============================================================
; Program: example.asm
; Description: Demonstrates standard program layout
; Assembler: NASM
; Platform:  Linux x86-64
; ============================================================

; --- Constants ---
section .rodata
    fmt_int     db  "%d", 10, 0     ; printf format for integer
    fmt_str     db  "%s", 0         ; printf format for string
    MAX_SIZE    equ 1024

; --- Initialized data ---
section .data
    greeting    db  "Hello, World!", 0
    numbers     dd  1, 2, 3, 4, 5
    count       dq  5

; --- Uninitialized data ---
section .bss
    buffer      resb MAX_SIZE       ; 1KB buffer
    result      resd 1              ; single 32-bit integer
    temp_array  resd 256            ; 256 integers

; --- Code ---
section .text
    global main
    extern printf

main:
    push    rbp
    mov     rbp, rsp

    ; ... program logic ...

    xor     eax, eax                ; return 0
    mov     rsp, rbp
    pop     rbp
    ret
```

### Tipik Proje Dizin Yapısı
```
project/
├── src/
│   ├── main.asm           ; Entry point
│   ├── io.asm             ; I/O routines
│   ├── math.asm           ; Arithmetic helpers
│   └── string.asm         ; String operations
├── include/
│   ├── constants.inc      ; Equ/constant definitions
│   ├── macros.inc         ; Shared macro definitions
│   └── structs.inc        ; Structure definitions
├── Makefile               ; Build configuration
├── linker.ld              ; Custom linker script (optional)
└── README.md
```

---

## Proje Yapılandırması ve Oluşturma Sistemi
### Linux'ta NASM + GCC
En yaygın iş akışı, bağlayıcı olarak GCC'yi kullanarak derlemeyi C'ye bağlar.
```makefile
# Makefile for NASM + GCC project
ASM      = nasm
CC       = gcc
ASMFLAGS = -f elf64 -g -F dwarf
CFLAGS   = -Wall -g -no-pie
LDFLAGS  =

SRCS     = main.asm io.asm math.asm
OBJS     = $(SRCS:.asm=.o)
TARGET   = program

all: $(TARGET)

%.o: %.asm
$(ASM) $(ASMFLAGS) $< -o $@

$(TARGET): $(OBJS)
$(CC) $(CFLAGS) $(OBJS) -o $(TARGET) $(LDFLAGS)

clean:
rm -f $(OBJS) $(TARGET)

debug: $(TARGET)
gdb ./$(TARGET)

run: $(TARGET)
./$(TARGET)

.PHONY: all clean debug run
```

### Windows'ta MASM (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### AT&T Sözdizimi ile GAS (GNU Assembler)
```makefile
# Makefile for GAS (AT&T syntax)
AS       = as
LD       = ld
ASFLAGS  = --gstabs
LDFLAGS  = -static

TARGET   = program

all: $(TARGET)

$(TARGET): main.o
$(LD) $(LDFLAGS) main.o -o $(TARGET)

main.o: main.s
$(AS) $(ASFLAGS) main.s -o main.o

clean:
rm -f main.o $(TARGET)
```

### Pure Assembly Programına Bağlama (C Çalışma Zamanı Yok)
```nasm
; standalone.asm — No C library dependency, Linux x86-64
section .data
    msg     db  'Standalone program', 10
    msg_len equ $ - msg

section .text
    global _start           ; Entry point for ELF (no main)

_start:
    ; write(1, msg, msg_len)
    mov     rax, 1          ; sys_write
    mov     rdi, 1          ; stdout
    mov     rsi, msg
    mov     rdx, msg_len
    syscall

    ; exit(0)
    mov     rax, 60         ; sys_exit
    xor     rdi, rdi        ; code 0
    syscall
```

```bash
# Build without C runtime
nasm -f elf64 standalone.asm -o standalone.o
ld standalone.o -o standalone
```

---

## Temel Kavramlar
| Konsept | Açıklama |
|-----------|------------|
| **Kayıtlar** | CPU'nun dahili depolaması (x86'da EAX, EBX, ECX, EDX; ARM'de R0-R15) |
| **Bellek adresleme** | RAM'e adresler aracılığıyla erişim (`MOV EAX, [0x1000]`) |
| **Yığın** | İşlev çağrıları ve yerel değişkenler için LIFO bellek bölgesi (`PUSH`, `POP`) |
| **Talimatlar** | Temel işlemler: aritmetik, mantık, veri hareketi, kontrol akışı |
| **Kesintiler / sistem çağrıları** | İşletim sisteminden hizmet isteme |
| **Arama kuralları** | İşlevler parametreleri ve dönüş değerlerini nasıl alır (mimariye göre değişir) |
---

## Test Etme ve Hata Ayıklama
### GDB (GNU Hata Ayıklayıcı)
GDB, Linux'ta derleme için standart hata ayıklayıcıdır. Talimatlarda ilerlemenizi, kayıtları incelemenizi ve belleği incelemenizi sağlar.
```bash
# Build with debug symbols
nasm -f elf64 -g -F dwarf program.asm -o program.o
gcc -g -no-pie program.o -o program

# Start GDB
gdb ./program
```

```gdb
# Essential GDB commands for assembly debugging
(gdb) break _start              # Set breakpoint at entry point
(gdb) break *0x401040           # Set breakpoint at specific address
(gdb) run                       # Start execution
(gdb) si                        # Step one instruction (stepi)
(gdb) ni                        # Step over one instruction (nexti)
(gdb) info registers            # Show all register values
(gdb) print $rax                # Print specific register
(gdb) x/10xw $rsp               # Examine 10 words of stack in hex
(gdb) x/s 0x402000              # Examine memory as string
(gdb) disas /r                  # Disassemble with raw bytes
(gdb) layout regs               # Show register + assembly view
(gdb) continue                  # Continue execution
```

### NASM Makrolarıyla Hata Ayıklama
```nasm
; Debug print macro — prints register value via C printf
%macro debug_print_reg 1
    push    rax
    push    rdi
    push    rsi
    mov     rsi, %1             ; value to print
    mov     rdi, fmt_int        ; format string
    xor     eax, eax            ; AL = 0 (no FP args)
    call    printf wrt ..plt
    pop     rsi
    pop     rdi
    pop     rax
%endmacro
```

### Yaygın Hata Ayıklama Modelleri
| Sorun | Belirti | Hata Ayıklama Tekniği |
|-----------|-----------|-----------|
| Seg hatası | Program SIGSEGV ile çöküyor | İşaretçi değerlerini kontrol edin; yığın hizalamasını doğrulayın |
| Sonsuz döngü | Program kilitleniyor | Döngüde kesme noktasını ayarlayın; durum bayraklarını kontrol edin |
| Yanlış sonuç | Yanlış hesaplama | Aritmetikte adım atın; her işlemden sonra kayıt değerlerini kontrol edin |
| Yığın bozulması | RET'te Çökme | PUSH/POP dengesini doğrulayın; RSP hizalamasını kontrol edin (16 bayt hizalanmış olmalıdır) |
| Yanlış sistem çağrısı | Beklenmeyen çekirdek davranışı | RAX'ta sistem çağrısı numarasını doğrulayın; argüman kayıtlarını kontrol edin |
---

## Birlikte Çalışabilirlik
### Assembly'den C Fonksiyonlarını Çağırma
```nasm
; Calling printf from assembly (Linux x86-64, System V ABI)
section .data
    fmt     db  "The answer is: %d", 10, 0

section .text
    global main
    extern printf

main:
    push    rbp
    mov     rbp, rsp

    ; printf requires RAX = 0 when passing integer args in registers
    mov     rdi, fmt            ; 1st arg: format string
    mov     rsi, 42             ; 2nd arg: the integer value
    xor     eax, eax            ; AL = 0 (no vector registers used)
    call    printf

    xor     eax, eax            ; return 0
    mov     rsp, rbp
    pop     rbp
    ret
```

### Sistem Çağrı Referansı (Linux x86-64)
| Sistem çağrısı | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|------------|-----|-----------|------------|------------|------------|
| oku | 0 | fd | buf | say | — |
| yaz | 1 | fd | buf | say | — |
| aç | 2 | yol adı | bayraklar | modu | — |
| kapat | 3 | fd | — | — | — |
| mmap | 9 | adres | uzunluk | koruma | bayraklar |
| çıkış | 60 | durum | — | — | — |
### C'de Satır İçi Montaj (GCC)
```c
// Using GCC inline assembly to access CPUID
#include <stdio.h>

int main() {
    unsigned int eax, ebx, ecx, edx;

    __asm__ volatile(
        "cpuid"
        : "=a"(eax), "=b"(ebx), "=c"(ecx), "=d"(edx)
        : "a"(0)  // input: EAX = 0 (get vendor string)
    );

    printf("CPU Vendor: %.4s%.4s%.4s\n",
           (char*)&ebx, (char*)&edx, (char*)&ecx);
    return 0;
}
```

---

## Tasarım Desenleri
### Desen 1: Akümülatörlü Döngü
```nasm
; Sum an array of integers — classic accumulator pattern
; RDI = pointer to array, ESI = count
; Returns sum in EAX
array_sum:
    xor     eax, eax            ; sum = 0 (accumulator)
    xor     ecx, ecx            ; i = 0 (counter)
.loop:
    cmp     ecx, esi
    jge     .done
    add     eax, [rdi + rcx*4]  ; sum += arr[i]
    inc     ecx
    jmp     .loop
.done:
    ret
```

### Desen 2: Dizi İşleme Boru Hattı
```nasm
; Convert string to uppercase in-place
; RDI = pointer to null-terminated string
to_upper:
    mov     al, [rdi]           ; load byte
    test    al, al              ; check for null terminator
    jz      .done
    cmp     al, 'a'             ; if byte < 'a', skip
    jl      .next
    cmp     al, 'z'             ; if byte > 'z', skip
    jg      .next
    sub     al, 32              ; convert lowercase to uppercase
    mov     [rdi], al
.next:
    inc     rdi
    jmp     to_upper
.done:
    ret
```

### Desen 3: Sevkiyat Tablosu (Anahtar/Kutu)
```nasm
; Jump table implementation — equivalent to switch/case
section .data
    dispatch_table dq case_0, case_1, case_2, case_3
    default_msg    db "Unknown option", 10, 0

section .text
; RDI = option number (0-3)
dispatch:
    cmp     rdi, 3
    ja      .default            ; out of range -> default
    jmp     [dispatch_table + rdi*8]

case_0:
    ; handle case 0
    ret
case_1:
    ; handle case 1
    ret
case_2:
    ; handle case 2
    ret
case_3:
    ; handle case 3
    ret
.default:
    ret
```

### Desen 4: Bağlantılı Liste Geçişi
```nasm
; Structure: Node { int value; Node* next; }
; RDI = pointer to head node
; Returns sum of all node values in EAX
list_sum:
    xor     eax, eax            ; sum = 0
    test    rdi, rdi            ; check for NULL head
    jz      .done
.traverse:
    add     eax, [rdi]          ; add node.value to sum
    mov     rdi, [rdi + 8]      ; move to node.next (offset 8)
    test    rdi, rdi            ; check for NULL
    jnz     .traverse
.done:
    ret
```

---

## Performans ve Optimizasyon
### Talimat Planlama
Modern CPU'lar, ardışık düzen ve sıra dışı yürütme yoluyla döngü başına birden fazla talimat yürütür. Bunu anlamak daha hızlı derleme yazmaya yardımcı olur.
```nasm
; BAD: Data dependency stalls the pipeline
mov     eax, [mem]          ; load (latency ~4 cycles)
add     ebx, eax            ; must wait for load to complete
mov     [mem2], ebx         ; must wait for add

; GOOD: Independent instructions fill the pipeline
mov     eax, [mem]          ; load
mov     ecx, [mem3]         ; independent load (executes in parallel)
add     ebx, eax            ; depends on first load
add     edx, ecx            ; independent — can execute while waiting
mov     [mem2], ebx
mov     [mem4], edx
```

### Önbellek Optimizasyonu
```nasm
; BAD: Stride access pattern (cache-unfriendly)
    xor     rcx, rcx
.loop:
    mov     al, [buffer + rcx*64]   ; each access is a cache miss
    inc     rcx
    cmp     rcx, 1024
    jl      .loop

; GOOD: Sequential access (cache-friendly)
    xor     rcx, rcx
.loop:
    mov     al, [buffer + rcx]      ; sequential — prefetcher helps
    inc     rcx
    cmp     rcx, 1024
    jl      .loop
```

### Optimizasyon Kontrol Listesi
| Tekniği | Etki | Açıklama |
|-----------|-----------|------------|
| **Kullanımı kaydedin** | Yüksek | Sıcak değişkenleri kayıtlarda tutun; hafıza erişimini engelle |
| **Döngü açma** | Orta | Yineleme başına birden fazla öğeyi işleyerek döngü yükünü azaltın |
| **SIMD (SSE/AVX)** | Çok Yüksek | 4-16 değeri vektör talimatlarıyla aynı anda işleyin |
| **Şube eliminasyonu** | Orta | Mümkün olduğunda koşullu atlamalar yerine CMOV kullanın |
| **Önbellek hizalaması** | Orta | Etkin döngüleri 16/32 baytlık sınırlara göre hizalayın |
| **Bellek erişim düzenleri** | Yüksek | Sıralı erişim; önbellek satırı bölünmelerini önleyin |
---

## Dağıtım ve Gerçek Dünya Kullanımı
### Montaj Programları Nasıl Dağıtılır?
Montaj programları doğrudan yerel makine kodu yürütülebilir dosyalarına derlenir. Çalışma zamanı yok, sanal makine yok ve tercüman gerekli değil. Dağıtım, ikili dosyayı hedef sisteme kopyalamak kadar basittir.
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### Gerçek Dünyadaki Kullanım Durumları
| Sanayi | Başvuru | Neden Montaj |
|----------|----------------|------------|
| **İşletim sistemleri** | Linux çekirdeği önyükleme koçanı, Windows HAL | Doğrudan donanım kontrolü, kesinti yönetimi |
| **Yerleşik ürün yazılımı** | Mikrodenetleyici önyükleyicileri, IoT cihazları | İşletim sistemi veya çalışma zamanı yok; katı hafıza sınırları |
| **Güvenlik** | Exploit geliştirme, kötü amaçlı yazılım analizi, tersine mühendislik | Derlenmiş ikili dosyalarla etkileşim kurmanın tek yolu |
| **Oyun motorları** | SIMD için optimize edilmiş matematik (matris dönüşümleri, fizik) | Kare başına hesaplamalar için maksimum verim |
| **Derleyiciler** | Kod oluşturma arka uçları (LLVM, GCC) | Optimize edilmiş makine kodu yayılıyor |
| **Kriptografi** | AES-NI, SHA talimat hızlandırma | Donanımla hızlandırılmış kripto işlemleri |
| **Cihaz sürücüleri** | GPU sürücüleri, ağ kartı donanım yazılımı | Doğrudan kayıt düzeyinde donanım erişimi |
### Eski Sistem Entegrasyonu
Birçok eski sistem, C kod tabanlarına gömülü montaj rutinleri içerir. Bunlar genellikle onlarca yıldır sürdürülen performans açısından kritik işlevler veya donanıma özgü rutinlerdir.
```c
// Legacy pattern: C code calling an assembly-optimized function
extern void fast_memcpy(void* dest, const void* src, size_t n);

void process_data(void) {
    char buffer[4096];
    // Calls hand-optimized assembly using REP MOVSQ or SIMD
    fast_memcpy(buffer, source_data, sizeof(buffer));
}
```

---

## Montaj Ne Zaman Kullanılmalı
| Senaryo | Neden Montaj | Daha İyi Alternatif |
|----------|----------------|--------|
| İşletim Sistemi çekirdeği geliştirme | Önyükleme kodu, kesme işleyicileri | Çoğu çekirdek kodu için C |
| Aygıt sürücüleri | Doğrudan donanım erişimi | C, Pas |
| Tersine mühendislik / güvenlik | Derlenmiş ikili dosyaları analiz etmenin tek yolu | — |
| Performans açısından kritik kod | Maksimum optimizasyon | Derleyici içsel bilgilerine sahip C/C++ |
| Gömülü ürün yazılımı (çıplak metal) | Üst düzey dil mevcut değil | C, Pas |
| Eğitim | Bilgisayar mimarisini anlamak | — |
| Genel uygulama geliştirme | Karmaşık programlar için pratik değildir | Herhangi bir üst düzey dil |
---

## Sentetik Soru-Cevap
### S1: RISC ve CISC derlemesi arasındaki fark nedir?
**C:** CISC (x86) karmaşık, değişken uzunlukta talimatlara sahiptir. RISC (ARM) basit, sabit uzunlukta talimatlara sahiptir:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### S2: Yığın montajda nasıl çalışır?
**C:** Yığın aşağı doğru büyüyor. `push`SP'yi ve depoları azaltır; `pop`SP'yi yükler ve artırır:
```asm
; x86 stack operations
push rax          ; save rax on stack
push rbx          ; save rbx
; ... do work ...
pop rbx           ; restore rbx
pop rax           ; restore rax

; Stack frame for functions
push rbp          ; save old base pointer
mov rbp, rsp      ; set new base pointer
sub rsp, 32       ; allocate 32 bytes for locals
; ... function body ...
mov rsp, rbp      ; deallocate locals
pop rbp           ; restore base pointer
ret               ; return
```

### S3: Montajdaki işlevleri nasıl çağırırım?
**A:** Çağrı kuralını izleyin (Linux'ta System V AMD64, Windows'ta Windows x64):
```asm
; System V AMD64: args in rdi, rsi, rdx, rcx, r8, r9
; Return value in rax
extern printf

section .data
    fmt db "Result: %d", 10, 0

section .text
global main
main:
    mov rdi, fmt      ; first arg: format string
    mov rsi, 42       ; second arg: integer
    xor rax, rax      ; no vector registers used
    call printf       ; call C function
    xor rax, rax      ; return 0
    ret
```

### S4: Bilinmesi gereken en önemli montaj talimatları nelerdir?
**C:** Veri hareketi, aritmetik, kontrol akışı ve yığın işlemleri çekirdeği oluşturur.
### S5: Montaj güvenlik araştırmasında nasıl kullanılır?
**C:** Tersine mühendislik, yararlanma geliştirme, kötü amaçlı yazılım analizi ve derleyici çıktısını anlama, bunların tümü derleme okuryazarlığı gerektirir.
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Montajda Döngü Uygulamak
**1. Adım: Sorunu Anlayın**
1'den N'ye kadar tam sayıları toplayın.
**2. Adım: Yaklaşımı Belirleyin**
Bir sayaç kaydı ve akümülatör kullanın.
**3. Adım: Uygulama**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**4. Adım: Optimize edin**
O(1) için O(N) yerine N*(N+1)/2 formülünü kullanın.
---

## Özet
Montaj dili, insan tarafından okunabilen kod ile CPU'ların yürüttüğü ham ikili dosya arasındaki köprüdür. Uygulama oluşturmak için pratik bir seçim değildir ancak bilgisayarların en düşük düzeyde nasıl çalıştığını anlamak için gereklidir. Sistem programcıları, güvenlik araştırmacıları ve gömülü geliştiriciler için montaj bilgisi çok değerlidir. Herkes için, montaj kavramlarını (kayıtlar, yığın, talimat döngüleri) anlamak sizi herhangi bir dilde daha iyi bir programcı yapar.