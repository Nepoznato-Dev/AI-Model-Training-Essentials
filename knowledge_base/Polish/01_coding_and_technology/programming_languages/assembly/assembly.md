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

# Język asemblera
Język asemblera jest językiem programowania najniższego poziomu zrozumiałym dla człowieka. Zapewnia bezpośrednią reprezentację instrukcji kodu maszynowego komputera przy użyciu kodów mnemonicznych (takich jak `MOV`, `ADD`, `JMP`) zamiast surowego kodu binarnego. Każdy język asemblera jest specyficzny dla konkretnej architektury procesora (x86, ARM, MIPS, RISC-V) — kod napisany dla jednej architektury nie będzie działał na innej.
Język asemblera nie jest używany do tworzenia aplikacji. Używa się go, gdy potrzebna jest absolutna kontrola nad sprzętem: pisanie jądra systemu operacyjnego, sterowników urządzeń, programów ładujących, wbudowanego oprogramowania sprzętowego, sekcji kodu krytycznych dla wydajności, inżynierii wstecznej i zrozumienia, w jaki sposób komputery faktycznie wykonują instrukcje.
---

## Dlaczego montaż ma znaczenie
- **Rozumienie sprzętu**: Jedyny sposób, aby dowiedzieć się dokładnie, co robi procesor na poziomie instrukcji.
- **Dostrajanie wydajności**: Krytyczne sekcje kodu można zoptymalizować w zakresie wykraczającym poza to, co produkują kompilatory.
- **Inżynieria wsteczna**: analiza złośliwego oprogramowania, badania bezpieczeństwa i zrozumienie prawnie zastrzeżonego oprogramowania.
- **Systemy wbudowane**: Niektóre mikrokontrolery nie obsługują języków wyższego poziomu.
- **Rozwój systemu operacyjnego**: Kod rozruchowy, procedury obsługi przerwań i przełączanie kontekstu wymagają montażu.
- **Edukacyjne**: Zrozumienie asemblera uczy, jak faktycznie działają komputery — pamięć, rejestry, stos i potok procesora.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Bardzo niski poziom** | Każda instrukcja jest odwzorowana na jedną operację maszyny | Używaj języków wyższego poziomu do wszystkiego z wyjątkiem krytycznych części |
| **Specyficzne dla architektury** | Kod x86 nie działa na ARM | Napisz przenośny kod w C/C++; używaj zestawu tylko tam, gdzie jest to potrzebne |
| **Rozszerzone** | Proste zadania wymagają wielu instrukcji | Używaj makr; zachowaj minimalną liczbę sekcji montażowych |
| **Brak przenośności** | Inna składnia dla każdego asemblera (NASM, GAS, MASM) | Użyj elementów wewnętrznych kompilatora lub zestawu wbudowanego |
| **Trudność debugowania** | Trudno prześledzić logikę na poziomie instrukcji | Użyj debugerów (GDB); swobodnie dodawaj komentarze |
---

## Przykład składni (zespół x86-64 — NASM)
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

### Przykład montażu ARM
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

## Zaawansowana składnia i wzorce
### x86-64 Tryby adresowania
Zrozumienie trybów adresowania ma kluczowe znaczenie dla pisania wydajnego asemblera. Każdy tryb kontroluje lokalizację operandów.
| Tryb | Składnia (NASM) | Opis |
|------|-------------------|------------|
| **Natychmiast** | `mov eax, 42`| Operand jest wartością stałą |
| **Zarejestruj się** | `mov eax, ebx`| Operand znajduje się w rejestrze |
| **Bezpośredni** | `mov eax, [0x4000]`| Operand znajduje się pod stałym adresem pamięci |
| **Zarejestruj się pośrednio** | `mov eax, [rbx]`| Operand znajduje się pod adresem w rejestrze |
| **Podstawa + przemieszczenie** | `mov eax, [rbx + 8]`| Adres = rejestr + stałe przesunięcie |
| **Indeks skalowany** | `mov eax, [rbx + rcx*4]`| Adres = podstawa + (indeks × skala) |
| **Pełny SIB** | `mov eax, [rbx + rcx*4 + 16]`| Podstawa + (indeks × skala) + przemieszczenie |
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

### System makro (NASM)
Makra umożliwiają definiowanie sekwencji instrukcji wielokrotnego użytku z parametrami, dzięki czemu montaż jest mniej powtarzalny.
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

### Układ ramki stosu
Zrozumienie ramki stosu jest niezbędne do pisania funkcji i debugowania.
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

## Architektura i projektowanie systemów
### Układ pamięci typowego procesu Linux x86-64
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

### Konwencja dotycząca struktury programu
Dobrze zorganizowany program montażu dzieli obawy na odrębne sekcje:
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

### Typowa struktura katalogu projektu
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

## Konfiguracja projektu i budowanie systemu
### NASM + GCC w systemie Linux
Najpopularniejszy zestaw łączy przepływu pracy z C przy użyciu GCC jako linkera.
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

