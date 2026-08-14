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
# Shell 和 PowerShell — 版本历史和演变
## Unix Shell 时间线
|版本 |年份|关键主题 |
|--------|------|------------|
|汤普森·什| 1971 |第一个 Unix shell (Ken Thompson) |
|谍影重重 | 1977 | **`sh`** — 脚本、变量、控制流 |
| csh | 1978 |类 C 语法、作业控制、别名 |
|克什 | 1983 | Korn shell —`sh`+`csh`功能 |
| bash | 1989 | **Bourne Again Shell** — GNU`sh`替代品 |
| bash 2.0 | bash 1996 |  `[[ ]]`、`(( ))`、`+=` |
| bash 3.0 | bash 2004 | `=~`正则表达式，`|&` |
| bash 4.0 | bash 2009 | **关联数组**、`mapfile`、`declare -g` |
| bash 4.3 | bash 2014年|发现 Shellshock 漏洞 |
| bash 5.0 | bash 2019 | 2019 `declare -n`名称参考、`printf %q` |
| bash 5.1 | bash 2020 |  `wait -n`、`shopt` 改进 |
| bash 5.2 | bash 2022 | 2022  `${var@U}`（大写）、`shopt -s compat` |
| zsh | 1990 |扩展 bash — 完成、主题 |
|鱼 | 2005 | **用户友好** — 自动建议、语法突出显示 |
|努壳 | 2019 | 2019结构化数据、表格管道|
|石油/奥什 | 2020 |与 Bash 兼容并具有更好的语义 |
## PowerShell 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| 1.0 | 2006 |初始版本（Microsoft，Jeffrey Snover）|
| 2.0 | 2009 | **模块**、远程处理、后台作业、事务 |
| 3.0 | 2012 |工作流程、`Invoke-RestMethod`、计划作业 |
| 4.0 | 2013 | **所需状态配置 (DSC)**、`if` /`switch`改进 |
| 5.0 | 2016 | 2016 **类**，`enum`，`using`，`using module` |
| 5.1 | 2017 | 2017最新仅 Windows 版本 |
| 6.0 | 2018 | **PowerShell Core** — 跨平台（Windows、Linux、macOS）|
| 6.1 | 2018 |  `ForEach-Object -Parallel`（实验）|
| 6.2 | 2019 | 2019 `&&`/`||`管道链运营商 |
| 7.0 | 2020 | **主要**：`?.` 空条件、`??` 空合并、`using assembly` |
| 7.1 | 2020 |三元运算符`? :`、`using module`改进 |
| 7.2 | 2021 | **LTS 版本**，`using namespace` 改进 |
| 7.3 | 7.3 2022 | 2022 `switch`改进、`ErrorView` 选项 |
| 7.4 | 7.4 2023 | `using module`改进，`Get-Error` |
| 7.5 | 7.5 2024 | 2024性能改进，`PSResourceGet` |
| 7.6 | 7.6 2025 | 2025持续发展|
## 主要里程碑
### Unix Shell 遗产 (1971–1989)
- **1971**：Thompson shell — 第一个 Unix shell，简单的命令执行
- **1977**：Bourne shell (`sh`) — 变量、控制流 (`if`、`while`)，此处文档
- **1978**：C shell (`csh`) — 类似 C 的语法、作业控制、别名、历史记录
- **1983**：Korn shell (`ksh`) —`sh`+`csh`中的最佳作品
### bash — 标准（1989 年至今）
- **1989**：Brian Fox 为 GNU 项目创建 bash — Bourne Again Shell
- **2.0 (1996)**：`[[ ]]` 测试、`(( ))` 算术、`+=` 
- **4.0 (2009)**：关联数组 (`declare -A`)、`mapfile` 
- **5.0 (2019)**：Namerefs，`printf %q` 
- **5.2 (2022)**：字符串大小写处理
### zsh — 高级用户的 Shell（1990 年至今）
- **1990**：Paul Falstad 创建 zsh — 结合了 bash、ksh、tcsh 功能
- **2000s**：oh-my-zsh 框架 — 主题、插件、完成
- **2019**：macOS 默认 shell（取代 bash）
### 鱼 — 友好的外壳（2005 年至今）
- **2005**：Axel Liljankrantz 创造了鱼 — “最后，一个交互式 shell”
- 自动建议、语法突出显示、基于 Web 的配置
- 不兼容 bash — 不同的脚本语言
### PowerShell — Microsoft 的 Shell（2006 年至今）
- **2006**：PowerShell 1.0 — 基于.NET、对象管道、cmdlet
- **2.0 (2009)**：模块、远程处理、后台作业
- **5.0 (2016)**：类、枚举
- **6.0 (2018)**：**跨平台** — PowerShell Core（基于 .NET Core 构建）
- **7.0 (2020)**：空条件`?.`、空合并`??`、三元 `?:`
## 语法演变
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

## 关键设计原则
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

## 生态系统增长
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
