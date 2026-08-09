---
# मेटाडेटा
शीर्षक: "विधानसभा भाषा"
विवरण: "असेंबली प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [असेंबली, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "उन्नत"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "31 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# सभा की भाषा
असेंबली भाषा निम्नतम स्तर की मानव-पठनीय प्रोग्रामिंग भाषा है। यह रॉ बाइनरी के बजाय स्मरक कोड (जैसे`MOV`,`ADD`,`JMP`) का उपयोग करके कंप्यूटर के मशीन कोड निर्देशों का प्रत्यक्ष प्रतिनिधित्व प्रदान करता है। प्रत्येक असेंबली भाषा एक विशेष प्रोसेसर आर्किटेक्चर (x86, ARM, MIPS, RISC-V) के लिए विशिष्ट है - एक आर्किटेक्चर के लिए लिखा गया कोड दूसरे पर नहीं चलेगा।
एप्लिकेशन बनाने के लिए असेंबली भाषा का उपयोग नहीं किया जाता है। इसका उपयोग तब किया जाता है जब आपको हार्डवेयर पर पूर्ण नियंत्रण की आवश्यकता होती है: ऑपरेटिंग सिस्टम कर्नेल, डिवाइस ड्राइवर, बूटलोडर, एम्बेडेड फ़र्मवेयर, प्रदर्शन-महत्वपूर्ण कोड अनुभाग, रिवर्स इंजीनियरिंग लिखना और यह समझना कि कंप्यूटर वास्तव में निर्देशों को कैसे निष्पादित करते हैं।
---

## विधानसभा क्यों मायने रखती है
- **हार्डवेयर समझ**: यह जानने का एकमात्र तरीका कि सीपीयू निर्देश स्तर पर क्या कर रहा है।
- **प्रदर्शन ट्यूनिंग**: महत्वपूर्ण कोड अनुभागों को कंपाइलर्स द्वारा तैयार किए गए कोड से परे अनुकूलित किया जा सकता है।
- **रिवर्स इंजीनियरिंग**: मैलवेयर विश्लेषण, सुरक्षा अनुसंधान, और मालिकाना सॉफ़्टवेयर को समझना।
- **एम्बेडेड सिस्टम**: कुछ माइक्रोकंट्रोलर के पास कोई उच्च-स्तरीय भाषा समर्थन नहीं है।
- **ओएस विकास**: बूट कोड, इंटरप्ट हैंडलर और संदर्भ स्विचिंग के लिए असेंबली की आवश्यकता होती है।
- **शैक्षिक**: असेंबली को समझना आपको सिखाता है कि कंप्यूटर वास्तव में कैसे काम करते हैं - मेमोरी, रजिस्टर, स्टैक और सीपीयू पाइपलाइन।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **अत्यंत निम्न स्तर** | प्रत्येक अनुदेश एक मशीन संचालन को मैप करता है | महत्वपूर्ण भागों को छोड़कर हर चीज़ के लिए उच्च-स्तरीय भाषाओं का उपयोग करें |
| **वास्तुकला-विशिष्ट** | x86 कोड ARM पर नहीं चलता | C/C++ में पोर्टेबल कोड लिखें; असेंबली का उपयोग केवल वहीं करें जहां आवश्यकता हो |
| **शब्दशः** | सरल कार्यों के लिए कई निर्देशों की आवश्यकता होती है | मैक्रोज़ का प्रयोग करें; असेंबली सेक्शन न्यूनतम रखें |
| **कोई पोर्टेबिलिटी नहीं** | प्रत्येक असेंबलर (NASM, GAS, MASM) के लिए अलग-अलग सिंटैक्स | कंपाइलर इंट्रिनिक्स या इनलाइन असेंबली का उपयोग करें |
| **डिबगिंग कठिनाई** | निर्देश स्तर पर तर्क का पता लगाना कठिन है | डिबगर्स (जीडीबी) का उपयोग करें; उदारतापूर्वक टिप्पणियाँ जोड़ें |
---

## सिंटैक्स उदाहरण (x86-64 असेंबली - NASM)
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

### एआरएम असेंबली उदाहरण
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

