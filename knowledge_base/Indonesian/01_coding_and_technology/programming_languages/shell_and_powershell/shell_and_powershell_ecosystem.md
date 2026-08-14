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
# Shell & PowerShell — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting untuk skrip shell (Bash/Zsh) dan PowerShell.
---

## Implementasi Shell
| cangkang | Peron | Catatan |
|-------|----------|-------|
| **Pesta** | Unix/Linux/macOS | Paling banyak digunakan |
| **Zsh** | bawaan macOS | Pesta yang Ditingkatkan |
| **Ikan** | Lintas platform | Mudah digunakan |
| **tanda hubung** | Debian/Ubuntu | Cepat, sesuai POSIX |
| **ksh** | Unix | Cangkang jagung |
| **PowerShell** | Lintas platform | Berorientasi objek (pwsh) |
| **Tidak apa-apa** | Lintas platform | Cangkang data terstruktur |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## Manajer Paket (Alat Shell)
| Alat | Tujuan |
|------|---------|
| **Minuman rumahan** | manajer paket macOS/Linux |
| **apt / enak / dnf** | Manajer paket Linux |
| **pkg** | Manajer paket FreeBSD |
| **Sendok** | Penginstal Windows CLI |
| **Cokelat** | Manajer paket Windows |
| **sayap** | Manajer paket Windows |
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

## Alat CLI Penting
| Alat | Tujuan |
|------|---------|
| **jq** | Pemrosesan JSON |
| **yq** | Pemrosesan YAML |
| **ripgrep (rg)** | Grep cepat |
| **fd** | Temukan cepat |
| **kelelawar** | Kucing yang ditingkatkan |
| **exa / eza** | Peningkatan ls |
| **fzf** | Penemu kabur |
| **htop** | Penampil proses |
| **tmux** | Terminal multiplekser |
| **ikal / wget** | Permintaan HTTP |
| **sed / awk** | Pemrosesan teks |
| **xargs** | Bangun perintah dari input |
| **membuat** | Pelari tugas |
| **masuk** | Jalankan perintah pada perubahan file |
| **paralel** | Eksekusi paralel |
| **periksa cangkang** | Linter skrip shell |
---

## Kerangka Kerja & Penyempurnaan Shell
| Alat | Tujuan |
|------|---------|
| **Ya ampun** | Kerangka kerja Zsh (tema, plugin) |
| **Presto** | Kerangka kerja Zsh (lebih cepat) |
| **Kapal Luar Angkasa** | Perintah lintas shell |
| **zsh-sugesti otomatis** | Saran otomatis |
| **penyorotan-sintaksis-zsh** | Penyorotan sintaks |
| **bash-itu** | Kerangka pesta |
| **atuin** | Riwayat cangkang (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## Modul PowerShell
| Modul | Tujuan |
|--------|---------|
| **PSReadLine** | Pengeditan baris perintah yang ditingkatkan |
| **Pengganggu** | Kerangka pengujian |
| **PSScriptAnalyzer** | Linting |
| **mewah-git** | Integrasi Git |
| **Ikon-Terminal** | Ikon berkas |
| **Pembaruan PSWindows** | Pembaruan Windows |
| **Az** | Manajemen Azure |
| **AWSPowerShell** | Manajemen AWS |
| **SqlServer** | Manajemen SQL Server |
| **Pode** | Kerangka web |
| **Dasbor Universal** | Dasbor web |
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

## Pengujian
| Kerangka | cangkang | Tujuan |
|-----------|-------|---------|
| **Kelelawar** | Pesta | Pengujian Otomatis Bash |
| **shunit2** | cangkang | pengujian gaya xUnit |
| **Pengganggu** | PowerShell | Menguji dan mengejek |
| **tegaskan.sh** | Pesta | Perpustakaan pernyataan |
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

## Kualitas Kode
| Alat | cangkang | Tujuan |
|------|-------|---------|
| **Periksa Shell** | Pesta/Zsh | Analisis linting dan statis |
| **sialan** | Pesta/Zsh | Pemformatan kode |
| **PSScriptAnalyzer** | PowerShell | Linting |
| **Pengaturan PSScript** | PowerShell | Memformat |
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

## Perpustakaan & Pola Utama
### Pesta
| Pola | Tujuan |
|---------|---------|
| **setel -euo pipefail** | Modus ketat |
| **perangkap** | Penanganan sinyal |
| **sumber / .** | Sertakan file |
| **dapatkan** | Penguraian argumen |
| **di sinidok** | String multi-baris |
| **proses substitusi** | `<()`dan`>()`|
| **array** | Terindeks dan asosiatif |
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
| Pola | Tujuan |
|---------|---------|
| **Pengikatan Cmdlet** | Fungsi lanjutan |
| **Parameter** | Atribut parameter |
| **Saluran** | Pipa objek |
| **Coba/Tangkap** | Penanganan kesalahan |
| **Kelas** | OOP |
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

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS** | Dukungan Shell/PowerShell |
| **Neovim** | Berbasis terminal |
| **Terminal Windows** | Terminal modern (PowerShell) |
| **iTerm2** | terminal macOS |
| **Melengkungkan** | Terminal bertenaga AI |
| **Alacritty** | Terminal dengan akselerasi GPU |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Kron** | Tugas terjadwal (Unix) |
| **sistemd** | Manajemen layanan (Linux) |
| **Penjadwal Tugas** | Tugas terjadwal Windows |
| **TITIK MASUK Docker** | Skrip kontainer |
| **Jalur CI/CD** | Tindakan GitHub, GitLab CI |
| **Mungkin** | Manajemen konfigurasi |
| **Terraform** | Infrastruktur sebagai kode |
---

## Ringkasan
Ekosistem skrip Shell beragam: **Bash** tetap menjadi standar universal, **Zsh** adalah default modern untuk penggunaan interaktif, dan **PowerShell** mendominasi administrasi Windows. Tumpukan standarnya adalah: **Bash/Zsh** untuk pembuatan skrip, **ShellCheck** untuk linting, **shfmt** untuk pemformatan, **Bats** untuk pengujian, **jq** untuk JSON, **ripgrep** untuk pencarian, dan **tmux** untuk terminal multiplexing. Untuk PowerShell: **Pester** untuk pengujian, **PSScriptAnalyzer** untuk linting, dan **PSReadLine** untuk pengeditan yang lebih baik. Skrip Shell sangat penting untuk otomatisasi, CI/CD, administrasi sistem, dan alur kerja DevOps.