---
# Metadata
title: "Shell & PowerShell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Shell and PowerShell ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# शेल और पावरशेल - इकोसिस्टम और टूलींग गाइड
यह मार्गदर्शिका शेल स्क्रिप्टिंग (बैश/ज़ेडएसएच) और पावरशेल के लिए आवश्यक टूल, फ्रेमवर्क और बुनियादी ढांचे को कवर करती है।
---

## शैल कार्यान्वयन
| शैल | प्लेटफार्म | नोट्स |
|-------|-------|-------|
| **बैश** | यूनिक्स/लिनक्स/मैकओएस | सर्वाधिक व्यापक रूप से उपयोग किया जाने वाला |
| **ज़श** | macOS डिफ़ॉल्ट | उन्नत बैश |
| **मछली** | क्रॉस-प्लेटफ़ॉर्म | उपयोगकर्ता के अनुकूल |
| **डैश** | डेबियन/उबंटू | तेज़, POSIX-अनुपालक |
| **क्ष** | यूनिक्स | मकई का खोल |
| **पावरशेल** | क्रॉस-प्लेटफ़ॉर्म | वस्तु-उन्मुख (pwsh) |
| **नुशेल** | क्रॉस-प्लेटफ़ॉर्म | संरचित डेटा शेल |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## पैकेज मैनेजर (शेल टूल्स)
| उपकरण | उद्देश्य |
|------|---------|
| **होमब्रू** | macOS/Linux पैकेज मैनेजर |
| **उपयुक्त/यम/डीएनएफ** | लिनक्स पैकेज प्रबंधक |
| **पीकेजी** | फ्रीबीएसडी पैकेज मैनेजर |
| **स्कूप** | विंडोज़ सीएलआई इंस्टॉलर |
| **चॉकलेट** | विंडोज़ पैकेज मैनेजर |
| **विंगेट** | विंडोज़ पैकेज मैनेजर |
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

## आवश्यक सीएलआई उपकरण
| उपकरण | उद्देश्य |
|------|---------|
| **jq** | JSON प्रोसेसिंग |
| **yq** | वाईएएमएल प्रोसेसिंग |
| **रिपग्रेप (आरजी)** | तेज़ ग्रेप |
| **एफडी** | तेजी से खोजें |
| **बल्ले** | उन्नत बिल्ली |
| **exa / eza** | उन्नत एलएस |
| **fzf** | फजी खोजक |
| **हटॉप** | प्रक्रिया दर्शक |
| **tmux** | टर्मिनल मल्टीप्लेक्सर |
| **कर्ल / wget** | HTTP अनुरोध |
| **sed / awk** | पाठ प्रसंस्करण |
| **xargs** | इनपुट से कमांड बनाएं |
| **बनाओ** | टास्क रनर |
| **प्रवेश** | फ़ाइल परिवर्तनों पर आदेश चलाएँ |
| **समानांतर** | समानांतर निष्पादन |
| **शेलचेक** | शैल स्क्रिप्ट लिंटर |
---

