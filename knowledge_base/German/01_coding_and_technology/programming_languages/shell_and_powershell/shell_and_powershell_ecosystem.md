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
# Shell & PowerShell – Leitfaden für Ökosysteme und Tools
Dieses Handbuch behandelt die wesentlichen Tools, Frameworks und Infrastruktur für Shell-Scripting (Bash/Zsh) und PowerShell.
---

## Shell-Implementierungen
| Schale | Plattform | Notizen |
|-------|----------|-------|
| **Bash** | Unix/Linux/macOS | Am häufigsten verwendet |
| **Zsh** | macOS-Standard | Verbesserte Bash |
| **Fisch** | Plattformübergreifend | Benutzerfreundlich |
| **Strich** | Debian/Ubuntu | Schnell, POSIX-konform |
| **ksh** | Unix | Kornschale |
| **PowerShell** | Plattformübergreifend | Objektorientiert (pwsh) |
| **Nushell** | Plattformübergreifend | Strukturierte Datenhülle |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## Paketmanager (Shell Tools)
| Werkzeug | Zweck |
|------|---------|
| **Homebrew** | macOS/Linux-Paketmanager |
| **apt / yum / dnf** | Linux-Paketmanager |
| **Pkg** | FreeBSD-Paketmanager |
| **Schaufel** | Windows CLI-Installationsprogramm |
| **Schokoladig** | Windows-Paketmanager |
| **winget** | Windows-Paketmanager |
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

## Wichtige CLI-Tools
| Werkzeug | Zweck |
|------|---------|
| **jq** | JSON-Verarbeitung |
| **yq** | YAML-Verarbeitung |
| **ripgrep (rg)** | Schnelles grep |
| **fd** | Schnell finden |
| **Fledermaus** | Verbesserte Katze |
| **exa / eza** | Erweitertes ls |
| **fzf** | Fuzzy-Finder |
| **htop** | Prozessbetrachter |
| **tmux** | Terminal-Multiplexer |
| **curl / wget** | HTTP-Anfragen |
| **sed / awk** | Textverarbeitung |
| **xargs** | Befehle aus Eingabe erstellen |
| **machen** | Task-Runner |
| **Eintritt** | Befehle für Dateiänderungen ausführen |
| **parallel** | Parallele Ausführung |
| **Shellcheck** | Shell-Skript-Linter |
---

## Shell-Frameworks und -Erweiterungen
| Werkzeug | Zweck |
|------|---------|
| **Oh mein Zsh** | Zsh-Framework (Themes, Plugins) |
| **Prezto** | Zsh-Framework (schneller) |
| **Raumschiff** | Cross-Shell-Eingabeaufforderung |
| **zsh-autosuggestions** | Automatische Vorschläge |
| **zsh-syntax-highlighting** | Syntaxhervorhebung |
| **bash-it** | Bash-Framework |
| **atuin** | Shell-Verlauf (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## PowerShell-Module
| Modul | Zweck |
|--------|---------|
| **PSReadLine** | Verbesserte Befehlszeilenbearbeitung |
| **Pester** | Testrahmen |
| **PSScriptAnalyzer** | Fusseln |
| **nobler Idiot** | Git-Integration |
| **Terminal-Icons** | Dateisymbole |
| **PSWindowsUpdate** | Windows-Updates |
| **Az** | Azure-Verwaltung |
| **AWSPowerShell** | AWS-Verwaltung |
| **SQLServer** | SQL Server-Verwaltung |
| **Pode** | Web-Framework |
| **Universelles Dashboard** | Web-Dashboards |
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

## Testen
| Rahmen | Schale | Zweck |
|-----------|-------|---------|
| **Fledermäuse** | Bash | Automatisiertes Bash-Testen |
| **shunit2** | Schale | Tests im xUnit-Stil |
| **Pester** | PowerShell | Testen und Spotten |
| **assert.sh** | Bash | Behauptungsbibliothek |
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

## Codequalität
| Werkzeug | Schale | Zweck |
|------|-------|---------|
| **ShellCheck** | Bash/Zsh | Flusen- und statische Analyse |
| **shfmt** | Bash/Zsh | Codeformatierung |
| **PSScriptAnalyzer** | PowerShell | Fusseln |
| **PSScriptSettings** | PowerShell | Formatierung |
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

## Wichtige Bibliotheken und Muster
### Bash
| Muster | Zweck |
|---------|---------|
| **set -euo pipefail** | Strenger Modus |
| **Falle** | Signalverarbeitung |
| **Quelle / .** | Dateien einschließen |
| **getopts** | Argumentanalyse |
| **hierdoc** | Mehrzeilige Zeichenfolgen |
| **Prozesssubstitution** | `<()`und`>()`|
| **Arrays** | Indiziert und assoziativ |
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
| Muster | Zweck |
|---------|---------|
| **CmdletBinding** | Erweiterte Funktion |
| **Parameter** | Parameterattribute |
| **Pipeline** | Objektpipeline |
| **Versuchen/Fangen** | Fehlerbehandlung |
| **Klassen** | OOP |
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

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code** | Shell/PowerShell-Unterstützung |
| **Neovim** | Terminalbasiert |
| **Windows-Terminal** | Modernes Terminal (PowerShell) |
| **iTerm2** | macOS-Terminal |
| **Warp** | KI-gestütztes Terminal |
| **Alacritty** | GPU-beschleunigtes Terminal |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Cron** | Geplante Aufgaben (Unix) |
| **systemd** | Dienstverwaltung (Linux) |
| **Aufgabenplaner** | Geplante Windows-Aufgaben |
| **Docker ENTRYPOINT** | Container-Skripte |
| **CI/CD-Pipelines** | GitHub-Aktionen, GitLab CI |
| **Ansible** | Konfigurationsmanagement |
| **Terraform** | Infrastruktur als Code |
---

## Zusammenfassung
Das Ökosystem von Shell-Scripting ist vielfältig: **Bash** bleibt der universelle Standard, **Zsh** ist der moderne Standard für die interaktive Nutzung und **PowerShell** dominiert die Windows-Verwaltung. Der Standard-Stack ist: **Bash/Zsh** für Skripterstellung, **ShellCheck** für Linting, **shfmt** für Formatierung, **Bats** für Tests, **jq** für JSON, **ripgrep** für die Suche und **tmux** für Terminal-Multiplexing. Für PowerShell: **Pester** zum Testen, **PSScriptAnalyzer** zum Linting und **PSReadLine** für die erweiterte Bearbeitung. Shell-Scripting ist für Automatisierung, CI/CD, Systemadministration und DevOps-Workflows unerlässlich.