### MASM w systemie Windows (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (Asembler GNU) ze składnią AT&T
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

### Łączenie programu czystego asemblera (bez środowiska wykonawczego C)
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

## Kluczowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Rejestry** | Pamięć wewnętrzna procesora (EAX, EBX, ECX, EDX na x86; R0-R15 na ARM) |
| **Adresowanie pamięci** | Dostęp do pamięci RAM poprzez adresy (`MOV EAX, [0x1000]`) |
| **Stos** | Obszar pamięci LIFO dla wywołań funkcji i zmiennych lokalnych (`PUSH`,`POP`) |
| **Instrukcja** | Podstawowe operacje: arytmetyka, logika, przenoszenie danych, przepływ sterowania |
| **Przerwania / wywołania systemowe** | Żądanie usług z systemu operacyjnego |
| **Przywoływanie konwencji** | Sposób, w jaki funkcje otrzymują parametry i zwracają wartości (różni się w zależności od architektury) |
---

## Testowanie i debugowanie
### GDB (Debuger GNU)
GDB to standardowy debuger do montażu w systemie Linux. Umożliwia przeglądanie instrukcji, sprawdzanie rejestrów i sprawdzanie pamięci.
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

### Debugowanie za pomocą makr NASM
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

### Typowe wzorce debugowania
| Problem | Objaw | Technika debugowania |
|--------|---------|--------------------------------|
| Segfault | Program ulega awarii z SIGSEGV | Sprawdź wartości wskaźników; sprawdź wyrównanie stosu |
| Nieskończona pętla | Program zawiesza się | Ustaw punkt przerwania w pętli; sprawdź flagi warunku |
| Zły wynik | Błędne obliczenia | Przejdź przez arytmetykę; sprawdź wartości rejestrów po każdej operacji |
| Uszkodzenie stosu | Awaria na RET | Sprawdź saldo PUSH/POP; sprawdź wyrównanie RSP (musi być wyrównane do 16 bajtów) |
| Złe wywołanie systemowe | Nieoczekiwane zachowanie jądra | Sprawdź numer wywołania systemowego w RAX; sprawdź rejestry argumentów |
---

## Interoperacyjność
### Wywoływanie funkcji C z zestawu
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

### Informacje o wywołaniach systemowych (Linux x86-64)
| Syscall | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|--------|-----|------------|------------|------------|------------|
| czytaj | 0 | fd | buf | liczyć | — |
| napisz | 1 | fd | buf | liczyć | — |
| otwarte | 2 | nazwa ścieżki | flagi | tryb | — |
| zamknij | 3 | fd | — | — | — |
| mapa | 9 | adres | długość | ochrona | flagi |
| wyjście | 60 | stan | — | — | — |
### Montaż liniowy w C (GCC)
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

## Wzorce projektowe
### Wzór 1: Pętla z akumulatorem
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

### Wzorzec 2: Potok przetwarzania ciągów
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

### Wzór 3: Tabela wysyłkowa (przełącznik/obudowa)
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

### Wzorzec 4: Przeglądanie listy połączonej
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

## Wydajność i optymalizacja
### Planowanie instrukcji
Nowoczesne procesory wykonują wiele instrukcji na cykl poprzez potokowanie i wykonywanie poza kolejnością. Zrozumienie tego pomaga w szybszym pisaniu asemblera.
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

### Optymalizacja pamięci podręcznej
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

### Lista kontrolna optymalizacji
| Technika | Wpływ | Opis |
|---------------|--------|------------|
| **Zarejestruj użycie** | Wysoki | Przechowuj gorące zmienne w rejestrach; unikaj dostępu do pamięci |
| **Odwijanie pętli** | Średni | Zmniejsz obciążenie pętli, przetwarzając wiele elementów na iterację |
| **SIMD (SSE/AVX)** | Bardzo wysoki | Przetwarzaj 4-16 wartości jednocześnie z instrukcjami wektorowymi |
| **Eliminacja oddziału** | Średni | Jeśli to możliwe, używaj CMOV zamiast skoków warunkowych |
| **Wyrównanie pamięci podręcznej** | Średni | Wyrównaj gorące pętle do granic 16/32 bajtów |
| **Wzorce dostępu do pamięci** | Wysoki | Dostęp sekwencyjny; unikaj podziału linii pamięci podręcznej |
---