## उन्नत सिंटैक्स और पैटर्न
### x86-64 एड्रेसिंग मोड
कुशल असेंबली लिखने के लिए एड्रेसिंग मोड को समझना महत्वपूर्ण है। प्रत्येक मोड नियंत्रित करता है कि ऑपरेंड कैसे स्थित हैं।
| मोड | सिंटैक्स (एनएएसएम) | विवरण |
|------|----------------------|----------------|
| **तत्काल** |  __संरक्षित_0__ | ऑपरेंड एक स्थिर मान है |
| **रजिस्टर** |  __संरक्षित_1__ | ऑपरेंड एक रजिस्टर में है |
| **प्रत्यक्ष** |  __संरक्षित_2__ | ऑपरेंड एक निश्चित मेमोरी एड्रेस पर है |
| **अप्रत्यक्ष पंजीकरण** |  __संरक्षित_3__ | ऑपरेंड एक रजिस्टर में पते पर है |
| **आधार + विस्थापन** |  __संरक्षित_4__ | पता = रजिस्टर + स्थिर ऑफसेट |
| **स्केल्ड इंडेक्स** |  __संरक्षित_5__ | पता = आधार + (सूचकांक × पैमाना) |
| **पूर्ण एसआईबी** |  __संरक्षित_6__ | आधार + (सूचकांक × स्केल) + विस्थापन |
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

### मैक्रो सिस्टम (एनएएसएम)
मैक्रोज़ आपको मापदंडों के साथ पुन: प्रयोज्य निर्देश अनुक्रमों को परिभाषित करने देते हैं, जिससे असेंबली कम दोहरावदार हो जाती है।
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

### स्टैक फ़्रेम लेआउट
फ़ंक्शन लिखने और डिबगिंग के लिए स्टैक फ़्रेम को समझना आवश्यक है।
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

## वास्तुकला एवं सिस्टम डिज़ाइन
### एक विशिष्ट x86-64 लिनक्स प्रक्रिया का मेमोरी लेआउट
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

### कार्यक्रम संरचना सम्मेलन
एक सुव्यवस्थित असेंबली कार्यक्रम चिंताओं को अलग-अलग वर्गों में अलग करता है:
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

### विशिष्ट परियोजना निर्देशिका संरचना
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### लिनक्स पर NASM + GCC
सबसे आम वर्कफ़्लो लिंकर के रूप में जीसीसी का उपयोग करके असेंबली को सी से जोड़ता है।
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

### विंडोज़ पर एमएएसएम (एमएल64)
```batch
@echo off
REM build.bat — MASM build script for Windows x64
ml64 /c /Zi /Fo main.obj main.asm
link /SUBSYSTEM:CONSOLE /DEBUG /OUT:program.exe main.obj kernel32.lib
```

### एटी एंड टी सिंटैक्स के साथ गैस (जीएनयू असेंबलर)।
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

### प्योर असेंबली प्रोग्राम को लिंक करना (कोई सी रनटाइम नहीं)
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

## महत्वपूर्ण अवधारणाएं
| संकल्पना | विवरण |
|---------|-----------------|
| **रजिस्टर** | सीपीयू का आंतरिक भंडारण (EAX, EBX, ECX, EDX x86 पर; R0-R15 ARM पर) |
| **स्मृति संबोधन** | पतों के माध्यम से रैम तक पहुंच (`MOV EAX, [0x1000]`) |
| **स्टैक** | फ़ंक्शन कॉल और स्थानीय चर के लिए LIFO मेमोरी क्षेत्र (`PUSH`, `POP`) |
| **निर्देश** | बुनियादी संचालन: अंकगणित, तर्क, डेटा आंदोलन, नियंत्रण प्रवाह |
| **व्यवधान/सिसकॉल** | ऑपरेटिंग सिस्टम से सेवाओं का अनुरोध |
| **कॉलिंग कन्वेंशन** | फ़ंक्शंस कैसे पैरामीटर प्राप्त करते हैं और मान लौटाते हैं (आर्किटेक्चर के अनुसार भिन्न होता है) |
---

## परीक्षण एवं डिबगिंग
### जीडीबी (जीएनयू डिबगर)
GDB Linux पर असेंबली के लिए मानक डिबगर है। यह आपको निर्देशों के माध्यम से आगे बढ़ने, रजिस्टरों का निरीक्षण करने और मेमोरी की जांच करने की सुविधा देता है।
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

### NASM मैक्रोज़ के साथ डिबगिंग
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

