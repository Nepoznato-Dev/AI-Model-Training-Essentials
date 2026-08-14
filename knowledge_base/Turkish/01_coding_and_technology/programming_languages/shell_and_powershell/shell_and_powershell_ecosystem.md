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
# Shell ve PowerShell — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz, kabuk komut dosyası oluşturma (Bash/Zsh) ve PowerShell için temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Kabuk Uygulamaları
| Kabuk | Platformu | Notlar |
|----------|----------|----------|
| **Bah** | Unix/Linux/macOS | En yaygın kullanılanlar |
| **Zsh** | macOS varsayılanı | Geliştirilmiş Bash |
| **Balık** | Çapraz platform | Kullanıcı dostu |
| **tire** | Debian/Ubuntu | Hızlı, POSIX uyumlu |
| **kş** | Unix | Korn kabuğu |
| **PowerShell** | Çapraz platform | Nesneye yönelik (pwsh) |
| **Nushell** | Çapraz platform | Yapılandırılmış veri kabuğu |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## Paket Yöneticileri (Kabuk Araçları)
| Araç | Amaç |
|------|------------|
| **Ev yapımı bira** | macOS/Linux paket yöneticisi |
| **apt / yum / dnf** | Linux paket yöneticileri |
| **pkg** | FreeBSD paket yöneticisi |
| **Kepçe** | Windows CLI yükleyicisi |
| **Çikolata** | Windows paket yöneticisi |
| **kanat** | Windows paket yöneticisi |
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

## Temel CLI Araçları
| Araç | Amaç |
|------|------------|
| **jq** | JSON işleme |
| **yq** | YAML işleme |
| **ripgrep (rg)** | Hızlı grep |
| **fd** | Hızlı bul |
| **yarasa** | Geliştirilmiş kedi |
| **exa / eza** | Geliştirilmiş l'ler |
| **fzf** | Bulanık bulucu |
| **htop** | Süreç görüntüleyici |
| **tmux** | Terminal çoklayıcı |
| **kıvrılma / wget** | HTTP istekleri |
| **sed / awk** | Metin işleme |
| **xargs** | Girişten komutlar oluşturun |
| **yap** | Görev çalıştırıcısı |
| **giriş** | Dosya değişikliklerinde komutları çalıştırın |
| **paralel** | Paralel yürütme |
| **kabuk kontrolü** | Kabuk betiği linter |
---

## Kabuk Çerçeveleri ve Geliştirmeleri
| Araç | Amaç |
|------|------------|
| **Aman Tanrım** | Zsh çerçevesi (temalar, eklentiler) |
| **Prezto** | Zsh çerçevesi (daha hızlı) |
| **Yıldız gemisi** | Çapraz kabuk istemi |
| **zsh-otomatik öneriler** | Otomatik öneriler |
| **zsh-sözdizimi-vurgulama** | Sözdizimi vurgulama |
| **bash-it** | Bash çerçevesi |
| **atuin** | Kabuk geçmişi (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## PowerShell Modülleri
| Modül | Amaç |
|----------|------------|
| **PSReadLine** | Gelişmiş komut satırı düzenleme |
| **Pester** | Test çerçevesi |
| **PSScriptAnalyzer** | Linting |
| **lüks-git** | Git entegrasyonu |
| **Terminal Simgeleri** | Dosya simgeleri |
| **PSWindows Güncellemesi** | Windows güncellemeleri |
| **Az** | Azure yönetimi |
| **AWSPowerShell** | AWS yönetimi |
| **SqlServer** | SQL Sunucu yönetimi |
| **Kapsül** | Web çerçevesi |
| **Evrensel Kontrol Paneli** | Web kontrol panelleri |
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

## Test etme
| Çerçeve | Kabuk | Amaç |
|-----------|----------|-----------|
| **Yarasalar** | Bash | Bash Otomatik Test |
| **şunit2** | Kabuk | xUnit tarzı test |
| **Pester** | PowerShell | Test etme ve alay etme |
| **assert.sh** | Bash | İddia kitaplığı |
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

## Kod Kalitesi
| Araç | Kabuk | Amaç |
|------|----------|-----------|
| **ShellCheck** | Bash/Zsh | Linting ve statik analiz |
| **shfmt** | Bash/Zsh | Kod biçimlendirme |
| **PSScriptAnalyzer** | PowerShell | Linting |
| **PSScript Ayarları** | PowerShell | Biçimlendirme |
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

## Anahtar Kitaplıklar ve Desenler
### Bash
| Desen | Amaç |
|-----------|-----------|
| **set -euo pipefail** | Katı mod |
| **tuzak** | Sinyal işleme |
| **kaynak / .** | Dosyaları dahil et |
| **getopt'lar** | Bağımsız değişken ayrıştırma |
| **heredoc** | Çok satırlı dizeler |
| **süreç ikamesi** | `<()`ve`>()`|
| **diziler** | İndekslenmiş ve ilişkisel |
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
| Desen | Amaç |
|-----------|-----------|
| **CmdletBinding** | Gelişmiş fonksiyon |
| **Parametre** | Parametre özellikleri |
| **Boru hattı** | Nesne boru hattı |
| **Dene/Yakala** | Hata işleme |
| **Sınıflar** | OOP |
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

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu** | Kabuk/PowerShell desteği |
| **Neovim** | Terminal tabanlı |
| **Windows Terminali** | Modern terminal (PowerShell) |
| **iTerm2** | macOS terminali |
| **Çarpma** | Yapay Zeka destekli terminal |
| **Alacritty** | GPU ile hızlandırılmış terminal |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Cron** | Zamanlanmış görevler (Unix) |
| **sistemd** | Hizmet yönetimi (Linux) |
| **Görev Zamanlayıcı** | Windows zamanlanmış görevleri |
| **Docker GİRİŞ NOKTASI** | Konteyner komut dosyaları |
| **CI/CD ardışık düzenleri** | GitHub Eylemleri, GitLab CI |
| **Ansible** | Konfigürasyon yönetimi |
| **Terraform** | Kod olarak altyapı |
---

## Özet
Kabuk komut dosyası oluşturma ekosistemi çeşitlidir: **Bash** evrensel standart olmaya devam ediyor, **Zsh** etkileşimli kullanım için modern varsayılandır ve **PowerShell** Windows yönetimine hakimdir. Standart yığın şöyledir: Komut dosyası oluşturma için **Bash/Zsh**, linting için **ShellCheck**, biçimlendirme için **shfmt**, test için **Bats**, JSON için **jq**, arama için **ripgrep** ve terminal çoğullaması için **tmux**. PowerShell için: Test için **Pester**, astarlama için **PSScriptAnalyzer** ve gelişmiş düzenleme için **PSReadLine**. Kabuk komut dosyası oluşturma, otomasyon, CI/CD, sistem yönetimi ve DevOps iş akışları için gereklidir.