## Wdrożenie i użytkowanie w świecie rzeczywistym
### Jak wdrażane są programy montażowe
Programy asemblerowe kompilują się bezpośrednio do plików wykonywalnych natywnego kodu maszynowego. Nie ma środowiska wykonawczego, maszyny wirtualnej i nie jest wymagany interpreter. Wdrożenie jest tak proste, jak skopiowanie pliku binarnego do systemu docelowego.
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### Rzeczywiste przypadki użycia
| Przemysł | Aplikacja | Dlaczego montaż |
|--------------|------------|------------|
| **Systemy operacyjne** | Odcinek rozruchowy jądra Linux, Windows HAL | Bezpośrednia kontrola sprzętu, obsługa przerwań |
| **Wbudowane oprogramowanie sprzętowe** | Bootloadery mikrokontrolerów, urządzenia IoT | Brak dostępnego systemu operacyjnego lub środowiska wykonawczego; ścisłe limity pamięci |
| **Bezpieczeństwo** | Rozwój exploitów, analiza złośliwego oprogramowania, inżynieria wsteczna | Jedyny sposób na interakcję ze skompilowanymi plikami binarnymi |
| **Silniki gier** | Matematyka zoptymalizowana pod kątem SIMD (transformacje macierzy, fizyka) | Maksymalna przepustowość dla obliczeń na klatkę |
| **Kompilatory** | Backendy do generowania kodu (LLVM, GCC) | Emitowanie zoptymalizowanego kodu maszynowego |
| **Kryptografia** | Przyspieszenie instrukcji AES-NI, SHA | Operacje kryptograficzne przyspieszane sprzętowo |
| **Sterowniki urządzeń** | sterowniki GPU, oprogramowanie karty sieciowej | Bezpośredni dostęp do sprzętu na poziomie rejestru |
### Integracja starszych systemów
Wiele starszych systemów zawiera procedury asemblera osadzone w bazach kodu C. Są to zazwyczaj funkcje krytyczne dla wydajności lub procedury specyficzne dla sprzętu, które są utrzymywane przez dziesięciolecia.
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

## Kiedy używać zestawu
| Scenariusz | Dlaczego montaż | Lepsza alternatywa |
|---------|------------|--------------------------------|
| Rozwój jądra systemu operacyjnego | Kod rozruchowy, obsługa przerwań | C dla większości kodu jądra |
| Sterowniki urządzeń | Bezpośredni dostęp do sprzętu | C, rdza |
| Inżynieria odwrotna / bezpieczeństwo | Jedyny sposób na analizę skompilowanych plików binarnych | — |
| Kod krytyczny dla wydajności | Maksymalna optymalizacja | C/C++ z elementami kompilatora |
| Wbudowane oprogramowanie sprzętowe (bare metal) | Brak dostępnego języka wyższego poziomu | C, rdza |
| Edukacja | Zrozumienie architektury komputera | — |
| Ogólne tworzenie aplikacji | Niepraktyczne w przypadku złożonych programów | Dowolny język wyższego poziomu |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica pomiędzy montażem RISC i CISC?
**A:** CISC (x86) zawiera złożone instrukcje o zmiennej długości. RISC (ARM) ma proste instrukcje o stałej długości:
```asm
; x86 (CISC) — variable length, many addressing modes
mov eax, [ebx + ecx*4 + 8]   ; complex memory access in one instruction

; ARM (RISC) — load/store architecture
ldr r0, [r1, r2, LSL #2]     ; load with shifted index
```

### P2: Jak stos działa w asemblerze?
**A:** Stos rośnie w dół. `push`zmniejsza SP i zapisuje; `pop`ładuje i zwiększa SP:
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

### P3: Jak wywołać funkcje w asemblerze?
**A:** Postępuj zgodnie z konwencją wywoływania (System V AMD64 w systemie Linux, Windows x64 w systemie Windows):
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

### P4: Jakie są najważniejsze instrukcje montażu, o których warto wiedzieć?
**O:** Przenoszenie danych, arytmetyka, przepływ sterowania i operacje na stosie stanowią rdzeń.
### P5: W jaki sposób montaż jest wykorzystywany w badaniach nad bezpieczeństwem?
**O:** Inżynieria wsteczna, tworzenie exploitów, analiza złośliwego oprogramowania i zrozumienie wyników działania kompilatora wymagają umiejętności korzystania z asemblera.
---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Implementacja pętli w asemblerze
**Krok 1: Zrozum problem**
Suma liczb całkowitych od 1 do N.
**Krok 2: Zidentyfikuj podejście**
Użyj rejestru licznikowego i akumulatora.
**Krok 3: Wdróż**```asm
; Sum 1 to N (N in ecx)
    xor eax, eax      ; eax = 0 (accumulator)
    mov ecx, 10       ; N = 10
.loop:
    add eax, ecx      ; sum += counter
    dec ecx           ; counter--
    jnz .loop         ; jump if not zero
    ; eax = 55 (1+2+...+10)
```

**Krok 4: Optymalizacja**
Użyj wzoru N*(N+1)/2 dla O(1) zamiast O(N).
---

## Streszczenie
Język asemblera jest pomostem pomiędzy kodem czytelnym dla człowieka a surowym plikiem binarnym wykonywanym przez procesory. Nie jest to praktyczny wybór do tworzenia aplikacji, ale jest niezbędny do zrozumienia, jak komputery działają na najniższym poziomie. Dla programistów systemów, badaczy bezpieczeństwa i programistów systemów wbudowanych wiedza o asemblerze jest bezcenna. Dla wszystkich innych zrozumienie koncepcji asemblera (rejestry, stos, cykle instrukcji) czyni cię lepszym programistą w dowolnym języku.