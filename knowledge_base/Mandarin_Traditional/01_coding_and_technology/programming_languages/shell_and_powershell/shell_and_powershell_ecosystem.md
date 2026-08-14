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

# Shell 和 PowerShell — 生態系統和工具指南
本指南涵蓋了 shell 腳本 (Bash/Zsh) 和 PowerShell 的基本工具、框架和基礎架構。
---

## 外殼實現
|殼牌|平台|筆記|
|--------|----------|--------|
| **猛擊** | Unix/Linux/macOS |使用最廣泛 |
| **Zsh** | macOS 預設 |增強的 Bash |
| **魚** |跨平台|使用者友善 |
| **破折號** | Debian/Ubuntu |快速、符合 POSIX 標準 |
| **克什** | Unix |科恩殼 |
| **PowerShell** |跨平台|物件導向（pwsh）|
| **空殼** |跨平台|結構化資料外殼|
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## 套件管理器（Shell 工具）
|工具|目的|
|------|---------|
| **自製** | macOS/Linux 套件管理器 |
| **apt / yum / dnf** | Linux 套件管理器 |
| **包裝** | FreeBSD 套件管理器 |
| **獨家報道** | Windows CLI 安裝程式 |
| **巧克力** | Windows 套件管理器 |
| **溫蓋特** | Windows 套件管理器 |
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

## 基本 CLI 工具
|工具|目的|
|------|---------|
| **jq** | JSON 處理 |
| **yq** | YAML 處理 |
| **ripgrep (rg)** |快速 grep |
| **FD** |快速尋找|
| **蝙蝠** |增強貓|
| **exa / eza** |增強型ls |
| **fzf** |模糊查找器|
| **htop** |進程檢視器|
| **tmux** |終端機多工器|
| **捲曲/wget** | HTTP 請求 |
| **sed / awk** |文字處理 |
| **xargs** |從輸入建置指令 |
| **製作** |任務運行器 |
| **進入** |對檔案更改運行命令 |
| **平行** |並行執行 |
| **shell檢查** | Shell 腳本 linter |
---

## Shell 框架和增強功能
|工具|目的|
|------|---------|
| **哦我的Zsh** | Zsh 框架（主題、外掛）|
| **普雷茲托** | Zsh 框架（更快）|
| **星艦** |跨 shell 提示 |
| **zsh-自動建議** |自動建議 |
| **zsh-語法反白** |語法高亮 |
| **猛擊它** | Bash 框架 |
| **學習** | Shell 歷史 (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## PowerShell 模組
|模組|目的|
|--------|---------|
| **PSReadLine** |增強的命令列編輯|
| **糾纏** |測試框架|
| **PSScriptAnalyzer** |絨毛 |
| **豪華 git** | Git 整合 |
| **終端圖示** |檔案圖示|
| **PSWindows更新** | Windows 更新 |
| **阿茲** | Azure 管理 |
| **AWSPowerShell** | AWS 管理 |
| **SqlServer** | SQL Server 管理 |
| **波德** |網頁框架|
| **通用儀表板** |網路儀表板 |
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

## 測試
|框架|壳牌|目的|
|------------|---------|---------|
| **蝙蝠** |猛擊 | Bash 自動化測試 |
| **舒單元2** |殼牌| xUnit 式測驗 |
| **糾纏** | PowerShell |測試與模擬|
| **斷言.sh** |猛擊 |斷言庫 |
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

## 程式碼品質
|工具|殼牌|目的|
|------|--------|---------|
| **ShellCheck** | bash/zsh | Linting 和靜態分析 |
| **shfmt** | bash/zsh |程式碼格式化 |
| **PSScriptAnalyzer** | PowerShell |絨毛 |
| **PSScript 設定** | PowerShell |格式化|
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

## 關鍵庫和模式
### 猛擊
|圖案|目的|
|---------|---------|
| **設定-euo管道故障** |嚴格模式 |
| **陷阱** |訊號處理|
| **來源/.** |包含文件 |
| **取得選擇** |參數解析 |
| **此處文檔** |多行字串 |
| **進程替換** |`<()`和`>()`|
| **陣列** |索引與關聯 |
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

### PowerShell
|圖案|目的|
|---------|---------|
| **CmdletBinding** |進階功能 |
| **參數** |參數屬性|
| **管道** |物件管道|
| **嘗試/捕捉** |錯誤處理 |
| **課程** |物件導向 |
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

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS 程式碼** | Shell/PowerShell 支援 |
| **Neovim** |基於終端 |
| **Windows 終端機** |現代終端機（PowerShell）|
| **iTerm2** | macOS 終端機 |
| **扭曲** | AI賦能終端|
| **欣喜** | GPU加速終端|
---

## 部署
|方法|筆記|
|--------|--------|
| **計劃** |計劃任務(Unix) |
| **系統** |服務管理(Linux) |
| **任務排程器** | Windows 排程任務 |
| **Docker 入口點** |容器腳本 |
| **CI/CD 管道** | GitHub Actions、GitLab CI |
| **Ansible** |設定管理 |
| **地形** |基礎設施即代碼 |
---

＃＃ 概括
Shell 腳本的生態系統是多種多樣的：**Bash** 仍然是通用標準，**Zsh** 是交互式使用的現代預設設置，而 **PowerShell** 主導著 Windows 管理。標準堆疊是：用於腳本編寫的 **Bash/Zsh**、用於 linting 的 **ShellCheck**、用於格式化的 **shfmt**、用於測試的 **Bats**、用於 JSON 的 **jq**、用於搜尋的 **ripgrep** 以及用於終端復用的 **tmux**。對於 PowerShell：**Pester** 用於測試，**PSScriptAnalyzer** 用於 linting，**PSReadLine** 用於增強編輯。 Shell 腳本對於自動化、CI/CD、系統管理和 DevOps 工作流程至關重要。