---
# Metadata
title: "Shell & PowerShell — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Shell/Bash and PowerShell with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [shell, bash, powershell, common-mistakes, anti-patterns, pitfalls, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# शेल और पावरशेल - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ शेल/बैश और पावरशेल में सबसे आम गलतियों, जाल और एंटी-पैटर्न को सूचीबद्ध करता है।
---

## 1. अउद्धृत चर (बैश)
```bash
# ❌ WRONG — word splitting and globbing
file="my file.txt"
cat $file  # tries: cat "my" "file.txt"

# ✅ CORRECT — always quote variables
cat "$file"
```

---

## 2.`[ ]`बनाम`[[ ]]`(बैश)
```bash
# ❌ WRONG — [ ] doesn't handle empty variables
name=""
if [ $name = "Alice" ]; then  # syntax error!
    echo "Hello"
fi

# ✅ CORRECT — [[ ]] is safer
if [[ $name = "Alice" ]]; then
    echo "Hello"
fi
```

---

## 3.`=`बनाम`-eq`(बैश)
```bash
# ❌ WRONG — string comparison for numbers
if [ $x = 5 ]; then  # works but semantically wrong

# ✅ CORRECT — numeric comparison
if [[ $x -eq 5 ]]; then
    echo "x is 5"
fi
```

---

## 4. निकास कोड की जाँच न करना (बैश)
```bash
# ❌ WRONG — ignoring failures
rm /important/file
cp backup /important/file  # runs even if rm failed!

# ✅ CORRECT — check exit codes
set -euo pipefail  # exit on error, undefined vars, pipe failures
rm /important/file || { echo "Failed"; exit 1; }
```

---

## 5. पावरशेल: स्ट्रिंग इंटरपोलेशन
```powershell
# ❌ WRONG — single quotes don't interpolate
$name = "Alice"
Write-Host 'Hello $name'  # prints: Hello $name

# ✅ CORRECT — double quotes for interpolation
Write-Host "Hello $name"  # prints: Hello Alice
```

---

## 6. पॉवरशेल:`==`बनाम `-eq`
```powershell
# ❌ WRONG — == is not PowerShell comparison
if ($x == 5) { }  # syntax error!

# ✅ CORRECT — use -eq, -ne, -gt, -lt
if ($x -eq 5) { Write-Host "x is 5" }
```

---

## 7. सबशेल वेरिएबल स्कोप (बैश)
```bash
# ❌ WRONG — pipe creates subshell
count=0
echo "hello" | while read line; do
    count=$((count + 1))
done
echo $count  # still 0! (subshell modification lost)

# ✅ CORRECT — use process substitution
count=0
while read line; do
    count=$((count + 1))
done < <(echo "hello")
echo $count  # 1
```

---

## 8. पावरशेल: पाइपलाइन ऑब्जेक्ट बनाम स्ट्रिंग्स
```powershell
# ❌ WRONG — treating pipeline objects as strings
Get-Process | Where-Object { $_ -match "chrome" }
# $_ is a Process object, not string

# ✅ CORRECT — access properties
Get-Process | Where-Object { $_.ProcessName -match "chrome" }
```

---

## सारांश
शेल स्क्रिप्टिंग ट्रैप: बैश में हमेशा वेरिएबल उद्धृत करें,`[ ]`पर`[[ ]]`का उपयोग करें,`set -euo pipefail`का उपयोग करें, निकास कोड की जांच करें, और सबशेल स्कोपिंग को समझें। पावरशेल ट्रैप: इंटरपोलेशन के लिए दोहरे उद्धरण चिह्नों का उपयोग करें,`-eq`का उपयोग करें न कि`==`का, और याद रखें कि पाइपलाइन ऑब्जेक्ट में गुण होते हैं। दोनों सावधानीपूर्वक उद्धरण और स्पष्ट त्रुटि प्रबंधन को पुरस्कृत करते हैं।