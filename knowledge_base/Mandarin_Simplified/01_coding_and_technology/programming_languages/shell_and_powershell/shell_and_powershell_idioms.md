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

# Shell 和 PowerShell — 惯用模式和最佳实践
本指南涵盖了 Bash/Zsh 和 PowerShell 脚本编写的惯用模式。
---

## Bash 习语
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

## PowerShell 惯用语
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

＃＃ 概括
Shell 习惯用法强调：`set -euo pipefail`、引用变量、`[[ ]]`over`[ ]`、参数扩展和清理陷阱。 PowerShell 习惯用法强调：CmdletBinding、管道处理、splatting 和结构化错误处理。遵循适用于 Bash 的 ShellCheck 和适用于 PowerShell 的 PSScriptAnalyzer。