### सामान्य डिबगिंग पैटर्न
| समस्या | लक्षण | डिबगिंग तकनीक |
|--|---|-----|
| सेगफॉल्ट | SIGSEGV के साथ प्रोग्राम क्रैश हो गया | सूचक मानों की जाँच करें; स्टैक संरेखण सत्यापित करें |
| अनंत पाश | प्रोग्राम हैंग हो गया | लूप में ब्रेकपॉइंट सेट करें; झंडों की स्थिति जांचें |
| गलत परिणाम | गलत गणना | अंकगणित के माध्यम से कदम बढ़ाएं; प्रत्येक ऑप के बाद रजिस्टर मानों की जाँच करें |
| ढेर भ्रष्टाचार | आरईटी पर क्रैश | पुश/पॉप संतुलन सत्यापित करें; आरएसपी संरेखण की जांच करें (16-बाइट संरेखित होना चाहिए) |
| ग़लत सिस्कल | अप्रत्याशित कर्नेल व्यवहार | RAX में syscall नंबर सत्यापित करें; तर्क रजिस्टरों की जाँच करें |
---

## अंतरसंचालनीयता
### असेंबली से सी फ़ंक्शंस को कॉल करना
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

### सिस्टम कॉल संदर्भ (लिनक्स x86-64)
| सिस्कल | रैक्स | Arg1 (आरडीआई) | Arg2 (RSI) | Arg3 (आरडीएक्स) | Arg4 (R10) |
|--|-----|--|----|--|----|
| पढ़ें | 0 | एफडी | बफ | गिनती | — |
| लिखें | 1 | एफडी | बफ | गिनती | — |
| खुला | 2 | पथनाम | झंडे | मोड | — |
| बंद करें | 3 | एफडी | — | — | — |
| एमएमएपी | 9 | पता | लंबाई | विरोध | झंडे |
| बाहर निकलें | 60 | स्थिति | — | — | — |
### सी (जीसीसी) में इनलाइन असेंबली
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

## डिज़ाइन पैटर्न
### पैटर्न 1: एक्युमुलेटर के साथ लूप
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

### पैटर्न 2: स्ट्रिंग प्रोसेसिंग पाइपलाइन
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

### पैटर्न 3: डिस्पैच टेबल (स्विच/केस)
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

### पैटर्न 4: लिंक्ड सूची ट्रैवर्सल
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

## प्रदर्शन एवं अनुकूलन
### अनुदेश निर्धारण
आधुनिक सीपीयू पाइपलाइनिंग और आउट-ऑफ-ऑर्डर निष्पादन के माध्यम से प्रति चक्र कई निर्देशों को निष्पादित करते हैं। इसे समझने से तेजी से असेंबली लिखने में मदद मिलती है।
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

### कैश अनुकूलन
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

### अनुकूलन चेकलिस्ट
| तकनीक | प्रभाव | विवरण |
|----|-------|----|
| **उपयोग पंजीकृत करें** | उच्च | रजिस्टरों में गर्म चर रखें; मेमोरी एक्सेस से बचें |
| **लूप का खुलना** | मध्यम | प्रति पुनरावृत्ति एकाधिक आइटम संसाधित करके लूप ओवरहेड को कम करें |
| **सिमड (एसएसई/एवीएक्स)** | बहुत ऊँचा | वेक्टर निर्देशों के साथ 4-16 मानों को एक साथ प्रोसेस करें |
| **शाखा उन्मूलन** | मध्यम | जहां संभव हो सशर्त छलांग के बजाय सीएमओवी का उपयोग करें |
| **कैश संरेखण** | मध्यम | हॉट लूप्स को 16/32-बाइट सीमाओं पर संरेखित करें |
| **मेमोरी एक्सेस पैटर्न** | उच्च | अनुक्रमिक पहुंच; कैश-लाइन विभाजन से बचें |
---

## परिनियोजन और वास्तविक दुनिया में उपयोग
### असेंबली प्रोग्राम कैसे तैनात किए जाते हैं
असेंबली प्रोग्राम सीधे मूल मशीन कोड निष्पादन योग्य में संकलित होते हैं। इसमें कोई रनटाइम, कोई वीएम और किसी दुभाषिया की आवश्यकता नहीं है। परिनियोजन बाइनरी को लक्ष्य प्रणाली में कॉपी करने जितना सरल है।
```bash
# Build a static binary (no shared library dependencies)
nasm -f elf64 program.asm -o program.o
ld -static program.o -o program

# The resulting binary runs on any compatible Linux system
file program
# program: ELF 64-bit LSB executable, x86-64, statically linked
```

