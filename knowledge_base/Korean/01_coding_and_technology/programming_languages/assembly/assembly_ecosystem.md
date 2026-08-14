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
# 조립 - 생태계 및 툴링 가이드
이 가이드에서는 어셈블리 생태계의 필수 도구, 어셈블러 및 인프라를 다룹니다.
---

## 아키텍처별 어셈블러
### x86/x86-64
| 어셈블러 | 플랫폼 | 메모 |
|------------|----------|-------|
| **NASM** | 크로스 플랫폼 | 가장 인기 있고 깔끔한 구문 |
| **마스** | 윈도우 | Microsoft 매크로 어셈블러 |
| **FASM** | 크로스 플랫폼 | 자체 호스팅, 빠른 |
| **가스(as)** | 리눅스/유닉스 | GNU 어셈블러(AT&T 구문) |
| **야스** | 크로스 플랫폼 | NASM 호환 |
| **UASM** | 크로스 플랫폼 | MASM 호환 |
### 팔
| 어셈블러 | 플랫폼 | 메모 |
|------------|----------|-------|
| **GNU(ARM)** | 크로스 플랫폼 | ARM 조립 |
| **케일 ASM** | 임베디드 | ARM 개발 |
| **ARM 어셈블러** | 팔 | ARM 컴파일러 제품군 |
### 다른
| 어셈블러 | 건축 | 메모 |
|------------|-------------|-------|
| **avr-as** | AVR | 마이크로컨트롤러 |
| **람** | Z80 | 레트로 컴퓨팅 |
| **ca65** | 6502 | NES, 코모도어 |
| **스핌 / 화성** | MIPS | 교육 |
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

## 디버거
| 도구 | 건축 | 목적 |
|------|-------------|---------|
| **GDB** | x86/ARM | GNU 디버거 |
| **lldb** | 크로스 플랫폼 | LLVM 디버거 |
| **x64dbg** | x86/x86-64 | Windows GUI 디버거 |
| **올리Dbg** | x86 | 클래식 Windows 디버거 |
| **IDA 프로** | 크로스 플랫폼 | 디스어셈블러/디컴파일러 |
| **기드라** | 크로스 플랫폼 | NSA 리버스 엔지니어링 |
| **레이더2** | 크로스 플랫폼 | CLI 리버스 엔지니어링 |
| **커터** | 크로스 플랫폼 | Radare2용 GUI |
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

## 에뮬레이터 및 시뮬레이터
| 도구 | 건축 | 목적 |
|------|-------------|---------|
| **QEMU** | 멀티아치 | 전체 시스템 에뮬레이션 |
| **보흐스** | x86 | x86 에뮬레이터 |
| **DOSBox** | x86 | DOS 환경 |
| **마메** | 멀티 | 아케이드/복고풍 에뮬레이션 |
| **스핌** | MIPS | MIPS 시뮬레이터 |
| **화성** | MIPS | MIPS IDE/시뮬레이터 |
| **심AVR** | AVR | AVR 시뮬레이터 |
| **유니콘** | 멀티아치 | CPU 에뮬레이션 프레임워크 |
---

## 빌드 도구
| 도구 | 목적 |
|------|---------|
| **만들기** | 클래식 빌드 자동화 |
| **CMake** | 크로스 플랫폼 빌드 |
| **ld** | GNU 링커 |
| **일드** | LLVM 링커 |
| **객체복사** | 바이너리 조작 |
| **objdump** | 분해 |
| **readelf / nm** | 기호검사 |
| **헥스 덤프** | 바이너리 검사 |
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

## 주요 라이브러리
| 도서관 | 건축 | 목적 |
|---------|-------------|---------|
| **libc** | x86/ARM | 표준 C 라이브러리(syscall 래퍼) |
| **리눅스 시스템콜** | x86/ARM | 직접 커널 호출 |
| **윈도우 API** | x86/x64 | Win32/64 API |
| **BIOS 인터럽트** | x86 | 레거시 PC BIOS |
| **DOS 인터럽트** | x86 | DOS 서비스 |
| **libgcc** | 크로스 플랫폼 | GCC 런타임 |
| **뉴립** | 임베디드 | 경량 libc |
---

## 테스트
| 도구 | 목적 |
|------|---------|
| **맞춤형 테스트 하네스** | 어셈블리 테스트 프레임워크 |
| **유니티** | C 기반 단위 테스트(혼합 프로젝트용) |
| **구글 테스트** | C++ 테스트(혼합 프로젝트용) |
| **맞춤 매크로** | 어설션 매크로 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **objdump -d** | 분해검사 |
| **기드라** | 리버스 엔지니어링 분석 |
| **IDA 프로** | 전문적인 분해 |
| **레이더2** | CLI 분석 |
| **발그린드** | 메모리 오류 감지 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + NASM** | 어셈블리 구문 강조 |
| **SASM** | 단순 ASM IDE(교육용) |
| **Emacs + nasm 모드** | 클래식 어셈블리 편집 |
| **화성** | MIPS 교육 IDE |
| **DOSBox + 편집** | 레트로 개발 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **정적 바이너리** | 직접 기계어 |
| **부팅 섹터** | 512바이트 부트로더 |
| **커널 모듈** | OS 커널 코드 |
| **펌웨어** | 임베디드 펌웨어 |
| **ROM/플래시** | 마이크로컨트롤러 코드 |
| **도커** | 빌드 환경 |
---

## 요약
Assembly의 생태계는 아키텍처에 따라 다르며 설계상 최소화되어 있습니다. 표준 툴체인은 어셈블리용 **NASM**(x86/x86-64) 또는 **GNU as**(ARM), 연결용 **ld**, 디버깅용 **GDB**, 리버스 엔지니어링용 **Ghidra** 또는 **IDA Pro**, 에뮬레이션용 **QEMU**입니다. Assembly는 운영 체제 개발, 임베디드 시스템, 리버스 엔지니어링, 성능이 중요한 코드 및 부트로더 개발에 탁월합니다. 생태계는 컴퓨터가 가장 낮은 수준에서 작동하는 방식을 이해하는 데 필수적입니다. 학습을 위해 **MARS**(MIPS) 및 **SASM**(x86)은 초보자에게 친숙한 환경을 제공합니다.