## शैल फ्रेमवर्क और संवर्द्धन
| उपकरण | उद्देश्य |
|------|---------|
| **ओह माय ज़श** | Zsh फ्रेमवर्क (थीम, प्लगइन्स) |
| **प्रेज़्टो** | Zsh ढांचा (तेज़) |
| **स्टारशिप** | क्रॉस-शेल प्रॉम्प्ट |
| **zsh-ऑटोसुझाव** | स्वतः सुझाव |
| **zsh-सिंटैक्स-हाइलाइटिंग** | सिंटैक्स हाइलाइटिंग |
| **बैश-इट** | बैश फ्रेमवर्क |
| **अतुइन** | शैल इतिहास (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## पावरशेल मॉड्यूल
| मॉड्यूल | उद्देश्य |
|-------|------|
| **पीएसरीडलाइन** | उन्नत कमांड-लाइन संपादन |
| **पेस्टर** | परीक्षण रूपरेखा |
| **PSScriptAnalyzer** | लिंटिंग |
| **पॉश-गिट** | गिट एकीकरण |
| **टर्मिनल-प्रतीक** | फ़ाइल चिह्न |
| **PSWindowsUpdate** | विंडोज़ अपडेट |
| **अज़** | नीला प्रबंधन |
| **AWSPowerShell** | एडब्लूएस प्रबंधन |
| **एसक्यूएलसर्वर** | SQL सर्वर प्रबंधन |
| **पोडे** | वेब ढाँचा |
| **यूनिवर्सल डैशबोर्ड** | वेब डैशबोर्ड |
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

## परीक्षण
| ढाँचा | शैल | उद्देश्य |
|----|-------|------|
| **चमगादड़** | बैश | बैश स्वचालित परीक्षण |
| **शुनीट2** | शैल | xUnit-शैली परीक्षण |
| **पेस्टर** | पावरशेल | परीक्षण और उपहास |
| **assert.sh** | बैश | अभिकथन पुस्तकालय |
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

## कोड गुणवत्ता
| उपकरण | शैल | उद्देश्य |
|------|-------|------|
| **शेलचेक** | बैश/ज़श | लिंटिंग और स्थैतिक विश्लेषण |
| **shfmt** | बैश/ज़श | कोड फ़ॉर्मेटिंग |
| **PSScriptAnalyzer** | पावरशेल | लिंटिंग |
| **पीएसस्क्रिप्टसेटिंग्स** | पावरशेल | स्वरूपण |
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

## प्रमुख पुस्तकालय एवं पैटर्न
### दे घुमा के
| पैटर्न | उद्देश्य |
|---------|---------|
| **सेट -यूओ पाइपफेल** | सख्त मोड |
| **जाल** | सिग्नल हैंडलिंग |
| **स्रोत / .** | फ़ाइलें शामिल करें |
| **गेटोप्ट्स** | तर्क विश्लेषण |
| **हेरेडोक** | बहु-पंक्ति तार |
| **प्रक्रिया प्रतिस्थापन** | `<()`और`>()`|
| **सरणी** | अनुक्रमित और सहयोगी |
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

### पावरशेल
| पैटर्न | उद्देश्य |
|---------|---------|
| **CmdletBinding** | उन्नत फ़ंक्शन |
| **पैरामीटर** | पैरामीटर विशेषताएँ |
| **पाइपलाइन** | ऑब्जेक्ट पाइपलाइन |
| **कोशिश करें/पकड़ें** | त्रुटि प्रबंधन |
| **कक्षाएं** | ओओपी |
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

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **वीएस कोड** | शेल/पॉवरशेल समर्थन |
| **नियोविम** | टर्मिनल-आधारित |
| **विंडोज टर्मिनल** | आधुनिक टर्मिनल (पॉवरशेल) |
| **iTerm2** | macOS टर्मिनल |
| **ताना** | एआई-संचालित टर्मिनल |
| **एलाक्रिटी** | जीपीयू-त्वरित टर्मिनल |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **क्रोन** | अनुसूचित कार्य (यूनिक्स) |
| **सिस्टमडी** | सेवा प्रबंधन (लिनक्स) |
| **कार्य अनुसूचक** | विंडोज़ निर्धारित कार्य |
| **डॉकर एंट्रीपॉइंट** | कंटेनर स्क्रिप्ट |
| **सीआई/सीडी पाइपलाइन** | GitHub क्रियाएँ, GitLab CI |
| **उत्तरदायी** | कॉन्फ़िगरेशन प्रबंधन |
| **टेराफॉर्म** | कोड के रूप में इंफ्रास्ट्रक्चर |
---

## सारांश
शेल स्क्रिप्टिंग का पारिस्थितिकी तंत्र विविध है: **बैश** सार्वभौमिक मानक बना हुआ है, **Zsh** इंटरैक्टिव उपयोग के लिए आधुनिक डिफ़ॉल्ट है, और **पॉवरशेल** विंडोज प्रशासन पर हावी है। मानक स्टैक है: स्क्रिप्टिंग के लिए **बैश/ज़श**, लिंटिंग के लिए **शेलचेक**, फ़ॉर्मेटिंग के लिए **shfmt**, परीक्षण के लिए **बैट**, JSON के लिए **jq**, खोज के लिए **ripgrep**, और टर्मिनल मल्टीप्लेक्सिंग के लिए **tmux**। पॉवरशेल के लिए: **पेस्टर** परीक्षण के लिए, **PSScriptAnalyzer** लिंटिंग के लिए, और **PSReadLine** उन्नत संपादन के लिए। ऑटोमेशन, सीआई/सीडी, सिस्टम एडमिनिस्ट्रेशन और डेवऑप्स वर्कफ़्लोज़ के लिए शेल स्क्रिप्टिंग आवश्यक है।