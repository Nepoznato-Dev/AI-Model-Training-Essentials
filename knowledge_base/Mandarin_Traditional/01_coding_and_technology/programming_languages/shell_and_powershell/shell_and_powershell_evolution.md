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
# Shell 和 PowerShell — 版本歷史和演變
## Unix Shell 時間線
|版本 |年份|關鍵主題 |
|--------|------|------------|
|湯普森·什| 1971 |第一個 Unix shell (Ken Thompson) |
|諜影重重 | 1977 | **`sh`** — 腳本、變數、控制流 |
| csh | 1978 |類別 C 文法、作業控制、別名 |
|克什 | 1983 | Korn shell —`sh`+`csh`功能 |
| bash | 1989 | **Bourne Again Shell** — GNU`sh`替代品 |
| bash 2.0 | bash 1996 | `[[ ]]`、`(( ))`、`+=` |
| bash 3.0 | bash 2004 |`=~`正規表示式，`|&` |
| bash 4.0 | bash 2009 | **關聯陣列**、`mapfile`、`declare -g` |
| bash 4.3 | bash 2014 |發現 Shellshock 漏洞 |
| bash 5.0 | bash 2019 | 2019`declare -n`名稱參考、`printf %q` |
| bash 5.1 | bash 2020 | `wait -n`、`shopt` 改進 |
| bash 5.2 | bash 2022 | 2022 `${var@U}`（大寫）、`shopt -s compat` |
| zsh | 1990 |擴充 bash — 完成、主題 |
|魚 | 2005 | **使用者友善** — 自動建議、語法反白 |
|努殼 | 2019 | 2019結構化資料、表格管道|
|石油/奧什 | 2020 |與 Bash 相容並具有更好的語義 |
## PowerShell 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 1.0 | 2006 |初始版本（Microsoft，Jeffrey Snover）|
| 2.0 | 2009 | **模組**、遠端處理、後台作業、事務 |
| 3.0 | 2012 |工作流程、`Invoke-RestMethod`、排程作業 |
| 4.0 | 2013 | **所需狀態配置 (DSC)**、`if` /`switch`改進 |
| 5.0 | 2016 | 2016 **類別**，`enum`，`using`，`using module` |
| 5.1 | 2017 | 2017最新僅 Windows 版本 |
| 6.0 | 2018 | **PowerShell Core** — 跨平台（Windows、Linux、macOS）|
| 6.1 | 2018 | `ForEach-Object -Parallel`（實驗）|
| 6.2 | 2019 | 2019`&&`/`||`管道鏈運營商 |
| 7.0 | 2020 | **主要**：`?.` 空條件、`??` 空合併、`using assembly` |
| 7.1 | 2020 |三元運算子`? :`、`using module`改進 |
| 7.2 | 2021 | **LTS 版本**，`using namespace` 改進 |
| 7.3 | 7.3 2022 | 2022`switch`改進、`ErrorView` 選項 |
| 7.4 | 7.4 2023 |`using module`改進，`Get-Error` |
| 7.5 | 7.5 2024 | 2024效能改進，`PSResourceGet` |
| 7.6 | 7.6 2025 | 2025持續發展|
## 主要里程碑
### Unix Shell 遺產 (1971–1989)
- **1971**：Thompson shell — 第一個 Unix shell，簡單的指令執行
- **1977**：Bourne shell (`sh`) — 變數、控制流程 (`if`、`while`)，此處文檔
- **1978**：C shell (`csh`) — 類似 C 的語法、作業控制、別名、歷史記錄
- **1983**：Korn shell (`ksh`) —`sh`+`csh`中的最佳作品
### bash — 標準（1989 年至今）
- **1989**：Brian Fox 為 GNU 計畫創作 bash — Bourne Again Shell
- **2.0 (1996)**：`[[ ]]` 測試、`(( ))` 算術、`+=`
- **4.0 (2009)**：關聯數組 (`declare -A`)、`mapfile`
- **5.0 (2019)**：Namerefs，`printf %q`
- **5.2 (2022)**：字串大小寫處理
### zsh — 高級用戶的 Shell（1990 年至今）
- **1990**：Paul Falstad 創建 zsh — 結合了 bash、ksh、tcsh 功能
- **2000s**：oh-my-zsh 框架 — 主題、外掛、完成
- **2019**：macOS 預設 shell（取代 bash）
### 魚 — 友善的外殼（2005 年至今）
- **2005**：Axel Liljankrantz 創造了魚 — “最後，一個互動式 shell”
- 自動建議、語法反白、基於 Web 的配置
- 不相容 bash — 不同的腳本語言
### PowerShell — Microsoft 的 Shell（2006 年至今）
- **2006**：PowerShell 1.0 — 基於.NET、物件管道、cmdlet
- **2.0 (2009)**：模組、遠端處理、後台作業
- **5.0 (2016)**：類別、枚舉
- **6.0 (2018)**：**跨平台** — PowerShell Core（基於 .NET Core 建置）
- **7.0 (2020)**：空條件`?.`、空合併`??`、三元 `?:`
## 語法演變
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

## 關鍵設計原則
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

## 生態系成長
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
