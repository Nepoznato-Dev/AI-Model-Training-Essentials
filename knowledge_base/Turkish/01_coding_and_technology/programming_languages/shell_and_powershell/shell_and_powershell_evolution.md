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
# Shell ve PowerShell — Sürüm Geçmişi ve Gelişimi
## Unix Kabuk Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Thompson sh | 1971 | İlk Unix kabuğu (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — komut dosyası oluşturma, değişkenler, kontrol akışı |
| csh | 1978 | C benzeri sözdizimi, iş kontrolü, takma adlar |
| ksh | 1983 | Korn kabuğu —`sh`+`csh`özellikleri |
| bash | 1989 | **Bourne Again Shell** — GNU`sh`değişimi |
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash3.0 | 2004 | `=~`normal ifade,`|&`|
| bash 4.0 | 2009 | **İlişkili diziler**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Shellshock güvenlik açığı keşfedildi |
| bash 5.0 | 2019 | `declare -n`ad referansları,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`iyileştirmeleri |
| bash 5.2 | 2022 | `${var@U}`(büyük harf),`shopt -s compat`|
| zsh | 1990 | Genişletilmiş bash — tamamlamalar, temalar |
| balık | 2005 | **Kullanıcı dostu** — otomatik öneriler, sözdizimi vurgulama |
| nushell | 2019 | Yapılandırılmış veriler, tabloların ardışık düzenleri |
| yağ/oş | 2020 | Daha iyi anlambilimle Bash uyumlu |
## PowerShell Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 1.0 | 2006 | İlk sürüm (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Modüller**, uzaktan iletişim, arka plan işleri, işlemler |
| 3.0 | 2012 | İş akışları, `Invoke-RestMethod`, planlanmış işler |
| 4.0 | 2013 | **İstenen Durum Yapılandırması (DSC)**,`if`/`switch`iyileştirmeleri |
| 5.0 | 2016 | **Sınıflar**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Yalnızca Windows'a özel son sürüm |
| 6.0 | 2018 | **PowerShell Core** — platformlar arası (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(deneysel) |
| 6.2 | 2019 | `&&`/`||`boru hattı zinciri operatörleri |
| 7.0 | 2020 | **Majör**:`?.`boş koşullu,`??`boş birleştirici,`using assembly`|
| 7.1 | 2020 | Üçlü operatör`? :`,`using module`iyileştirmeleri |
| 7.2 | 2021 | **LTS sürümü**,`using namespace`iyileştirmeleri |
| 7.3 | 2022 | `switch`iyileştirmeleri,`ErrorView`seçenekleri |
| 7.4 | 2023 | `using module`iyileştirmeleri,`Get-Error`|
| 7.5 | 2024 | Performans iyileştirmeleri,`PSResourceGet`|
| 7.6 | 2025 | Devam eden geliştirme |
## Önemli Kilometre Taşları
### Unix Kabuk Mirası (1971–1989)
- **1971**: Thompson kabuğu — ilk Unix kabuğu, basit komut çalıştırma
- **1977**: Bourne kabuğu (`sh`) — değişkenler, kontrol akışı (`if`,`while`), burada belgeler
- **1978**: C kabuğu (`csh`) — C benzeri sözdizimi, iş kontrolü, takma adlar, geçmiş
- **1983**: Korn kabuğu (`ksh`) —`sh`+ `csh`'nin en iyisi
### bash — Standart (1989-günümüz)
- **1989**: Brian Fox, GNU projesi için bash yarattı — Bourne Again Shell
- **2.0 (1996)**:`[[ ]]`testi,`(( ))`aritmetiği,`+=`
- **4.0 (2009)**: İlişkisel diziler (`declare -A`),`mapfile`
- **5,0 (2019)**: Ad referansları,`printf %q`
- **5.2 (2022)**: Dizi büyük/küçük harf manipülasyonu
### zsh — Uzman Kullanıcının Kabuğu (1990-günümüz)
- **1990**: Paul Falstad zsh'yi yarattı — bash, ksh, tcsh özelliklerini birleştirdi
- **2000'ler**: oh-my-zsh çerçevesi — temalar, eklentiler, tamamlamalar
- **2019**: macOS varsayılan kabuğu (bash'ın yerine geçer)
### balık - Dost Kabuk (2005-günümüz)
- **2005**: Axel Liljankrantz balık yaratıyor — "Sonunda etkileşimli bir kabuk"
- Otomatik öneriler, sözdizimi vurgulama, web tabanlı yapılandırma
- Bash uyumlu değil — farklı kodlama dili
### PowerShell — Microsoft'un Kabuğu (2006-günümüz)
- **2006**: PowerShell 1.0 — .NET tabanlı, nesne hattı, cmdlet'ler
- **2.0 (2009)**: Modüller, uzaktan iletişim, arka plan işleri
- **5.0 (2016)**: Sınıflar, numaralandırmalar
- **6.0 (2018)**: **Platformlar arası** — PowerShell Core (.NET Core üzerinde oluşturulmuştur)
- **7,0 (2020)**: Boş koşullu `?.`, boş birleştirici `??`, üçlü `?:`
## Söz Dizimi Gelişimi
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

## Temel Tasarım İlkeleri
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

## Ekosistem Büyümesi
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
