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
# Shell & PowerShell — Riwayat Versi & Evolusi
## Garis Waktu Unix Shell
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Thompson sh | 1971 | Cangkang Unix pertama (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — skrip, variabel, aliran kontrol |
| csh | 1978 | Sintaks seperti C, kontrol pekerjaan, alias |
| ksh | 1983 | Cangkang Korn — fitur`sh`+`csh`|
| pesta | 1989 | **Bourne Again Shell** — pengganti GNU`sh`|
| pesta 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| pesta 3.0 | 2004 |  Regex `=~`,`|&`|
| pesta 4.0 | 2009 | **Array asosiatif**,`mapfile`,`declare -g`|
| pesta 4.3 | 2014 | Kerentanan Shellshock ditemukan |
| pesta 5.0 | 2019 |  Referensi nama `declare -n`,`printf %q`|
| pesta 5.1 | 2020 |  Peningkatan `wait -n`,`shopt`|
| pesta 5.2 | 2022 | `${var@U}`(huruf besar),`shopt -s compat`|
| zsh | 1990 | Pesta yang diperluas — penyelesaian, tema |
| ikan | 2005 | **Mudah digunakan** — saran otomatis, penyorotan sintaksis |
| singkatnya | 2019 | Data terstruktur, alur tabel |
| minyak/osh | 2020 | Kompatibel dengan Bash dengan semantik yang lebih baik |
## Garis Waktu PowerShell
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 1.0 | 2006 | Rilis awal (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Modul**, jarak jauh, pekerjaan latar belakang, transaksi |
| 3.0 | 2012 | Alur kerja, `Invoke-RestMethod`, pekerjaan terjadwal |
| 4.0 | 2013 | **Konfigurasi Status yang Diinginkan (DSC)**, penyempurnaan`if`/`switch`|
| 5.0 | 2016 | **Kelas**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Versi terakhir khusus Windows |
| 6.0 | 2018 | **PowerShell Core** — lintas platform (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(percobaan) |
| 6.2 | 2019 |  Operator rantai pipa`&&`/`||`|
| 7.0 | 2020 | **Mayor**:`?.`null-kondisional,`??`penggabungan null,`using assembly`|
| 7.1 | 2020 | Peningkatan operator ternary `? :`,`using module`|
| 7.2 | 2021 | **Rilis LTS**, peningkatan`using namespace`|
| 7.3 | 2022 |  Peningkatan `switch`, opsi`ErrorView`|
| 7.4 | 2023 |  Peningkatan `using module`,`Get-Error`|
| 7.5 | 2024 | Peningkatan kinerja,`PSResourceGet`|
| 7.6 | 2025 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Warisan Unix Shell (1971–1989)
- **1971**: Thompson shell — shell Unix pertama, eksekusi perintah sederhana
- **1977**: Bourne shell (`sh`) — variabel, aliran kontrol (`if`,`while`), di sini-dokumen
- **1978**: C shell (`csh`) — Sintaks mirip C, kontrol pekerjaan, alias, riwayat
- **1983**: Korn shell (`ksh`) — terbaik dari`sh`+ `csh`
### bash — Standar (1989–sekarang)
- **1989**: Brian Fox membuat bash untuk proyek GNU — Bourne Again Shell
- **2.0 (1996)**: Tes `[[ ]]`, aritmatika `(( ))`,`+=`
- **4.0 (2009)**: Array asosiatif (`declare -A`),`mapfile`
- **5.0 (2019)**: Namaref,`printf %q`
- **5.2 (2022)**: Manipulasi huruf besar-kecil
### zsh — Shell Pengguna yang Kuat (1990–sekarang)
- **1990**: Paul Falstad membuat zsh — menggabungkan fitur bash, ksh, tcsh
- **2000an**: kerangka kerja oh-my-zsh — tema, plugin, penyelesaian
- **2019**: shell default macOS (menggantikan bash)
### ikan — Cangkang Ramah (2005–sekarang)
- **2005**: Axel Liljankrantz menciptakan ikan — "Akhirnya, cangkang interaktif"
- Saran otomatis, penyorotan sintaksis, konfigurasi berbasis web
- Tidak kompatibel dengan bash — bahasa skrip berbeda
### PowerShell — Microsoft Shell (2006–sekarang)
- **2006**: PowerShell 1.0 — pipa objek, cmdlet berbasis .NET
- **2.0 (2009)**: Modul, jarak jauh, pekerjaan latar belakang
- **5.0 (2016)**: Kelas, enum
- **6.0 (2018)**: **Lintas platform** — PowerShell Core (dibangun di .NET Core)
- **7.0 (2020)**:`?.`bersyarat nol,`??`penggabungan nol, ternary `?:`
## Evolusi Sintaks
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

## Prinsip Desain Utama
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

## Pertumbuhan Ekosistem
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
