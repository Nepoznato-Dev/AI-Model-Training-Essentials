---
# Metadata
title: "Shell & PowerShell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Shell and PowerShell ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [shell, powershell, bash, ecosystem, tooling, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Shell & PowerShell — คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นสำหรับการเขียนสคริปต์เชลล์ (Bash/Zsh) และ PowerShell
---

## การใช้งานเชลล์
| เชลล์ | แพลตฟอร์ม | หมายเหตุ |
|-------|----------|-------|
| **ทุบตี** | ยูนิกซ์/ลินุกซ์/macOS | ใช้กันอย่างแพร่หลายที่สุด |
| **Zsh** | ค่าเริ่มต้นของ macOS | ทุบตีขั้นสูง |
| **ปลา** | ข้ามแพลตฟอร์ม | ใช้งานง่าย |
| **เส้นประ** | เดเบียน/อูบุนตู | รวดเร็ว รองรับ POSIX |
| **ksh** | ยูนิกซ์ | เปลือกกร |
| **พาวเวอร์เชลล์** | ข้ามแพลตฟอร์ม | เชิงวัตถุ (pwsh) |
| **สรุป** | ข้ามแพลตฟอร์ม | เชลล์ข้อมูลที่มีโครงสร้าง |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## ผู้จัดการแพ็คเกจ (เครื่องมือเชลล์)
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **โฮมบรูว์** | ตัวจัดการแพ็คเกจ macOS/Linux |
| **ฉลาด / ยำ / dnf** | ตัวจัดการแพ็คเกจ Linux |
| **แพ็ก** | ตัวจัดการแพ็คเกจ FreeBSD |
| **สกู๊ป** | ตัวติดตั้ง Windows CLI |
| **ช็อคโกแลต** | ตัวจัดการแพ็คเกจ Windows |
| **ปีก** | ตัวจัดการแพ็คเกจ Windows |
```bash
# Homebrew
brew install jq ripgrep fd bat    # install tools
brew upgrade                      # upgrade all

# apt (Debian/Ubuntu)
sudo apt update && sudo apt install -y jq curl

# PowerShell
Install-Module -Name PSReadLine -Force
```

---

## เครื่องมือ CLI ที่จำเป็น
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **เจคิว** | การประมวลผล JSON |
| **ใช่แล้ว** | การประมวลผล YAML |
| **ripgrep (rg)** | grep รวดเร็ว |
| **เอฟดี** | ค้นหาอย่างรวดเร็ว |
| **ค้างคาว** | ปรับปรุงแมว |
| **exa / eza** | ปรับปรุง ls |
| **fzf** | ตัวค้นหาเลือน |
| **htop** | โปรแกรมดูกระบวนการ |
| **tmux** | เทอร์มินัลมัลติเพล็กเซอร์ |
| **ขด / wget** | คำขอ HTTP |
| **sed / awk** | การประมวลผลข้อความ |
| **xargs** | สร้างคำสั่งจากอินพุต |
| **ทำ** | นักวิ่งงาน |
| **ทางเข้า** | รันคำสั่งเกี่ยวกับการเปลี่ยนแปลงไฟล์ |
| **ขนาน** | การดำเนินการแบบขนาน |
| **เช็คเชลล์** | เชลล์สคริปต์ linter |
---

