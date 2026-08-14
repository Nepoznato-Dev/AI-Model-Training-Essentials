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
# Shell i PowerShell — przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę do skryptów powłoki (Bash/Zsh) i programu PowerShell.
---

## Implementacje powłoki
| Powłoka | Platforma | Notatki |
|-------|----------|-------|
| **Bash** | Unix/Linux/macOS | Najczęściej używane |
| **Zsz** | Domyślny system macOS | Ulepszony Bash |
| **Ryba** | Wieloplatformowe | Przyjazny dla użytkownika |
| **kreska** | Debian/Ubuntu | Szybki, zgodny z POSIX |
| **ksz** | Uniksa | Muszla Korna |
| **PowerShell** | Wieloplatformowe | Obiektowy (pwsh) |
| **Nic** | Wieloplatformowe | Strukturalna powłoka danych |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## Menedżerowie pakietów (narzędzia powłoki)
| Narzędzie | Cel |
|------|-------------|
| **Domowe piwo** | Menedżer pakietów macOS/Linux |
| **apt / mniam / dnf** | Menedżerowie pakietów Linuksa |
| **opk** | Menedżer pakietów FreeBSD |
| **Miarka** | Instalator CLI systemu Windows |
| **Czekolada** | Menedżer pakietów Windows |
| **skrzydło** | Menedżer pakietów Windows |
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

## Niezbędne narzędzia CLI
| Narzędzie | Cel |
|------|-------------|
| **jq** | Przetwarzanie JSON |
| **yq** | Przetwarzanie YAML |
| **ripgrep (rg)** | Szybki grep |
| **fd** | Szybkie wyszukiwanie |
| **nietoperz** | Ulepszony kot |
| **exa / eza** | Ulepszone ls |
| **fzf** | Wyszukiwarka rozmyta |
| **htop** | Przeglądarka procesów |
| **tmux** | Multiplekser terminalowy |
| **curl / wget** | Żądania HTTP |
| **sed / awk** | Przetwarzanie tekstu |
| **xargs** | Kompiluj polecenia z danych wejściowych |
| **zrób** | Osoba wykonująca zadanie |
| **wejście** | Uruchom polecenia po zmianach plików |
| **równolegle** | Wykonanie równoległe |
| **sprawdzenie powłoki** | Linter skryptu powłoki |
---

## Struktury i ulepszenia powłoki
| Narzędzie | Cel |
|------|-------------|
| **O mój Boże** | Framework Zsh (motywy, wtyczki) |
| **Prezent** | Framework Zsh (szybszy) |
| **Statek kosmiczny** | Podpowiedź międzypowłokowa |
| **autosugestie zsh** | Automatyczne sugestie |
| **podświetlanie składni zsh** | Podświetlanie składni |
| **walenie** | Framework Basha |
| **atuna** | Historia powłoki (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## Moduły PowerShell
| Moduł | Cel |
|------------|--------|
| **PSReadLine** | Ulepszona edycja w wierszu poleceń |
| **Pester** | Ramy testowania |
| **Analizator PSScript** | Linting |
| **elegancki git** | Integracja z Gitem |
| **Ikony terminala** | Ikony plików |
| **PSWindowsUpdate** | Aktualizacje systemu Windows |
| **Az** | Zarządzanie platformą Azure |
| **AWSPowerShell** | Zarządzanie AWS |
| **Serwer SQL** | Zarządzanie SQL Serverem |
| **Pode** | Struktura internetowa |
| **Uniwersalny pulpit nawigacyjny** | Panele internetowe |
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

## Testowanie
| Ramy | Powłoka | Cel |
|----------|-------|--------|
| **Nietoperze** | Uderz | Automatyczne testowanie Bash |
| **niech2** | Powłoka | Testowanie w stylu xUnit |
| **Pester** | PowerShell | Testowanie i kpiny |
| **assert.sh** | Uderz | Biblioteka asercji |
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

## Jakość kodu
| Narzędzie | Powłoka | Cel |
|------|-------|--------|
| **Kontrola powłoki** | Bash/Zsh | Linting i analiza statyczna |
| **shffmt** | Bash/Zsh | Formatowanie kodu |
| **Analizator PSScript** | PowerShell | Linting |
| **Ustawienia PSScript** | PowerShell | Formatowanie |
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

## Kluczowe biblioteki i wzorce
### Basia
| Wzór | Cel |
|--------|---------|
| **ustaw -euo awaria potoku** | Tryb ścisły |
| **pułapka** | Obsługa sygnału |
| **źródło / .** | Dołącz pliki |
| **getopty** | Analiza argumentów |
| **heredok** | Ciągi wieloliniowe |
| **podstawienie procesu** | `<()`i`>()`|
| **tablice** | Indeksowane i asocjacyjne |
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
| Wzór | Cel |
|--------|---------|
| **Wiązanie poleceń cmdlet** | Zaawansowana funkcja |
| **Parametr** | Atrybuty parametrów |
| **Rurociąg** | Potok obiektowy |
| **Spróbuj/złap** | Obsługa błędów |
| **Zajęcia** | Ups |
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

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS** | Obsługa powłoki/PowerShell |
| **Neovim** | Oparte na terminalu |
| **Terminal Windows** | Nowoczesny terminal (PowerShell) |
| **iTerm2** | terminal macOS |
| **Wypaczenie** | Terminal zasilany sztuczną inteligencją |
| **Alakryt** | Terminal z akceleracją GPU |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Cron** | Zaplanowane zadania (Unix) |
| **system** | Zarządzanie usługami (Linux) |
| **Harmonogram zadań** | Zaplanowane zadania systemu Windows |
| **PUNKT WEJŚCIA DOKOWANEGO** | Skrypty kontenerowe |
| **rurociągi CI/CD** | Akcje GitHub, GitLab CI |
| **Ansible** | Zarządzanie konfiguracją |
| **Terraforma** | Infrastruktura jako kod |
---

## Streszczenie
Ekosystem skryptów powłoki jest zróżnicowany: **Bash** pozostaje uniwersalnym standardem, **Zsh** jest nowoczesnym standardem domyślnym do użytku interaktywnego, a **PowerShell** dominuje w administrowaniu systemem Windows. Standardowy stos to: **Bash/Zsh** do tworzenia skryptów, **ShellCheck** do lintingu, **shfmt** do formatowania, **Bats** do testowania, **jq** do JSON, **ripgrep** do wyszukiwania i **tmux** do multipleksowania terminali. W przypadku PowerShell: **Pester** do testowania, **PSScriptAnalyzer** do lintingu i **PSReadLine** do ulepszonej edycji. Skrypty powłoki są niezbędne w procesach automatyzacji, CI/CD, administrowania systemem i DevOps.