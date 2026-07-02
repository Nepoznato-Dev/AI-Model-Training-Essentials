# Git कमांड्स त्वरित संदर्भ

वर्ज़न कंट्रोल के लिए आवश्यक Git कमांड्स।

---

## सेटअप और कॉन्फ़िगरेशन

```bash
# उपयोगकर्ता जानकारी कॉन्फ़िगर करें
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# कॉन्फ़िगरेशन देखें
git config --list
git config user.name

# डिफ़ॉल्ट ब्रांच नाम सेट करें
git config --global init.defaultBranch main
```

---

## रिपॉज़िटरी प्रारंभ करना

```bash
# नई रिपॉज़िटरी प्रारंभ करें
git init

# मौजूदा रिपॉज़िटरी क्लोन करें
git clone <url>
git clone <url> folder-name

# विशेष ब्रांच क्लोन करें
git clone -b branch-name <url>
```

---

## मूल कार्यप्रवाह

```bash
# स्थिति जाँचें
git status

# बदलाव देखें
git diff
git diff --staged

# फ़ाइलें स्टेज करें
git add file.txt          # विशेष फ़ाइल
git add .                 # सभी फ़ाइलें
git add *.py              # पैटर्न के अनुसार मिलान

# बदलाव कमिट करें
git commit -m "Commit message"
git commit -am "Message"  # ट्रैक की गई फ़ाइलों को stage और commit करें

# कमिट इतिहास देखें
git log
git log --oneline
git log --graph --oneline --all
```

---

## ब्रांचिंग

```bash
# ब्रांचों की सूची देखें
git branch                # स्थानीय ब्रांचें
git branch -a             # सभी ब्रांचें
git branch -r             # रिमोट ब्रांचें

# ब्रांच बनाएँ
git branch branch-name
git checkout -b branch-name   # बनाएँ और बदलें

# ब्रांच बदलें
git checkout branch-name
git switch branch-name        # नया सिंटैक्स

# वर्तमान ब्रांच का नाम बदलें
git branch -m new-name

# ब्रांच हटाएँ
git branch -d branch-name     # सुरक्षित हटाएँ (merge हो चुकी)
git branch -D branch-name     # बलपूर्वक हटाएँ

# ब्रांच मर्ज करें
git merge branch-name

# ब्रांच रीबेस करें
git rebase main
```

---

## रिमोट ऑपरेशन्स

```bash
# रिमोट्स देखें
git remote -v

# रिमोट जोड़ें
git remote add origin <url>

# रिमोट से फ़ेच करें
git fetch origin
git fetch --all

# बदलाव पुल करें (फ़ेच + मर्ज)
git pull origin main
git pull --rebase origin main

# बदलाव पुश करें
git push origin main
git push -u origin main     # upstream सेट करें
git push --force            # बलपूर्वक push करें (सावधानी से उपयोग करें)
git push --force-with-lease # अधिक सुरक्षित बलपूर्वक push

# टैग्स पुश करें
git push --tags
```

---

## बदलाव वापस लेना

```bash
# फ़ाइल को स्टेज से हटाएँ (बदलाव बनाए रखें)
git reset HEAD file.txt
git restore --staged file.txt

# वर्किंग डायरेक्टरी के बदलाव हटाएँ
git checkout -- file.txt
git restore file.txt

# अंतिम कमिट में संशोधन करें
git commit --amend -m "New message"
git commit --amend --no-edit

# कमिट रिवर्ट करें (साझा रिपॉज़िटरीज़ के लिए सुरक्षित)
git revert commit-hash

# पिछले कमिट पर रीसेट करें
git reset --soft HEAD~1     # बदलाव स्टेज की हुई स्थिति में रखें
git reset --mixed HEAD~1    # बदलाव अनस्टेज की हुई स्थिति में रखें (default)
git reset --hard HEAD~1     # सभी बदलाव हटाएँ (खतरनाक)
```

---

## स्टैशिंग

```bash
# प्रगति पर काम सहेजें
git stash
git stash save "message"

# स्टैशों की सूची देखें
git stash list

# स्टैश लागू करें
git stash apply             # सबसे हाल का
git stash apply stash@{1}   # विशेष stash

# लागू करें और हटाएँ
git stash pop

# स्टैश हटाएँ
git stash drop stash@{1}

# सभी स्टैश साफ़ करें
git stash clear
```