## กรอบงานเชลล์และการปรับปรุง
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **โอ้ มาย ซช** | กรอบงาน Zsh (ธีม, ปลั๊กอิน) |
| **เพรซโต** | กรอบงาน Zsh (เร็วกว่า) |
| **เอ็นเตอร์ไพรส์** | พรอมต์ Cross-shell |
| **zsh-คำแนะนำอัตโนมัติ** | คำแนะนำอัตโนมัติ |
| **zsh-เน้นไวยากรณ์** | การเน้นไวยากรณ์ |
| **ทุบตีมัน** | กรอบทุบตี |
| **ทูอิน** | ประวัติเชลล์ (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## โมดูล PowerShell
| โมดูล | วัตถุประสงค์ |
|--------|---------|
| **PSReadLine** | การแก้ไขบรรทัดคำสั่งที่ได้รับการปรับปรุง |
| **ตัวรบกวน** | กรอบการทดสอบ |
| **PSScriptAnalyzer** | สำลี |
| **posh-git** | บูรณาการ Git |
| **เทอร์มินัล-ไอคอน** | ไอคอนไฟล์ |
| **PSWindowsUpdate** | อัพเดต Windows |
| **แอซ** | การจัดการ Azure |
| **AWSPowerShell** | การจัดการ AWS |
| **SqlServer** | การจัดการเซิร์ฟเวอร์ SQL |
| **โพด** | กรอบงานเว็บ |
| **แดชบอร์ดสากล** | เว็บแดชบอร์ด |
```powershell
# Install modules
Install-Module -Name PSReadLine -Force
Install-Module -Name Pester -Force
Install-Module -Name PSScriptAnalyzer -Force
Install-Module -Name Az -Force

# Import module
Import-Module Az
```

---

## การทดสอบ
| กรอบ | เชลล์ | วัตถุประสงค์ |
|----------|-------|---------|
| **ค้างคาว** | ทุบตี | Bash การทดสอบอัตโนมัติ |
| **shunit2** | เชลล์ | การทดสอบสไตล์ xUnit |
| **ตัวรบกวน** | พาวเวอร์เชลล์ | การทดสอบและการเยาะเย้ย |
| **assert.sh** | ทุบตี | ไลบรารีการยืนยัน |
```bash
# Bats example
#!/usr/bin/env bats

@test "addition" {
  result=$((2 + 3))
  [ "$result" -eq 5 ]
}

@test "file exists" {
  [ -f "/etc/passwd" ]
}

@test "command succeeds" {
  run echo "hello"
  [ "$status" -eq 0 ]
  [ "$output" = "hello" ]
}
```

```powershell
# Pester example
Describe "UserService" {
    It "finds user by id" {
        $user = Get-User -Id 1
        $user.Name | Should -Be "Alice"
    }
    
    It "throws when user not found" {
        { Get-User -Id 999 } | Should -Throw
    }
}
```

---

## คุณภาพรหัส
| เครื่องมือ | เชลล์ | วัตถุประสงค์ |
|-|-------|---------|
| **เชลล์เช็ค** | ทุบตี / Zsh | การวิเคราะห์ขุยและแบบคงที่ |
| **shfmt** | ทุบตี / Zsh | การจัดรูปแบบโค้ด |
| **PSScriptAnalyzer** | พาวเวอร์เชลล์ | สำลี |
| **การตั้งค่า PSScript** | พาวเวอร์เชลล์ | การจัดรูปแบบ |
```bash
# ShellCheck
shellcheck script.sh        # lint
shellcheck -s bash script.sh  # specify shell

# shfmt
shfmt -w script.sh          # format
shfmt -d script.sh          # diff (check only)
```

```powershell
# PSScriptAnalyzer
Invoke-ScriptAnalyzer -Path .\script.ps1
Invoke-ScriptAnalyzer -Path .\script.ps1 -Fix  # auto-fix
```

---

## ไลบรารีและรูปแบบที่สำคัญ
### ทุบตี
| รูปแบบ | วัตถุประสงค์ |
|---------|---------|
| **set -euo pipefail** | โหมดเข้มงวด |
| **กับดัก** | การจัดการสัญญาณ |
| **ที่มา / .** | รวมไฟล์ |
| **getopts** | การแยกวิเคราะห์อาร์กิวเมนต์ |
| **เอกสาร** | สตริงหลายบรรทัด |
| **การทดแทนกระบวนการ** | `<()`และ`>()`|
| **อาร์เรย์** | จัดทำดัชนีและเชื่อมโยง |
```bash
#!/usr/bin/env bash
set -euo pipefail

# Functions
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

# Argument parsing
while getopts "hn:v" opt; do
  case $opt in
    h) echo "Usage: $0 [-h] [-n name] [-v]"; exit 0 ;;
    n) NAME="$OPTARG" ;;
    v) VERBOSE=true ;;
  esac
done

# Cleanup trap
cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT
```

### พาวเวอร์เชลล์
| รูปแบบ | วัตถุประสงค์ |
|---------|---------|
| **CmdletBinding** | ฟังก์ชั่นขั้นสูง |
| **พารามิเตอร์** | แอ็ตทริบิวต์พารามิเตอร์ |
| **ไปป์ไลน์** | ไปป์ไลน์วัตถุ |
| **ลอง/จับ** | การจัดการข้อผิดพลาด |
| **ชั้นเรียน** | อุ๊ย |
```powershell
function Get-User {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Id,
        
        [ValidateSet("json", "xml")]
        [string]$Format = "json"
    )
    
    try {
        $user = Invoke-RestMethod -Uri "https://api.example.com/users/$Id"
        return $user
    }
    catch {
        Write-Error "Failed to get user: $_"
    }
}
```

---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **รหัส VS** | รองรับเชลล์/PowerShell |
| **นีโอวิม** | บนเทอร์มินัล |
| **เทอร์มินัล Windows** | เทอร์มินัลสมัยใหม่ (PowerShell) |
| **iTerm2** | เทอร์มินัล macOS |
| **วาร์ป** | เทอร์มินัลที่ขับเคลื่อนด้วย AI |
| **อลาคริตตี** | เทอร์มินัลที่เร่งด้วย GPU |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ครอน** | งานที่กำหนดเวลาไว้ (Unix) |
| **systemd** | การจัดการบริการ (Linux) |
| **ตัวกำหนดเวลางาน** | งานที่กำหนดเวลาไว้ของ Windows |
| **จุดเข้าเทียบท่านักเทียบท่า** | สคริปต์คอนเทนเนอร์ |
| **ไปป์ไลน์ CI/CD** | การดำเนินการ GitHub, GitLab CI |
| **เข้าใจได้** | การจัดการการกำหนดค่า |
| **ภูมิประเทศ** | โครงสร้างพื้นฐานเป็นรหัส |
---

## สรุป
ระบบนิเวศของการเขียนสคริปต์เชลล์มีความหลากหลาย: **Bash** ยังคงเป็นมาตรฐานสากล **Zsh** เป็นค่าเริ่มต้นสมัยใหม่สำหรับการใช้งานเชิงโต้ตอบ และ **PowerShell** ครอบงำการดูแลระบบ Windows สแต็กมาตรฐานคือ: **Bash/Zsh** สำหรับการเขียนสคริปต์ **ShellCheck** สำหรับ Linting **shfmt** สำหรับการจัดรูปแบบ **Bats** สำหรับการทดสอบ **jq** สำหรับ JSON **ripgrep** สำหรับการค้นหา และ **tmux** สำหรับเทอร์มินัลมัลติเพล็กซ์ สำหรับ PowerShell: **Pester** สำหรับการทดสอบ **PSScriptAnalyzer** สำหรับขุย และ **PSReadLine** สำหรับการแก้ไขที่ได้รับการปรับปรุง การเขียนสคริปต์เชลล์เป็นสิ่งจำเป็นสำหรับระบบอัตโนมัติ, CI/CD, การดูแลระบบ และเวิร์กโฟลว์ DevOps