### वास्तविक दुनिया में उपयोग के मामले
| उद्योग | आवेदन | विधानसभा क्यों |
|---|----|---|
| **ऑपरेटिंग सिस्टम** | लिनक्स कर्नेल बूट स्टब, विंडोज़ एचएएल | प्रत्यक्ष हार्डवेयर नियंत्रण, व्यवधान प्रबंधन |
| **एम्बेडेड फ़र्मवेयर** | माइक्रोकंट्रोलर बूटलोडर, IoT डिवाइस | कोई ओएस या रनटाइम उपलब्ध नहीं; सख्त स्मृति सीमाएं |
| **सुरक्षा** | शोषण विकास, मैलवेयर विश्लेषण, रिवर्स इंजीनियरिंग | संकलित बायनेरिज़ के साथ बातचीत करने का एकमात्र तरीका |
| **गेम इंजन** | SIMD-अनुकूलित गणित (मैट्रिक्स रूपांतरण, भौतिकी) | प्रति-फ़्रेम गणना के लिए अधिकतम थ्रूपुट |
| **संकलक** | कोड जेनरेशन बैकएंड (एलएलवीएम, जीसीसी) | अनुकूलित मशीन कोड उत्सर्जित करना |
| **क्रिप्टोग्राफी** | एईएस-एनआई, एसएचए अनुदेश त्वरण | हार्डवेयर-त्वरित क्रिप्टो संचालन |
| **डिवाइस ड्राइवर** | GPU ड्राइवर, नेटवर्क कार्ड फ़र्मवेयर | डायरेक्ट रजिस्टर-स्तरीय हार्डवेयर एक्सेस |
### लीगेसी सिस्टम एकीकरण
कई विरासत प्रणालियों में सी कोडबेस के भीतर एम्बेडेड असेंबली रूटीन होते हैं। ये आमतौर पर प्रदर्शन-महत्वपूर्ण कार्य या हार्डवेयर-विशिष्ट रूटीन हैं जिन्हें दशकों से बनाए रखा गया है।
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

## असेंबली का उपयोग कब करें
| परिदृश्य | विधानसभा क्यों | बेहतर विकल्प |
|---|---|-----|
| ओएस कर्नेल विकास | बूट कोड, इंटरप्ट हैंडलर | अधिकांश कर्नेल कोड के लिए C |
| डिवाइस ड्राइवर | प्रत्यक्ष हार्डवेयर पहुंच | सी, जंग |
| रिवर्स इंजीनियरिंग/सुरक्षा | संकलित बायनेरिज़ का विश्लेषण करने का एकमात्र तरीका | — |
| प्रदर्शन-महत्वपूर्ण कोड | अधिकतम अनुकूलन | कंपाइलर इंट्रिनिक्स के साथ सी/सी++ |
| एंबेडेड फ़र्मवेयर (नंगे धातु) | कोई उच्च स्तरीय भाषा उपलब्ध नहीं है | सी, जंग |
| शिक्षा | कंप्यूटर आर्किटेक्चर को समझना | — |
| सामान्य अनुप्रयोग विकास | जटिल कार्यक्रमों के लिए अव्यावहारिक | कोई भी उच्च स्तरीय भाषा |
---

## सारांश
असेंबली भाषा मानव-पठनीय कोड और सीपीयू द्वारा निष्पादित कच्चे बाइनरी के बीच का पुल है। यह अनुप्रयोगों के निर्माण के लिए एक व्यावहारिक विकल्प नहीं है, लेकिन यह समझने के लिए आवश्यक है कि कंप्यूटर निम्नतम स्तर पर कैसे काम करते हैं। सिस्टम प्रोग्रामर, सुरक्षा शोधकर्ताओं और एम्बेडेड डेवलपर्स के लिए, असेंबली ज्ञान अमूल्य है। बाकी सभी के लिए, असेंबली अवधारणाओं (रजिस्टर, स्टैक, निर्देश चक्र) को समझना आपको किसी भी भाषा में एक बेहतर प्रोग्रामर बनाता है।