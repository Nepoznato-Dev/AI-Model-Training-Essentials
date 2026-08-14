---
# Metadata
title: "Shell & PowerShell — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, safe shell and PowerShell scripts."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [shell, powershell, bash, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Shell & PowerShell — Pola Idiomatik & Praktik Terbaik
Panduan ini mencakup pola idiomatik untuk skrip Bash/Zsh dan PowerShell.
---

## Idiom Bash
```bash
#!/usr/bin/env bash
set -euo pipefail

# ✅ Quote all variables
echo "Hello, $USER"
cp "$src" "$dest"

# ✅ Use [[ ]] over [ ]
if [[ -f "$file" ]]; then
    echo "File exists"
fi

# ✅ Parameter expansion
name="${name:-default}"
count="${#array[@]}"
basename="${file##*/}"
extension="${file##*.}"

# ✅ Local variables in functions
my_func() {
    local result
    result=$(compute "$1")
    echo "$result"
}

# ✅ Process substitution
diff <(sort file1) <(sort file2)

# ✅ Here documents
cat <<EOF
Hello, $USER
Today is $(date)
EOF

# ✅ Cleanup trap
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT
```

---

## Idiom PowerShell
```powershell
# ✅ CmdletBinding for advanced functions
function Get-UserData {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [int]$Id,
        
        [ValidateSet("json", "xml")]
        [string]$Format = "json"
    )
    
    begin { $results = @() }
    process {
        $user = Invoke-RestMethod -Uri "https://api.example.com/users/$Id"
        $results += $user
    }
    end { return $results }
}

# ✅ Pipeline
Get-Process | Where-Object CPU -gt 10 | Sort-Object CPU -Descending | Select-Object -First 5

# ✅ String interpolation
$message = "Hello, $env:USERNAME! You have $($items.Count) items."

# ✅ Error handling
try {
    $result = Invoke-WebRequest -Uri $url -ErrorAction Stop
} catch {
    Write-Error "Request failed: $_"
}

# ✅ Splatting
$params = @{
    Path        = "C:\data"
    Filter      = "*.txt"
    Recurse     = $true
}
Get-ChildItem @params
```

---

## Ringkasan
Idiom shell menekankan:`set -euo pipefail`, variabel kutipan,`[[ ]]`di atas`[ ]`, perluasan parameter, dan jebakan pembersihan. Idiom PowerShell menekankan: CmdletBinding, pemrosesan alur, percikan, dan penanganan kesalahan terstruktur. Ikuti ShellCheck untuk Bash dan PSScriptAnalyzer untuk PowerShell.