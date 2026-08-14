<!--
---
# Metadata
title: "Shell & PowerShell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Shell and PowerShell ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Shell at PowerShell — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, frameworks, at imprastraktura para sa shell scripting (Bash/Zsh) at PowerShell.
---

## Mga Pagpapatupad ng Shell
| Shell | Platform | Mga Tala |
|-------|----------|-------|
| **Bash** | Unix/Linux/macOS | Pinakalawak na ginagamit |
| **Zsh** | default ng macOS | Pinahusay na Bash |
| ** Isda** | Cross-platform | User-friendly |
| **gitling** | Debian/Ubuntu | Mabilis, sumusunod sa POSIX |
| **ksh** | Unix | Korn shell |
| **PowerShell** | Cross-platform | Object-oriented (pwsh) |
| **Nushell** | Cross-platform | Structured data shell |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## Package Managers (Shell Tools)
| Tool | Layunin |
|------|---------|
| **Homebrew** | macOS/Linux package manager |
| **apt / yum / dnf** | Linux package managers |
| **pkg** | Tagapamahala ng package ng FreeBSD |
| **Scoop** | Windows CLI installer |
| **Chocolatey** | Windows package manager |
| **winget** | Windows package manager |
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

## Mahahalagang CLI Tools
| Tool | Layunin |
|------|---------|
| **jq** | Pagproseso ng JSON |
| **yq** | YAML processing |
| **ripgrep (rg)** | Mabilis na grep |
| **fd** | Mabilis na mahanap |
| **bat** | Pinahusay na pusa |
| **exa / eza** | Pinahusay na ls |
| **fzf** | Fuzzy finder |
| **htop** | Viewer ng proseso |
| **tmux** | Terminal multiplexer |
| **curl / wget** | Mga kahilingan sa HTTP |
| **sed / awk** | Pagproseso ng teksto |
| **xargs** | Bumuo ng mga command mula sa input |
| **gumawa** | Task runner |
| **entr** | Patakbuhin ang mga utos sa mga pagbabago sa file |
| **parallel** | Parallel execution |
| **shellcheck** | Shell script linter |
---

## Shell Frameworks at Enhancements
| Tool | Layunin |
|------|---------|
| **Oh My Zsh** | Zsh framework (mga tema, plugin) |
| **Prezto** | Zsh framework (mas mabilis) |
| **Starship** | Cross-shell prompt |
| **zsh-autosuggestions** | Mga awtomatikong suhestyon |
| **zsh-syntax-highlighting** | Syntax highlighting |
| **bash-it** | Bash framework |
| **atuin** | Kasaysayan ng shell (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## Mga Module ng PowerShell
| Module | Layunin |
|--------|---------|
| **PSReadLine** | Pinahusay na pag-edit ng command-line |
| **Pester** | Balangkas ng pagsubok |
| **PSScriptAnalyzer** | Linting |
| **posh-git** | Pagsasama ng Git |
| **Terminal-Icon** | Mga icon ng file |
| **PSWindowsUpdate** | Mga update sa Windows |
| **Az** | Pamamahala ng Azure |
| **AWSPowerShell** | Pamamahala ng AWS |
| **SqlServer** | Pamamahala ng SQL Server |
| **Pode** | Web framework |
| **Pangkalahatang Dashboard** | Mga dashboard sa web |
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

## Pagsubok
| Balangkas | Shell | Layunin |
|-----------|-------|---------|
| **Mga paniki** | Bash | Bash Automated Testing |
| **shunit2** | Shell | xUnit-style na pagsubok |
| **Pester** | PowerShell | Pagsubok at panunuya |
| **assert.sh** | Bash | Aklatan ng paninindigan |
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

## Kalidad ng Code
| Tool | Shell | Layunin |
|------|-------|---------|
| **ShellCheck** | Bash/Zsh | Linting at static na pagsusuri |
| **shfmt** | Bash/Zsh | Pag-format ng code |
| **PSScriptAnalyzer** | PowerShell | Linting |
| **PSScriptSettings** | PowerShell | Pag-format |
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

## Mga Pangunahing Aklatan at Pattern
### Bash
| Pattern | Layunin |
|---------|---------|
| **set -euo pipefail** | Mahigpit na mode |
| **bitag** | Paghawak ng signal |
| **pinagmulan / .** | Isama ang mga file |
| **getopts** | Pag-parse ng argumento |
| **heredoc** | Multi-line na mga string |
| **prosesong pagpapalit** | `<()`at`>()`|
| **mga array** | Na-index at nag-uugnay |
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
| Pattern | Layunin |
|---------|---------|
| **CmdletBinding** | Advanced na function |
| **Parameter** | Mga katangian ng parameter |
| **Pipeline** | Object pipeline |
| **Subukan/Mahuli** | Error sa pangangasiwa |
| **Mga Klase** | OOP |
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

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code** | Suporta sa Shell/PowerShell |
| **Neovim** | Nakabatay sa terminal |
| **Windows Terminal** | Modernong terminal (PowerShell) |
| **iTerm2** | macOS terminal |
| **Warp** | terminal na pinapagana ng AI |
| **Alacritty** | GPU-accelerated na terminal |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Cron** | Mga nakaiskedyul na gawain (Unix) |
| **systemd** | Pamamahala ng serbisyo (Linux) |
| **Task Scheduler** | Mga nakaiskedyul na gawain sa Windows |
| **Docker ENTRYPOINT** | Mga script ng container |
| **CI/CD pipelines** | Mga Pagkilos sa GitHub, GitLab CI |
| **Ansible** | Pamamahala ng configuration |
| **Terraform** | Imprastraktura bilang code |
---

## Buod
Ang ecosystem ng Shell scripting ay magkakaiba: **Bash** ay nananatiling pangkalahatang pamantayan, **Zsh** ay ang modernong default para sa interactive na paggamit, at **PowerShell** ay nangingibabaw sa Windows administration. Ang karaniwang stack ay: **Bash/Zsh** para sa scripting, **ShellCheck** para sa linting, **shfmt** para sa pag-format, **Bats** para sa pagsubok, **jq** para sa JSON, **ripgrep** para sa paghahanap, at **tmux** para sa terminal multiplexing. Para sa PowerShell: **Pester** para sa pagsubok, **PSScriptAnalyzer** para sa linting, at **PSReadLine** para sa pinahusay na pag-edit. Mahalaga ang Shell scripting para sa automation, CI/CD, system administration, at mga workflow ng DevOps.