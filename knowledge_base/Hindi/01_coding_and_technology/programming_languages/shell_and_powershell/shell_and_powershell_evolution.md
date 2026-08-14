---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# शैल और पावरशेल - संस्करण इतिहास और विकास
## यूनिक्स शैल टाइमलाइन
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| थॉम्पसन श | 1971 | पहला यूनिक्स शेल (केन थॉम्पसन) |
| बॉर्न श | 1977 | **`sh`** — स्क्रिप्टिंग, वेरिएबल्स, नियंत्रण प्रवाह |
| सीएसएच | 1978 | सी-जैसे वाक्यविन्यास, कार्य नियंत्रण, उपनाम |
| क्ष | 1983 | कॉर्न शेल -`sh`+`csh`विशेषताएं |
| बैश | 1989 | **बॉर्न अगेन शेल** — GNU`sh`प्रतिस्थापन |
| बैश 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| बैश 3.0 | 2004 | `=~`रेगेक्स,`|&`|
| बैश 4.0 | 2009 | **सहयोगी सारणियाँ**,`mapfile`,`declare -g`|
| बैश 4.3 | 2014 | शेलशॉक भेद्यता की खोज |
| बैश 5.0 | 2019 | `declare -n`नेमरेफ्स,`printf %q`|
| बैश 5.1 | 2020 | `wait -n`,`shopt`सुधार |
| बैश 5.2 | 2022 | `${var@U}`(अपरकेस),`shopt -s compat`|
| ज़श | 1990 | विस्तारित बैश - पूर्णताएं, थीम |
| मछली | 2005 | **उपयोगकर्ता के अनुकूल** - स्वत: सुझाव, वाक्यविन्यास हाइलाइटिंग |
| नुशेल | 2019 | संरचित डेटा, तालिकाओं की पाइपलाइन |
| तेल/ओश | 2020 | बेहतर शब्दार्थ के साथ बैश-संगत |
## पावरशेल टाइमलाइन
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| 1.0 | 2006 | आरंभिक रिलीज (माइक्रोसॉफ्ट, जेफरी स्नोवर) |
| 2.0 | 2009 | **मॉड्यूल**, रिमोटिंग, पृष्ठभूमि नौकरियां, लेनदेन |
| 3.0 | 2012 | वर्कफ़्लोज़, `Invoke-RestMethod`, शेड्यूल किए गए कार्य |
| 4.0 | 2013 | **वांछित राज्य विन्यास (डीएससी)**,`if`/`switch`सुधार |
| 5.0 | 2016 | **कक्षाएं**,`enum`,`using`,`using module`|
| 5.1 | 2017 | अंतिम विंडोज़-केवल संस्करण |
| 6.0 | 2018 | **पॉवरशेल कोर** - क्रॉस-प्लेटफ़ॉर्म (विंडोज़, लिनक्स, मैकओएस) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(प्रायोगिक) |
| 6.2 | 2019 | `&&`/`||`पाइपलाइन श्रृंखला ऑपरेटर |
| 7.0 | 2020 | **प्रमुख**:`?.`शून्य-सशर्त,`??`शून्य-एकलीकरण,`using assembly`|
| 7.1 | 2020 | टर्नरी ऑपरेटर`? :`,`using module`सुधार |
| 7.2 | 2021 | **एलटीएस रिलीज**,`using namespace`सुधार |
| 7.3 | 2022 | `switch`सुधार,`ErrorView`विकल्प |
| 7.4 | 2023 | `using module`सुधार,`Get-Error`|
| 7.5 | 2024 | प्रदर्शन में सुधार,`PSResourceGet`|
| 7.6 | 2025 | निरंतर विकास |
## प्रमुख मील के पत्थर
### यूनिक्स शैल हेरिटेज (1971-1989)
- **1971**: थॉम्पसन शेल - पहला यूनिक्स शेल, सरल कमांड निष्पादन
- **1977**: बॉर्न शेल (`sh`) - चर, नियंत्रण प्रवाह (`if`, `while`), यहां-दस्तावेज़
- **1978**: सी शेल (`csh`) - सी-जैसे सिंटैक्स, कार्य नियंत्रण, उपनाम, इतिहास
- **1983**: कॉर्न शेल (`ksh`) -`sh`+`csh`में से सर्वश्रेष्ठ
### बैश - द स्टैंडर्ड (1989-वर्तमान)
- **1989**: ब्रायन फॉक्स ने जीएनयू प्रोजेक्ट - बॉर्न अगेन शेल के लिए पार्टी बनाई
- **2.0 (1996)**:`[[ ]]`परीक्षण,`(( ))`अंकगणित,`+=`
- **4.0 (2009)**: सहयोगी सारणी (`declare -A`),`mapfile`
- **5.0 (2019)**: नेमरेफ्स,`printf %q`
- **5.2 (2022)**: स्ट्रिंग केस हेरफेर
### zsh - द पावर यूजर शेल (1990-वर्तमान)
- **1990**: पॉल फालस्टेड ने zsh बनाया - बैश, ksh, tcsh सुविधाओं को संयोजित किया
- **2000**: ओह-माय-ज़श फ्रेमवर्क - थीम, प्लगइन्स, पूर्णताएँ
- **2019**: macOS डिफ़ॉल्ट शेल (बैश की जगह)
### मछली - द फ्रेंडली शेल (2005-वर्तमान)
- **2005**: एक्सल लिलजानक्रांत्ज़ ने मछली बनाई - "आखिरकार, एक इंटरैक्टिव शेल"
- ऑटोसुझाव, सिंटैक्स हाइलाइटिंग, वेब-आधारित कॉन्फ़िगरेशन
- बैश-संगत नहीं - भिन्न स्क्रिप्टिंग भाषा
### पावरशेल - माइक्रोसॉफ्ट का शेल (2006-वर्तमान)
- **2006**: पावरशेल 1.0 — .NET-आधारित, ऑब्जेक्ट पाइपलाइन, सीएमडीलेट्स
- **2.0 (2009)**: मॉड्यूल, रिमोटिंग, पृष्ठभूमि नौकरियां
- **5.0 (2016)**: कक्षाएं, एनम
- **6.0 (2018)**: **क्रॉस-प्लेटफ़ॉर्म** — पावरशेल कोर (.NET कोर पर निर्मित)
- **7.0 (2020)**: अशक्त-सशर्त `?.`, अशक्त-समायोजित `??`, टर्नरी `?:`
## सिंटेक्स इवोल्यूशन
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

## मुख्य डिज़ाइन सिद्धांत
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

## पारिस्थितिकी तंत्र का विकास
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
