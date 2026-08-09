---
# मेटाडेटा
शीर्षक: "गिट कमांड त्वरित संदर्भ"
विवरण: "गिट कमांड और वर्कफ़्लोज़"
श्रेणी: "त्वरित संदर्भ"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
review_by: "त्वरित संदर्भ नॉलेज बेस टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [गिट, कमांड, त्वरित-संदर्भ]
कठिनाई_स्तर: "शुरुआती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "16 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# Git कमांड त्वरित संदर्भ
संस्करण नियंत्रण के लिए आवश्यक Git कमांड।
---

## सेटअप और कॉन्फ़िगरेशन
```bash
# Configure user info
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View configuration
git config --list
git config user.name

# Set default branch name
git config --global init.defaultBranch main
```

---

## रिपॉजिटरी आरंभीकरण
```bash
# Initialize new repository
git init

# Clone existing repository
git clone <url>
git clone <url> folder-name

# Clone specific branch
git clone -b branch-name <url>
```

---

## बुनियादी कार्यप्रवाह
```bash
# Check status
git status

# View changes
git diff
git diff --staged

# Stage files
git add file.txt          # Specific file
git add .                 # All files
git add *.py              # Pattern match

# Commit changes
git commit -m "Commit message"
git commit -am "Message"  # Stage and commit tracked files

# View commit history
git log
git log --oneline
git log --graph --oneline --all
```

---

## शाखा लगाना
```bash
# List branches
git branch                # Local branches
git branch -a             # All branches
git branch -r             # Remote branches

# Create branch
git branch branch-name
git checkout -b branch-name   # Create and switch

# Switch branches
git checkout branch-name
git switch branch-name        # Newer syntax

# Rename current branch
git branch -m new-name

# Delete branch
git branch -d branch-name     # Safe delete (merged)
git branch -D branch-name     # Force delete

# Merge branch
git merge branch-name

# Rebase branch
git rebase main
```

---

## रिमोट संचालन
```bash
# View remotes
git remote -v

# Add remote
git remote add origin <url>

# Fetch from remote
git fetch origin
git fetch --all

# Pull changes (fetch + merge)
git pull origin main
git pull --rebase origin main

# Push changes
git push origin main
git push -u origin main     # Set upstream
git push --force            # Force push (use carefully)
git push --force-with-lease # Safer force push

# Push tags
git push --tags
```

---

## परिवर्तनों को पूर्ववत करना
```bash
# Unstage file (keep changes)
git reset HEAD file.txt
git restore --staged file.txt

# Discard working changes
git checkout -- file.txt
git restore file.txt

# Amend last commit
git commit --amend -m "New message"
git commit --amend --no-edit

# Revert commit (safe for shared repos)
git revert commit-hash

# Reset to previous commit
git reset --soft HEAD~1     # Keep changes staged
git reset --mixed HEAD~1    # Keep changes unstaged (default)
git reset --hard HEAD~1     # Discard all changes (dangerous)
```

---

## छिपाना
```bash
# Save work in progress
git stash
git stash save "message"

# List stashes
git stash list

# Apply stash
git stash apply             # Most recent
git stash apply stash@{1}   # Specific stash

# Apply and remove
git stash pop

# Drop stash
git stash drop stash@{1}

# Clear all stashes
git stash clear
```

---

## टैग
```bash
# List tags
git tag
git tag -l "v1.*"

# Create tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # Annotated tag

# Checkout tag
git checkout v1.0.0

# Delete tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## देखना और खोजना
```bash
# Show commit details
git show commit-hash
git show --stat commit-hash

# Blame (who changed what)
git blame file.txt

# Search commits
git log --grep="keyword"
git log --author="name"

# Search code in history
git log -S"function_name"

# View file at specific commit
git show commit-hash:file.txt
```

---

## उन्नत संचालन
```bash
# Cherry-pick commit
git cherry-pick commit-hash

# Interactive rebase
git rebase -i HEAD~5

# Squash commits (during rebase)
# Change 'pick' to 'squash' or 's' in editor

# Create patch
git format-patch -1 commit-hash

# Apply patch
git apply patch-file.patch
git am patch-file.patch

# Submodules
git submodule add <url> path
git submodule update --init --recursive
```

---

## साफ - सफाई
```bash
# Remove untracked files (dry run)
git clean -n
git clean -f                # Actually remove

# Remove untracked directories
git clean -fd

# Prune deleted remote branches
git fetch --prune
git remote prune origin
```

---

## सामान्य कार्यप्रवाह
### नई सुविधा शुरू करें```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... work ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Create PR/MR on platform
```

### मेन के साथ सिंक करें```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Resolve conflicts if any
git push --force-with-lease
```

### हॉटफ़िक्स वर्कफ़्लो```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... fix ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## .gitignore पैटर्न
```gitignore
# Ignore specific file
filename.txt

# Ignore all .log files
*.log

# Ignore directory
node_modules/
__pycache__/

# Negate (include despite earlier pattern)
!important.log

# Comment
# This is a comment
```

---

## कीबोर्ड शॉर्टकट (गिट बैश)
| शॉर्टकट | कार्रवाई |
|---|--------|
|  __संरक्षित_0__ | रिवर्स सर्च हिस्ट्री |
|  __संरक्षित_1__ | स्वतः पूर्ण |
|  __संरक्षित_2__ | आदेश रद्द करें |
|  __संरक्षित_3__ | प्रक्रिया निलंबित करें |
|  __संरक्षित_4__ | निलंबित प्रक्रिया फिर से शुरू करें |
---

## सर्वोत्तम प्रथाएं
✅ **करें:**
- स्पष्ट, वर्णनात्मक प्रतिबद्ध संदेश लिखें
- तार्किक समूहों के साथ बार-बार प्रतिबद्ध रहें
- सुविधाओं/सुधारों के लिए शाखाओं का उपयोग करें
- काम शुरू करने से पहले खींच लें
- अक्सर`git status`की समीक्षा करें
❌ **नहीं करें:**
- संवेदनशील डेटा प्रतिबद्ध करें (एपीआई कुंजी, पासवर्ड)
- साझा शाखाओं पर बलपूर्वक दबाव डालें
- बड़ी बाइनरी फ़ाइलें प्रतिबद्ध करें
- मर्ज विवादों पर ध्यान न दें
- सीधे मुख्य/मास्टर पर काम करें
---

## प्रतिबद्ध संदेश सम्मेलन
```
type(scope): subject

body (optional)

footer (optional)
```

**प्रकार:**
- __प्रोटेक्टेड_0__ : नई सुविधा
- __प्रोटेक्टेड_1__ : बग फिक्स
- __संरक्षित_2__ : दस्तावेज़ीकरण
- __संरक्षित_3__ : फ़ॉर्मेटिंग
-`refactor`: कोड पुनर्गठन
- __संरक्षित_5__ : परीक्षण
- __संरक्षित_6__ : रखरखाव
**उदाहरण:**```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*अंतिम अद्यतन: जुलाई 2026 | गिट 2.x*