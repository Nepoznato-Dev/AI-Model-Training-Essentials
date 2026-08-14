---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [shell, powershell, bash, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# 셸 및 PowerShell - 버전 기록 및 발전
## 유닉스 쉘 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 톰슨 쉬 | 1971 | 최초의 Unix 쉘(Ken Thompson) |
| 본 쉬 | 1977 | **`sh`** — 스크립팅, 변수, 제어 흐름 |
| csh | 1978 | C와 유사한 구문, 작업 제어, 별칭 |
| 크쉬 | 1983년 | Korn 쉘 —`sh`+`csh`기능 |
| 강타 | 1989 | **Bourne Again Shell** — GNU`sh`대체 |
| 배쉬 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| 배쉬 3.0 | 2004년 | `=~`정규식,`|&`|
| 배쉬 4.0 | 2009 | **연관 배열**,`mapfile`,`declare -g`|
| 배쉬 4.3 | 2014 | Shellshock 취약점 발견 |
| 배쉬 5.0 | 2019 | `declare -n`이름 참조,`printf %q`|
| 배쉬 5.1 | 2020 | `wait -n`,`shopt`개선 |
| 배쉬 5.2 | 2022 |  `${var@U}`(대문자),`shopt -s compat`|
| zsh | 1990 | 확장된 bash — 완성, 테마 |
| 물고기 | 2005년 | **사용자 친화적** — 자동 제안, 구문 강조 |
| 간단히 말해서 | 2019 | 구조화된 데이터, 테이블 파이프라인 |
| 석유/산업안전보건 | 2020 | 더 나은 의미론으로 Bash와 호환 가능 |
## 파워셸 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 2006년 | 최초 릴리스(Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **모듈**, 원격, 백그라운드 작업, 트랜잭션 |
| 3.0 | 2012 | 워크플로, `Invoke-RestMethod`, 예약된 작업 |
| 4.0 | 2013 | **원하는 상태 구성(DSC)**,`if`/`switch`개선 |
| 5.0 | 2016 | **클래스**,`enum`,`using`,`using module`|
| 5.1 | 2017 | 마지막 Windows 전용 버전 |
| 6.0 | 2018 | **PowerShell Core** — 크로스 플랫폼(Windows, Linux, macOS) |
| 6.1 | 2018 |  `ForEach-Object -Parallel`(실험적) |
| 6.2 | 2019 | `&&`/`||`파이프라인 체인 운영자 |
| 7.0 | 2020 | **주요**:`?.`null 조건부,`??`null 병합,`using assembly`|
| 7.1 | 2020 | 삼항 연산자`? :`,`using module`개선 |
| 7.2 | 2021 | **LTS 릴리스**,`using namespace`개선 |
| 7.3 | 2022 | `switch`개선,`ErrorView`옵션 |
| 7.4 | 2023년 | `using module`개선,`Get-Error`|
| 7.5 | 2024 | 성능 개선,`PSResourceGet`|
| 7.6 | 2025 | 지속적인 개발 |
## 주요 이정표
### 유닉스 쉘 유산(1971~1989)
- **1971**: Thompson 쉘 — 최초의 Unix 쉘, 간단한 명령 실행
- **1977**: Bourne 쉘(`sh`) — 변수, 제어 흐름(`if`,`while`), 여기 문서
- **1978**: C 쉘(`csh`) — C와 유사한 구문, 작업 제어, 별칭, 기록
- **1983**: Korn 쉘(`ksh`) —`sh`+`csh`중 최고
### bash — 표준(1989~현재)
- **1989**: Brian Fox가 GNU 프로젝트용 bash 생성 — Bourne Again Shell
- **2.0 (1996)**:`[[ ]]`테스트,`(( ))`산술,`+=`
- **4.0(2009)**: 연관 배열(`declare -A`),`mapfile`
- **5.0 (2019)**: 이름 참조,`printf %q`
- **5.2(2022)**: 문자열 대소문자 조작
### zsh — 고급 사용자 셸(1990~현재)
- **1990**: Paul Falstad가 zsh 생성 — bash, ksh, tcsh 기능 결합
- **2000년대**: oh-my-zsh 프레임워크 — 테마, 플러그인, 완성
- **2019**: macOS 기본 셸(bash 대체)
### 물고기 — 친근한 껍질(2005~현재)
- **2005**: Axel Liljankrantz가 물고기를 만듭니다 — "마지막으로 대화형 쉘이 탄생했습니다"
- 자동 제안, 구문 강조, 웹 기반 구성
- bash와 호환되지 않음 — 다른 스크립팅 언어
### PowerShell — Microsoft의 셸(2006~현재)
- **2006**: PowerShell 1.0 — .NET 기반, 개체 파이프라인, cmdlet
- **2.0(2009)**: 모듈, 원격, 백그라운드 작업
- **5.0 (2016)**: 클래스, 열거형
- **6.0(2018)**: **크로스 플랫폼** — PowerShell Core(.NET Core 기반)
- **7.0(2020)**: Null 조건부`?.`, Null 병합`??`, 삼항 `?:`
## 구문 진화
```bash
# Bourne shell (1977): Basic scripting
#!/bin/sh
name="World"
echo "Hello, $name"
for file in *.txt; do
  echo "Processing $file"
done

# bash 4.0: Associative arrays
declare -A colors
colors[red]="#FF0000"
colors[green]="#00FF00"
echo "${colors[red]}"

# bash 5.0+: Modern bash
mapfile -t lines < input.txt
for line in "${lines[@]}"; do
  echo "${line^^}"  # uppercase
done

# zsh + oh-my-zsh: Enhanced interactive
# Autosuggestions, syntax highlighting, git aliases

# fish: Modern interactive
# Autosuggestions, web config, not bash-compatible
function greet
    echo "Hello, $argv"
end
```

```powershell
# PowerShell 1.0: Basic cmdlets
Get-Process | Where-Object { $_.CPU -gt 100 }

# PowerShell 5.0: Classes
class Person {
    [string]$Name
    [int]$Age
    Person([string]$n, [int]$a) { $this.Name = $n; $this.Age = $a }
}

# PowerShell 7.0+: Modern syntax
$person = [Person]::new("Alice", 30)
$name = $person?.Name ?? "Unknown"  # null-conditional, null-coalescing
$result = $x -gt 0 ? "positive" : "non-positive"  # ternary

# PowerShell: Object pipeline (unique feature)
Get-ChildItem |
  Where-Object { $_.Extension -eq ".md" } |
  ForEach-Object { $_.FullName }
```

## 주요 디자인 원칙
```
Shell (bash/zsh):
1. "Text is the universal interface" — pipes connect everything
2. "Do one thing well" — small tools, compose via pipes
3. "Everything is a file" — Unix philosophy
4. "Backward compatible" — 40-year-old scripts still work

PowerShell:
1. "Objects, not text" — pipeline passes .NET objects
2. "Consistent" — Verb-Noun naming (Get-Process, Set-Location)
3. "Extensible" — modules, providers, remoting
4. "Cross-platform" — PowerShell 7+ runs everywhere
```

## 생태계 성장
```
1971: Thompson shell — first Unix shell
1977: Bourne shell (sh) — scripting begins
1989: bash — GNU shell, becomes Linux default
1990: zsh — power user shell
2005: fish — user-friendly shell
2006: PowerShell 1.0 — Microsoft's object shell
2010: oh-my-zsh — zsh framework (themes, plugins)
2018: PowerShell 6.0 — cross-platform
2019: nushell — structured data shell
2020: PowerShell 7.0 — modern syntax
2025: bash remains the default on Linux/macOS
       PowerShell dominates Windows administration
       zsh is macOS default; fish gaining popularity
```
