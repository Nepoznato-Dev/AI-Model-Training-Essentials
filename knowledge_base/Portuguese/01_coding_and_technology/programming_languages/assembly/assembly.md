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

# Linguagem Assembly
A linguagem assembly é a linguagem de programação legível por humanos de nível mais baixo. Ele fornece uma representação direta das instruções de código de máquina de um computador usando códigos mnemônicos (como`MOV`,`ADD`,`JMP`) em vez de binário bruto. Cada linguagem assembly é específica para uma arquitetura de processador específica (x86, ARM, MIPS, RISC-V) — o código escrito para uma arquitetura não será executado em outra.
A linguagem assembly não é usada para construir aplicativos. Ele é usado quando você precisa de controle absoluto sobre o hardware: escrever kernels de sistema operacional, drivers de dispositivos, bootloaders, firmware incorporado, seções de código de desempenho crítico, engenharia reversa e entender como os computadores realmente executam instruções.
---

## Por que a montagem é importante
- **Entendimento de hardware**: a única maneira de saber exatamente o que a CPU está fazendo no nível de instrução.
- **Ajuste de desempenho**: seções críticas de código podem ser otimizadas além do que os compiladores produzem.
- **Engenharia reversa**: análise de malware, pesquisa de segurança e compreensão de software proprietário.
- **Sistemas embarcados**: Alguns microcontroladores não possuem suporte a linguagens de nível superior.
- **Desenvolvimento de SO**: código de inicialização, manipuladores de interrupção e alternância de contexto exigem montagem.
- **Educacional**: Noções básicas sobre montagem ensinam como os computadores realmente funcionam: memória, registros, pilha e pipeline da CPU.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Nível extremamente baixo** | Cada instrução é mapeada para uma operação de máquina | Use linguagens de nível superior para tudo, exceto as partes críticas |
| **Específico para arquitetura** | código x86 não funciona em ARM | Escreva código portátil em C/C++; use assembly somente quando necessário |
| **Detalhado** | Tarefas simples requerem muitas instruções | Utilize macros; mantenha as seções de montagem mínimas |
| **Sem portabilidade** | Sintaxe diferente para cada montador (NASM, GAS, MASM) | Use intrínsecos do compilador ou assembly embutido |
| **Dificuldade de depuração** | Lógica difícil de rastrear no nível da instrução | Utilize depuradores (GDB); adicione comentários generosamente |
---

## Exemplo de sintaxe (montagem x86-64 - NASM)
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

### Exemplo de montagem ARM
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

## Sintaxe e padrões avançados
### Modos de endereçamento x86-64
Compreender os modos de endereçamento é fundamental para escrever uma montagem eficiente. Cada modo controla como os operandos são localizados.
| Modo | Sintaxe (NASM) | Descrição |
|------|---------------|------------|
| **Imediato** | `mov eax, 42`| Operando é um valor constante |
| **Registrar** | `mov eax, ebx`| O operando está em um registrador |
| **Direto** | `mov eax, [0x4000]`| O operando está em um endereço de memória fixo |
| **Cadastro indireto** | `mov eax, [rbx]`| O operando está no endereço em um registro |
| **Base + deslocamento** | `mov eax, [rbx + 8]`| Endereço = registro + deslocamento constante |
| **Índice escalonado** | `mov eax, [rbx + rcx*4]`| Endereço = base + (índice × escala) |
| **SIB completo** | `mov eax, [rbx + rcx*4 + 16]`| Base + (índice × escala) + deslocamento |
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

### O Sistema Macro (NASM)
As macros permitem definir sequências de instruções reutilizáveis ​​com parâmetros, tornando a montagem menos repetitiva.
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

### Layout do quadro de pilha
Compreender o stack frame é essencial para escrever funções e depurar.
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

## Arquitetura e Design de Sistema
### Layout de memória de um processo Linux x86-64 típico
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

### Convenção sobre Estrutura do Programa
Um programa de montagem bem organizado separa as preocupações em seções distintas:
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

### Estrutura típica de diretório de projeto
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

## Configuração do projeto e sistema de construção
### NASM + GCC no Linux
O fluxo de trabalho mais comum vincula o assembly com C usando GCC como vinculador.
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

###MASM no Windows (ML64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### GAS (GNU Assembler) com sintaxe AT&T
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

### Vinculando um programa Pure Assembly (sem tempo de execução C)
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

## Conceitos-chave
| Conceito | Descrição |
|--------|-------------|
| **Registros** | Armazenamento interno da CPU (EAX, EBX, ECX, EDX em x86; R0-R15 em ARM) |
| **Endereçamento de memória** | Acessando RAM via endereços (`MOV EAX, [0x1000]`) |
| **Pilha** | Região de memória LIFO para chamadas de função e variáveis ​​locais (`PUSH`,`POP`) |
| **Instruções** | Operações básicas: aritmética, lógica, movimentação de dados, fluxo de controle |
| **Interrupções/chamadas de sistema** | Solicitando serviços do sistema operacional |
| **Convenções de chamada** | Como as funções recebem parâmetros e retornam valores (varia de acordo com a arquitetura) |
---

## Teste e depuração
### GDB (depurador GNU)
GDB é o depurador padrão para montagem no Linux. Ele permite percorrer instruções, inspecionar registros e examinar a memória.
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

### Depuração com macros NASM
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