---

## टैग्स

```bash
# टैग्स की सूची देखें
git tag
git tag -l "v1.*"

# टैग बनाएँ
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # annotation वाला टैग

# टैग चेकआउट करें
git checkout v1.0.0

# टैग हटाएँ
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## देखना और खोजना

```bash
# कमिट विवरण दिखाएँ
git show commit-hash
git show --stat commit-hash

# ब्लेम (किसने क्या बदला)
git blame file.txt

# कमिट्स खोजें
git log --grep="keyword"
git log --author="name"

# इतिहास में कोड खोजें
git log -S"function_name"

# विशेष कमिट पर फ़ाइल देखें
git show commit-hash:file.txt
```

---

## उन्नत ऑपरेशन्स

```bash
# कमिट चेरी-पिक करें
git cherry-pick commit-hash

# इंटरैक्टिव रीबेस
git rebase -i HEAD~5

# कमिट्स स्क्वैश करें (रीबेस के दौरान)
# एडिटर में 'pick' को 'squash' या 's' में बदलें

# पैच बनाएँ
git format-patch -1 commit-hash

# पैच लागू करें
git apply patch-file.patch

git am patch-file.patch

# सबमॉड्यूल्स
git submodule add <url> path
git submodule update --init --recursive
```

---

## सफ़ाई

```bash
# अनट्रैक्ड फ़ाइलें हटाएँ (ड्राई रन)
git clean -n
git clean -f                # वास्तव में हटाएँ

# अनट्रैक्ड डायरेक्टरीज़ हटाएँ
git clean -fd

# हटाई गई रिमोट ब्रांचों को प्रून करें
git fetch --prune
git remote prune origin
```

---

## सामान्य कार्यप्रवाह

### नई फ़ीचर शुरू करें
```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... काम ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# प्लेटफ़ॉर्म पर PR/MR बनाएँ
```

### main के साथ सिंक करें
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# यदि कोई कॉन्फ्लिक्ट्स हों, तो उन्हें रिज़ॉल्व करें
git push --force-with-lease
```

### हॉटफिक्स कार्यप्रवाह
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... सुधार ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## .gitignore पैटर्न्स

```gitignore
# विशेष फ़ाइल को अनदेखा करें
filename.txt

# सभी .log फ़ाइलों को अनदेखा करें
*.log

# डायरेक्टरी को अनदेखा करें
node_modules/
__pycache__/

# निगेट करें (पहले के पैटर्न के बावजूद शामिल करें)
!important.log

# टिप्पणी
# यह एक टिप्पणी है
```

---

## कीबोर्ड शॉर्टकट्स (Git Bash)

| शॉर्टकट | क्रिया |
|----------|--------|
| `Ctrl+R` | इतिहास में उल्टी दिशा में खोजें |
| `Tab` | अपने-आप पूरा करें |
| `Ctrl+C` | कमांड रद्द करें |
| `Ctrl+Z` | प्रक्रिया निलंबित करें |
| `fg` | निलंबित प्रक्रिया फिर शुरू करें |

---

## सर्वोत्तम अभ्यास

✅ **करें:**
- स्पष्ट, वर्णनात्मक कमिट संदेश लिखें
- तार्किक समूहों में बार-बार कमिट करें
- फीचर्स/फिक्सेस के लिए ब्रांचों का उपयोग करें
- काम शुरू करने से पहले पुल करें
- `git status` को अक्सर जाँचें

❌ **न करें:**
- संवेदनशील डेटा (API keys, passwords) कमिट न करें
- साझा ब्रांचों पर फ़ोर्स पुश न करें
- बड़ी बाइनरी फ़ाइलें कमिट न करें
- मर्ज कॉन्फ्लिक्ट्स को अनदेखा न करें
- सीधे main/master पर काम न करें

---

## कमिट संदेश नियम

```
type(scope): subject

body (optional)

footer (optional)
```

**प्रकार:**
- `feat`: नई फ़ीचर
- `fix`: बग ठीक करना
- `docs`: प्रलेखन
- `style`: स्वरूपण
- `refactor`: कोड का पुनर्गठन
- `test`: परीक्षण
- `chore`: रखरखाव

**उदाहरण:**
```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*अंतिम अपडेट: जून 2025 | Git 2.x*
