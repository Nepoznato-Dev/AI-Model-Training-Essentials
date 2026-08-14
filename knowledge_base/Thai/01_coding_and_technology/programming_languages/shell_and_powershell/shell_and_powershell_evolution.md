<!--
---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Shell & PowerShell — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์ของ Unix Shell
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| ทอมป์สัน ช | 1971 | เชลล์ Unix ตัวแรก (Ken Thompson) |
| บอร์น ช | 2520 | **`sh`** — การเขียนสคริปต์ ตัวแปร โฟลว์ควบคุม |
| ซีเอสเอช | 1978 | ไวยากรณ์เหมือน C, การควบคุมงาน, นามแฝง |
| ksh | 1983 | คอร์นเชลล์ — คุณสมบัติ`sh`+`csh`|
| ทุบตี | 1989 | **Bourne Again Shell** — การแทนที่ GNU`sh`|
| ทุบตี 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| ทุบตี 3.0 | 2547 | `=~`regex,`|&`|
| ทุบตี 4.0 | 2552 | **อาร์เรย์ที่เกี่ยวข้อง**,`mapfile`,`declare -g`|
| ทุบตี 4.3 | 2014 | ค้นพบช่องโหว่ Shellshock |
| ทุบตี 5.0 | 2019 | `declare -n`การอ้างอิงชื่อ,`printf %q`|
| ทุบตี 5.1 | 2020 | `wait -n`, การปรับปรุง`shopt`|
| ทุบตี 5.2 | 2022 | `${var@U}`(ตัวพิมพ์ใหญ่),`shopt -s compat`|
| zsh | 1990 | Extended bash — เสร็จสิ้น, ธีม |
| ปลา | 2548 | **ใช้งานง่าย** — คำแนะนำอัตโนมัติ การเน้นไวยากรณ์ |
| สรุป | 2019 | ข้อมูลที่มีโครงสร้างไปป์ไลน์ของตาราง |
| น้ำมัน/osh | 2020 | เข้ากันได้กับ Bash ด้วยความหมายที่ดีกว่า |
## ไทม์ไลน์ของ PowerShell
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| 1.0 | 2549 | การเปิดตัวครั้งแรก (Microsoft, Jeffrey Snover) |
| 2.0 | 2552 | **โมดูล** งานระยะไกล งานเบื้องหลัง ธุรกรรม |
| 3.0 | 2555 | เวิร์กโฟลว์`Invoke-RestMethod`งานที่กำหนดเวลาไว้ |
| 4.0 | 2013 | **การกำหนดค่าสถานะที่ต้องการ (DSC)** การปรับปรุง`if`/`switch`|
| 5.0 | 2559 | **คลาส**,`enum`,`using`,`using module`|
| 5.1 | 2017 | เวอร์ชันล่าสุดเฉพาะ Windows |
| 6.0 | 2018 | **PowerShell Core** — ข้ามแพลตฟอร์ม (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(ทดลอง) |
| 6.2 | 2019 | `&&`/`||`ตัวดำเนินการโซ่ไปป์ไลน์ |
| 7.0 | 2020 | **หลัก**:`?.`แบบมีเงื่อนไข null,`??`การรวมเป็น null,`using assembly`|
| 7.1 | 2020 | ตัวดำเนินการแบบไตรภาค`? :`การปรับปรุง`using module`|
| 7.2 | 2021 | **รุ่น LTS** การปรับปรุง`using namespace`|
| 7.3 | 2022 |  การปรับปรุง`switch`ตัวเลือก`ErrorView`|
| 7.4 | 2023 |  การปรับปรุง `using module`,`Get-Error`|
| 7.5 | 2024 | การปรับปรุงประสิทธิภาพ`PSResourceGet`|
| 7.6 | 2025 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### มรดก Unix Shell (1971–1989)
- **1971**: Thompson Shell — เชลล์ Unix ตัวแรก การดำเนินการคำสั่งอย่างง่าย
- **1977**: บอร์นเชลล์ (`sh`) — ตัวแปร, โฟลว์ควบคุม (`if`,`while`), เอกสารที่นี่
- **1978**: C เชลล์ (`csh`) — ไวยากรณ์คล้าย C, การควบคุมงาน, นามแฝง, ประวัติ
- **1983**: Korn เชลล์ (`ksh`) — ดีที่สุดของ`sh`+ `csh`
### ทุบตี - เดอะสแตนดาร์ด (2532–ปัจจุบัน)
- **1989**: Brian Fox สร้าง bash สำหรับโปรเจ็กต์ GNU — Bourne Again Shell
- **2.0 (1996)**: การทดสอบ `[[ ]]`, เลขคณิต `(( ))`,`+=`
- **4.0 (2009)**: อาร์เรย์เชื่อมโยง (`declare -A`),`mapfile`
- **5.0 (2019)**: เนมเรฟ,`printf %q`
- **5.2 (2022)**: การจัดการสตริงเคส
### zsh - เชลล์ผู้ใช้ระดับสูง (1990–ปัจจุบัน)
- **1990**: Paul Falstad สร้าง zsh — รวมฟีเจอร์ bash, ksh, tcsh
- **2000s**: เฟรมเวิร์ก oh-my-zsh — ธีม, ปลั๊กอิน, ส่วนเสริม
- **2019**: เชลล์เริ่มต้นของ macOS (แทนที่ bash)
### ปลา - The Friendly Shell (2548–ปัจจุบัน)
- **2005**: Axel Liljankrantz สร้างปลา — "ในที่สุด เปลือกแบบโต้ตอบได้"
- คำแนะนำอัตโนมัติ การเน้นไวยากรณ์ การกำหนดค่าบนเว็บ
- ไม่รองรับการทุบตี — ภาษาสคริปต์ที่แตกต่างกัน
### PowerShell — Microsoft's Shell (2549–ปัจจุบัน)
- **2006**: PowerShell 1.0 — ไปป์ไลน์วัตถุที่ใช้ .NET, cmdlets
- **2.0 (2009)**: โมดูล งานระยะไกล งานเบื้องหลัง
- **5.0 (2016)**: คลาส, การแจกแจง
- **6.0 (2018)**: **ข้ามแพลตฟอร์ม** — PowerShell Core (สร้างบน .NET Core)
- **7.0 (2020)**:`?.`แบบมีเงื่อนไข Null,`??`แบบรวมค่า Null,`?:`แบบไตรภาค
## วิวัฒนาการไวยากรณ์
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

## หลักการออกแบบที่สำคัญ
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

## การเติบโตของระบบนิเวศ
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