### Padrões comuns de depuração
| Problema | Sintoma | Técnica de depuração |
|--------|---------|-------------------|
| Segfault | Programa trava com SIGSEGV | Verifique os valores do ponteiro; verifique o alinhamento da pilha |
| Laço infinito | Programa trava | Definir ponto de interrupção em loop; verificar sinalizadores de condição |
| Resultado errado | Cálculo incorreto | Percorra a aritmética; verifique os valores do registro após cada operação |
| Corrupção de pilha | Falha no RET | Verifique o saldo PUSH/POP; verifique o alinhamento RSP (deve estar alinhado com 16 bytes) |
| Chamada de sistema errada | Comportamento inesperado do kernel | Verifique o número do syscall no RAX; verificar registros de argumentos |
---

## Interoperabilidade
### Chamando funções C do Assembly
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

### Referência de chamada do sistema (Linux x86-64)
| Syscall | RAX | Arg1 (RDI) | Arg2 (RSI) | Arg3 (RDX) | Arg4 (R10) |
|---------|-----|------------|------------|------------|------------|
| leia | 0 | fd | buf | contar | — |
| escrever | 1 | fd | buf | contar | — |
| aberto | 2 | nome do caminho | bandeiras | modo | — |
| fechar | 3 | fd | — | — | — |
| mapa mm | 9 | endereço | comprimento | lucro | bandeiras |
| saída | 60 | estado | — | — | — |
### Montagem embutida em C (GCC)
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

## Padrões de Projeto
### Padrão 1: Loop com acumulador
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

### Padrão 2: Pipeline de processamento de strings
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

### Padrão 3: Tabela de Despacho (Switch/Case)
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

### Padrão 4: travessia de lista vinculada
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

## Desempenho e otimização
### Agendamento de instruções
CPUs modernas executam múltiplas instruções por ciclo por meio de pipeline e execução fora de ordem. Compreender isso ajuda a escrever uma montagem mais rápida.
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

### Otimização de Cache
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

### Lista de verificação de otimização
| Técnica | Impacto | Descrição |
|-----------|--------|-------------|
| **Registrar uso** | Alto | Mantenha variáveis ​​quentes em registros; evite acesso à memória |
| **Desenrolamento do laço** | Médio | Reduza a sobrecarga do loop processando vários itens por iteração |
| **SIMD (SSE/AVX)** | Muito alto | Processe 4-16 valores simultaneamente com instruções vetoriais |
| **Eliminação de filial** | Médio | Use CMOV em vez de saltos condicionais sempre que possível |
| **Alinhamento de cache** | Médio | Alinhe os hot loops aos limites de 16/32 bytes |
| **Padrões de acesso à memória** | Alto | Acesso sequencial; evite divisões de linha de cache |
---

## Implantação e uso no mundo real
### Como os programas Assembly são implantados
Os programas assembly são compilados diretamente em executáveis ​​​​de código de máquina nativo. Não há tempo de execução, nem VM, nem intérprete necessário. A implantação é tão simples quanto copiar o binário para o sistema de destino.
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### Casos de uso do mundo real
| Indústria | Aplicação | Por que montagem |
|----------|-------------|-------------|
| **Sistemas operacionais** | Esboço de inicialização do kernel Linux, Windows HAL | Controle direto de hardware, tratamento de interrupções |
| **Firmware incorporado** | Bootloaders de microcontroladores, dispositivos IoT | Nenhum sistema operacional ou tempo de execução disponível; limites rígidos de memória |
| **Segurança** | Desenvolvimento de exploits, análise de malware, engenharia reversa | Única maneira de interagir com binários compilados |
| **Motores de jogo** | Matemática otimizada para SIMD (transformadas de matriz, física) | Taxa de transferência máxima para cálculos por quadro |
| **Compiladores** | Back-ends de geração de código (LLVM, GCC) | Emissão de código de máquina otimizado |
| **Criptografia** | AES-NI, aceleração de instrução SHA | Operações criptográficas aceleradas por hardware |
| **Drivers de dispositivo** | Drivers de GPU, firmware de placa de rede | Acesso direto ao hardware em nível de registro |
### Integração de sistema legado
Muitos sistemas legados contêm rotinas de montagem incorporadas em bases de código C. Normalmente, essas são funções críticas de desempenho ou rotinas específicas de hardware que foram mantidas por décadas.
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

## Quando usar montagem
| Cenário | Por que montagem | Melhor Alternativa |
|----------|-------------|-------------------|
| Desenvolvimento do kernel do sistema operacional | Código de inicialização, manipuladores de interrupção | C para a maior parte do código do kernel |
| Drivers de dispositivo | Acesso direto ao hardware | C, ferrugem |
| Engenharia reversa/segurança | Única maneira de analisar binários compilados | — |
| Código crítico para desempenho | Otimização máxima | C/C++ com intrínsecos do compilador |
| Firmware incorporado (bare metal) | Nenhuma linguagem de nível superior disponível | C, ferrugem |
| Educação | Compreendendo a arquitetura de computadores | — |
| Desenvolvimento geral de aplicações | Impraticável para programas complexos | Qualquer linguagem de nível superior |
---

## Resumo
A linguagem assembly é a ponte entre o código legível por humanos e o binário bruto que as CPUs executam. Não é uma escolha prática para a construção de aplicações, mas é essencial para a compreensão de como os computadores funcionam no nível mais baixo. Para programadores de sistemas, pesquisadores de segurança e desenvolvedores incorporados, o conhecimento de montagem é inestimável. Para todos os outros, compreender os conceitos de assembly (registros, pilha, ciclos de instrução) torna você um programador melhor em qualquer linguagem.